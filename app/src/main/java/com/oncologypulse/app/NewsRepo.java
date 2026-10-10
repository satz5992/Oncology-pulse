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
        URL url = new URL(BuildConfig.NEWS_URL + "?t=" + System.currentTimeMillis());
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
        try (FileOutputStream out = new FileOutputStream(new File(ctx.getFilesDir(), CACHE_FILE))) {
            out.write(json.getBytes(StandardCharsets.UTF_8));
        } catch (Exception ignored) {}
    }

    /** Last downloaded feed, or the copy bundled with the app. */
    static String cached(Context ctx) {
        File f = new File(ctx.getFilesDir(), CACHE_FILE);
        try {
            if (f.exists()) return readAll(new FileInputStream(f));
            return readAll(ctx.getAssets().open("news.json"));
        } catch (Exception e) {
            return "{\"items\":[]}";
        }
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
