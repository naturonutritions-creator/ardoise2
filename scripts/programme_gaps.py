# -*- coding: utf-8 -*-
"""
Comble les manques identifies par rapport aux programmes officiels (6e/5e)
et corrige 2 bugs de classement (nombres-relatifs en double, cycle-de-l-eau
mal classe en 5e SVT).
"""
import re

PATH = "src/content/lessons.ts"

def lesson_block(d):
    obj = ", ".join(f'"{o}"' for o in d["objectifs"])
    cont = ", ".join('"' + c.replace("\\", "\\\\").replace('"', '\\"') + '"' for c in d["contenu"])
    illus = ""
    if d.get("illustration"):
        illus = f'\n    illustration: `{d["illustration"]}`,'
    q_items = []
    for q in d["quiz"]:
        choix = ", ".join('"' + c.replace('"', '\\"') + '"' for c in q["choix"])
        expl = q["explication"].replace('"', '\\"')
        q_items.append(
            f'      {{\n        id: "{q["id"]}",\n        enonce: "{q["enonce"]}",\n'
            f'        choix: [{choix}],\n        reponse: {q["reponse"]},\n'
            f'        explication: "{expl}",\n      }}'
        )
    quiz_block = (
        f'quiz: {{\n    slug: "quiz-{d["slug"]}",\n    titre: "Quiz — {d["titre"]}",\n'
        f'    questions: [\n' + ",\n".join(q_items) + "\n    ],\n  },"
    )
    return (
        f'  {{\n    slug: "{d["slug"]}",\n    titre: "{d["titre"]}",\n'
        f'    matiere: "{d["matiere"]}",\n    niveau: "{d["niveau"]}",\n'
        f'    duree: "{d["duree"]}",\n    resume: "{d["resume"]}",\n'
        f'    objectifs: [{obj}],\n    contenu: [{cont}],{illus}\n    {quiz_block}\n  }},'
    )

def replace_lesson(txt, old_slug, new_dict):
    start = txt.index(f'  {{\n    slug: "{old_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    new_block = lesson_block(new_dict)
    return txt[:start] + new_block + txt[nxt:]

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]


