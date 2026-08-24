# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

def q(id_, enonce, choix, reponse, explication):
    choix_str = ", ".join('"' + c.replace('"', '\\"') + '"' for c in choix)
    return f'''      {{
        id: "{id_}",
        enonce: "{enonce}",
        choix: [{choix_str}],
        reponse: {reponse},
        explication: "{explication}",
      }}'''

def lesson_block(slug, titre, matiere, niveau, duree, resume, objectifs, contenu, illustration, quiz_slug, quiz_titre, qs):
    obj_str = ", ".join('"' + o.replace('"', '\\"') + '"' for o in objectifs)
    qs_str = ",\n".join(qs)
    cont_str = ", ".join('"' + c.replace('"', '\\"') + '"' for c in contenu)
    return f'''  {{
    slug: "{slug}",
    titre: "{titre}",
    matiere: "{matiere}",
    niveau: "{niveau}",
    duree: "{duree}",
    resume: "{resume}",
    objectifs: [{obj_str}],
    contenu: [{cont_str}],
    illustration: `{illustration}`,
    quiz: {{
    slug: "{quiz_slug}",
    titre: "{quiz_titre}",
    questions: [
{qs_str}
    ],
  }},
  }},
'''

svg_cellule = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<ellipse cx="120" cy="95" rx="90" ry="65" fill="#c8ecdc" stroke="#2f9e6f" stroke-width="3"/>
<circle cx="130" cy="95" r="30" fill="#2f9e6f"/><text x="130" y="99" text-anchor="middle" font-size="8" fill="#fff">Noyau</text>
<text x="120" y="175" text-anchor="middle" font-size="10" fill="#22303f">Cellule (membrane, cytoplasme, noyau)</text>
<circle cx="270" cy="40" r="10" fill="#3b7bd6"/><rect x="255" y="130" width="30" height="8" fill="#e08a2a"/><path d="M270 150 v20" stroke="#5b6470" stroke-width="4"/>
</svg>'''

svg_reproduction = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="90" cy="95" r="30" fill="#f3c9ce"/><text x="90" y="145" text-anchor="middle" font-size="9" fill="#22303f">Gamète femelle</text>
<circle cx="200" cy="95" r="18" fill="#cfe3fb"/><text x="200" y="130" text-anchor="middle" font-size="9" fill="#22303f">Gamète mâle</text>
<path d="M120 95 H175" stroke="#5b6470" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#f1)"/>
<circle cx="280" cy="95" r="24" fill="#e08a2a"/><text x="280" y="135" text-anchor="middle" font-size="9" fill="#22303f">Cellule-œuf</text>
<defs><marker id="f1" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

svg_photosynthese = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="45" cy="35" r="18" fill="#f2c94c"/>
<path d="M160 30 q50 0 40 60 q40 10 10 50 q-30 20 -60 -10 q-40 10 -40 -40 q0 -50 50 -60 z" fill="#2f9e6f"/>
<path d="M45 53 L120 90" stroke="#f2c94c" stroke-width="2" marker-end="url(#f2)"/>
<text x="10" y="120" font-size="9" fill="#22303f">CO₂ + eau</text>
<path d="M20 110 L90 100" stroke="#3b7bd6" stroke-width="2" marker-end="url(#f2)"/>
<text x="230" y="60" font-size="9" fill="#22303f">Sucres + O₂</text>
<path d="M195 70 L225 60" stroke="#e08a2a" stroke-width="2" marker-end="url(#f2)"/>
<defs><marker id="f2" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

svg_infection = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M160 20 L230 50 V100 C230 150 190 175 160 180 C130 175 90 150 90 100 V50 Z" fill="#cfe3fb" stroke="#3b7bd6" stroke-width="3"/>
<circle cx="130" cy="60" r="8" fill="#d1495b"/><circle cx="170" cy="45" r="6" fill="#d1495b"/><circle cx="190" cy="75" r="7" fill="#d1495b"/>
<rect x="250" y="80" width="8" height="60" fill="#5b6470" transform="rotate(30 254 110)"/>
<text x="160" y="20" text-anchor="middle" font-size="9" fill="#22303f">Protection et vaccination</text>
</svg>'''

