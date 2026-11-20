# SatisfyCloud logo kit

Brand colours
- Satisfy Blue  #0B63F6  (rgb 11,99,246)
- Ink           #0B1220  (text on light)
- White         #FFFFFF
- Mist          #F4F7FF  (light background)
- Black         #000000  (one-colour print)

Folders (all files are in `dist/`)
- `svg/`  master vector files (outlined paths, no fonts needed): mark_*, mark-tight_*, lockup-horizontal*, lockup-stacked*, each in colour / blue / white / black / on-background variants. `-com` = with ".com"
- `png/`  transparent PNGs (marks 64-1024 px, lockups 2400 px wide) and on-background versions
- `jpg/`  white-background JPGs of the colour lockups
- `pdf/`  vector PDFs of the lockups
- `web/`  favicon.ico / favicon.svg (small-size mark with a wider gap), apple-touch-icon, android + maskable icons, app icons, circle avatar, OG image 1200x630, site.webmanifest, head-snippet.html

Usage rules
- Mark alone for avatars, favicons, app icons; mark + text for headers, documents, packaging.
- Keep clear space around the logo equal to the height of the mark's S-gap bend (~ 1/4 of the mark height).
- Minimum size: mark 16 px (use favicon.svg below 32 px), horizontal lockup 120 px wide.
- The wordmark is set in Inter Display Bold, converted to outlines. Replace it with a custom-drawn wordmark later if wanted; the mark does not change.
- `build/` holds the Python scripts that generate every file (`kit.py`, `export.py`).
