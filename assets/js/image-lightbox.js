(() => {
  const dialog = document.getElementById("image-lightbox");
  const expandedImage = dialog?.querySelector("img");
  const closeButton = dialog?.querySelector(".image-lightbox-close");
  const guideImages = document.querySelectorAll(".guide-content img");

  if (!dialog || !expandedImage || !closeButton || guideImages.length === 0) return;

  let activeTrigger = null;

  guideImages.forEach((image) => {
    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "guide-image-zoom";
    trigger.setAttribute("aria-haspopup", "dialog");
    trigger.setAttribute("aria-label", `Enlarge image: ${image.alt || "Guide image"}`);
    image.parentNode.replaceChild(trigger, image);
    trigger.append(image);

    trigger.addEventListener("click", () => {
      activeTrigger = trigger;
      expandedImage.src = image.currentSrc || image.src;
      expandedImage.alt = image.alt;
      dialog.showModal();
      closeButton.focus();
    });
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