svg_conditions = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="30" y="150" width="10" height="20" fill="#5b6470"/><rect x="30" y="30" width="10" height="120" fill="#e7e9ec"/>
<rect x="27" y="70" width="16" height="80" fill="#d1495b"/>
<path d="M100 150 C100 90 140 90 140 40" stroke="#2f9e6f" stroke-width="4" fill="none"/>
<text x="120" y="175" text-anchor="middle" font-size="9" fill="#22303f">Croissance selon la température</text>
<rect x="220" y="60" width="80" height="90" fill="#cfe3fb" opacity="0.6"/><text x="260" y="105" text-anchor="middle" font-size="9" fill="#22303f">Zone favorable</text>
</svg>'''

svg_ressources = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="10" y="10" width="300" height="40" fill="#cfe3fb"/><text x="160" y="35" text-anchor="middle" font-size="10" fill="#22303f">Eau</text>
<rect x="10" y="50" width="300" height="60" fill="#e7e9ec"/><text x="160" y="85" text-anchor="middle" font-size="10" fill="#22303f">Roches et minerais</text>
<rect x="10" y="110" width="300" height="60" fill="#5b6470"/><text x="160" y="145" text-anchor="middle" font-size="10" fill="#fff">Énergies fossiles</text>
</svg>'''

lessons_out = []

lessons_out.append(lesson_block(
    "unite-diversite-organismes-5e", "Unité et diversité des organismes vivants", "svt", "5e", "20 min",
    "Comprendre que tous les êtres vivants sont constitués de cellules, tout en présentant une immense diversité.",
    ["Comprendre que la cellule est l'unité de base du vivant", "Distinguer organismes unicellulaires et pluricellulaires", "Relier unité de structure et diversité du monde vivant"],
    [
        "Tous les êtres vivants, aussi différents soient-ils (une bactérie, un champignon, un chêne, un être humain), sont constitués d'au moins une cellule : la cellule est l'unité de base de tous les organismes vivants. Une cellule est une structure microscopique délimitée par une membrane, contenant un cytoplasme et, le plus souvent, un noyau qui renferme l'information génétique.",
        "On distingue les organismes unicellulaires, constitués d'une seule cellule (bactéries, certaines algues microscopiques), et les organismes pluricellulaires, constitués de très nombreuses cellules organisées en tissus et en organes (un être humain adulte compte des dizaines de milliers de milliards de cellules). Malgré cette différence de complexité, toutes les cellules partagent une organisation de base commune.",
        "Cette unité de structure au niveau cellulaire n'empêche pas une immense diversité du vivant : les organismes se distinguent par leur forme, leur taille, leur mode de nutrition, leur milieu de vie ou leur mode de reproduction. Cette diversité résulte de millions d'années d'évolution, chaque espèce s'étant progressivement adaptée à son environnement."
    ],
    svg_cellule, "quiz-unite-diversite-organismes-5e", "Quiz — Unité et diversité des organismes vivants",
    [
        q("q1", "Quelle est l'unité de base de tous les organismes vivants ?", ["L'organe", "La cellule", "Le tissu", "L'atome"], 1, "La cellule est l'unité de base commune à tous les organismes vivants."),
        q("q2", "Qu'est-ce qu'un organisme unicellulaire ?", ["Un organisme constitué d'une seule cellule", "Un organisme sans aucune cellule", "Un organisme constitué de milliards de cellules", "Un organisme végétal uniquement"], 0, "Un organisme unicellulaire est constitué d'une seule cellule, comme une bactérie."),
        q("q3", "Qu'est-ce qu'un organisme pluricellulaire ?", ["Un organisme sans cellule", "Un organisme constitué de nombreuses cellules organisées", "Un organisme unicellulaire", "Un minéral"], 1, "Un organisme pluricellulaire est constitué de nombreuses cellules organisées en tissus et organes."),
        q("q4", "Que contient généralement une cellule, en plus de la membrane et du cytoplasme ?", ["Un noyau contenant l'information génétique", "Un squelette osseux", "Des poumons", "Rien d'autre"], 0, "La cellule contient le plus souvent un noyau qui renferme l'information génétique."),
        q("q5", "Un être humain adulte est-il un organisme unicellulaire ?", ["Oui", "Non, c'est un organisme pluricellulaire", "Cela dépend des personnes", "Il n'a pas de cellules"], 1, "Un être humain adulte est pluricellulaire, composé de dizaines de milliers de milliards de cellules."),
        q("q6", "Toutes les cellules partagent-elles une organisation de base commune ?", ["Non, elles sont toutes complètement différentes", "Oui, malgré la diversité des organismes", "Seulement chez les animaux", "Seulement chez les végétaux"], 1, "Malgré la diversité des organismes, toutes les cellules partagent une organisation de base commune."),
        q("q7", "D'où vient l'immense diversité du monde vivant malgré l'unité cellulaire ?", ["Du hasard sans aucune cause", "De millions d'années d'évolution et d'adaptation", "Elle n'existe pas réellement", "D'une seule mutation récente"], 1, "La diversité du vivant résulte de millions d'années d'évolution et d'adaptation à des environnements variés."),
        q("q8", "Citez un exemple d'organisme unicellulaire.", ["Un chêne", "Une bactérie", "Un être humain", "Un chat"], 1, "Une bactérie est un exemple d'organisme unicellulaire."),
        q("q9", "Qu'est-ce que le cytoplasme d'une cellule ?", ["Le contenu interne de la cellule, entourant le noyau", "La membrane externe", "Un organe complet", "Un tissu osseux"], 0, "Le cytoplasme est le contenu interne de la cellule, dans lequel baigne le noyau."),
        q("q10", "La diversité des organismes se manifeste-t-elle uniquement par leur taille ?", ["Oui, uniquement", "Non, aussi par la forme, la nutrition, le milieu de vie, la reproduction", "Non, uniquement par la couleur", "La diversité n'existe pas"], 1, "La diversité se manifeste par de nombreux critères : forme, taille, nutrition, milieu de vie, reproduction."),
    ]
))

