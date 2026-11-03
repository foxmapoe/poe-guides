import re
from pathlib import Path
from urllib.parse import unquote

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
A = '{{ a }}'

ZONES = {
    'act-1/twilight-strand': {
        'layouts': {
            'TopRight': ('Top Right', 'twilight%20strand', 'Go north-east'),
            'Top': ('Top', 'twilight%20strand%20Top', 'Go north-east, same read as Top Right'),
            'Right': ('Right', 'twilight%20strand%20Right', 'Go full right, next to the water'),
        },
        'crop': (1110, 570, 1420, 880),
        'plates': [
            (None, None, ('Thumb shape on the left wall?', [('Yes', 'TopRight'), ('Yes', 'Top'), ('No', 'Right')])),
        ],
        'sections': [
            ('Top Right', 'The_Twilight_Strand_macro_beach4_o0', 'TopRight'),
            ('Right', 'The_Twilight_Strand_macro_beach5_o0', 'Right'),
            ('Top', 'The_Twilight_Strand_macro_beach6_o0', 'Top'),
        ],
    },
    'act-1/coast': {
        'layouts': {
            'Long': ('Long', 'The_Coast_Long_o0', 'New instance, or inside path (−35 s)'),
            'Pistol': ('Pistol', 'The_Coast_pistol', 'Wall north, up the ramp, then the top wall'),
            'Dildo': ('Dildo', 'The_Coast_Dildo', 'Over it, then left after the ledge'),
            'RightLedge': ('Right Ledge', 'The_Coast_RightLedge', 'Go right and follow the water'),
            'Pocket': ('Pocket', 'The_Coast_Fast', 'Keep going north-east'),
            'UTurn': ('U Turn', 'The_Coast_Uturn', 'Round the U, then straight east'),
            'Top': ('Top', 'The_Coast_Top', 'South, inside wall to the ledge, then the right wall'),
            'LeftLedge': ('Left Ledge', 'The_Coast_LeftLedge', 'To the wall, then the mountain south-east'),
            'FakeLedge': ('Fake Ledge', 'The_Coast_FakeLedge', 'Take the middle. The edges are dead ends'),
        },
        'plates': [
            ('Right · run north-east', 'Right%20Entrance', ('Straight wall by the entrance?', [
                ('Yes', ('Go a bit north. Second wall?', [('No', 'Long'), ('Narrow corridor', 'Pistol')])),
                ('No', ('Dildo?', [('Yes', 'Dildo'), ('No', ('Then:', [
                    ('Ledge shape north', 'Pocket'), ('Mountain bends into a U', 'UTurn'), ('Neither', 'RightLedge')], 1))])),
            ])),
            ('Left · run south-east', 'Left%20Orientation', ('Can you go up at the top wall?', [
                ('No', 'Top'),
                ('Yes', ('Then:', [('Wall lets you go east', 'LeftLedge'), ('Path through the middle', 'FakeLedge')])),
            ])),
        ],
        'sections': [
            ('Long Coast (Longest Layout)', 'The_Coast_macro_terraces1_1_1_o0', 'Long'),
            ('Pocket (Fastest Layout)', 'The_Coast_macro_terraces1_1_4_o0', 'Pocket'),
            ('Pistol', 'The_Coast_macro_terraces1_2_1_o0', 'Pistol'),
            ('Dildo Shape', 'The_Coast_macro_terraces1_2_2_o0', 'Dildo'),
            ('Right Ledge', 'The_Coast_macro_terraces1_3_1_o0', 'RightLedge'),
            ('U Turn', 'The_Coast_macro_terraces1_4_1_o0', 'UTurn'),
            ('Top', 'The_Coast_macro_terraces1_4_2_o0', 'Top'),
            ('Left Ledge', 'The_Coast_macro_terraces1_5_1_o0', 'LeftLedge'),
            ('Fake Ledge', 'The_Coast_macro_terraces1_5_2_o0', 'FakeLedge'),
        ],
    },
    'act-1/tidal-island': {
        'simple': 'Go left, turn back at the ledge',
        'layouts': {
            '1': ('Layout 1', 'The_Tidal_Island_island%201', 'Keep going left'),
            '2': ('Layout 2', 'The_Tidal_Island_island%202', 'Wide gap, keep going left'),
            '3': ('Layout 3', 'The_Tidal_Island_island%203', 'Keep going left'),
            '4': ('Layout 4', 'The_Tidal_Island_island%204', 'Keep going left'),
            '5': ('Layout 5', 'The_Tidal_Island_island%205', 'Narrow gap, turn back and go right'),
            '6': ('Layout 6', 'The_Tidal_Island_island%206', 'Keep going left'),
            '7': ('Layout 7', 'The_Tidal_Island_island%207', 'Keep going left'),
            '8': ('Layout 8', 'The_Tidal_Island_island%208', 'Go right'),
            '9': ('Layout 9', 'The_Tidal_Island_island%209', 'Keep going left'),
            '10': ('Layout 10', 'The_Tidal_Island_island%2010', 'Turn back at the ledge'),
            '11': ('Layout 11', 'The_Tidal_Island_island%2011', 'Turn back at the ledge'),
            '12': ('Layout 12', 'The_Tidal_Island_island%2012', 'Keep going left'),
            '13': ('Layout 13', 'The_Tidal_Island_island%2013', 'Keep going left'),
            '14': ('Layout 14', 'The_Tidal_Island_island%2014', 'Keep going left'),
            '15': ('Layout 15', 'The_Tidal_Island_island%2015', 'Go right'),
        },
        'plates': [
            ('Left entrance', 'Left', ('Ledge or rock?', [
                ('Neither', ['1', '4']),
                ('Rock', ('Second rock curves?', [('Left', ['3', '6', '7']), ('Right', '8')], 0)),
                ('Ledge', ('Gap from the wall to the ledge?', [('Wide', '2'), ('Narrow', '5')])),
            ])),
            ('Right entrance', 'Right', ('Ledge or rock?', [
                ('Neither', ['9', '12']),
                ('Rock', ('First rock curved?', [('Yes', '13'), ('No', ('Second rock curves?', [('Left', '14'), ('Right', '15')]))], 0)),
                ('Ledge', ['10', '11']),
            ])),
        ],
        'sections': [
            ('Layout 1', 'The_Tidal_Island_island1_1_o0', '1'),
            ('Layout 2', 'The_Tidal_Island_island1_2_o0', '2'),
            ('Layout 3', 'The_Tidal_Island_island1_3_o0', '3'),
            ('Layout 4', 'The_Tidal_Island_island1_4_o0', '4'),
            ('Layout 5', 'The_Tidal_Island_island1_5_o0', '5'),
            ('Layout 6', 'The_Tidal_Island_island2_1_o0', '6'),
            ('Layout 7', 'The_Tidal_Island_island2_2_o0', '7'),
            ('Layout 8', 'The_Tidal_Island_island2_3_o0', '8'),
            ('Layout 9', 'The_Tidal_Island_island3_1_o0', '9'),
            ('Layout 10', 'The_Tidal_Island_island3_2_o0', '10'),
            ('Layout 11', 'The_Tidal_Island_island3_3_o0', '11'),
            ('Layout 12', 'The_Tidal_Island_island3_4_o0', '12'),
            ('Layout 13', 'The_Tidal_Island_island4_1_o0', '13'),
            ('Layout 14', 'The_Tidal_Island_island4_2_o0', '14'),
            ('Layout 15', 'The_Tidal_Island_island4_3_o0', '15'),
        ],
    },
    'act-1/submerged-passage': {
        'layouts': {
            '1': ('Layout 1', 'Submerged%201', 'Right, then left into Depths. Ledge is up-left of the boat'),
            '2': ('Layout 2', 'Submerged%202', 'Down to the wall, then top left up to Depths. Ledge is left of the boat'),
            '3': ('Layout 3', 'Submerged%203', 'Right, then down-right into Depths. Ledge is up from the boat'),
            '4': ('Layout 4', 'Submerged%204', 'Straight down to Depths. Ledge is up from the boat'),
            '5': ('Layout 5', 'Submerged%205', 'Right, then down-left into Depths. Ledge is right of the boat'),
            '6': ('Layout 6', 'Submerged%206', 'Straight down to Depths. Ledge is right of the boat'),
        },
        'plates': [
            (None, None, ('Waypoint above or below the entrance?', [
                ('Above', ('Real path left?', [('Yes', ['1', '5']), ('No', '3')])),
                ('Below', ('Straight east wall at the bottom?', [('No', ['4', '6']), ('Yes', '2')], 0)),
            ])),
        ],
        'sections': [
            ('Layout 1', 'The_Submerged_Passage_cave1_1_o0', '1'),
            ('Layout 2', 'The_Submerged_Passage_cave1_2_o0', '2'),
            ('Layout 3', 'The_Submerged_Passage_cave1_3_o0', '3'),
            ('Layout 4', 'The_Submerged_Passage_cave1_4_o0', '4'),
            ('Layout 5', 'The_Submerged_Passage_cave2_1_o0', '5'),
            ('Layout 6', 'The_Submerged_Passage_cave2_2_o0', '6'),
        ],
    },
}


