# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

illustrations = {
    "classification-etres-vivants": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="10" y="10" width="300" height="170" rx="14" fill="#eef3f6" stroke="#5b6470" stroke-width="2"/>
<rect x="30" y="30" width="260" height="130" rx="12" fill="#c8ecdc" stroke="#2f9e6f" stroke-width="2"/><text x="160" y="45" text-anchor="middle" font-size="9" fill="#22303f">Êtres vivants</text>
<rect x="50" y="55" width="120" height="90" rx="10" fill="#cfe3fb" stroke="#3b7bd6" stroke-width="2"/><text x="110" y="70" text-anchor="middle" font-size="9" fill="#22303f">Animaux</text>
<rect x="70" y="85" width="80" height="50" rx="8" fill="#3b7bd6"/><text x="110" y="115" text-anchor="middle" font-size="9" fill="#fff">Vertébrés</text>
<rect x="190" y="55" width="100" height="90" rx="10" fill="#fbe4c4" stroke="#e08a2a" stroke-width="2"/><text x="240" y="105" text-anchor="middle" font-size="9" fill="#22303f">Végétaux</text>
</svg>''',
    "etats-eau-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="20" y="120" width="70" height="50" fill="#a8c6ea"/><text x="55" y="150" text-anchor="middle" fill="#22303f" font-size="10">Glace</text>
<circle cx="270" cy="145" r="45" fill="#cfe3fb"/><text x="270" y="150" text-anchor="middle" font-size="11" fill="#22303f">Eau liquide</text>
<g fill="#9fc7ee"><circle cx="140" cy="35" r="4"/><circle cx="160" cy="20" r="4"/><circle cx="180" cy="45" r="4"/><circle cx="120" cy="55" r="4"/></g>
<text x="155" y="15" text-anchor="middle" font-size="11" fill="#22303f">Vapeur d'eau</text>
<path d="M95 130 L135 60" stroke="#5b6470" stroke-width="2" marker-end="url(#e1)"/>
<path d="M155 65 L230 125" stroke="#5b6470" stroke-width="2" marker-end="url(#e1)"/>
<defs><marker id="e1" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>''',
    "sources-energie-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="55" cy="55" r="26" fill="#f2c94c"/><text x="55" y="100" text-anchor="middle" font-size="10" fill="#22303f">Renouvelable</text>
<g stroke="#2f9e6f" stroke-width="4"><line x1="150" y1="40" x2="150" y2="110"/><line x1="150" y1="40" x2="130" y2="75"/><line x1="150" y1="40" x2="170" y2="85"/></g>
<rect x="230" y="40" width="26" height="60" fill="#5b6470"/><text x="243" y="115" text-anchor="middle" font-size="10" fill="#22303f">Non renouvelable</text>
<rect x="200" y="130" width="120" height="6" fill="#e7e9ec"/>
</svg>''',
    "systeme-solaire-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="30" cy="95" r="22" fill="#f2c94c"/>
<circle cx="90" cy="95" r="5" fill="#5b6470"/><circle cx="120" cy="95" r="8" fill="#e08a2a"/><circle cx="155" cy="95" r="9" fill="#3b7bd6"/><circle cx="185" cy="95" r="7" fill="#d1495b"/>
<circle cx="230" cy="95" r="16" fill="#fbe4c4"/><circle cx="280" cy="95" r="14" fill="#cfe3fb"/>
<text x="160" y="15" text-anchor="middle" font-size="10" fill="#22303f">Le Soleil et les planètes (ordre schématique)</text>
</svg>''',
    "besoins-reproduction-vegetaux-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="160" cy="50" r="16" fill="#f2c94c"/>
<circle cx="160" cy="80" r="18" fill="#f3c9ce"/><circle cx="140" cy="70" r="12" fill="#f3c9ce"/><circle cx="180" cy="70" r="12" fill="#f3c9ce"/><circle cx="140" cy="92" r="12" fill="#f3c9ce"/><circle cx="180" cy="92" r="12" fill="#f3c9ce"/>
<line x1="160" y1="98" x2="160" y2="170" stroke="#2f9e6f" stroke-width="5"/>
<path d="M160 150 q-25 -5 -35 10" stroke="#2f9e6f" stroke-width="4" fill="none"/>
<path d="M160 140 q25 -5 35 10" stroke="#2f9e6f" stroke-width="4" fill="none"/>
<text x="160" y="185" text-anchor="middle" font-size="10" fill="#22303f">Fleur, tige, lumière et eau</text>
</svg>''',
    "fonctions-nutrition-animaux-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="55" cy="80" r="30" fill="#c8ecdc"/><path d="M45 75 q10 -12 20 0" stroke="#2f9e6f" stroke-width="3" fill="none"/><text x="55" y="130" text-anchor="middle" font-size="10" fill="#22303f">Herbivore</text>
<circle cx="160" cy="80" r="30" fill="#f3c9ce"/><path d="M150 75 l10 10 l10 -10" stroke="#d1495b" stroke-width="3" fill="none"/><text x="160" y="130" text-anchor="middle" font-size="10" fill="#22303f">Carnivore</text>
<circle cx="265" cy="80" r="30" fill="#fbe4c4"/><text x="265" y="85" text-anchor="middle" font-size="14" fill="#22303f">?</text><text x="265" y="130" text-anchor="middle" font-size="10" fill="#22303f">Omnivore</text>
</svg>''',
    "ecosystemes-biodiversite-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="50" cy="140" r="10" fill="#2f9e6f"/><text x="50" y="170" text-anchor="middle" font-size="9" fill="#22303f">Végétal</text>
<circle cx="160" cy="90" r="14" fill="#e08a2a"/><text x="160" y="120" text-anchor="middle" font-size="9" fill="#22303f">Herbivore</text>
<circle cx="270" cy="45" r="18" fill="#d1495b"/><text x="270" y="75" text-anchor="middle" font-size="9" fill="#22303f">Carnivore</text>
<path d="M60 130 L150 100" stroke="#5b6470" stroke-width="2" marker-end="url(#e2)"/>
<path d="M175 82 L255 55" stroke="#5b6470" stroke-width="2" marker-end="url(#e2)"/>
<defs><marker id="e2" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>''',
    "changement-climatique-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="270" cy="35" r="18" fill="#f2c94c"/>
<path d="M10 60 H310" stroke="#e7e9ec" stroke-width="10"/>
<path d="M240 60 L200 20" stroke="#f2c94c" stroke-width="2" marker-end="url(#e3)"/>
<path d="M150 60 L150 20" stroke="#f2c94c" stroke-width="2" marker-end="url(#e3)"/>
<path d="M150 65 L150 140" stroke="#d1495b" stroke-width="2" marker-end="url(#e3)"/>
<path d="M200 65 L230 140" stroke="#d1495b" stroke-width="2" marker-end="url(#e3)"/>
<text x="160" y="180" text-anchor="middle" font-size="10" fill="#22303f">Chaleur retenue (effet de serre)</text>
<defs><marker id="e3" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>''',
    "systeme-digestif-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="50" cy="25" r="13" fill="#e08a2a"/><text x="50" y="15" text-anchor="middle" font-size="8" fill="#22303f">Bouche</text>
<path d="M50 38 C50 65 75 65 75 95" stroke="#e08a2a" stroke-width="7" fill="none"/>
<ellipse cx="105" cy="115" rx="30" ry="25" fill="#d1495b"/><text x="105" y="120" text-anchor="middle" font-size="8" fill="#fff">Estomac</text>
<path d="M135 120 q35 5 15 35 q-25 15 55 5 q35 -10 15 -25" stroke="#f2c94c" stroke-width="7" fill="none"/>
<text x="220" y="180" text-anchor="middle" font-size="9" fill="#22303f">Intestin grêle et gros intestin</text>
</svg>''',
    "puberte-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="30" y="130" width="40" height="50" fill="#cfe3fb"/><text x="50" y="185" text-anchor="middle" font-size="9" fill="#22303f">Enfance</text>
<rect x="130" y="90" width="40" height="90" fill="#c8ecdc"/><text x="150" y="185" text-anchor="middle" font-size="9" fill="#22303f">Puberté</text>
<rect x="230" y="50" width="40" height="130" fill="#fbe4c4"/><text x="250" y="185" text-anchor="middle" font-size="9" fill="#22303f">Âge adulte</text>
<path d="M20 178 L300 20" stroke="#5b6470" stroke-width="2" stroke-dasharray="4 4"/>
</svg>''',
    "sommeil-6e": '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M110 30 a45 45 0 1 0 45 70 a55 55 0 1 1 -45 -70 z" fill="#5b6470"/>
<circle cx="230" cy="40" r="4" fill="#f2c94c"/><circle cx="255" cy="60" r="3" fill="#f2c94c"/><circle cx="210" cy="65" r="3" fill="#f2c94c"/>
<text x="200" y="100" font-size="16" fill="#3b7bd6">Z z z</text>
<path d="M60 150 a70 25 0 1 0 200 0 a70 25 0 1 0 -200 0" fill="none" stroke="#cfe3fb" stroke-width="3"/>
<text x="160" y="185" text-anchor="middle" font-size="10" fill="#22303f">Cycles de sommeil</text>
</svg>''',
}

count = 0
for slug, svg in illustrations.items():
    idx = txt.index(f'slug: "{slug}"')
    quiz_idx = txt.index("quiz: {", idx)
    marker = "    quiz: {"
    assert txt[quiz_idx-4:quiz_idx+7] == marker, (slug, txt[quiz_idx-4:quiz_idx+20])
    insertion = f"illustration: `{svg}`,\n    "
    txt = txt[:quiz_idx] + insertion + txt[quiz_idx:]
    count += 1

with open(path, 'w') as f:
    f.write(txt)
print("6e illustrations added:", count)
