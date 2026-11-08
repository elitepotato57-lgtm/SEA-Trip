// Saves the app on the phone so it opens with no signal.
const APP = "sea-trip-app-v1-1";
const TILES = "sea-trip-tiles-v1";
const CORE = ["./", "./index.html", "./manifest.webmanifest", "./icon-180.png", "./icon-192.png", "./icon-512.png",
  "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(APP).then(cache => Promise.all(CORE.map(u =>
    fetch(u).then(res => { if (res.ok) return cache.put(u, res); }).catch(() => {})
  ))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== APP && k !== TILES).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

async function trim(cache, max){
  const keys = await cache.keys();
  for (let i = 0; i < keys.length - max; i++) await cache.delete(keys[i]);
}

const SAVE = /(^|\.)cdnjs\.cloudflare\.com$|^fonts\.(googleapis|gstatic)\.com$|(^|\.)wikipedia\.org$|(^|\.)wikimedia\.org$/;

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const isTile = url.hostname === "server.arcgisonline.com";
  const same = url.origin === self.location.origin;
  if (!same && !isTile && !SAVE.test(url.hostname)) return;

  if (isTile){
    // satellite tiles: use a saved copy if we have one, otherwise fetch and keep it
    e.respondWith(caches.open(TILES).then(async cache => {
      const hit = await cache.match(req);
      if (hit) return hit;
      try {
        const res = await fetch(req);
        if (res && (res.ok || res.type === "opaque")) cache.put(req, res.clone()).then(() => trim(cache, 400)).catch(() => {});
        return res;
      } catch (err) { return new Response("", {status: 504}); }
    }));
    return;
  }

  // app, map library, fonts and photos: show the saved copy straight away, refresh it in the background
  e.respondWith(caches.open(APP).then(async cache => {
    const hit = await cache.match(req, {ignoreSearch: same});
    const fresh = fetch(req).then(res => {
      if (res && (res.ok || res.type === "opaque")) cache.put(req, res.clone()).catch(() => {});
      return res;
    }).catch(() => null);
    if (hit) return hit;
    const res = await fresh;
    if (res) return res;
    if (req.mode === "navigate") return (await cache.match("./index.html")) || (await cache.match("./")) || new Response("Offline", {status: 503});
    return new Response("", {status: 504});
  }));
});