def folded(n):
    return isinstance(n, tuple) and len(n) > 2


def cols(n):
    if isinstance(n, str):
        return 1
    if isinstance(n, list):
        return len(n)
    if folded(n):
        return n[2]
    return inner(n)


def inner(n):
    return sum(cols(c) for _, c in n[1])


def size(path):
    with Image.open(path) as im:
        return im.size


class Page:
    def __init__(self, slug, zone):
        self.dir = ROOT / 'assets' / 'guides' / slug
        self.L = zone['layouts']
        self.crop = zone.get('crop')

    def small(self, img, crop):
        out = self.dir / 'cards' / f'{unquote(img)}.webp'
        with Image.open(self.dir / f'{unquote(img)}.webp') as im:
            if crop:
                im = im.crop(crop)
            im.thumbnail((640, 640))
            out.parent.mkdir(exist_ok=True)
            im.save(out, quality=82, method=6)
            w, h = im.size
        return (f'<img data-full="{A}{img}.webp" src="{A}cards/{img}.webp" width="{w}" height="{h}" '
                f'decoding="async"')

    def card(self, k):
        name, img, do = self.L[k]
        pic = f'{self.small(img, self.crop)} alt="{name} route">' if img else ''
        return f'<div class="cp-leaf"><b>{name}</b>{pic}<span>{do}</span></div>'

    def kids(self, node, rows, at=0):
        out = ''
        for ans, c in node[1]:
            w = cols(c)
            if isinstance(c, str):
                body = '<div class="cp-stem"></div>' + self.card(c)
            elif isinstance(c, list):
                body = self.kids(('', [('', k) for k in c]), rows, at)
            elif folded(c):
                rows.append((c, at + w / 2))
                body = '<div class="cp-stem"></div>'
            else:
                body = self.sub(c, rows, at)
            label = f'<i>{ans}</i>' if ans else ''
            out += f'<li style="flex:{w}">{label}{body}</li>'
            at += w
        return f'<ul>{out}</ul>'

    def sub(self, node, rows, at=0):
        return f'<div class="cp-q">{node[0]}</div>{self.kids(node, rows, at)}'

    def row(self, node, n, x):
        k = inner(node)
        start = min(max(0, round(2 * x - k)), 2 * n - 2 * k)
        return (f'<div class="cp-row" style="grid-template-columns:repeat({2 * n},1fr);--x:{x / n:.4%}">'
                f'<div class="cp-q">{node[0]}</div>'
                f'<div class="cp-rowkids" style="grid-column:{start + 1}/{start + 2 * k + 1}">{self.kids(node, [])}</div></div>')

    def root(self, label, head):
        return (f'<div class="cp-root"><b>{label}</b>'
                f'{self.small(head, None)} fetchpriority="high" alt="{label.split(" ")[0]} orientation at the entrance"></div>')

    def plate(self, label, head, node):
        rows = []
        tree = self.sub(node, rows)
        root = '' if label is None else self.root(label, head)
        return f'<div class="cp">{root}{tree}{"".join(self.row(r, inner(node), x) for r, x in rows)}</div>'


