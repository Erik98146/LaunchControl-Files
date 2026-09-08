# Editing the LaunchControl User Guide

The published guide is `index.html` in the repo root. **Never edit that file by hand** — it is
generated. Edit the files in this folder, then rebuild:

```
python guide/build_guide.py
```

That rewrites `index.html`. Open it in a browser to check, then commit both the sources
and the rebuilt `index.html` (GitHub serves the built file).

One-time setup on a new machine: `pip install markdown pillow`.

A rendered copy of this page with live examples is `README.html` (open it in a browser).
Regenerate it after editing this file with `python guide/build_guide.py --readme`.

## What lives where

| Path | What it is |
|---|---|
| `guide.cfg` | Title, version, date, hero picture, the dark "Start here" box, image settings |
| `chapters/NN-name.md` | One file per chapter. Chapters are ordered by the `NN-` prefix; the number in the page is assigned at build time |
| `images/` | Every picture used in the guide. Add new ones here |
| `template.html` | The page skeleton and the stylesheet. This is where the look lives; you rarely touch it |
| `build_guide.py` | The build script |

## Chapters and sections

```markdown
# Install & Quick Start            ← the chapter title (exactly one per file)

::: lead
One or two sentences shown large under the chapter title.
:::

## Install the Hub                 ← a numbered section (2.1, 2.2, …)

### Schedules                      ← an unnumbered sub-section
```

To **add a chapter**, create a new file such as `07b-the-touch-8-display.md` or renumber the
prefixes; the table of contents and chapter numbers follow the file order automatically.
To **remove a chapter**, delete its file. Links to a chapter use its title, lower-cased with
hyphens: `[see Security](#security)`.

## Text

Plain paragraphs separated by a blank line. `**bold**`, `*italic*`,
`[link text](https://example.com)`. Links starting with `https://` open in a new tab.
A `- ` at the start of a line makes a bullet. A `> ` makes a quotation.

## Numbered steps (the blue circles)

Any numbered list becomes the step cards. Put the step title in bold first:

```markdown
1. **Connect RV-C.** Connect the Hub to the coach's RV-C bus.
2. **Connect power.** Use either 12–24 V or USB-C, never both.
```

## Colored boxes

```markdown
::: note "Wi-Fi compatibility"
The blue box. The title in quotes is optional.
:::

::: warning "Connection types vary by RV"
The orange box.
:::

::: technical
The dark expandable "Technical detail (optional)" box.
Give it a different heading with:  ::: technical "Some other heading"
:::
```

Delete the three lines to remove a box. A box may contain several paragraphs, bullets or a
table.

## Pictures

Put the file in `images/`, then on a line of its own:

```markdown
![Alt text for screen readers](images/floor-plan-page.png)
![Alt text](images/hub-wiring.png "The caption shown under the picture")
![Alt text](images/dashboard.png "")
```

- With no quoted caption, the alt text is used as the caption.
- An empty caption `""` shows the picture with no caption.
- A row of small pictures side by side (up to three per row) is a gallery:

```markdown
::: gallery "Initial setup"
![Step 1](images/setup-1.png)
![Step 2](images/setup-2.png)
![Step 3](images/setup-3.png)
:::
```

Large PNG screenshots are re-encoded as WebP inside the built page (the files in `images/`
are never changed). `guide.cfg` sets the size threshold and quality; `--no-webp` turns it off.

## Tables

```markdown
| Component | What it does |
| --- | --- |
| LaunchControl Hub | The central controller. |
| Web Dashboard | The browser interface. |
```

Use `<br>` inside a cell for a line break. Bold and links work inside cells.

The grouped card-binding table in Chapter 4 has its own block:

```markdown
::: bindings
### Inverter
| Card element | DGN name | DGN | Field |
| Watts | Inverter Out Power | 1FFD5 | Real Power |
Note: any plain line becomes an italic note row.

### Shore Power
| Card element | DGN name | DGN | Field |
| Watts | Charger Input Power | 1FFC8 | Real Power |
:::
```

## Version and date

In `guide.cfg`: `version = 0.4` and `date = auto` (today's date at build time) or a fixed
date such as `date = August 30, 2026`.

## If the build prints a WARNING

It names the file and the problem (an unclosed `:::`, a missing picture, an unknown box
type). Fix it and build again; the page is still written so you can look at it.
