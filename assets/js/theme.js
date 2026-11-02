(() => {
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  if (!toggle) return;

  const currentTheme = () => (root.dataset.theme === "light" ? "light" : "dark");
  const updateLabel = () => {
    toggle.textContent = currentTheme() === "dark" ? "Light mode" : "Dark mode";
  };

  updateLabel();
  toggle.addEventListener("click", () => {
    const nextTheme = currentTheme() === "dark" ? "light" : "dark";
    if (nextTheme === "dark") {
      delete root.dataset.theme;
    } else {
      root.dataset.theme = nextTheme;
    }
    try {
      localStorage.setItem("poe-guides-theme", nextTheme);
    } catch (_) {}
    updateLabel();
  });
})();
