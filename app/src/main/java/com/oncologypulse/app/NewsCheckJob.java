package com.oncologypulse.app;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.job.JobInfo;
import android.app.job.JobParameters;
import android.app.job.JobScheduler;
import android.app.job.JobService;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.os.Build;

import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/** Background check every few hours: downloads the feed and notifies about new items. */
public class NewsCheckJob extends JobService {
    private static final int JOB_ID = 4201;
    static final String CHANNEL_ID = "pulse_updates";

    static void schedule(Context ctx) {
        JobScheduler js = (JobScheduler) ctx.getSystemService(Context.JOB_SCHEDULER_SERVICE);
        if (js == null) return;
        for (JobInfo j : js.getAllPendingJobs()) if (j.getId() == JOB_ID) return;
        JobInfo job = new JobInfo.Builder(JOB_ID, new ComponentName(ctx, NewsCheckJob.class))
                .setRequiredNetworkType(JobInfo.NETWORK_TYPE_ANY)
                .setPeriodic(4 * 60 * 60 * 1000L)
                .setPersisted(true)
                .build();
        js.schedule(job);
    }

    @Override
    public boolean onStartJob(JobParameters params) {
        new Thread(() -> {
            try {
                String json = NewsRepo.fetch();
                NewsRepo.saveCache(this, json);
                if (NewsRepo.hasSeenAnything(this)) {
                    Set<String> seen = NewsRepo.seen(this);
                    List<JSONObject> fresh = new ArrayList<>();
                    for (JSONObject o : NewsRepo.items(json)) if (!seen.contains(o.optString("id"))) fresh.add(o);
                    if (!fresh.isEmpty()) notifyNew(this, fresh);
                } else {
                    NewsRepo.markAllSeen(this, json);
                }
                jobFinished(params, false);
            } catch (Exception e) {
                jobFinished(params, true);
            }
        }).start();
        return true;
    }

    @Override
    public boolean onStopJob(JobParameters params) {
        return true;
    }

    static void ensureChannel(Context ctx) {
        if (Build.VERSION.SDK_INT < 26) return;
        NotificationManager nm = ctx.getSystemService(NotificationManager.class);
        NotificationChannel ch = new NotificationChannel(CHANNEL_ID,
                ctx.getString(R.string.channel_name), NotificationManager.IMPORTANCE_DEFAULT);
        ch.setDescription(ctx.getString(R.string.channel_desc));
        nm.createNotificationChannel(ch);
    }

    private static void notifyNew(Context ctx, List<JSONObject> fresh) {
        ensureChannel(ctx);
        NotificationManager nm = (NotificationManager) ctx.getSystemService(Context.NOTIFICATION_SERVICE);
        if (nm == null) return;

        // Practice-changing items first, then newest.
        fresh.sort((a, b) -> {
            boolean pa = "practice-changing".equals(a.optString("impact"));
            boolean pb = "practice-changing".equals(b.optString("impact"));
            if (pa != pb) return pa ? -1 : 1;
            return b.optString("date").compareTo(a.optString("date"));
        });

        int n = fresh.size();
        String title = n == 1 ? "New in oncology" : n + " new oncology updates";
        StringBuilder big = new StringBuilder();
        for (int i = 0; i < Math.min(n, 5); i++) {
            if (i > 0) big.append("\n");
            big.append("• ").append(fresh.get(i).optString("title"));
        }

        Intent open = new Intent(ctx, MainActivity.class).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        PendingIntent pi = PendingIntent.getActivity(ctx, 0, open,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);

        Notification.Builder b = Build.VERSION.SDK_INT >= 26
                ? new Notification.Builder(ctx, CHANNEL_ID)
                : new Notification.Builder(ctx);
        b.setSmallIcon(R.drawable.ic_stat_pulse)
                .setContentTitle(title)
                .setContentText(fresh.get(0).optString("title"))
                .setStyle(new Notification.BigTextStyle().bigText(big.toString()))
                .setColor(0xFFB8365F)
                .setContentIntent(pi)
                .setAutoCancel(true);
        try {
            nm.notify(1, b.build());
        } catch (SecurityException ignored) {
            // Notifications not allowed; the app still shows the items when opened.
        }
    }
}
