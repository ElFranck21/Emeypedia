const CACHE_NAME = 'emeypedia-v1';
const OFFLINE_URL = '/static/pwa/offline.html';
const INDEX_URL = '/';
const ASSETS = [
  INDEX_URL,
  OFFLINE_URL,
  '/static/pwa/manifest.json',
  '/static/pwa/icons/icon-192.png',
  '/static/css/index.css',
  '/static/assets/banner1.png',
];

// Instalación: cache de assets esenciales
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Activación: limpia caches antiguos
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: navegación y recursos estáticos
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => caches.match(OFFLINE_URL))
    );
    return;
  }

  // Cache-first para recursos estáticos
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(resp => {
        caches.open(CACHE_NAME).then(cache => {
          try { cache.put(event.request, resp.clone()); } catch(e){}
        });
        return resp;
      }).catch(() => {
        if (event.request.destination === 'image') {
          return caches.match('/static/pwa/icons/icon-192.png');
        }
      });
    })
  );
});
