package com.oncologypulse.app;

import android.content.Context;
import android.content.SharedPreferences;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/** Downloads, caches and diffs the news feed (data/news.json in the GitHub repo). */
final class NewsRepo {
    private static final String CACHE_FILE = "news.json";
    private static final String PREFS = "pulse";
    private static final String KEY_SEEN = "seen_ids";

    private NewsRepo() {}

    /** Fetch the latest feed from the network. Throws on any failure. */
    static String fetch() throws Exception {
        return fetchAny("news.json");
    }

    /** Mirrors of the repo's data folder, tried in order. raw.githubusercontent.com is
     *  blocked on some Indian mobile networks, so CDN mirrors are used as fallbacks. */
    private static String[] mirrors(String file) {
        String repo = BuildConfig.DATA_REPO;
        return new String[]{
            "https://raw.githubusercontent.com/" + repo + "/main/data/" + file,
            "https://cdn.jsdelivr.net/gh/" + repo + "@main/data/" + file,
            "https://cdn.statically.io/gh/" + repo + "/main/data/" + file,
            "https://github.com/" + repo + "/raw/main/data/" + file
        };
    }

    /** Try every mirror; return the copy with the newest "updated" (or highest "version"). */
    private static String fetchAny(String file) throws Exception {
        String best = null; String bestKey = ""; Exception last = null;
        for (String u : mirrors(file)) {
            try {
                String body = fetchUrl(u);
                String key = freshness(body);
                if (best == null || key.compareTo(bestKey) > 0) { best = body; bestKey = key; }
                if (u.contains("raw.githubusercontent")) break; // primary is authoritative
            } catch (Exception e) { last = e; }
        }
        if (best == null) throw last != null ? last : new Exception("No mirror reachable");
        return best;
    }

    /** Sortable freshness key: ISO "updated" timestamp, or zero-padded "version". */
    static String freshness(String json) {
        try {
            JSONObject o = new JSONObject(json);
            String up = o.optString("updated", "");
            if (!up.isEmpty()) return up;
            return String.format("%08d", o.optInt("version", 0));
        } catch (Exception e) { return ""; }
    }

    /** The landmark-trials library: newest downloaded copy, else the bundled one. */
    static String trials(Context ctx) {
        return newest(ctx, "trials.json", "{\"trials\":[]}");
    }

    /** Download the trials library if a newer version is published; returns true if updated. */
    static boolean refreshTrials(Context ctx) {
        try {
            String body = fetchAny("trials.json");
            int remote = new JSONObject(body).optInt("version", 0);
            int local = new JSONObject(trials(ctx)).optInt("version", 0);
            if (remote <= local) return false;
            try (FileOutputStream out = new FileOutputStream(new File(ctx.getFilesDir(), "trials.json"))) {
                out.write(body.getBytes(StandardCharsets.UTF_8));
            }
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static String fetchUrl(String base) throws Exception {
        URL url = new URL(base + "?t=" + System.currentTimeMillis());
        HttpURLConnection c = (HttpURLConnection) url.openConnection();
        c.setConnectTimeout(15000);
        c.setReadTimeout(20000);
        c.setUseCaches(false);
        c.setRequestProperty("Cache-Control", "no-cache");
        try {
            int code = c.getResponseCode();
            if (code != 200) throw new Exception("Server answered " + code);
            String body = readAll(c.getInputStream());
            new JSONObject(body); // validate before caching
            return body;
        } finally {
            c.disconnect();
        }
    }

    static void saveCache(Context ctx, String json) {
        if (freshness(json).compareTo(freshness(cached(ctx))) < 0) return; // never go backwards
        try (FileOutputStream out = new FileOutputStream(new File(ctx.getFilesDir(), CACHE_FILE))) {
            out.write(json.getBytes(StandardCharsets.UTF_8));
        } catch (Exception ignored) {}
    }

    /** Last downloaded feed, or the copy bundled with the app. */
    static String cached(Context ctx) {
        return newest(ctx, CACHE_FILE, "{\"items\":[]}");
    }

    /** Whichever is fresher: the last downloaded copy or the copy bundled in this APK. */
    private static String newest(Context ctx, String name, String empty) {
        String saved = null, bundled = null;
        try { File f = new File(ctx.getFilesDir(), name); if (f.exists()) saved = readAll(new FileInputStream(f)); } catch (Exception ignored) {}
        try { bundled = readAll(ctx.getAssets().open(name)); } catch (Exception ignored) {}
        if (saved == null) return bundled != null ? bundled : empty;
        if (bundled == null) return saved;
        return freshness(bundled).compareTo(freshness(saved)) > 0 ? bundled : saved;
    }

    static List<JSONObject> items(String json) {
        List<JSONObject> list = new ArrayList<>();
        try {
            JSONArray arr = new JSONObject(json).optJSONArray("items");
            if (arr != null) for (int i = 0; i < arr.length(); i++) list.add(arr.getJSONObject(i));
        } catch (Exception ignored) {}
        return list;
    }

    static boolean hasSeenAnything(Context ctx) {
        return prefs(ctx).contains(KEY_SEEN);
    }

    static Set<String> seen(Context ctx) {
        return new HashSet<>(prefs(ctx).getStringSet(KEY_SEEN, new HashSet<>()));
    }

    static void markAllSeen(Context ctx, String json) {
        Set<String> ids = new HashSet<>();
        for (JSONObject o : items(json)) ids.add(o.optString("id"));
        prefs(ctx).edit().putStringSet(KEY_SEEN, ids).apply();
    }

    private static SharedPreferences prefs(Context ctx) {
        return ctx.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
    }

    private static String readAll(InputStream in) throws Exception {
        try (InputStream is = in; ByteArrayOutputStream out = new ByteArrayOutputStream()) {
            byte[] buf = new byte[16384];
            int n;
            while ((n = is.read(buf)) > 0) out.write(buf, 0, n);
            return out.toString("UTF-8");
        }
    }
}
