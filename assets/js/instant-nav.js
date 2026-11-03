(() => {
  const pages = new Map();

  const internal = (link) =>
    link && link.origin === location.origin && !link.target && !link.hasAttribute("download") &&
    !/\.\w+$/.test(link.pathname);

  const warmImages = (doc) => {
    doc.querySelectorAll(".guide-content img").forEach((image, i) => {
      if (i < 6) new Image().src = new URL(image.getAttribute("src"), location.href).href;
    });
  };

  const load = (url) => {
    const key = url.split("#")[0];
    if (!pages.has(key)) {
      pages.set(key, fetch(key)
        .then((response) => {
          if (!response.ok) throw new Error(response.status);
          return response.text();
        })
        .then((html) => {
          const doc = new DOMParser().parseFromString(html, "text/html");
          warmImages(doc);
          return doc;
        })
        .catch((error) => {
          pages.delete(key);
          throw error;
        }));
    }
    return pages.get(key);
  };

  const swap = (doc, url) => {
    const sidebar = document.querySelector(".sidebar");
    const scroll = sidebar?.scrollTop ?? 0;
    document.getElementById("main").replaceWith(document.importNode(doc.getElementById("main"), true));
    document.title = doc.title;
    const nextSidebar = document.querySelector(".sidebar");
    if (nextSidebar) nextSidebar.scrollTop = scroll;
    const hash = new URL(url).hash;
    const target = hash && document.getElementById(decodeURIComponent(hash.slice(1)));
    if (target) target.scrollIntoView();
    else window.scrollTo(0, 0);
    document.dispatchEvent(new Event("guide:load"));
  };

  const go = async (url, push) => {
    try {
      const doc = await load(url);
      if (!doc.getElementById("main")) throw new Error("main");
      if (push) history.pushState(null, "", url);
      swap(doc, url);
    } catch (_) {
      location.href = url;
    }
  };

  const prefetch = (event) => {
    const link = event.target.closest?.("a[href]");
    if (internal(link) && link.pathname !== location.pathname) load(link.href);
  };

  document.addEventListener("pointerover", prefetch, { passive: true });
  document.addEventListener("touchstart", prefetch, { passive: true });
  document.addEventListener("focusin", prefetch);

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[href]");
    if (!internal(link) || event.defaultPrevented || event.button !== 0 ||
        event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (link.pathname === location.pathname && link.hash) return;
    event.preventDefault();
    go(link.href, true);
  });

  history.scrollRestoration = "manual";
  window.addEventListener("popstate", () => go(location.href, false));
})();