lessons_out.append(lesson_block(
    "reproduction-sexuee-etres-vivants-5e", "La reproduction sexuée chez les êtres vivants", "svt", "5e", "20 min",
    "Comprendre le principe de la reproduction sexuée et la diversité génétique qu'elle engendre chez les descendants.",
    ["Définir la reproduction sexuée", "Comprendre le rôle des cellules reproductrices (gamètes)", "Expliquer pourquoi les descendants ne sont jamais identiques aux parents"],
    [
        "La reproduction sexuée nécessite la fusion de deux cellules reproductrices, appelées gamètes : un gamète mâle et un gamète femelle, apportés chacun par un parent différent. Cette fusion, appelée fécondation, donne naissance à une nouvelle cellule, appelée cellule-œuf, qui va se diviser de nombreuses fois pour former un nouvel individu.",
        "La reproduction sexuée existe chez de très nombreuses espèces, animales comme végétales : chez les animaux, la fécondation peut être interne (à l'intérieur du corps de la femelle, comme chez les mammifères) ou externe (dans l'eau, comme chez de nombreux poissons) ; chez les plantes à fleurs, elle passe par la pollinisation, qui permet aux gamètes mâles (contenus dans le pollen) de rencontrer les gamètes femelles.",
        "Contrairement à la reproduction asexuée (bouturage, division), la reproduction sexuée mélange le patrimoine génétique des deux parents : chaque descendant reçoit une combinaison unique de gènes, ce qui explique qu'il ne soit jamais parfaitement identique à ses parents ni à ses frères et sœurs (sauf cas particulier des vrais jumeaux). Cette diversité génétique est un avantage pour l'adaptation et la survie d'une espèce face aux changements de son environnement."
    ],
    svg_reproduction, "quiz-reproduction-sexuee-etres-vivants-5e", "Quiz — La reproduction sexuée chez les êtres vivants",
    [
        q("q1", "Que faut-il pour qu'il y ait reproduction sexuée ?", ["Une seule cellule qui se divise", "La fusion d'un gamète mâle et d'un gamète femelle", "Aucune cellule reproductrice", "Un bouturage"], 1, "La reproduction sexuée nécessite la fusion d'un gamète mâle et d'un gamète femelle."),
        q("q2", "Comment appelle-t-on la fusion des deux gamètes ?", ["La pollinisation", "La fécondation", "La germination", "La mutation"], 1, "La fusion des deux gamètes s'appelle la fécondation."),
        q("q3", "Qu'obtient-on après la fécondation ?", ["Un gamète", "Une cellule-œuf", "Un pollen", "Rien de particulier"], 1, "La fécondation donne naissance à une cellule-œuf, qui se divisera pour former un nouvel individu."),
        q("q4", "Qu'est-ce qu'une fécondation interne ?", ["Une fécondation qui a lieu dans l'eau", "Une fécondation à l'intérieur du corps de la femelle", "Une fécondation sans gamètes", "Une fécondation chez les plantes uniquement"], 1, "Une fécondation interne a lieu à l'intérieur du corps de la femelle, comme chez les mammifères."),
        q("q5", "Comment les gamètes mâles atteignent-ils les gamètes femelles chez les plantes à fleurs ?", ["Par la pollinisation", "Par la digestion", "Par la respiration", "Elles ne se rencontrent jamais"], 0, "Chez les plantes à fleurs, la pollinisation permet au pollen (gamètes mâles) d'atteindre les gamètes femelles."),
        q("q6", "Pourquoi un enfant n'est-il jamais identique à ses parents ?", ["Car il n'a aucun gène de ses parents", "Car la reproduction sexuée mélange le patrimoine génétique des deux parents", "Ce n'est pas vrai, il est toujours identique", "Car les gènes changent après la naissance"], 1, "La reproduction sexuée mélange les gènes des deux parents, créant une combinaison unique chez chaque descendant."),
        q("q7", "Quel type de fécondation est externe, comme chez de nombreux poissons ?", ["Dans l'eau, hors du corps de la femelle", "À l'intérieur du corps de la femelle", "Sans aucun gamète", "Impossible chez les poissons"], 0, "Chez de nombreux poissons, la fécondation a lieu dans l'eau, hors du corps de la femelle : elle est externe."),
        q("q8", "Les vrais jumeaux sont-ils génétiquement identiques ?", ["Non, jamais", "Oui, cas particulier issu d'une même cellule-œuf", "Cela dépend du sexe", "Ils n'existent pas biologiquement"], 1, "Les vrais jumeaux proviennent d'une même cellule-œuf qui s'est divisée en deux : ils sont génétiquement identiques."),
        q("q9", "Quel est l'avantage de la diversité génétique apportée par la reproduction sexuée ?", ["Aucun avantage", "Elle aide l'espèce à s'adapter aux changements de son environnement", "Elle rend tous les individus identiques", "Elle empêche toute évolution"], 1, "La diversité génétique aide une espèce à mieux s'adapter aux changements de son environnement."),
        q("q10", "La reproduction sexuée existe-t-elle uniquement chez les animaux ?", ["Oui, uniquement chez les animaux", "Non, elle existe aussi chez les plantes à fleurs", "Non, uniquement chez les plantes", "Elle n'existe nulle part"], 1, "La reproduction sexuée existe chez de nombreuses espèces animales et végétales."),
    ]
))

