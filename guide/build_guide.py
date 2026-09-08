#!/usr/bin/env python3
"""Build the LaunchControl User Guide.

    python guide/build_guide.py            # writes ../index.html
    python guide/build_guide.py --out x.html
    python guide/build_guide.py --no-webp  # keep every image byte-for-byte

Sources (all under guide/):
    guide.cfg          page settings: title, version, date, hero image, Start-here box
    chapters/NN-*.md   one Markdown file per chapter, in filename order
    images/            pictures referenced from the chapters
    template.html      page skeleton + stylesheet (the "style" lives here)

See guide/README.md for the Markdown syntax the chapters use.
"""
import argparse
import base64
import configparser
import datetime as dt
import html
import io
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit('The "markdown" package is missing. Run:  pip install markdown pillow')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

MD_EXT = ['tables']


# --------------------------------------------------------------------------- helpers
def md(text):
    """Markdown -> HTML for a body of ordinary text (paragraphs, lists, tables, links)."""
    out = markdown.markdown(text.strip(), extensions=MD_EXT, output_format='html')
    out = ol_to_steps(out)
    out = re.sub(r'<table>', '<div class="lc-table-wrap"><table>', out)
    out = re.sub(r'</table>', '</table></div>', out)
    out = re.sub(r'<a href="(https://[^"]*)">', r'<a href="\1" rel="noopener" target="_blank">', out)
    return out


def ol_to_steps(h):
    """Every numbered list becomes the numbered step cards."""
    def one(m):
        items = re.findall(r'<li>(.*?)</li>', m.group(1), re.S)
        cards = []
        for i, body in enumerate(items, 1):
            body = body.strip()
            body = re.sub(r'^<p>(.*)</p>$', r'\1', body, flags=re.S)
            t = re.match(r'<strong>(.*?)</strong>\s*(.*)$', body, re.S)
            if t:
                inner = f'<strong class="lc-step__title">{t.group(1)}</strong> {t.group(2)}'.rstrip()
            else:
                inner = body
            cards.append(f'<p class="lc-step"><span class="lc-step__number">{i}</span>'
                         f'<span class="lc-step__content">{inner}</span></p>')
        return '\n'.join(cards)
    return re.sub(r'<ol>(.*?)</ol>', one, h, flags=re.S)


_ids = set()


def slugify(text):
    """Heading -> id, Pandoc style, unique across the document."""
    s = html.unescape(text).lower()
    s = re.sub(r'[^\w\s.\-]', '', s, flags=re.U)
    s = re.sub(r'\s+', '-', s).strip('-')
    s = re.sub(r'^[^a-z]+', '', s) or 'section'
    base, n = s, 1
    while s in _ids:
        n += 1
        s = f'{base}-{n - 1}'
    _ids.add(s)
    return s


def inline_md(text):
    """Inline Markdown (bold, links) for headings/captions -> HTML without the <p>."""
    h = markdown.markdown(text.strip(), output_format='html')
    return re.sub(r'^<p>(.*)</p>$', r'\1', h.strip(), flags=re.S)


# --------------------------------------------------------------------------- images
class Images:
    def __init__(self, cfg, webp):
        self.threshold = cfg.getint('images', 'webp_threshold_kb', fallback=150) * 1024 if webp else 0
        self.quality = cfg.getint('images', 'webp_quality', fallback=88)
        self.cache = {}
        self.stats = []
        self.pil = None
        if self.threshold:
            try:
                from PIL import Image
                self.pil = Image
            except ImportError:
                warn('Pillow is not installed; images are embedded as-is. Run:  pip install pillow')
                self.threshold = 0

    def data_uri(self, rel):
        if rel in self.cache:
            return self.cache[rel]
        path = HERE / rel
        if not path.is_file():
            warn(f'missing image: {rel}')
            return rel
        raw = path.read_bytes()
        mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
                '.webp': 'image/webp', '.gif': 'image/gif', '.svg': 'image/svg+xml'}.get(path.suffix.lower(), 'application/octet-stream')
        data = raw
        if self.threshold and path.suffix.lower() == '.png' and len(raw) > self.threshold:
            im = self.pil.open(io.BytesIO(raw))
            buf = io.BytesIO()
            im.save(buf, 'WEBP', quality=self.quality, method=6)
            if len(buf.getvalue()) < len(raw):
                data, mime = buf.getvalue(), 'image/webp'
        self.stats.append((rel, len(raw), len(data)))
        uri = f'data:{mime};base64,' + base64.b64encode(data).decode('ascii')
        self.cache[rel] = uri
        return uri


IMG_RE = re.compile(r'^!\[(?P<alt>[^\]]*)\]\((?P<src>[^\s)]+)(?:\s+"(?P<cap>[^"]*)")?\)\s*$')


