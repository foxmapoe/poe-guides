#!/usr/bin/env python3
"""Refresh guide layout WebPs from matching PNGs in Layouts/A<n>."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert Layouts/A<n> PNGs to WebP, replacing guide assets with "
            "the same basename in assets/guides/act-n."
        )
    )
    parser.add_argument(
        "acts",
        metavar="ACT",
        type=int,
        nargs="*",
        default=list(range(2, 11)),
        help="acts to process (default: 2 through 10)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=90,
        help="WebP quality from 0 to 100 (default: 90)",
    )
    return parser.parse_args()


def webp_mode(image: Image.Image) -> Image.Image:
    has_alpha = image.mode in ("RGBA", "LA") or "transparency" in image.info
    return image.convert("RGBA" if has_alpha else "RGB")


def main() -> int:
    args = parse_args()
    if not 0 <= args.quality <= 100:
        raise SystemExit("--quality must be between 0 and 100")

    jobs: list[tuple[Path, Path]] = []
    unmatched: list[Path] = []
    ambiguous: list[tuple[Path, list[Path]]] = []

    for act in args.acts:
        source_root = ROOT / "Layouts" / f"A{act}"
        asset_root = ROOT / "assets" / "guides" / f"act-{act}"
        destinations: dict[str, list[Path]] = {}
        for destination in asset_root.rglob("*.webp"):
            destinations.setdefault(destination.stem, []).append(destination)

        for source in sorted(source_root.rglob("*.png")):
            matches = destinations.get(source.stem, [])
            if len(matches) == 1:
                jobs.append((source, matches[0]))
            elif not matches:
                unmatched.append(source)
            else:
                ambiguous.append((source, matches))

    if ambiguous:
        details = "\n".join(
            f"{source}: " + ", ".join(map(str, matches))
            for source, matches in ambiguous
        )
        raise SystemExit("Ambiguous destination assets; no files converted:\n" + details)

    for source, destination in jobs:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            dir=destination.parent,
            suffix=".webp",
            delete=False,
        ) as temporary_file:
            temporary = Path(temporary_file.name)
        try:
            with Image.open(source) as image:
                webp_mode(image).save(
                    temporary,
                    format="WEBP",
                    quality=args.quality,
                    method=6,
                )
            os.replace(temporary, destination)
        finally:
            temporary.unlink(missing_ok=True)

    print(f"Converted {len(jobs)} PNGs to matching guide WebP assets.")
    if unmatched:
        print(f"Skipped {len(unmatched)} PNGs without a matching guide WebP:")
        for source in unmatched:
            print(f"  {source.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
