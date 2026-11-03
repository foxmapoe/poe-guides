#!/usr/bin/env python3
"""Compress staged guide WebP images, or check images changed in a pull request."""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGE_ROOT = ROOT / "assets" / "guides"
MAX_BYTES = 1024 * 1024
RASTER_SUFFIXES = {".webp", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff"}


def git_paths(*args):
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE
    )
    return [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]


def changed_images(base):
    paths = git_paths("diff", "--name-only", "-z", "--diff-filter=ACM", f"{base}...HEAD")
    return [path for path in paths if Path(path).suffix.lower() in RASTER_SUFFIXES]


def guide_image(path):
    file_path = (ROOT / path).resolve()
    return file_path.is_relative_to(IMAGE_ROOT) and file_path.is_file()


def encoded_copy(image_path):
    from PIL import Image

    with tempfile.NamedTemporaryFile(suffix=".webp", dir=image_path.parent, delete=False) as tmp:
        temp_path = Path(tmp.name)
    try:
        with Image.open(image_path) as image:
            image.save(temp_path, "WEBP", quality=90, method=6)
        return temp_path
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def compress(path, stage=True):
    image_path = ROOT / path
    if image_path.suffix.lower() != ".webp":
        print(f"{path}: guide images must use WebP format", file=sys.stderr)
        return False

    if not guide_image(path):
        return True

    if image_path.stat().st_size <= MAX_BYTES:
        return True

    temp_path = encoded_copy(image_path)
    try:
        if temp_path.stat().st_size < image_path.stat().st_size:
            temp_path.chmod(image_path.stat().st_mode)
            temp_path.replace(image_path)
            print(f"Compressed {path}")
        else:
            print(f"Already compact: {path}")
    finally:
        temp_path.unlink(missing_ok=True)

    if stage:
        subprocess.run(["git", "add", "--", path], cwd=ROOT, check=True)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-changed", metavar="BASE", help="check changed pull-request images against a base commit")
    parser.add_argument("paths", nargs="*", help="guide image paths to compress instead of staged images")
    args = parser.parse_args()

    if args.check_changed:
        if args.paths:
            parser.error("image paths cannot be combined with --check-changed")
        paths = [path for path in changed_images(args.check_changed) if guide_image(path)]
        invalid = [path for path in paths if Path(path).suffix.lower() != ".webp"]
        oversized = [path for path in paths if (ROOT / path).stat().st_size > MAX_BYTES]
        for path in invalid:
            print(f"{path}: convert guide images to WebP before submitting", file=sys.stderr)
        for path in oversized:
            print(f"{path}: exceeds the 1 MiB limit; run `python3 tools/compress_images.py` and commit the result", file=sys.stderr)
        return 1 if invalid or oversized else 0

    stage = not args.paths
    if args.paths:
        paths = args.paths
        invalid = [path for path in paths if not guide_image(path) or Path(path).suffix.lower() != ".webp"]
    else:
        staged = git_paths("diff", "--cached", "--name-only", "-z", "--diff-filter=ACM")
        paths = [path for path in staged if Path(path).suffix.lower() == ".webp"]
        invalid = [path for path in staged
                   if Path(path).suffix.lower() in RASTER_SUFFIXES - {".webp"} and guide_image(path)]
    if invalid:
        for path in invalid:
            print(f"{path}: convert guide images to WebP before committing", file=sys.stderr)
        return 1

    unstaged = [] if args.paths else [path for path in paths if subprocess.run(
        ["git", "diff", "--quiet", "--", path], cwd=ROOT
    ).returncode != 0]
    if unstaged:
        for path in unstaged:
            print(f"{path}: stage or discard working-tree changes before image compression", file=sys.stderr)
        return 1

    ok = True
    for path in paths:
        ok = compress(path, stage=stage) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
