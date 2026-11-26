#!/usr/bin/env python3
# Entry: a newspaper image summarising 25 November 2026 world news.
# render.py renders 53 stories into the approved 1024x1024 entry.png.
# Identical local inputs produce deterministic, byte-identical output.
# Rendering and this output-copy entrypoint require no network access.
"""Copy the approved image to the program/v1 output path (Python 3.13 stdlib)."""

import argparse
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_path", nargs="?", default="/output/entry.png")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent / "entry.png"
    destination = Path(args.output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
