import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A = '{{ a }}'

ZONES = {
    'act-1/twilight-strand': {
        'layouts': {
            'TopRight': ('Top Right', 'twilight%20strand', 'Go north-east'),
            'Top': ('Top', 'twilight%20strand%20Top', 'Go north-east, same read as Top Right'),
            'Right': ('Right', 'twilight%20strand%20Right', 'Go full right, next to the water'),
        },
        'ratio': '16/9',
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
                    ('Ledge shape north', 'Pocket'), ('Mountain bends into a U', 'UTurn'), ('Neither', 'RightLedge')], 'fold'))])),
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
}


def folded(n):
    return not isinstance(n, str) and len(n) > 2


def cols(n):
    if isinstance(n, str) or folded(n):
        return 1
    return sum(cols(c) for _, c in n[1])


class Page:
    def __init__(self, zone):
        self.L = zone['layouts']
        self.style = f' style="--r:{zone["ratio"]}"' if 'ratio' in zone else ''

    def card(self, k):
        name, img, do = self.L[k]
        return (f'<div class="cp-leaf"><b>{name}</b>'
                f'<img src="{A}{img}.webp" alt="{name} route"><span>{do}</span></div>')

    def kids(self, node, rows):
        out = ''
        for ans, c in node[1]:
            if isinstance(c, str):
                body = '<div class="cp-stem"></div>' + self.card(c)
            elif folded(c):
                rows.append(c)
                body = '<div class="cp-stem"></div>'
            else:
                body = self.sub(c, rows)
            out += f'<li style="flex:{cols(c)}"><i>{ans}</i>{body}</li>'
        return f'<ul>{out}</ul>'

    def sub(self, node, rows):
        return f'<div class="cp-q">{node[0]}</div>{self.kids(node, rows)}'

    def row(self, node, n):
        k = len(node[1])
        return (f'<div class="cp-row" style="grid-template-columns:repeat({n},1fr);--x:{(n - .5) / n:.4%}">'
                f'<div class="cp-q" style="grid-column:{n}">{node[0]}</div>'
                f'<div class="cp-rowkids" style="grid-column:{n - k + 1}/{n + 1}">{self.kids(node, [])}</div></div>')

    def plate(self, label, head, node):
        rows = []
        tree = self.sub(node, rows)
        root = '' if label is None else (
            f'<div class="cp-root"><b>{label}</b>'
            f'<img src="{A}{head}.webp" alt="{label.split(" ")[0]} orientation at the entrance"></div>')
        return f'<div class="cp"{self.style}>{root}{tree}{"".join(self.row(r, cols(node)) for r in rows)}</div>'


def write(slug, zone):
    path = ROOT / '_guides' / f'{slug}.md'
    front = re.match(r'---\n.*?\n---\n', path.read_text(encoding='utf-8'), re.S).group(0)
    page = Page(zone)
    plates = '\n'.join(page.plate(*p) for p in zone['plates'])
    sections = '\n'.join(
        f'### {title}\n\n![{title} layout]({A}{macro}.webp)\n![{zone["layouts"][k][0]} route]({A}{zone["layouts"][k][1]}.webp)\n'
        for title, macro, k in zone['sections'])
    assign = f"{{% assign a = '/assets/guides/{slug}/' | relative_url %}}"
    path.write_text(f'{front}\n{assign}\n\n{plates}\n\n## Layouts\n\n{sections}', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    for slug, zone in ZONES.items():
        write(slug, zone)
        print('wrote', slug)
