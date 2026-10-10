package com.oncologypulse.app;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import org.json.JSONObject;

public class MainActivity extends Activity {
    private WebView web;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        web = new WebView(this);
        setContentView(web);

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);
        web.setBackgroundColor(getColor(R.color.bg));

        web.addJavascriptInterface(new Bridge(), "Android");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest req) {
                Uri u = req.getUrl();
                if ("http".equals(u.getScheme()) || "https".equals(u.getScheme())) {
                    openExternal(u.toString());
                    return true;
                }
                return false;
            }
        });
        web.loadUrl("file:///android_asset/index.html");

        NewsCheckJob.ensureChannel(this);
        NewsCheckJob.schedule(this);
        if (Build.VERSION.SDK_INT >= 33
                && checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS}, 7);
        }
    }

    private void openExternal(String url) {
        try {
            startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url)));
        } catch (Exception ignored) {}
    }

    @Override
    public void onBackPressed() {
        web.evaluateJavascript("window.handleBack && window.handleBack()", r -> {
            if (!"true".equals(r)) MainActivity.super.onBackPressed();
        });
    }

    private void deliver(String fn, String payload) {
        String arg = JSONObject.quote(payload);
        runOnUiThread(() -> web.evaluateJavascript("window." + fn + " && window." + fn + "(" + arg + ")", null));
    }

    /** Methods the page calls as window.Android.* */
    private class Bridge {
        @JavascriptInterface
        public String cached() {
            return NewsRepo.cached(MainActivity.this);
        }

        @JavascriptInterface
        public void refresh() {
            new Thread(() -> {
                try {
                    String json = NewsRepo.fetch();
                    NewsRepo.saveCache(MainActivity.this, json);
                    NewsRepo.markAllSeen(MainActivity.this, json);
                    deliver("onNews", json);
                } catch (Exception e) {
                    deliver("onNewsError", "Couldn't reach the update server. Showing saved news.");
                }
            }).start();
        }

        @JavascriptInterface
        public String trials() {
            return NewsRepo.trials(MainActivity.this);
        }

        @JavascriptInterface
        public void refreshTrials() {
            new Thread(() -> {
                if (NewsRepo.refreshTrials(MainActivity.this)) {
                    deliver("onTrials", NewsRepo.trials(MainActivity.this));
                }
            }).start();
        }

        @JavascriptInterface
        public void open(String url) {
            openExternal(url);
        }

        @JavascriptInterface
        public void share(String text) {
            Intent i = new Intent(Intent.ACTION_SEND).setType("text/plain").putExtra(Intent.EXTRA_TEXT, text);
            runOnUiThread(() -> startActivity(Intent.createChooser(i, "Share")));
        }

        @JavascriptInterface
        public String version() {
            return BuildConfig.VERSION_NAME;
        }
    }
}
