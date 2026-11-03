(() => {
  const dialog = document.getElementById("image-lightbox");
  const expandedImage = dialog?.querySelector("img");
  const closeButton = dialog?.querySelector(".image-lightbox-close");

  if (!dialog || !expandedImage || !closeButton) return;

  let activeTrigger = null;
  let triggers = [];
  const fullSrc = (image) => image.dataset.full ? new URL(image.dataset.full, location.href).href : image.currentSrc || image.src;
  const warm = (image) => { if (image.dataset.full) new Image().src = fullSrc(image); };

  const show = (trigger) => {
    const image = trigger.querySelector("img");
    activeTrigger = trigger;
    expandedImage.src = fullSrc(image);
    expandedImage.alt = image.alt;
  };

  const bind = () => {
    triggers = [];
    document.querySelectorAll(".guide-content img").forEach((image) => {
      const trigger = document.createElement("button");
      trigger.type = "button";
      trigger.className = "guide-image-zoom";
      trigger.setAttribute("aria-haspopup", "dialog");
      trigger.setAttribute("aria-label", `Enlarge image: ${image.alt || "Guide image"}`);
      image.parentNode.replaceChild(trigger, image);
      trigger.append(image);
      triggers.push(trigger);

      trigger.addEventListener("pointerenter", () => warm(image), { once: true });
      trigger.addEventListener("focus", () => warm(image), { once: true });
      trigger.addEventListener("click", () => {
        show(trigger);
        dialog.showModal();
        closeButton.focus();
      });
    });
  };

  bind();
  document.addEventListener("guide:load", bind);

  dialog.addEventListener("keydown", (event) => {
    const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
    if (!step || !activeTrigger) return;
    event.preventDefault();
    const next = triggers[(triggers.indexOf(activeTrigger) + step + triggers.length) % triggers.length];
    show(next);
    warm(triggers[(triggers.indexOf(next) + step + triggers.length) % triggers.length].querySelector("img"));
  });

  closeButton.addEventListener("click", () => dialog.close());

  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });

  dialog.addEventListener("close", () => {
    expandedImage.removeAttribute("src");
    activeTrigger?.focus();
    activeTrigger = null;
  });
})();