lessons_out.append(lesson_block(
    "origine-matiere-organique-5e", "L'origine de la matière organique des végétaux", "svt", "5e", "20 min",
    "Comprendre comment les plantes vertes produisent leur propre matière organique grâce à la photosynthèse.",
    ["Définir la matière organique", "Comprendre le principe de la photosynthèse", "Identifier les besoins d'une plante verte pour produire sa matière"],
    [
        "La matière organique est la matière qui constitue les êtres vivants (feuilles, bois, chair...). Contrairement aux animaux, qui doivent manger d'autres êtres vivants pour obtenir leur matière organique, les plantes vertes sont capables de produire elles-mêmes leur matière organique : on dit qu'elles sont autotrophes, littéralement « qui se nourrissent elles-mêmes ».",
        "Ce phénomène s'appelle la photosynthèse : à la lumière, les feuilles absorbent le dioxyde de carbone de l'air et l'eau puisée par les racines, et les transforment en matière organique (des sucres) grâce à l'énergie lumineuse captée par la chlorophylle, le pigment vert des feuilles. La photosynthèse produit aussi du dioxygène, rejeté dans l'atmosphère.",
        "La photosynthèse n'a lieu qu'à la lumière : la nuit, les plantes respirent comme les animaux (elles consomment du dioxygène et rejettent du dioxyde de carbone), mais en journée, la photosynthèse est largement supérieure à la respiration, ce qui fait des plantes vertes des productrices nettes de matière organique et de dioxygène, à la base de presque toutes les chaînes alimentaires."
    ],
    svg_photosynthese, "quiz-origine-matiere-organique-5e", "Quiz — L'origine de la matière organique des végétaux",
    [
        q("q1", "Qu'est-ce que la matière organique ?", ["Uniquement les roches", "La matière qui constitue les êtres vivants", "Uniquement l'eau", "Un gaz rare"], 1, "La matière organique est la matière qui constitue les êtres vivants."),
        q("q2", "Pourquoi dit-on que les plantes vertes sont autotrophes ?", ["Elles mangent d'autres êtres vivants", "Elles produisent elles-mêmes leur matière organique", "Elles ne se nourrissent jamais", "Elles vivent sans lumière"], 1, "Autotrophe signifie qu'un organisme produit lui-même sa matière organique, comme les plantes vertes."),
        q("q3", "Comment s'appelle le phénomène qui permet aux plantes de produire leur matière organique ?", ["La respiration", "La photosynthèse", "La digestion", "La fermentation"], 1, "Ce phénomène s'appelle la photosynthèse."),
        q("q4", "Quels éléments les feuilles absorbent-elles pour la photosynthèse ?", ["De l'oxygène et du sucre", "Le dioxyde de carbone de l'air et l'eau des racines", "Uniquement de la terre", "Rien du tout"], 1, "Les feuilles absorbent le dioxyde de carbone de l'air et l'eau puisée par les racines."),
        q("q5", "Quel pigment capte l'énergie lumineuse dans les feuilles ?", ["La mélanine", "La chlorophylle", "L'hémoglobine", "Le carotène uniquement"], 1, "La chlorophylle, le pigment vert des feuilles, capte l'énergie lumineuse nécessaire à la photosynthèse."),
        q("q6", "Que produit la photosynthèse, en plus des sucres ?", ["Du dioxyde de carbone uniquement", "Du dioxygène", "De l'azote", "Rien d'autre"], 1, "La photosynthèse produit du dioxygène, rejeté dans l'atmosphère."),
        q("q7", "La photosynthèse a-t-elle lieu la nuit ?", ["Oui, tout le temps", "Non, elle nécessite la lumière", "Oui, mais plus lentement", "Cela dépend de la plante"], 1, "La photosynthèse n'a lieu qu'à la lumière ; la nuit, les plantes respirent comme les animaux."),
        q("q8", "Que font les plantes la nuit, en l'absence de lumière ?", ["Rien du tout", "Elles respirent : consomment du dioxygène et rejettent du dioxyde de carbone", "Elles font uniquement de la photosynthèse", "Elles arrêtent de vivre"], 1, "La nuit, les plantes respirent, consommant du dioxygène et rejetant du dioxyde de carbone, comme les animaux."),
        q("q9", "Pourquoi les plantes vertes sont-elles à la base de presque toutes les chaînes alimentaires ?", ["Elles ne sont jamais mangées", "Elles produisent la matière organique dont dépendent de nombreux autres êtres vivants", "Elles ne produisent rien d'utile", "Elles sont toutes vénéneuses"], 1, "Les plantes vertes produisent la matière organique qui nourrit directement ou indirectement de nombreux autres êtres vivants."),
        q("q10", "Les animaux peuvent-ils produire leur propre matière organique comme les plantes ?", ["Oui, tous les animaux le peuvent", "Non, ils doivent manger d'autres êtres vivants pour l'obtenir", "Seulement les animaux verts", "Seulement la nuit"], 1, "Contrairement aux plantes vertes, les animaux doivent manger d'autres êtres vivants pour obtenir leur matière organique."),
    ]
))