def figure_html(line, images):
    m = IMG_RE.match(line)
    alt, src, cap = m.group('alt'), m.group('src'), m.group('cap')
    caption = alt if cap is None else cap
    fig = (f'<figure class="lc-figure"><img alt="{html.escape(alt, quote=True)}" decoding="async" loading="lazy" '
           f'src="{images.data_uri(src)}">')
    if caption:
        fig += f'<figcaption>{inline_md(caption)}</figcaption>'
    return fig + '</figure>'


def gallery_html(arg, body, images):
    imgs = []
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        m = IMG_RE.match(line)
        if not m:
            warn(f'gallery: not an image line: {line[:60]}')
            continue
        imgs.append(f'<img alt="{html.escape(m.group("alt"), quote=True)}" decoding="async" loading="lazy" '
                    f'src="{images.data_uri(m.group("src"))}">')
    h = '<figure class="lc-figure lc-figure--gallery"><div class="lc-figure__gallery">' + ''.join(imgs) + '</div>'
    if arg:
        h += f'<figcaption>{inline_md(arg)}</figcaption>'
    return h + '</figure>'


def bindings_html(body):
    rows = []
    first_group = True
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('#'):
            if not first_group:
                rows.append('<tr class="lc-binding-spacer" aria-hidden="true"><td colspan="4"></td></tr>')
            first_group = False
            rows.append(f'<tr class="lc-binding-group"><th colspan="4" scope="colgroup">{inline_md(line.lstrip("#").strip())}</th></tr>')
            expect_header = True
        elif line.startswith('|'):
            cells = [inline_md(c.strip()) for c in line.strip('|').split('|')]
            if expect_header:
                rows.append('<tr class="lc-binding-columns">' + ''.join(f'<th scope="col">{c}</th>' for c in cells) + '</tr>')
                expect_header = False
            else:
                rows.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
        else:
            rows.append(f'<tr class="lc-binding-note"><td colspan="4">{inline_md(line)}</td></tr>')
    return '<div class="lc-table-wrap"><table class="lc-binding-table"><tbody>\n' + '\n'.join(rows) + '\n</tbody></table></div>'


# --------------------------------------------------------------------------- blocks
FENCE_RE = re.compile(r'^:::\s*(?P<kind>[a-z]+)(?:\s+"(?P<arg>[^"]*)")?\s*$')


def render_body(lines, images, where):
    """Chapter/section body (no headings) -> HTML. Handles ::: fences and figure lines."""
    out, plain = [], []

    def flush():
        if any(l.strip() for l in plain):
            out.append(md('\n'.join(plain)))
        plain.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        m = FENCE_RE.match(line)
        if m:
            flush()
            kind, arg = m.group('kind'), m.group('arg') or ''
            j = i + 1
            body = []
            while j < len(lines) and lines[j].strip() != ':::':
                body.append(lines[j])
                j += 1
            if j >= len(lines):
                warn(f'{where}: "::: {kind}" is never closed with ":::"')
            body = '\n'.join(body)
            out.append(fence_html(kind, arg, body, images, where))
            i = j + 1
            continue
        if IMG_RE.match(line):
            flush()
            out.append(figure_html(line.strip(), images))
            i += 1
            continue
        plain.append(line)
        i += 1
    flush()
    return '\n'.join(out)


def fence_html(kind, arg, body, images, where):
    if kind == 'lead':
        return f'<div class="lc-lead">{md(body)}</div>'
    if kind in ('note', 'warning'):
        title = f'<div class="lc-callout__title">{inline_md(arg)}</div>' if arg else ''
        return f'<aside class="lc-callout lc-callout--{kind}">{title}{md(body)}</aside>'
    if kind == 'technical':
        summary = arg or 'Technical detail (optional)'
        return f'<details class="lc-callout lc-callout--technical"><summary>{inline_md(summary)}</summary>{md(body)}</details>'
    if kind == 'gallery':
        return gallery_html(arg, body, images)
    if kind == 'bindings':
        return bindings_html(body)
    warn(f'{where}: unknown block type "::: {kind}" (use lead, note, warning, technical, gallery or bindings)')
    return md(body)


HEAD_RE = re.compile(r'^(#{1,3})\s+(.*?)\s*#*\s*$')


