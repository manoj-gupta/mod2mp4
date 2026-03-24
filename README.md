# From Forgotten Camcorder Files to Watchable Memories 🎥

Years ago, I used a Canon FS200 camcorder to capture countless moments—family gatherings, holidays, and most importantly, videos of my kids growing up. Like many camcorders from that era, it recorded videos in the `.MOD` format, accompanied by `.MOI` metadata files.

At the time, everything worked fine. But fast forward to today, and things have changed.

## The Problem

Modern devices—smart TVs, laptops, and even many media players—don’t support `.MOD` files out of the box. Over time, I realized:

* I couldn’t play these videos easily on my TV
* Many apps didn’t recognize the format
* The original recording dates were not visible
* The files just sat there… inaccessible

These weren’t just files—they were memories. And they deserved better.

## The Goal

I wanted a simple way to:

* Convert `.MOD` files into a widely supported format (`.mp4`)
* Preserve the original recording date (from `.MOI` files)
* Process multiple folders easily
* Avoid complex tools or manual steps

## The Solution

This script was built to solve exactly that.

It:

* Converts `.MOD` → `.MP4` using FFmpeg
* Extracts the actual recording date from `.MOI` files
* Applies that timestamp to the output file
* Supports multiple input directories
* Provides a dry-run mode to preview changes
* Produces clean, organized output

## Why `.MOI` Matters

While `.MOD` contains the video, `.MOI` holds metadata—especially the **true recording date**.

Without it:

* You lose the original timeline of your videos
* Files appear with incorrect or random dates

This script reads `.MOI` files and restores that context.

## Example

```
Input:
  MOV00A.MOD
  MOV00A.MOI

Output:
  mp4/your-folder/MOV00A.mp4  (with correct recording date)
```

## Usage

Preview what will happen:

```
./convert_mod dir1 dir2 --dry-run
```

Run the conversion:

```
./convert_mod dir1 dir2
```

Custom output location:

```
./convert_mod dir1 --output-dir ~/Videos/converted
```

## Why This Matters

Old formats shouldn’t lock away meaningful moments.

Technology moves forward—but our memories shouldn’t get left behind because of it.

This script is a small bridge between:

* legacy formats
* modern devices
* and the moments that matter

## Final Thoughts

If you have old camcorder footage sitting in `.MOD` files, you’re not alone. And the good news is—you don’t have to lose access to them.

Convert them, organize them, and most importantly—watch them again.

Because those videos aren’t just files.
They’re your story.
