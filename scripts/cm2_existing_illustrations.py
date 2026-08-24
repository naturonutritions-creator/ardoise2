# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

illustrations = {
    "systeme-solaire-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="40" cy="95" r="26" fill="#f2c94c"/><text x="40" y="135" text-anchor="middle" font-size="10" fill="#22303f">Soleil</text>
<circle cx="120" cy="95" r="35" fill="none" stroke="#cfe3fb" stroke-width="2"/><circle cx="155" cy="95" r="6" fill="#3b7bd6"/>
<circle cx="120" cy="95" r="65" fill="none" stroke="#cfe3fb" stroke-width="2"/><circle cx="185" cy="95" r="9" fill="#2f9e6f"/>
<circle cx="120" cy="95" r="95" fill="none" stroke="#cfe3fb" stroke-width="2"/><circle cx="215" cy="95" r="7" fill="#d1495b"/>
<text x="120" y="12" text-anchor="middle" font-size="10" fill="#22303f">Le système solaire (orbites schématiques)</text>
</svg>''',
    "volcans-seismes-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M60 170 L140 40 L220 170 Z" fill="#5b6470"/>
<path d="M110 170 L140 90 L170 170 Z" fill="#d1495b"/>
<circle cx="140" cy="60" r="10" fill="#f2c94c"/>
<path d="M240 150 h20 l6 -16 l6 24 l6 -20 l6 12 h20" stroke="#3b7bd6" stroke-width="3" fill="none"/>
<text x="140" y="20" text-anchor="middle" font-size="10" fill="#22303f">Volcan</text>
<text x="278" y="180" text-anchor="middle" font-size="10" fill="#22303f">Onde sismique</text>
</svg>''',
    "cycle-eau-ressources-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="55" cy="35" r="20" fill="#f2c94c"/>
<ellipse cx="180" cy="45" rx="45" ry="22" fill="#e7e9ec"/>
<path d="M20 160 H300" stroke="#3b7bd6" stroke-width="10"/>
<path d="M60 100 C70 70 90 70 90 100" stroke="#e08a2a" stroke-width="2" fill="none" marker-end="url(#c)"/>
<path d="M170 70 L160 150" stroke="#3b7bd6" stroke-width="2" marker-end="url(#c)"/>
<path d="M190 70 L200 150" stroke="#3b7bd6" stroke-width="2" marker-end="url(#c)"/>
<text x="160" y="180" text-anchor="middle" font-size="10" fill="#22303f">Le cycle de l'eau</text>
<defs><marker id="c" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>''',
    "unite-diversite-vivant-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="160" cy="95" r="45" fill="#c8ecdc" stroke="#2f9e6f" stroke-width="2"/><circle cx="160" cy="95" r="14" fill="#2f9e6f"/>
<text x="160" y="150" text-anchor="middle" font-size="10" fill="#22303f">Une cellule (point commun)</text>
<circle cx="45" cy="55" r="16" fill="#3b7bd6"/><text x="45" y="30" text-anchor="middle" font-size="9" fill="#22303f">Animal</text>
<path d="M275 40 v40" stroke="#2f9e6f" stroke-width="6"/><text x="275" y="30" text-anchor="middle" font-size="9" fill="#22303f">Végétal</text>
<circle cx="55" cy="150" r="10" fill="#e08a2a"/><text x="55" y="172" text-anchor="middle" font-size="9" fill="#22303f">Champignon</text>
</svg>''',
    "digestion-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="60" cy="25" r="14" fill="#e08a2a"/><text x="60" y="15" text-anchor="middle" font-size="8" fill="#22303f">Bouche</text>
<path d="M60 39 C60 70 90 70 90 100" stroke="#e08a2a" stroke-width="8" fill="none"/>
<ellipse cx="120" cy="120" rx="35" ry="28" fill="#d1495b"/><text x="120" y="125" text-anchor="middle" font-size="8" fill="#fff">Estomac</text>
<path d="M150 130 q40 10 20 40 q-30 20 60 10 q40 -10 20 -30" stroke="#f2c94c" stroke-width="8" fill="none"/>
<text x="230" y="185" text-anchor="middle" font-size="9" fill="#22303f">Intestins</text>
</svg>''',
    "respiration-circulation-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M110 40 C80 40 70 90 100 110 C80 120 90 150 120 140 L120 40 Z" fill="#cfe3fb"/>
<path d="M210 40 C240 40 250 90 220 110 C240 120 230 150 200 140 L200 40 Z" fill="#cfe3fb"/>
<text x="160" y="25" text-anchor="middle" font-size="10" fill="#22303f">Poumons</text>
<path d="M145 100 q15 -20 30 0 q15 -20 30 0 q0 25 -30 45 q-30 -20 -30 -45 z" fill="#d1495b"/>
<text x="160" y="175" text-anchor="middle" font-size="10" fill="#22303f">Cœur</text>
</svg>''',
    "reproduction-humaine-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="90" cy="95" r="26" fill="#f3c9ce"/><text x="90" y="140" text-anchor="middle" font-size="9" fill="#22303f">Ovule</text>
<circle cx="180" cy="95" r="8" fill="#3b7bd6"/><path d="M188 95 L215 95" stroke="#3b7bd6" stroke-width="2"/><text x="185" y="120" text-anchor="middle" font-size="9" fill="#22303f">Spermatozoïde</text>
<path d="M120 95 H160" stroke="#5b6470" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#d)"/>
<circle cx="270" cy="95" r="20" fill="#e08a2a"/><text x="270" y="130" text-anchor="middle" font-size="9" fill="#22303f">Embryon</text>
<defs><marker id="d" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>''',
    "squelette-muscles-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="160" cy="30" r="16" fill="none" stroke="#5b6470" stroke-width="3"/>
<line x1="160" y1="46" x2="160" y2="120" stroke="#5b6470" stroke-width="3"/>
<line x1="160" y1="65" x2="120" y2="100" stroke="#5b6470" stroke-width="3"/>
<line x1="160" y1="65" x2="200" y2="100" stroke="#5b6470" stroke-width="3"/>
<line x1="160" y1="120" x2="130" y2="175" stroke="#5b6470" stroke-width="3"/>
<line x1="160" y1="120" x2="190" y2="175" stroke="#5b6470" stroke-width="3"/>
<ellipse cx="140" cy="82" rx="8" ry="14" fill="#d1495b" opacity="0.7"/>
<text x="160" y="15" text-anchor="middle" font-size="10" fill="#22303f">Squelette et muscles</text>
</svg>''',
    "electricite-securite-cm2": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="40" y="80" width="30" height="16" fill="#5b6470"/><text x="55" y="115" text-anchor="middle" font-size="9" fill="#22303f">Pile</text>
<path d="M70 88 H150" stroke="#5b6470" stroke-width="3"/>
<circle cx="175" cy="88" r="22" fill="#fbe4c4" stroke="#e08a2a" stroke-width="3"/><text x="175" y="125" text-anchor="middle" font-size="9" fill="#22303f">Ampoule</text>
<path d="M197 88 H260 V150 H70 V96" stroke="#5b6470" stroke-width="3" fill="none"/>
<path d="M260 30 L280 60 H240 Z" fill="#f2c94c" stroke="#d1495b" stroke-width="2"/><text x="260" y="25" text-anchor="middle" font-size="9" fill="#d1495b">Danger</text>
</svg>''',
}

count = 0
for slug, svg in illustrations.items():
    idx = txt.index(f'slug: "{slug}"')
    quiz_idx = txt.index("quiz: {", idx)
    marker = "    quiz: {"
    # ensure we insert right before "    quiz: {" at this position
    assert txt[quiz_idx-4:quiz_idx+7] == marker, txt[quiz_idx-4:quiz_idx+20]
    insertion = f"illustration: `{svg}`,\n    "
    txt = txt[:quiz_idx] + insertion + txt[quiz_idx:]
    count += 1

with open(path, 'w') as f:
    f.write(txt)
print("illustrations added:", count)