def image(d, alt, img):
    w, h = size(d / f'{unquote(img)}.webp')
    return f'![{alt}]({A}{img}.webp){{: width="{w}" height="{h}"}}'


def write(slug, zone):
    path = ROOT / '_guides' / f'{slug}.md'
    front = re.match(r'---\n.*?\n---\n', path.read_text(encoding='utf-8'), re.S).group(0)
    page = Page(slug, zone)
    plates = '\n'.join(page.plate(*p) for p in zone['plates'])
    if 'simple' in zone:
        roots = ''.join(page.root(label, head) for label, head, _ in zone['plates'])
        plates = (f'<div class="cp-mode"><input type="radio" name="mode" id="mode-simple" checked><label for="mode-simple">Simple</label>'
                  f'<input type="radio" name="mode" id="mode-advanced"><label for="mode-advanced">Advanced</label>'
                  f'<div class="cp-simple"><b>{zone["simple"]}</b><div>{roots}</div></div>'
                  f'<div class="cp-advanced">{plates}</div></div>')
    sections = '\n'.join(
        f'### {title}\n\n{image(page.dir, f"{title} layout", macro)}\n'
        + (f'{image(page.dir, zone["layouts"][k][0] + " route", zone["layouts"][k][1])}\n' if k else '')
        for title, macro, k in zone['sections'])
    assign = f"{{% assign a = '/assets/guides/{slug}/' | relative_url %}}"
    path.write_text(f'{front}\n{assign}\n\n{plates}\n\n## Layouts\n\n{sections}', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    for slug, zone in ZONES.items():
        write(slug, zone)
        print('wrote', slug)
