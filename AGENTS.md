# Project guidance

## Project shape

- This is a static Jekyll site published from the repository root with GitHub Pages. Keep runtime behavior and content static; avoid adding a server or build service.
- `_guides/` is the Jekyll `guides` collection. `_layouts/default.html` provides the page shell, `_layouts/guide.html` renders guide pages, and `_includes/guide-navigation.html` builds the act and zone sidebar.
- `_data/acts.yml` defines the acts shown in navigation and on the index. Keep those labels and act numbers consistent with guide front matter.
- Use `relative_url` for internal page and asset links so the site works with both a root domain and a GitHub Pages project `baseurl`.

## Writing guides

- Start from `templates/guide.md`; add each page at `_guides/act-<number>/<short-slug>.md`.
- Set `title` to the displayed zone name, `act` to a quoted act number such as `"1"`, `order` to a numeric position within the act, and `game_version` to the version the route was checked against. `updated` is optional and should use `YYYY-MM-DD`.
- The `order` field controls both the homepage list and sidebar order. Keep values unique and in campaign route order. Act 1 currently follows the sequence represented by its guide pages.
- Use Markdown headings for route, landmarks, useful details, and maps. Keep directions specific and distinguish verified information from draft notes; do not invent route details.
- Store images under `assets/guides/act-<number>/<area-slug>/`, matching the guide path. Link them with `relative_url`, provide useful alt text, and keep images focused and reasonably small.
- Update `CONTRIBUTING.md` if guide metadata or contribution steps change.

## Navigation and accessibility

- The sidebar uses native `<details>` and `<summary>` elements so acts expand independently without JavaScript. Preserve keyboard operation, visible focus, and the active zone's `aria-current="page"` marker.
- Keep text and background colors at WCAG AA contrast: at least 4.5:1 for normal text and 3:1 for large text. Check hover, visited, selected, and muted text states against their actual backgrounds.
- Scope header navigation styles to `.header-inner nav`; a generic `nav a` selector also affects the campaign sidebar. Give sidebar links explicit readable colors.
- Define shared colors in `assets/css/site.css` and avoid opacity that reduces text contrast.
- Dark mode is the default. Keep dark tokens on `:root` and light overrides under `:root[data-theme="light"]`; the header toggle and saved preference are managed by `assets/js/theme.js`.

## Local development and publishing

- On systems where gems cannot be installed system-wide, configure a project-local Bundler path once:

  ```sh
  bundle config set --local path vendor/bundle
  bundle install
  bundle exec jekyll serve --livereload
  ```

- Keep `vendor` excluded in `_config.yml`; otherwise Jekyll may try to render installed gem files as site content. `.bundle/`, `vendor/bundle/`, `_site/`, and `.jekyll-cache/` are local/generated files and should stay out of Git.
- Verify site changes with `bundle exec jekyll build`.
- `.github/workflows/pages.yml` builds the site with the Jekyll dependency locked in `Gemfile.lock` and deploys it from the `main` branch. In GitHub repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
- For a project URL such as `https://OWNER.github.io/REPO/`, set `baseurl: "/REPO"` in `_config.yml`. Keep it empty for a root domain or custom domain.
