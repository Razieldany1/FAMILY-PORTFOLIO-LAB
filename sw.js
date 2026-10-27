// FAMILY PORTFOLIO LAB v1.6B — Cloudflare root navigation fix
const CACHE = 'family-portfolio-lab-v2-0-3-ui-fix';
const PREFIX = 'family-portfolio-lab-';
const ASSETS = ['/', '/style.css', '/app.js', '/manifest.webmanifest', '/icon.svg', '/icon-192.png', '/icon-512.png'];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(key => key.startsWith(PREFIX) && key !== CACHE).map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);
  if (request.method !== 'GET' || url.origin !== self.location.origin) return;
  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const response = await fetch('/');
        if (response.ok) return response;
      } catch (_) { /* offline fallback */ }
      const cache = await caches.open(CACHE);
      return (await cache.match('/')) || Response.error();
    })());
    return;
  }
  event.respondWith((async () => {
    try {
      const response = await fetch(request);
      if (response.ok) return response;
    } catch (_) { /* offline fallback */ }
    return (await caches.match(request)) || Response.error();
  })());
});