# ============================================================
# BUG FIX 1 : nombres-relatifs (5e maths, doublon) ->
#             La divisibilite et les nombres premiers
# ============================================================
DIVISIBILITE = {
    "slug": "divisibilite-nombres-premiers-5e",
    "titre": "La divisibilité et les nombres premiers",
    "matiere": "mathematiques",
    "niveau": "5e",
    "duree": "20 min",
    "resume": "Reconnaître les diviseurs et multiples d'un nombre entier, et identifier les nombres premiers.",
    "objectifs": [
        "Reconnaître si un nombre est divisible par 2, 3, 5, 9 ou 10",
        "Distinguer un nombre premier d'un nombre composé",
        "Décomposer un nombre en produit de facteurs premiers",
    ],
    "contenu": [
        "Un nombre entier a est divisible par un nombre entier b non nul s'il existe un entier k tel que a = b × k. On dit alors que b est un diviseur de a et que a est un multiple de b. Des critères simples permettent de repérer certaines divisibilités sans poser la division : un nombre est divisible par 2 s'il se termine par 0, 2, 4, 6 ou 8 ; par 5 s'il se termine par 0 ou 5 ; par 10 s'il se termine par 0 ; par 3 (et par 9) si la somme de ses chiffres est elle-même divisible par 3 (ou par 9).",
        "Un nombre premier est un nombre entier supérieur à 1 qui possède exactement deux diviseurs : 1 et lui-même. Les premiers nombres premiers sont 2, 3, 5, 7, 11, 13, 17, 19... et 2 est le seul nombre premier pair. Un nombre supérieur à 1 qui n'est pas premier est dit composé : il peut alors s'écrire comme un produit d'au moins deux nombres premiers.",
        "Décomposer un nombre en produit de facteurs premiers, c'est l'écrire comme un produit de nombres premiers : par exemple 60 = 2 × 2 × 3 × 5. Cette décomposition, unique à l'ordre des facteurs près, sert notamment à simplifier des fractions ou à calculer le PGCD (plus grand diviseur commun) de deux nombres.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « 8 est un diviseur de 24 » ?", "choix": ["24 est un multiple de 8", "8 est un multiple de 24", "24 divisé par 8 n'est pas un nombre entier", "8 est premier"], "reponse": 0, "explication": "Si 8 est un diviseur de 24, alors 24 est un multiple de 8 (24 = 8 × 3)."},
        {"id": "q2", "enonce": "Un nombre est divisible par 5 s'il se termine par...", "choix": ["0 ou 5", "0 uniquement", "2, 4, 6 ou 8", "n'importe quel chiffre"], "reponse": 0, "explication": "Un nombre est divisible par 5 s'il se termine par 0 ou par 5."},
        {"id": "q3", "enonce": "Comment savoir si un nombre est divisible par 3 ?", "choix": ["S'il se termine par 3", "Si la somme de ses chiffres est divisible par 3", "S'il est pair", "S'il est premier"], "reponse": 1, "explication": "Un nombre est divisible par 3 si la somme de ses chiffres est elle-même divisible par 3."},
        {"id": "q4", "enonce": "Combien de diviseurs possède un nombre premier ?", "choix": ["Un seul", "Exactement deux : 1 et lui-même", "Trois ou plus", "Aucun"], "reponse": 1, "explication": "Un nombre premier possède exactement deux diviseurs : 1 et lui-même."},
        {"id": "q5", "enonce": "Quel est le seul nombre premier pair ?", "choix": ["4", "1", "2", "0"], "reponse": 2, "explication": "2 est le seul nombre premier pair : tous les autres nombres pairs sont divisibles par 2 en plus d'eux-mêmes."},
        {"id": "q6", "enonce": "1 est-il un nombre premier ?", "choix": ["Oui", "Non, car il n'a qu'un seul diviseur", "Oui, car il n'a pas de diviseur", "Cela dépend"], "reponse": 1, "explication": "1 n'est pas premier : par définition, un nombre premier doit avoir exactement deux diviseurs distincts, or 1 n'en a qu'un."},
        {"id": "q7", "enonce": "Qu'est-ce qu'un nombre composé ?", "choix": ["Un nombre premier", "Un nombre supérieur à 1 qui n'est pas premier", "Un nombre négatif", "Un nombre décimal"], "reponse": 1, "explication": "Un nombre composé est un nombre supérieur à 1 qui possède plus de deux diviseurs."},
        {"id": "q8", "enonce": "Quelle est la décomposition en facteurs premiers de 60 ?", "choix": ["6 × 10", "2 × 2 × 3 × 5", "4 × 15", "2 × 30"], "reponse": 1, "explication": "60 = 2 × 2 × 3 × 5, où 2, 3 et 5 sont tous des nombres premiers."},
        {"id": "q9", "enonce": "À quoi sert la décomposition en facteurs premiers ?", "choix": ["À rien de particulier", "À simplifier des fractions et calculer le PGCD", "À multiplier plus vite", "À compter les chiffres d'un nombre"], "reponse": 1, "explication": "La décomposition en facteurs premiers permet notamment de simplifier des fractions et de calculer le PGCD de deux nombres."},
        {"id": "q10", "enonce": "7 est-il un nombre premier ?", "choix": ["Non, il est divisible par 2", "Oui, ses seuls diviseurs sont 1 et 7", "Non, c'est un nombre composé", "Cela dépend du contexte"], "reponse": 1, "explication": "7 est premier : ses seuls diviseurs sont 1 et 7."},
    ],
}

