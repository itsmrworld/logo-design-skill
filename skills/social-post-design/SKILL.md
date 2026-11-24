---
name: social-post-design
description: Design high-graphics social media posts, Facebook covers and stories for a hosting / cloud / SaaS brand (SatisfyCloud) from a short brief or from competitor example images. Use when the user asks for a post, cover photo, story, banner or ad graphic, shares example ads to learn from, or wants a design that matches a caption. Contains the brand constants, the patterns learned from reference ads, platform safe zones, working HTML/Playwright templates and the mistakes to avoid.
---

# Social post design (SatisfyCloud)

You act as a senior social/ad designer. Deliver finished PNGs, not mock-ups, and **look at every render** before replying.
Reply in the user's language (Bengali is fine), but **text inside the graphics is English** unless told otherwise.

## Workflow
1. Read the brief + caption. The graphic's text must match the caption (same locations, same features, same CTA).
2. If example images are attached, read `references/examples.md`, add what is new about them (layout, hero visual, type, colour, psychology) and then design something *better and different*, never a copy.
3. Pick a template in `templates/`, adapt the text/data, render with Playwright (Chromium is pre-installed; `executable_path=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`, `args=['--no-sandbox']`), view the PNG, iterate until nothing is clipped/overlapping.
4. Write the caption file next to the images (English + Bengali), commit, push.
5. Say plainly what is assumed (claims, feature names) and what was not verified.

## Brand constants
- Logo mark: `satisfycloud/dist/svg/mark-tight_white.svg` (single path, recolour with `fill`). Wordmark = "SatisfyCloud", Inter Display Bold, tracking -0.03em.
- Colours: brand blue `#0B63F6`; for the VPS/network series `#1A73E8` (user-specified); ink `#0B1220`; deep navy `#02081f`; green status `#2ee59d`/`#12a05c`.
- Fonts available on the box: Inter / Inter Display only (no Bengali font → keep Bengali out of images; put it in captions).
- Include `<meta charset="utf-8">` in every HTML (otherwise arrows/dashes break).

## What the reference ads do (learn from, don't copy)
See `references/examples.md`. In short: one dominant hero visual (server rack / dashboard), a big high-contrast headline, a *blue highlight box* behind the key phrase, a pill grid of specs, a solid blue contact bar at the bottom, soft glow and reflections. We add: real world-map data viz, 3D CSS racks, glass UI, orbit/hub diagrams.

## Rules
- Never put prices unless the user supplies them. Never invent stats, phone numbers, plans. Brief-supplied claims ("6 hubs", "60 seconds") may be used but flag them as unverified.
- One focal point, generous breathing room, max 2 typefaces weights families, 3 colours + neutrals.
- Do not reuse the same hero visual across cover and post (the user notices).
- **Facebook cover** 2000×1125 (16:9). Safe zone for all views: x 150-1850, y 230-920 (mobile web crops to ~2.7:1 centred; desktop ~2.63:1). Keep bottom-left clear of key content (profile photo on app). Preview all crops before delivering (`preview-desktop-mobile.png`).
- **Square post** 1080×1080 (export @2x). **Story** 1080×1920: keep key content inside y 250-1670 (top profile bar, bottom reply bar).
- Check with the user's own screenshots if they send them; they are the ground truth for how it displays.

## Technique notes
- 3D server rack: CSS cuboid (`transform-style:preserve-3d`, front/left/right/top faces with `backface-visibility:hidden`, `rotateY(-34deg)`). Fill units with bay slots + LED dots.
- Dotted world map: `pip install global-land-mask`; sample land on a lat/lon grid, project into a trapezoid (tilt), draw hubs with real lon/lat, arcs as parabolas.
- Glass UI: `rgba(255,255,255,.1)` + border + `backdrop-filter:blur`, inner top highlight, soft coloured shadow.
- Giant background word behind the hero (gradient fading to transparent) gives instant "premium ad" depth.
- Always remove hard-edged gradient bands, clipped blur filters (give `filter` an enlarged region) and text that touches borders.

## Templates (all read the logo path at the top; adjust `../dist/svg/...` to where the logo kit lives)
- `cover-3d-dashboard.py`  dark cinematic cover with tilted dashboard + phone + floating cards (+ light orbit post inside).
- `cover-orbit-hero.py`    light cover/post with glowing cloud hero and orbiting feature chips.
- `story-dotted-world-map.py` 1080×1920 story: space background, dotted world map, hub arcs, callouts, feature cards, CTA.
- `post-hero-server-rack.py` 1080×1080 dark ad: giant "VPS" word, 3D rack, six location pills, spec grid, contact bar.
- `post-light-orbit-cards.py` 1080×1080 light "Global VPS" post with server core + six location pills.

## Using the website's own data and imagery
- When the user shares screenshots of satisfycloud.com (the live site is not reachable from this box), read prices/labels from them at zoom (crop + upscale) and **verify each number** before using it.
- Pricing posts: show first-year price, label it clearly, and add a fine-print line that renewal/transfer prices apply later (the site lists them). Never claim "up to X%" unless that is the maximum on the site.
- Website imagery may be reused as a background (crop from the screenshot, upscale, blur slightly, `mix-blend-mode:screen` on a dark background, radial mask to fade edges). Saved in `satisfycloud/social/assets/`.
- Template: `post-domain-pricing-dark.py` (popular TLD table, "included with every domain" feature cards, website portrait glow, bottom bar). For domain posts show POPULAR extensions (.com .net .org + popular cheap ones), never obscure ones like .cfd as the headline.