lessons_out.append(lesson_block(
    "risque-infectieux-protection-organisme-5e", "Le risque infectieux et la protection de l'organisme", "svt", "5e", "20 min",
    "Comprendre comment les microbes peuvent provoquer des maladies et comment l'organisme et la vaccination s'en protègent.",
    ["Distinguer les grandes familles de microbes", "Comprendre les modes de transmission des microbes", "Expliquer le principe de la vaccination"],
    [
        "De nombreuses maladies sont causées par des micro-organismes invisibles à l'œil nu, qu'on appelle microbes : les bactéries (responsables par exemple de l'angine), les virus (responsables par exemple de la grippe ou du rhume), et les champignons microscopiques. Certains microbes sont utiles ou inoffensifs (comme la plupart des bactéries de notre intestin), mais d'autres, appelés pathogènes, provoquent des maladies infectieuses.",
        "Les microbes se transmettent de différentes façons : par l'air (toux, éternuements), par contact direct (mains, peau), par l'eau ou les aliments contaminés, ou par les liquides biologiques. Se laver les mains régulièrement, tousser dans son coude, et bien cuire certains aliments sont des gestes simples qui limitent fortement la transmission des microbes.",
        "L'organisme se défend naturellement contre les microbes grâce à son système immunitaire, qui reconnaît et élimine les intrus. La vaccination renforce cette défense : elle consiste à injecter une version inactive ou affaiblie d'un microbe (ou une de ses parties), ce qui permet à l'organisme de fabriquer des défenses (anticorps) sans développer la maladie, et de réagir beaucoup plus vite en cas d'infection réelle par la suite."
    ],
    svg_infection, "quiz-risque-infectieux-protection-organisme-5e", "Quiz — Le risque infectieux et la protection de l'organisme",
    [
        q("q1", "Qu'est-ce qu'un microbe ?", ["Un très grand animal", "Un micro-organisme invisible à l'œil nu", "Une plante uniquement", "Un minéral"], 1, "Un microbe est un micro-organisme invisible à l'œil nu (bactérie, virus, champignon microscopique)."),
        q("q2", "Tous les microbes sont-ils dangereux ?", ["Oui, tous sans exception", "Non, certains sont utiles ou inoffensifs", "Non, aucun n'est dangereux", "Cela dépend uniquement de leur couleur"], 1, "Certains microbes sont utiles ou inoffensifs, comme la plupart des bactéries de notre intestin."),
        q("q3", "Quel microbe est responsable de la grippe ?", ["Une bactérie", "Un virus", "Un champignon", "Aucun microbe"], 1, "La grippe est causée par un virus."),
        q("q4", "Citez un mode de transmission des microbes.", ["Par la pensée", "Par l'air, le contact direct, l'eau ou les aliments contaminés", "Les microbes ne se transmettent jamais", "Uniquement par la lumière"], 1, "Les microbes se transmettent par l'air, le contact direct, l'eau ou des aliments contaminés."),
        q("q5", "Pourquoi se laver les mains régulièrement est-il utile ?", ["Cela n'a aucun effet", "Cela limite la transmission des microbes", "Cela rend malade", "Cela sert uniquement à sentir bon"], 1, "Se laver les mains régulièrement limite fortement la transmission des microbes."),
        q("q6", "Qu'est-ce que le système immunitaire ?", ["Un organe unique", "Le système qui défend l'organisme contre les microbes", "Un microbe particulier", "Un muscle"], 1, "Le système immunitaire reconnaît et élimine les microbes qui menacent l'organisme."),
        q("q7", "Que contient un vaccin ?", ["Le microbe complet et actif à pleine puissance", "Une version inactive ou affaiblie d'un microbe (ou une de ses parties)", "Uniquement de l'eau", "Un médicament contre la douleur"], 1, "Un vaccin contient une version inactive ou affaiblie d'un microbe, ou une de ses parties."),
        q("q8", "Que permet la vaccination ?", ["De développer la maladie volontairement", "De fabriquer des défenses (anticorps) sans développer la maladie", "De rendre le corps plus faible", "Rien de particulier"], 1, "La vaccination permet à l'organisme de fabriquer des anticorps sans développer la maladie réelle."),
        q("q9", "Après la vaccination, comment l'organisme réagit-il face à une infection réelle ?", ["Il ne réagit pas du tout", "Il réagit beaucoup plus vite grâce aux défenses déjà présentes", "Il réagit plus lentement", "Il devient plus vulnérable"], 1, "Grâce aux défenses déjà fabriquées, l'organisme réagit beaucoup plus vite en cas d'infection réelle après vaccination."),
        q("q10", "Tousser dans son coude est-il un bon geste pour limiter la transmission des microbes ?", ["Non, cela n'a aucun effet", "Oui, cela limite la propagation par l'air", "Non, cela propage plus de microbes", "Seulement en hiver"], 1, "Tousser dans son coude limite la propagation des microbes par l'air."),
    ]
))