# ============================================================
# BUG FIX 2 : cycle-de-l-eau (5e SVT, hors-programme) ->
#             Les phenomenes meteorologiques
# ============================================================
METEO = {
    "slug": "phenomenes-meteorologiques-5e",
    "titre": "Les phénomènes météorologiques",
    "matiere": "svt",
    "niveau": "5e",
    "duree": "20 min",
    "resume": "Comprendre l'origine des principaux phénomènes météorologiques et leurs liens avec le climat.",
    "objectifs": [
        "Identifier les principaux phénomènes météorologiques",
        "Comprendre le rôle de l'atmosphère et du Soleil dans la météo",
        "Distinguer météo et climat",
    ],
    "contenu": [
        "La météorologie étudie les phénomènes atmosphériques : vent, pluie, nuages, tempêtes, gel... Ils résultent des mouvements de l'air et de l'eau dans l'atmosphère, eux-mêmes provoqués par l'énergie reçue du Soleil, qui chauffe inégalement la surface de la Terre selon la latitude, la saison et le relief. L'air chaud, plus léger, s'élève ; l'air froid, plus dense, descend : ces mouvements créent les vents et les grandes circulations atmosphériques.",
        "Les nuages se forment lorsque la vapeur d'eau contenue dans l'air se condense en fines gouttelettes ou en cristaux de glace, en général quand une masse d'air humide s'élève et se refroidit. Quand ces gouttelettes deviennent trop lourdes, elles tombent sous forme de précipitations : pluie, neige ou grêle selon la température. Les tempêtes et les orages résultent de forts contrastes de température et de pression entre différentes masses d'air.",
        "Il ne faut pas confondre météo et climat : la météo décrit l'état de l'atmosphère à un instant et un lieu donnés (il pleut aujourd'hui à Lyon), tandis que le climat correspond aux conditions atmosphériques moyennes observées sur une longue période, généralement 30 ans, dans une région (le climat méditerranéen est chaud et sec en été). Le changement climatique modifie progressivement ces moyennes à l'échelle mondiale.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="270" cy="35" r="20" fill="#f4b942"/>\n<ellipse cx="90" cy="60" rx="55" ry="26" fill="#cfd8e3"/><ellipse cx="140" cy="55" rx="40" ry="22" fill="#e3e8ee"/>\n<g stroke="#3b7bd6" stroke-width="3" stroke-linecap="round"><line x1="60" y1="100" x2="50" y2="120"/><line x1="85" y1="100" x2="75" y2="120"/><line x1="110" y1="100" x2="100" y2="120"/><line x1="135" y1="100" x2="125" y2="120"/></g>\n<path d="M20 170 q40 -25 80 0 q40 -25 80 0 q40 -25 80 0" fill="none" stroke="#22303f" stroke-width="2"/>\n<text x="160" y="185" text-anchor="middle" font-size="10" fill="#22303f">Soleil, nuages, pluie : la météo</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qui provoque les mouvements de l'air à l'origine des vents ?", "choix": ["Le chauffage inégal de la Terre par le Soleil", "La rotation de la Lune", "Les marées", "Le magnétisme terrestre"], "reponse": 0, "explication": "Le Soleil chauffe inégalement la surface terrestre, ce qui crée des différences de température à l'origine des vents."},
        {"id": "q2", "enonce": "Comment se comporte l'air chaud par rapport à l'air froid ?", "choix": ["Il descend, car il est plus dense", "Il s'élève, car il est plus léger", "Il reste immobile", "Il devient invisible"], "reponse": 1, "explication": "L'air chaud est plus léger que l'air froid : il a tendance à s'élever."},
        {"id": "q3", "enonce": "Comment se forment les nuages ?", "choix": ["Par évaporation de la roche", "Par condensation de la vapeur d'eau dans l'air", "Par le vent seul", "Ils ne se forment jamais, ils existent depuis toujours"], "reponse": 1, "explication": "Les nuages se forment quand la vapeur d'eau se condense en gouttelettes ou cristaux de glace."},
        {"id": "q4", "enonce": "Que se passe-t-il quand les gouttelettes d'un nuage deviennent trop lourdes ?", "choix": ["Elles remontent plus haut", "Elles tombent sous forme de précipitations", "Elles disparaissent", "Elles se transforment en vent"], "reponse": 1, "explication": "Les gouttelettes trop lourdes tombent : c'est la pluie, la neige ou la grêle selon la température."},
        {"id": "q5", "enonce": "Quelle est la différence entre météo et climat ?", "choix": ["Il n'y a aucune différence", "La météo est l'état de l'atmosphère à un instant donné, le climat est une moyenne sur le long terme", "Le climat change tous les jours, pas la météo", "La météo concerne uniquement la pluie"], "reponse": 1, "explication": "La météo décrit l'état ponctuel de l'atmosphère, le climat correspond aux conditions moyennes observées sur environ 30 ans."},
        {"id": "q6", "enonce": "Sur combien d'années calcule-t-on généralement un climat ?", "choix": ["1 an", "5 ans", "Environ 30 ans", "100 ans exactement"], "reponse": 2, "explication": "Le climat se définit à partir de moyennes calculées sur environ 30 années d'observations."},
        {"id": "q7", "enonce": "Qu'est-ce qui provoque les orages et tempêtes ?", "choix": ["De forts contrastes de température et de pression entre masses d'air", "L'absence totale de vent", "Le froid uniquement", "La chaleur uniquement"], "reponse": 0, "explication": "Les orages et tempêtes naissent de forts contrastes de température et de pression entre masses d'air."},
        {"id": "q8", "enonce": "Sous quelle forme tombent les précipitations quand il fait très froid ?", "choix": ["Pluie uniquement", "Neige ou grêle", "Brouillard", "Rosée"], "reponse": 1, "explication": "Quand la température est basse, les précipitations tombent sous forme de neige ou de grêle."},
        {"id": "q9", "enonce": "Le changement climatique modifie...", "choix": ["La météo d'un seul jour", "Les moyennes climatiques à l'échelle mondiale sur le long terme", "Uniquement la couleur du ciel", "Rien de mesurable"], "reponse": 1, "explication": "Le changement climatique modifie progressivement les conditions atmosphériques moyennes à l'échelle mondiale."},
        {"id": "q10", "enonce": "«Il pleut aujourd'hui à Lyon» est une observation...", "choix": ["Climatique", "Météorologique", "Géologique", "Astronomique"], "reponse": 1, "explication": "Cette observation ponctuelle relève de la météo, pas du climat."},
    ],
}

print("Chargement du fichier...")
with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = replace_lesson(txt, "nombres-relatifs", DIVISIBILITE)
txt = replace_lesson(txt, "cycle-de-l-eau", METEO)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print("Bugs corriges : divisibilite-nombres-premiers-5e, phenomenes-meteorologiques-5e")
