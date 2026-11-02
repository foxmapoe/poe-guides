---
layout: default
title: Contribute
permalink: /CONTRIBUTING/
---

# Contribute a guide or correction

Guides are Markdown files, so you can propose edits directly in GitHub without installing anything.

## Edit a guide in your browser

1. Open the guide file in the repository and select the pencil icon.
2. Make your changes using Markdown. Keep route steps short and name visible landmarks.
3. Preview the change, then select **Propose changes** to open a pull request.
4. In the pull request description, mention the game version and what you changed.

## Add a guide

1. Copy `templates/guide.md` into `_guides/act-<number>/`, and name it with a short lowercase area slug, such as `the-coast.md`.
2. Fill in the title, act number, numeric order within the act, current game version, and last checked date in the front matter. Match the zone order used in the campaign.
3. Replace the example sections with the route details. Remove sections that do not apply.
4. Propose the new file in a pull request.

## Add images

Upload images under `assets/guides/<area-slug>/` using **Add file → Upload files** in GitHub. Link them from the guide using a site-relative path, and include descriptive alt text. Keep images focused on the information needed to follow the route and compress large files before uploading.

You can also open an issue and attach an image there if you need help adding it to the repository.

## Guide checklist

- The area name and act are correct.
- Route steps use clear landmarks and explain the next exit or destination.
- The game version and last checked date are current.
- Images have descriptive alt text and are readable on mobile.
- Screenshots do not contain personal information.
