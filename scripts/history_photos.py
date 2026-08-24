import re

path = "src/content/lessons.ts"
with open(path, encoding="utf-8") as f:
    txt = f.read()

BASE = "https://commons.wikimedia.org/wiki/Special:FilePath/"

photos = {
    "la-prehistoire": (
        BASE + "Lascaux_painting.jpg",
        "Peinture rupestre representant des aurochs et des chevaux dans la grotte de Lascaux",
        "Grotte de Lascaux, peinture rupestre (env. -18 000 ans) — Wikimedia Commons, domaine public",
    ),
    "art-prehistorique-6e": (
        BASE + "Lascaux_painting.jpg",
        "Peinture rupestre representant des aurochs et des chevaux dans la grotte de Lascaux",
        "Grotte de Lascaux, peinture rupestre (env. -18 000 ans) — Wikimedia Commons, domaine public",
    ),
    "neolithique": (
        BASE + "Stonehenge_back_wide.jpg",
        "Stonehenge, monument megalithique construit au Neolithique en Angleterre",
        "Stonehenge, vestige megalithique du Neolithique — Wikimedia Commons",
    ),
    "gaule-romaine-cm1": (
        BASE + "Siege-alesia-vercingetorix-jules-cesar.jpg",
        "Vercingetorix jette ses armes aux pieds de Jules Cesar, tableau de Lionel Royer (1899)",
        "Lionel Royer, Vercingetorix jette ses armes aux pieds de Cesar, 1899 — Wikimedia Commons, domaine public",
    ),
    "jules-cesar-gaule-6e": (
        BASE + "Siege-alesia-vercingetorix-jules-cesar.jpg",
        "Vercingetorix jette ses armes aux pieds de Jules Cesar, tableau de Lionel Royer (1899)",
        "Lionel Royer, Vercingetorix jette ses armes aux pieds de Cesar, 1899 — Wikimedia Commons, domaine public",
    ),
    "clovis-merovingiens-cm1": (
        BASE + "Bapteme_de_clovis.jpg",
        "Le bapteme de Clovis, roi des Francs, par saint Remi",
        "Le bapteme de Clovis — Wikimedia Commons, domaine public",
    ),
    "charlemagne-carolingiens-cm1": (
        BASE + "Albrecht_D%C3%BCrer_-_Emperor_Charlemagne.jpg",
        "Portrait imaginaire de l'empereur Charlemagne par Albrecht Durer (v. 1512)",
        "Albrecht Durer, Portrait de Charlemagne, v. 1512 — Wikimedia Commons, domaine public",
    ),
    "empire-carolingien-charlemagne-5e": (
        BASE + "Albrecht_D%C3%BCrer_-_Emperor_Charlemagne.jpg",
        "Portrait imaginaire de l'empereur Charlemagne par Albrecht Durer (v. 1512)",
        "Albrecht Durer, Portrait de Charlemagne, v. 1512 — Wikimedia Commons, domaine public",
    ),
    "louis-xiv-cm1": (
        BASE + "Portrait_of_Louis_XIV_of_France_in_Coronation_Robes_%28by_Hyacinthe_Rigaud%29_-_Louvre_Museum.jpg",
        "Portrait de Louis XIV en habit de sacre, par Hyacinthe Rigaud (1701)",
        "Hyacinthe Rigaud, Louis XIV en habit de sacre, 1701, musee du Louvre — Wikimedia Commons, domaine public",
    ),
    "louis-xiv-lumieres-cm2": (
        BASE + "Portrait_of_Louis_XIV_of_France_in_Coronation_Robes_%28by_Hyacinthe_Rigaud%29_-_Louvre_Museum.jpg",
        "Portrait de Louis XIV en habit de sacre, par Hyacinthe Rigaud (1701)",
        "Hyacinthe Rigaud, Louis XIV en habit de sacre, 1701, musee du Louvre — Wikimedia Commons, domaine public",
    ),
    "renaissance-arts-sciences-cm2": (
        BASE + "Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg",
        "La Joconde, portrait peint par Leonard de Vinci (v. 1503-1519)",
        "Leonard de Vinci, La Joconde, v. 1503-1519, musee du Louvre — Wikimedia Commons, domaine public",
    ),
    "revolution-francaise-cm2": (
        BASE + "Jacques_Louis_David_-_Le_serment_du_Jeu_de_Paume_-_Google_Art_Project.jpg",
        "Le Serment du Jeu de Paume, tableau de Jacques-Louis David (1791)",
        "Jacques-Louis David, Le Serment du Jeu de Paume, 1791, chateau de Versailles — Wikimedia Commons, domaine public",
    ),
    "guerres-mondiales-construction-europeenne-cm2": (
        BASE + "French_87th_Regiment_Cote_34_Verdun_1916.jpg",
        "Soldats francais du 87e regiment pres de Verdun en 1916, Premiere Guerre mondiale",
        "Soldats francais a Verdun, 1916 — Wikimedia Commons, domaine public",
    ),
    "egypte-pharaons-6e": (
        BASE + "Tutankhamun%27s_mask,_Burton_photograph_P0744,_1922.jpg",
        "Masque funeraire en or du pharaon Toutankhamon, photographie lors de sa decouverte en 1922",
        "Masque de Toutankhamon, photographie Harry Burton, 1922 — Wikimedia Commons, domaine public",
    ),
    "grece-antique-cites-6e": (
        BASE + "Acropolis_Parthenon_Athens_Greece.jpg",
        "Le Parthenon sur l'Acropole d'Athenes",
        "Le Parthenon, Acropole d'Athenes — Wikimedia Commons",
    ),
    "rome-monarchie-empire-6e": (
        BASE + "Colosseum_of_Rome,_Italy.jpg",
        "Le Colisee de Rome, amphitheatre construit au Ier siecle apr. J.-C.",
        "Colisee de Rome — Wikimedia Commons",
    ),
    "byzance-heritiere-empire-romain-5e": (
        BASE + "Hagia_Sophia_Interior_Panorama.jpg",
        "Interieur de Sainte-Sophie (Hagia Sophia) a Istanbul, chef-d'oeuvre de l'architecture byzantine",
        "Interieur de Sainte-Sophie, Istanbul — Wikimedia Commons",
    ),
    "naissance-diffusion-islam-5e": (
        BASE + "Jerusalem_Dome_of_the_rock_BW_14.JPG",
        "Le Dome du Rocher a Jerusalem, l'un des premiers grands monuments de l'architecture islamique (VIIe siecle)",
        "Dome du Rocher, Jerusalem — Wikimedia Commons, domaine public",
    ),
    "renaissance-humanisme-decouvertes-5e": (
        BASE + "Vasco_da_Gama_-_1838.png",
        "Portrait de Vasco de Gama, navigateur portugais des Grandes Decouvertes (gravure, 1838)",
        "Portrait de Vasco de Gama, gravure de 1838 — Wikimedia Commons, domaine public",
    ),
    "moliere-comedie-5e": (
        BASE + "Moli%C3%A8re_-_Nicolas_Mignard_%281658%29.jpg",
        "Portrait de Moliere par Nicolas Mignard (1658)",
        "Nicolas Mignard, Portrait de Moliere, 1658 — Wikimedia Commons, domaine public",
    ),
    "fables-la-fontaine-francais-6e": (
        BASE + "Portrait_Jean_de_la_fontaine.jpg",
        "Portrait de Jean de La Fontaine, fabuliste francais du XVIIe siecle",
        "Portrait de Jean de La Fontaine — Wikimedia Commons",
    ),
}

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

missing = []
count = 0
for slug, (url, alt, credit) in photos.items():
    marker = f'slug: "{slug}"'
    idx = txt.find(marker)
    if idx == -1:
        missing.append(slug)
        continue
    quiz_idx = txt.index("quiz: {", idx)
    insertion = f'photo: {{ url: "{esc(url)}", alt: "{esc(alt)}", credit: "{esc(credit)}" }},\n    '
    txt = txt[:quiz_idx] + insertion + txt[quiz_idx:]
    count += 1

print("inserted:", count, "missing:", missing)

with open(path, "w", encoding="utf-8") as f:
    f.write(txt)
