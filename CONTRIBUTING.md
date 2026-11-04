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

Store images in a folder matching each guide's act and area slug. For example, images for `_guides/act-1/coast.md` go in `assets/guides/act-1/coast/`. Use clear, consistent filenames such as `route-map.webp` and `landmarks.webp`.

Use WebP for guide images and keep each file at most 1 MiB. To compress staged guide images automatically before committing, install the image tool dependency and enable the repository hook once:

```sh
python3 -m pip install -r tools/requirements.txt
git config core.hooksPath .githooks
```

The hook re-encodes staged WebP images larger than 1 MiB at quality 90 and stages the smaller result. If you upload images through GitHub or skip the hook, the pull request image check enforces the format and size limit. To compress selected files without staging them, pass their paths to `python3 tools/compress_images.py`.

Open the matching folder in GitHub and choose **Add file → Upload files**. Link each image from the relevant section of the guide using `relative_url`, and write alt text that describes the route information shown:

```markdown
![Coast route from the Twilight Strand entrance to the Mud Flats exit, with the waypoint marked.]({{ '/assets/guides/act-1/coast/route-map.webp' | relative_url }})
```

Keep images focused on the information needed to follow the route and readable on mobile.

You can also open an issue and attach an image there if you need help adding it to the repository.

## Guide checklist

- The area name and act are correct.
- Route steps use clear landmarks and explain the next exit or destination.
- The game version and last checked date are current.
- Images have descriptive alt text and are readable on mobile.
- Screenshots do not contain personal information.
