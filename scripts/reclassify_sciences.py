# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

SVT = {
    # CP
    "le-vivant-et-non-vivant-cp", "bien-manger-cp", "meteo-et-saisons-cp",
    # CE1
    "les-vegetaux-ce1", "animaux-et-leurs-petits-ce1", "le-cycle-de-l-eau-ce1",
    "regimes-alimentaires-animaux-ce1", "chaines-alimentaires-ce1", "hygiene-de-vie-ce1",
    # CE2
    "categories-d-aliments-et-equilibre-ce2", "le-squelette-et-les-muscles-ce2",
    "les-chaines-alimentaires-ce2", "cycle-de-vie-du-papillon-ce2",
    "le-mouvement-du-soleil-et-les-heures-ce2", "les-plantes-reproduction-et-croissance-ce2",
    "protection-de-l-environnement-ce2",
    # CM1
    "ecosystemes-cm1", "cycle-de-vie-etres-vivants-cm1",
    # CM2
    "systeme-solaire-cm2", "volcans-seismes-cm2", "cycle-eau-ressources-cm2",
    "unite-diversite-vivant-cm2", "digestion-cm2", "respiration-circulation-cm2",
    "reproduction-humaine-cm2", "squelette-muscles-cm2",
    # 6e
    "classification-etres-vivants", "systeme-solaire-6e", "besoins-reproduction-vegetaux-6e",
    "fonctions-nutrition-animaux-6e", "ecosystemes-biodiversite-6e", "changement-climatique-6e",
    "systeme-digestif-6e", "puberte-6e", "sommeil-6e",
    # 5e
    "cycle-de-l-eau",
    # 4e
    "activite-interne-globe",
    # 3e
    "genetique-heredite",
    # 2nde
    "terre-planete-habitable",
    # 1re
    "systeme-immunitaire",
    # terminale
    "genetique-evolution",
}

PHYSIQUE_CHIMIE = {
    # CP
    "les-materiaux-cp",
    # CE1
    "etats-de-l-eau-ce1", "experiences-eau-air-ce1", "objets-techniques-ce1",
    # CE2
    "etats-de-la-matiere", "changements-d-etat-ce2", "circuits-electriques-et-securite-ce2",
    # CM1
    "objets-techniques-cm1", "energies-cm1", "circuit-electrique-cm1", "algorithmes-programmation-cm1",
    # CM2
    "electricite-securite-cm2",
    # 6e
    "etats-eau-6e", "sources-energie-6e",
}

idx_slug = 0
count_svt = 0
count_pc = 0
missing = []

import re
lesson_re = re.compile(r'(\n  \{\n    slug: "([^"]+)",\n    titre: "[^"]*",\n    matiere: ")sciences(",)')

def repl(m):
    global count_svt, count_pc, missing
    slug = m.group(2)
    if slug in SVT:
        count_svt += 1
        return m.group(1) + "svt" + m.group(3)
    elif slug in PHYSIQUE_CHIMIE:
        count_pc += 1
        return m.group(1) + "physique-chimie" + m.group(3)
    else:
        missing.append(slug)
        return m.group(0)

new_txt, n = lesson_re.subn(repl, txt)
print("total sciences lessons matched:", n)
print("reclassified SVT:", count_svt)
print("reclassified Physique-Chimie:", count_pc)
print("MISSING (left as sciences, need manual check):", missing)

with open(path, 'w') as f:
    f.write(new_txt)