def parse_chapter(text, where):
    """-> (title, intro_lines, [ (h2 title, intro_lines, [ (h3 title, lines) ]) ])"""
    title, intro, sections = None, [], []
    cur2 = cur3 = None
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = True
        elif line.strip() == ':::':
            in_fence = False
        m = None if in_fence else HEAD_RE.match(line)
        if m and not line.startswith('####'):
            level, t = len(m.group(1)), m.group(2)
            if level == 1:
                if title is not None:
                    warn(f'{where}: a second "# " heading; each chapter file holds one chapter')
                title = t
                continue
            if level == 2:
                cur2 = [t, [], []]
                cur3 = None
                sections.append(cur2)
                continue
            if level == 3:
                if cur2 is None:
                    warn(f'{where}: "### {t}" appears before any "## " section')
                    cur2 = ['', [], []]
                    sections.append(cur2)
                cur3 = [t, []]
                cur2[2].append(cur3)
                continue
        if cur3 is not None:
            cur3[1].append(line)
        elif cur2 is not None:
            cur2[1].append(line)
        else:
            intro.append(line)
    if title is None:
        warn(f'{where}: no "# Chapter title" line')
        title = where
    return title, intro, sections


def chapter_html(num, text, images, where):
    title, intro, sections = parse_chapter(text, where)
    cid = slugify(title)
    h = [f'<section class="level1"><div class="lc-chapter-label">Chapter {num:02d}</div>'
         f'<h1 id="{cid}">{num}. {inline_md(title)}</h1>']
    h.append(render_body(intro, images, where))
    for n2, (t2, body2, subs) in enumerate(sections, 1):
        h.append(f'<section class="level2"><h2 id="{slugify(t2)}">{num}.{n2} {inline_md(t2)}</h2>')
        h.append(render_body(body2, images, where))
        for t3, body3 in subs:
            h.append(f'<section class="level3"><h3 id="{slugify(t3)}">{inline_md(t3)}</h3>')
            h.append(render_body(body3, images, where))
            h.append('</section>')
        h.append('</section>')
    h.append('<a class="lc-back-to-top" href="#top">Back to top ↑</a></section>')
    return cid, title, '\n'.join(h)


# --------------------------------------------------------------------------- README.html
PLACEHOLDER_SVG = ('data:image/svg+xml;utf8,' +
                   '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="300"><rect width="100%" height="100%" fill="%23cfe0e8"/>'
                   '<text x="50%" y="50%" font-family="sans-serif" font-size="26" fill="%23335" text-anchor="middle">picture</text></svg>')


class PlaceholderImages(Images):
    """README examples reference pictures that do not exist; show a placeholder instead of warning."""

    def data_uri(self, rel):
        if (HERE / rel).is_file():
            return super().data_uri(rel)
        return PLACEHOLDER_SVG


README_CSS = '''
.lc-layout { display: block; max-width: 1180px; }
.lc-manual__content > h1 { font-size: 40px; margin: 8px 0 20px; }
.lc-manual__content > h2 { margin-top: 44px; padding-top: 22px; border-top: 1px solid var(--lc-line); }
.ex { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 18px; margin: 18px 0 28px; }
.ex__label { margin: 0 0 6px; color: var(--lc-muted); font-size: 12px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }
.ex__src pre { margin: 0; padding: 16px 18px; color: #dce9ef; background: var(--lc-navy); border-radius: 11px; font-size: 13.5px; line-height: 1.55; overflow-x: auto; white-space: pre-wrap; }
.ex__out { padding: 18px 22px; background: var(--lc-paper); border: 1px solid var(--lc-line); border-radius: 11px; overflow: hidden; }
.ex__out > :first-child { margin-top: 0; } .ex__out > :last-child { margin-bottom: 0; }
.ex__out .level1 { margin: 0; padding: 26px; box-shadow: none; }
.ex__out .lc-figure__gallery img { max-height: 120px; }
pre.cmd { padding: 14px 18px; color: #dce9ef; background: var(--lc-navy); border-radius: 11px; font-size: 14px; }
code { padding: 1px 5px; background: #e8eef2; border-radius: 4px; font-size: .92em; }
pre code { padding: 0; background: none; }
@media (max-width: 820px) { .ex { grid-template-columns: 1fr; } }
'''


