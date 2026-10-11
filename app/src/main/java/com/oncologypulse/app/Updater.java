package com.oncologypulse.app;

import android.app.Activity;
import android.app.DownloadManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.Uri;
import android.os.Build;
import android.os.Environment;
import android.provider.Settings;

import org.json.JSONObject;

import java.io.File;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * In-app updates for the sideloaded APK. Each GitHub build publishes version.json next to
 * OncologyPulse.apk on the "latest" release; the app compares versionCode with its own,
 * downloads the new APK with DownloadManager and hands it to the system installer.
 */
final class Updater {
    private static final String BASE = "https://github.com/" + BuildConfig.DATA_REPO + "/releases/latest/download/";
    static final String VERSION_URL = BASE + "version.json";
    static final String APK_URL = BASE + "OncologyPulse.apk";

    private Updater() {}

    /** Returns version.json if a newer build exists, otherwise null. Network errors return null. */
    static JSONObject checkNewer() {
        try {
            HttpURLConnection c = (HttpURLConnection) new URL(VERSION_URL + "?t=" + System.currentTimeMillis()).openConnection();
            c.setInstanceFollowRedirects(true);
            c.setConnectTimeout(15000);
            c.setReadTimeout(20000);
            c.setUseCaches(false);
            try {
                if (c.getResponseCode() != 200) return null;
                InputStream in = c.getInputStream();
                ByteArrayOutputStream out = new ByteArrayOutputStream();
                byte[] buf = new byte[8192]; int n;
                while ((n = in.read(buf)) > 0) out.write(buf, 0, n);
                JSONObject v = new JSONObject(out.toString("UTF-8"));
                return v.optInt("versionCode", 0) > BuildConfig.VERSION_CODE ? v : null;
            } finally {
                c.disconnect();
            }
        } catch (Exception e) {
            return null;
        }
    }

    /** True when Android will let this app open the installer (Android 8+ asks once per app). */
    static boolean canInstall(Context ctx) {
        return Build.VERSION.SDK_INT < 26 || ctx.getPackageManager().canRequestPackageInstalls();
    }

    /** Opens the system screen where the user allows this app to install updates. */
    static void openInstallPermission(Activity a) {
        if (Build.VERSION.SDK_INT >= 26) {
            a.startActivity(new Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,
                    Uri.parse("package:" + a.getPackageName())));
        }
    }

    /** Starts the download; when it finishes the system installer opens. Returns the download id. */
    static long download(Activity a, String versionName, Runnable onFailed) {
        DownloadManager dm = (DownloadManager) a.getSystemService(Context.DOWNLOAD_SERVICE);
        String name = "OncologyPulse-" + versionName + ".apk";
        File old = new File(a.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS), name);
        if (old.exists()) old.delete();
        DownloadManager.Request r = new DownloadManager.Request(Uri.parse(APK_URL + "?t=" + System.currentTimeMillis()))
                .setTitle("Oncology Pulse " + versionName)
                .setDescription("Downloading update")
                .setMimeType("application/vnd.android.package-archive")
                .setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE)
                .setDestinationInExternalFilesDir(a, Environment.DIRECTORY_DOWNLOADS, name);
        final long id = dm.enqueue(r);

        BroadcastReceiver done = new BroadcastReceiver() {
            @Override
            public void onReceive(Context ctx, Intent intent) {
                if (intent.getLongExtra(DownloadManager.EXTRA_DOWNLOAD_ID, -1) != id) return;
                try { ctx.unregisterReceiver(this); } catch (Exception ignored) {}
                Uri apk = dm.getUriForDownloadedFile(id);
                if (apk == null) { onFailed.run(); return; }
                Intent install = new Intent(Intent.ACTION_VIEW)
                        .setDataAndType(apk, "application/vnd.android.package-archive")
                        .addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_ACTIVITY_NEW_TASK);
                try { ctx.startActivity(install); } catch (Exception e) { onFailed.run(); }
            }
        };
        IntentFilter f = new IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE);
        if (Build.VERSION.SDK_INT >= 33) a.registerReceiver(done, f, Context.RECEIVER_EXPORTED);
        else a.registerReceiver(done, f);
        return id;
    }
}