lessons_out.append(lesson_block(
    "conditions-developpement-etres-vivants-5e", "Les conditions de développement des êtres vivants", "svt", "5e", "20 min",
    "Comprendre comment les conditions du milieu (température, eau, lumière) influencent la répartition des espèces.",
    ["Identifier les facteurs qui influencent le développement d'un être vivant", "Comprendre la notion de conditions favorables et défavorables", "Relier la répartition d'une espèce aux caractéristiques de son milieu"],
    [
        "Le développement et la survie d'un être vivant dépendent des conditions du milieu dans lequel il se trouve : la température, la disponibilité en eau, la lumière, la nature du sol ou la présence de nourriture. Chaque espèce a une gamme de conditions favorables, en dehors de laquelle son développement ralentit, s'arrête, ou devient impossible.",
        "Par exemple, la plupart des végétaux ont besoin d'une température suffisante pour germer et pousser : c'est pourquoi de nombreuses graines restent en dormance pendant l'hiver et ne germent qu'au retour de conditions favorables au printemps. De la même façon, certains animaux hibernent ou migrent pour éviter des conditions défavorables comme le grand froid ou le manque de nourriture.",
        "La répartition géographique d'une espèce sur Terre s'explique en grande partie par ces conditions de développement : un cactus ne pousse pas en Antarctique, un ours polaire ne survit pas sous les tropiques. Le changement climatique modifie ces conditions dans de nombreuses régions du monde, ce qui pousse certaines espèces à déplacer leur aire de répartition ou menace leur survie si elles ne peuvent pas s'adapter assez vite."
    ],
    svg_conditions, "quiz-conditions-developpement-etres-vivants-5e", "Quiz — Les conditions de développement des êtres vivants",
    [
        q("q1", "De quoi dépend le développement d'un être vivant ?", ["Uniquement de sa couleur", "Des conditions du milieu (température, eau, lumière...)", "Du hasard uniquement", "De rien de particulier"], 1, "Le développement d'un être vivant dépend des conditions de son milieu : température, eau, lumière, sol, nourriture."),
        q("q2", "Que se passe-t-il en dehors de la gamme de conditions favorables à une espèce ?", ["Rien ne change", "Son développement ralentit, s'arrête ou devient impossible", "Elle se développe encore mieux", "Elle change instantanément d'espèce"], 1, "En dehors des conditions favorables, le développement d'une espèce ralentit, s'arrête, ou devient impossible."),
        q("q3", "Pourquoi de nombreuses graines restent-elles en dormance en hiver ?", ["Elles sont mortes", "Elles attendent des conditions de température favorables pour germer", "Elles n'ont jamais besoin de germer", "Elles préfèrent le froid extrême"], 1, "Les graines restent en dormance en hiver et germent au retour de conditions favorables, comme au printemps."),
        q("q4", "Pourquoi certains animaux hibernent-ils ?", ["Pour s'amuser", "Pour éviter des conditions défavorables comme le grand froid ou le manque de nourriture", "Cela n'a aucune utilité", "Uniquement pour dormir plus longtemps sans raison"], 1, "L'hibernation permet à certains animaux d'éviter des conditions défavorables (froid, manque de nourriture)."),
        q("q5", "Pourquoi un cactus ne pousse-t-il pas en Antarctique ?", ["Il n'y a pas de sable en Antarctique", "Les conditions (froid extrême) ne sont pas favorables à son développement", "Les cactus n'existent pas vraiment", "Il n'y a pas de raison particulière"], 1, "Les conditions extrêmes de l'Antarctique ne sont pas favorables au développement d'un cactus."),
        q("q6", "Le changement climatique peut-il modifier la répartition des espèces ?", ["Non, jamais", "Oui, en modifiant les conditions favorables dans certaines régions", "Seulement pour les plantes", "Seulement dans les océans"], 1, "Le changement climatique modifie les conditions de nombreux milieux, ce qui affecte la répartition des espèces."),
        q("q7", "Qu'est-ce que la migration permet à certains animaux ?", ["De rester toujours au même endroit", "D'éviter des conditions défavorables selon la saison", "De disparaître définitivement", "De changer d'espèce"], 1, "La migration permet à certains animaux de trouver des conditions plus favorables selon la saison."),
        q("q8", "Un ours polaire pourrait-il facilement survivre sous les tropiques ?", ["Oui, sans problème", "Non, les conditions ne lui sont pas favorables", "Oui, il préfère la chaleur", "Cela n'a pas d'importance pour sa survie"], 1, "Un ours polaire est adapté au froid et ne pourrait pas facilement survivre sous les tropiques."),
        q("q9", "La répartition géographique d'une espèce est-elle liée aux conditions de son milieu ?", ["Non, c'est totalement aléatoire", "Oui, elle s'explique en grande partie par ces conditions", "Non, uniquement par la volonté de l'espèce", "Cela ne concerne que les animaux"], 1, "La répartition géographique d'une espèce s'explique en grande partie par les conditions de développement de son milieu."),
        q("q10", "Que peut menacer le changement climatique chez certaines espèces ?", ["Rien du tout", "Leur survie si elles ne peuvent pas s'adapter assez vite", "Uniquement leur couleur", "Cela les rend plus nombreuses systématiquement"], 1, "Le changement climatique peut menacer la survie d'espèces incapables de s'adapter assez vite aux nouvelles conditions."),
    ]
))

