#!/usr/bin/env python3
"""Preflight WeChat sticker GIFs and known upload artwork dimensions."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from PIL import Image

DEFAULT_LABELS = ["开心", "生气", "委屈", "大笑", "疑问", "好的", "收到", "没问题", "嗯"]
ASSET_SPECS = {
    "聊天页图标.png": (("PNG",), (50, 50), 100 * 1024, "compression threshold shown in supplied guide"),
    "表情封面.png": (("PNG",), (240, 240), 500 * 1024, "compression threshold shown in supplied guide"),
    "详情页横幅.jpg": (("JPEG", "PNG"), (750, 400), 500 * 1024, "compression threshold shown in supplied guide"),
    "主页横幅.jpg": (("JPEG", "PNG"), (750, 400), 80 * 1024, "maximum shown in artist-profile guide"),
    "头像.png": (("PNG", "JPEG"), (640, 640), 500 * 1024, "maximum shown in artist-profile guide"),
}
APPRECIATION_NAMES = ("赞赏引导图.png", "赞赏引导图.jpg", "赞赏致谢图.png", "赞赏致谢图.jpg", "感谢.png", "感谢.jpg")

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", type=Path, help="Album folder containing GIFs and optional 投稿素材 folder")
    parser.add_argument("--labels", nargs="+", help="Ordered sticker meanings (9 to 12); file names are NN-label.gif")
    args = parser.parse_args()
    labels = args.labels or DEFAULT_LABELS
    if not 9 <= len(labels) <= 12:
        parser.error("provide between 9 and 12 labels")
    root = args.pack
    if not root.is_dir():
        print(f"ERROR: folder does not exist: {root}")
        return 2
    errors: list[str] = []
    notes: list[str] = []
    common_size = None
    for index, label in enumerate(labels, 1):
        path = root / f"{index:02d}-{label}.gif"
        if not path.is_file():
            errors.append(f"missing sticker: {path.name}")
            continue
        try:
            with Image.open(path) as im:
                if im.format != "GIF":
                    errors.append(f"{path.name}: expected GIF, got {im.format}")
                    continue
                if getattr(im, "n_frames", 1) < 2:
                    errors.append(f"{path.name}: must contain multiple frames")
                if im.info.get("loop") != 0:
                    errors.append(f"{path.name}: expected infinite loop (GIF loop=0)")
                if im.width != im.height:
                    errors.append(f"{path.name}: expected square canvas, got {im.size}")
                if common_size is None:
                    common_size = im.size
                elif im.size != common_size:
                    errors.append(f"{path.name}: inconsistent dimensions {im.size}; expected {common_size}")
                notes.append(f"GIF {path.name}: {im.width}x{im.height}, {im.n_frames} frames, {path.stat().st_size:,} bytes")
        except Exception as exc:
            errors.append(f"{path.name}: cannot read image ({exc})")

    assets = root / "投稿素材"
    for name, (formats, dimensions, limit, reason) in ASSET_SPECS.items():
        path = assets / name
        if not path.exists():
            continue
        try:
            with Image.open(path) as im:
                if im.format not in formats:
                    errors.append(f"{name}: expected {formats}, got {im.format}")
                if im.size != dimensions:
                    errors.append(f"{name}: expected {dimensions[0]}x{dimensions[1]}, got {im.width}x{im.height}")
                size = path.stat().st_size
                if size > limit:
                    notes.append(f"SIZE NOTE {name}: {size:,} bytes exceeds {limit:,} ({reason})")
                else:
                    notes.append(f"OK {name}: {im.width}x{im.height}, {size:,} bytes")
        except Exception as exc:
            errors.append(f"{name}: cannot read image ({exc})")

    for name in APPRECIATION_NAMES:
        path = assets / name
        if path.exists():
            try:
                with Image.open(path) as im:
                    if im.format not in ("PNG", "JPEG"):
                        errors.append(f"{name}: expected PNG or JPEG, got {im.format}")
                    notes.append(f"APPRECIATION {name}: {im.width}x{im.height}, {path.stat().st_size:,} bytes; confirm current page limits")
            except Exception as exc:
                errors.append(f"{name}: cannot read image ({exc})")
    for note in notes:
        print(note)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} issue(s)")
        return 1
    print(f"PASS: {len(labels)} GIF files are structurally valid. Inspect all artwork and current platform rules before upload.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
