#!/usr/bin/env python3

import os
import re
import subprocess
import argparse
from datetime import datetime

def extract_date_from_moi(moi_path):
    try:
        with open(moi_path, "rb") as f:
            data = f.read().decode(errors="ignore")

        match = re.search(r"\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}", data)
        if match:
            return datetime.strptime(match.group(0), "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Failed to read MOI: {moi_path} ({e}")
    return None


def collect_mod_files(input_dirs):
    mod_files = []
    for input_dir in input_dirs:
        input_dir = os.path.abspath(input_dir)

        if not os.path.isdir(input_dir):
            print(f"Skipping invalid directory: {input_dir}")
            continue

        for file in os.listdir(input_dir):
            if file.lower().endswith(".mod"):
                mod_files.append((input_dir, os.path.join(input_dir, file)))
    return mod_files


def convert_mod_to_mp4(input_dirs, output_root, dry_run=False):
    mod_files = collect_mod_files(input_dirs)
    total = len(mod_files)

    if total == 0:
        print("No .MOD files found.")
        return

    print(f"Found {total} file(s)\n")

    for idx, (input_dir, mod_path) in enumerate(mod_files, start=1):
        base_name = os.path.splitext(os.path.basename(mod_path))[0]
        moi_path = os.path.join(input_dir, base_name + ".MOI")

        dir_name = os.path.basename(os.path.normpath(input_dir))
        output_dir = os.path.join(output_root, dir_name)
        output_path = os.path.join(output_dir, base_name + ".mp4")

        print(f"[{idx}/{total}] {mod_path}")
        print(f"  → {output_path}")

        if dry_run:
            print("  🔍 Dry run\n")
            continue

        os.makedirs(output_dir, exist_ok=True)

        command = [
            "ffmpeg",
            "-loglevel", "error",   # ✅ suppress most output
            "-i", mod_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            output_path
        ]

        try:
            subprocess.run(command, check=True)

            recording_date = extract_date_from_moi(moi_path) if os.path.exists(moi_path) else None

            if recording_date:
                ts = recording_date.timestamp()
                os.utime(output_path, (ts, ts))
            else:
                stat = os.stat(mod_path)
                os.utime(output_path, (stat.st_atime, stat.st_mtime))

        except subprocess.CalledProcessError:
            print(f"  ❌ Error converting {mod_path}")

        print()

    print("🎉 Done." if not dry_run else "🔍 Dry run complete.")


def main():
    parser = argparse.ArgumentParser(
        prog="convert_mod",
        description="Convert .MOD/.MOI to .MP4"
    )

    parser.add_argument(
        "input_dirs",
        nargs="+",
        help="Input directories"
    )

    parser.add_argument(
        "--output-dir",
        default="./mp4",
        help="Output directory (default: ./mp4)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview only"
    )

    args = parser.parse_args()

    convert_mod_to_mp4(
        args.input_dirs,
        os.path.abspath(args.output_dir),
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