lessons_out.append(lesson_block(
    "ressources-naturelles-terre-5e", "L'exploitation des ressources naturelles de la Terre", "svt", "5e", "20 min",
    "Découvrir les grandes ressources naturelles terrestres (eau, roches, énergies fossiles) et les enjeux de leur exploitation.",
    ["Identifier les grandes ressources naturelles exploitées par l'être humain", "Comprendre la différence entre ressource renouvelable et non renouvelable", "Comprendre les enjeux liés à la gestion durable des ressources"],
    [
        "L'être humain exploite de nombreuses ressources naturelles fournies par la Terre : l'eau (pour boire, irriguer, produire de l'électricité), les roches et minerais (pour construire, fabriquer des objets), et les énergies fossiles comme le pétrole, le charbon et le gaz naturel, formées en profondeur sur des millions d'années à partir de matière organique ancienne.",
        "Certaines ressources sont renouvelables à l'échelle humaine (l'eau douce se renouvelle grâce au cycle de l'eau, tant qu'elle n'est pas surexploitée), tandis que d'autres sont non renouvelables : les énergies fossiles s'épuisent, car leur formation prend des millions d'années, bien plus longtemps que le rythme auquel l'être humain les consomme.",
        "L'exploitation des ressources naturelles pose des enjeux importants : l'extraction de roches et de minerais peut abîmer les paysages et les milieux naturels, l'utilisation des énergies fossiles rejette du dioxyde de carbone qui contribue au changement climatique, et certaines ressources en eau douce se raréfient dans plusieurs régions du monde. Une gestion durable cherche à limiter le gaspillage et à préserver ces ressources pour les générations futures."
    ],
    svg_ressources, "quiz-ressources-naturelles-terre-5e", "Quiz — L'exploitation des ressources naturelles de la Terre",
    [
        q("q1", "Citez une ressource naturelle exploitée par l'être humain.", ["L'eau", "La musique", "Le langage", "Les mathématiques"], 0, "L'eau est une ressource naturelle essentielle exploitée par l'être humain."),
        q("q2", "Comment se forment les énergies fossiles comme le pétrole ?", ["Instantanément", "En profondeur, sur des millions d'années à partir de matière organique ancienne", "À la surface en quelques années", "Elles ne se forment pas naturellement"], 1, "Les énergies fossiles se forment en profondeur sur des millions d'années à partir de matière organique ancienne."),
        q("q3", "L'eau douce est-elle une ressource renouvelable ?", ["Non, jamais", "Oui, grâce au cycle de l'eau, tant qu'elle n'est pas surexploitée", "Seulement en hiver", "Elle n'existe pas naturellement"], 1, "L'eau douce se renouvelle grâce au cycle de l'eau, tant qu'elle n'est pas surexploitée."),
        q("q4", "Pourquoi les énergies fossiles sont-elles non renouvelables ?", ["Elles se forment très vite", "Leur formation prend des millions d'années, bien plus longtemps que leur consommation", "Elles n'existent pas en quantité limitée", "Elles se renouvellent chaque année"], 1, "Les énergies fossiles s'épuisent car leur formation est bien plus lente que le rythme de consommation humaine."),
        q("q5", "Quel impact peut avoir l'extraction de roches et de minerais ?", ["Aucun impact", "Elle peut abîmer les paysages et les milieux naturels", "Elle améliore toujours l'environnement", "Elle n'a lieu nulle part sur Terre"], 1, "L'extraction de roches et de minerais peut abîmer les paysages et les milieux naturels."),
        q("q6", "Que rejette l'utilisation des énergies fossiles ?", ["De l'oxygène pur uniquement", "Du dioxyde de carbone qui contribue au changement climatique", "Rien du tout", "De l'eau uniquement"], 1, "L'utilisation des énergies fossiles rejette du dioxyde de carbone, qui contribue au changement climatique."),
        q("q7", "Les ressources en eau douce sont-elles menacées dans certaines régions du monde ?", ["Non, jamais", "Oui, elles se raréfient dans plusieurs régions", "Elles sont illimitées partout", "Cela ne concerne que les océans"], 1, "Les ressources en eau douce se raréfient dans plusieurs régions du monde."),
        q("q8", "Que cherche à faire une gestion durable des ressources ?", ["Consommer le plus possible sans limite", "Limiter le gaspillage et préserver les ressources pour l'avenir", "Épuiser rapidement toutes les ressources", "Ignorer les enjeux environnementaux"], 1, "Une gestion durable cherche à limiter le gaspillage et à préserver les ressources pour les générations futures."),
        q("q9", "Le charbon est-il une énergie fossile ?", ["Non, c'est une énergie renouvelable", "Oui, comme le pétrole et le gaz naturel", "Non, ce n'est pas une source d'énergie", "Il n'existe pas naturellement"], 1, "Le charbon est une énergie fossile, tout comme le pétrole et le gaz naturel."),
        q("q10", "Pourquoi est-il important de préserver les ressources naturelles ?", ["Ce n'est pas important", "Pour les générations futures et l'équilibre de l'environnement", "Uniquement pour des raisons économiques immédiates", "Les ressources naturelles sont illimitées"], 1, "Préserver les ressources naturelles est important pour les générations futures et l'équilibre de l'environnement."),
    ]
))

marker = "\n  {\n    "
idx = txt.index('slug: "cycle-de-l-eau"')
# make sure we match the 5e lesson and not another lesson with a similar substring
while True:
    seg_check = txt[idx:idx+200]
    if '"5e"' in seg_check:
        break
    idx = txt.index('slug: "cycle-de-l-eau"', idx+1)
next_pos = txt.index(marker, idx) + 1
new_block = "".join(lessons_out)
txt = txt[:next_pos] + new_block + txt[next_pos:]

with open(path, 'w') as f:
    f.write(txt)
print("5e SVT new lessons inserted:", len(lessons_out))