def build_readme(out):
    images = PlaceholderImages(configparser.ConfigParser(interpolation=None), webp=False)
    src = (HERE / 'README.md').read_text(encoding='utf-8')
    parts = re.split(r'^```(\w*)\n(.*?)^```\s*$', src, flags=re.S | re.M)
    h = []
    for i in range(0, len(parts), 3):
        if parts[i].strip():
            h.append(md(parts[i]))
        if i + 2 < len(parts):
            lang, code = parts[i + 1], parts[i + 2]
            if lang == 'markdown':
                clean = [re.sub(r'\s*←.*$', '', l) for l in code.rstrip('\n').splitlines()]
                if any(re.match(r'^#{1,2}\s', l) for l in clean):
                    rendered = chapter_html(2, '\n'.join(clean), images, 'README')[2]
                else:
                    rendered = render_body(clean, images, 'README')
                h.append('<div class="ex"><div class="ex__src"><p class="ex__label">You type</p><pre>'
                         + html.escape(code.rstrip('\n')) + '</pre></div>'
                         '<div class="ex__out-wrap"><p class="ex__label">You get</p><div class="ex__out">'
                         + rendered + '</div></div></div>')
            else:
                h.append('<pre class="cmd">' + html.escape(code.rstrip('\n')) + '</pre>')
    tpl = (HERE / 'template.html').read_text(encoding='utf-8')
    style = re.search(r'<style>.*?</style>', tpl, re.S).group(0)
    page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Editing the LaunchControl User Guide</title>' + style + '<style>' + README_CSS + '</style></head>'
            '<body><div class="lc-layout"><main class="lc-manual__content">' + '\n'.join(h) +
            '</main></div><footer class="lc-footer"><strong>LaunchControl</strong><br>User guide editing reference — '
            'generated from guide/README.md by build_guide.py --readme</footer></body></html>\n')
    Path(out).write_text(page, encoding='utf-8', newline='\n')
    print(f'  wrote {out}')


# --------------------------------------------------------------------------- main
_warnings = []


def warn(msg):
    _warnings.append(msg)
    print('WARNING:', msg, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default=str(ROOT / 'index.html'), help='output file (default: repo-root index.html)')
    ap.add_argument('--no-webp', action='store_true', help='embed images exactly as stored, no WebP re-encoding')
    ap.add_argument('--readme', action='store_true', help='render guide/README.md to guide/README.html (syntax reference with live examples)')
    args = ap.parse_args()
    if args.readme:
        build_readme(HERE / 'README.html')
        return 1 if _warnings else 0

    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(HERE / 'guide.cfg', encoding='utf-8')
    g = cfg['guide']
    images = Images(cfg, webp=not args.no_webp)

    files = sorted((HERE / 'chapters').glob('*.md'))
    if not files:
        sys.exit('no chapter files in guide/chapters/')
    toc, bodies = [], []
    for num, f in enumerate(files, 1):
        cid, title, body = chapter_html(num, f.read_text(encoding='utf-8'), images, f.name)
        toc.append(f'<a class="lc-toc__link" href="#{cid}"><span>{num:02d}</span>{inline_md(title)}</a>')
        bodies.append(body)
        print(f'  chapter {num:02d}  {title}')

    sh = cfg['start_here'] if cfg.has_section('start_here') else {}
    start_here = ''
    if sh.get('heading'):
        start_here = (f'<aside class="lc-start-here"><div class="lc-start-here__badge">{html.escape(sh.get("badge", "Start here"))}</div>'
                      f'<div><h2>{inline_md(sh["heading"])}</h2>{md(sh.get("text", ""))}'
                      f'<a href="{html.escape(sh.get("link", "#"), quote=True)}">{inline_md(sh.get("link_text", "Open"))}</a></div></aside>')

    date = g.get('date', 'auto').strip()
    if date.lower() in ('', 'auto'):
        d = dt.date.today()
        date = f'{d:%B} {d.day}, {d.year}'

    page = (HERE / 'template.html').read_text(encoding='utf-8')
    fields = {
        'title': html.escape(g.get('title', 'User Guide')),
        'eyebrow': html.escape(g.get('eyebrow', '')),
        'lead': html.escape(g.get('lead', '')),
        'description': html.escape(g.get('description', ''), quote=True),
        'version': html.escape(g.get('version', '')),
        'date': html.escape(date),
        'hero_image': images.data_uri(g.get('hero_image', '')),
        'hero_alt': html.escape(g.get('hero_alt', ''), quote=True),
        'footer': inline_md(g.get('footer', '')),
        'toc': '\n'.join(toc),
        'start_here': start_here,
        'chapters': '\n'.join(bodies),
    }
    for k, v in fields.items():
        page = page.replace('{{' + k + '}}', v)
    left = re.findall(r'{{\w+}}', page)
    if left:
        warn(f'template placeholders not filled: {left}')

    out = Path(args.out)
    out.write_text(page, encoding='utf-8', newline='\n')

    total_in = sum(s[1] for s in images.stats)
    total_out = sum(s[2] for s in images.stats)
    print(f'\n  {len(images.stats)} images: {total_in / 1024:,.0f} KB on disk -> {total_out / 1024:,.0f} KB embedded')
    print(f'  wrote {out}  ({out.stat().st_size / 1024 / 1024:.2f} MB)')
    if _warnings:
        print(f'\n  {len(_warnings)} warning(s) above — fix them and build again.')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
