# -*- coding: utf-8 -*-
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

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

CIRCUIT = {
    "slug": "circuit-electrique-5e",
    "titre": "Le circuit électrique",
    "matiere": "physique-chimie", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre le fonctionnement d'un circuit électrique simple et son schéma normalisé.",
    "objectifs": ["Identifier les éléments d'un circuit électrique simple", "Utiliser les symboles normalisés pour schématiser un circuit", "Distinguer circuit ouvert et circuit fermé"],
    "contenu": [
        "Un circuit électrique simple est constitué d'un générateur, comme une pile ou une batterie, de fils de connexion, d'un récepteur comme une lampe, et généralement d'un interrupteur. Le générateur fournit l'énergie électrique nécessaire au fonctionnement du récepteur ; les fils permettent au courant électrique de circuler entre les différents éléments, qui forment ensemble une boucle fermée appelée circuit.",
        "Pour qu'un courant électrique circule et que la lampe s'allume, le circuit doit être fermé, c'est-à-dire qu'il ne doit y avoir aucune interruption entre les éléments. Si l'interrupteur est ouvert, ou si un fil est coupé, le circuit est dit ouvert et aucun courant ne circule : la lampe reste éteinte.",
        "Pour représenter un circuit électrique de façon claire et universelle, on utilise un schéma normalisé avec des symboles conventionnels : deux traits de longueur différente pour une pile, un cercle avec une croix pour une lampe, une ligne brisée pour un interrupteur ouvert. Ce schéma permet à n'importe qui, dans n'importe quel pays, de comprendre comment le circuit est construit sans ambiguïté.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<rect x="40" y="60" width="240" height="90" fill="none" stroke="#22303f" stroke-width="2"/>\n<line x1="120" y1="60" x2="115" y2="45" stroke="#22303f" stroke-width="4"/><line x1="130" y1="60" x2="130" y2="40" stroke="#22303f" stroke-width="2"/>\n<circle cx="280" cy="105" r="16" fill="none" stroke="#e08a2a" stroke-width="2"/><line x1="269" y1="94" x2="291" y2="116" stroke="#e08a2a" stroke-width="2"/><line x1="291" y1="94" x2="269" y2="116" stroke="#e08a2a" stroke-width="2"/>\n<text x="160" y="175" text-anchor="middle" font-size="10" fill="#22303f">Un circuit fermé : le courant circule</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Quel élément fournit l'énergie électrique dans un circuit simple ?", "choix": ["La lampe", "Le générateur (pile ou batterie)", "L'interrupteur", "Le fil"], "reponse": 1, "explication": "Le générateur, comme une pile, fournit l'énergie électrique nécessaire au circuit."},
        {"id": "q2", "enonce": "Quel élément permet d'ouvrir ou de fermer un circuit ?", "choix": ["La lampe", "Le générateur", "L'interrupteur", "Le fil de connexion"], "reponse": 2, "explication": "L'interrupteur permet d'ouvrir ou de fermer le circuit à volonté."},
        {"id": "q3", "enonce": "Pour que la lampe s'allume, le circuit doit être...", "choix": ["Ouvert", "Fermé", "Coupé", "Aucun rapport avec l'état du circuit"], "reponse": 1, "explication": "Le circuit doit être fermé, sans interruption, pour que le courant circule et que la lampe s'allume."},
        {"id": "q4", "enonce": "Que se passe-t-il si un fil du circuit est coupé ?", "choix": ["Rien ne change", "Le circuit est ouvert, aucun courant ne circule", "La lampe brille plus fort", "Le générateur explose"], "reponse": 1, "explication": "Un fil coupé ouvre le circuit : plus aucun courant ne peut circuler."},
        {"id": "q5", "enonce": "Comment représente-t-on une pile dans un schéma normalisé ?", "choix": ["Un cercle avec une croix", "Deux traits de longueur différente", "Une ligne brisée", "Un triangle"], "reponse": 1, "explication": "Une pile est représentée par deux traits parallèles de longueur différente."},
        {"id": "q6", "enonce": "Comment représente-t-on une lampe dans un schéma normalisé ?", "choix": ["Un cercle avec une croix à l'intérieur", "Un rectangle plein", "Une ligne brisée", "Un triangle plein"], "reponse": 0, "explication": "Une lampe est représentée par un cercle contenant une croix."},
        {"id": "q7", "enonce": "À quoi sert un schéma normalisé ?", "choix": ["À rendre le circuit joli", "À être compris par n'importe qui, dans n'importe quel pays", "À cacher le fonctionnement du circuit", "Il ne sert à rien"], "reponse": 1, "explication": "Le schéma normalisé utilise des symboles universels compréhensibles partout dans le monde."},
        {"id": "q8", "enonce": "Un circuit ouvert permet-il au courant de circuler ?", "choix": ["Oui, toujours", "Non, il y a une interruption qui empêche le courant de circuler", "Cela dépend de la couleur des fils", "Oui, mais plus lentement"], "reponse": 1, "explication": "Un circuit ouvert comporte une interruption qui empêche la circulation du courant."},
        {"id": "q9", "enonce": "Quels sont les éléments de base d'un circuit électrique simple ?", "choix": ["Un générateur, des fils et un récepteur", "Uniquement de l'eau", "Uniquement un aimant", "Uniquement de la lumière"], "reponse": 0, "explication": "Un circuit simple comprend un générateur, des fils de connexion et un récepteur, souvent avec un interrupteur."},
        {"id": "q10", "enonce": "Qu'est-ce qu'un récepteur dans un circuit électrique ?", "choix": ["Un composant qui utilise l'énergie électrique, comme une lampe", "Le générateur", "Un fil isolant", "Un interrupteur uniquement"], "reponse": 0, "explication": "Un récepteur, comme une lampe, utilise l'énergie électrique fournie par le générateur."},
    ],
}

DIPOLES = {
    "slug": "dipoles-serie-derivation-5e",
    "titre": "Les associations de dipôles en série et en dérivation",
    "matiere": "physique-chimie", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre les deux façons d'associer plusieurs dipôles dans un circuit électrique.",
    "objectifs": ["Distinguer un montage en série d'un montage en dérivation", "Comprendre l'effet d'une association en série sur la luminosité des lampes", "Comprendre l'effet d'une association en dérivation sur le fonctionnement des récepteurs"],
    "contenu": [
        "Un dipôle est un composant électrique relié au reste du circuit par deux bornes, comme une lampe, une pile ou un interrupteur. Lorsqu'on associe plusieurs dipôles les uns à la suite des autres, en une seule boucle, on parle de montage en série : le courant électrique traverse alors chaque dipôle l'un après l'autre.",
        "Dans un montage en série, si l'on ajoute plusieurs lampes, chacune reçoit une part réduite de l'énergie totale et brille donc moins fort qu'une lampe seule. De plus, si l'on retire ou dévisse une seule lampe, tout le circuit s'ouvre et toutes les autres lampes s'éteignent : les dipôles en série dépendent les uns des autres.",
        "Lorsqu'on associe plusieurs dipôles sur des branches différentes reliées aux mêmes deux points du circuit, on parle de montage en dérivation, aussi appelé montage en parallèle. Chaque lampe fonctionne alors de façon indépendante et brille avec son éclat normal : si l'on retire une lampe, les autres continuent de fonctionner, car le courant peut toujours circuler par les autres branches. C'est ce principe qui est utilisé pour l'installation électrique d'une maison.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<rect x="20" y="40" width="120" height="60" fill="none" stroke="#22303f" stroke-width="2"/>\n<circle cx="55" cy="70" r="10" fill="none" stroke="#e08a2a" stroke-width="2"/><circle cx="105" cy="70" r="10" fill="none" stroke="#e08a2a" stroke-width="2"/>\n<text x="80" y="115" text-anchor="middle" font-size="9" fill="#22303f">Série</text>\n<rect x="180" y="30" width="120" height="90" fill="none" stroke="#22303f" stroke-width="2"/>\n<line x1="180" y1="55" x2="300" y2="55" stroke="#22303f" stroke-width="1"/><line x1="180" y1="95" x2="300" y2="95" stroke="#22303f" stroke-width="1"/>\n<circle cx="240" cy="55" r="9" fill="none" stroke="#e08a2a" stroke-width="2"/><circle cx="240" cy="95" r="9" fill="none" stroke="#e08a2a" stroke-width="2"/>\n<text x="240" y="140" text-anchor="middle" font-size="9" fill="#22303f">Dérivation</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un dipôle ?", "choix": ["Un composant relié au circuit par deux bornes", "Un fil isolant", "Un générateur uniquement", "Une source de lumière naturelle"], "reponse": 0, "explication": "Un dipôle est un composant relié au reste du circuit par deux bornes."},
        {"id": "q2", "enonce": "Dans un montage en série, comment le courant traverse-t-il les dipôles ?", "choix": ["Il traverse chaque dipôle l'un après l'autre", "Il évite tous les dipôles", "Il ne circule pas", "Il traverse tous les dipôles en même temps sur des branches différentes"], "reponse": 0, "explication": "Dans un montage en série, le courant traverse chaque dipôle l'un après l'autre, en une seule boucle."},
        {"id": "q3", "enonce": "Que se passe-t-il si on ajoute plusieurs lampes en série ?", "choix": ["Chacune brille plus fort", "Chacune reçoit une part réduite de l'énergie et brille moins fort", "Rien ne change", "Elles explosent"], "reponse": 1, "explication": "En série, chaque lampe reçoit une part réduite de l'énergie totale et brille donc moins fort."},
        {"id": "q4", "enonce": "Que se passe-t-il si on retire une lampe d'un montage en série ?", "choix": ["Les autres lampes continuent de briller normalement", "Le circuit s'ouvre et toutes les lampes s'éteignent", "Rien ne change", "Seule cette lampe s'éteint"], "reponse": 1, "explication": "En série, retirer une lampe ouvre tout le circuit : toutes les lampes s'éteignent."},
        {"id": "q5", "enonce": "Comment appelle-t-on aussi le montage en dérivation ?", "choix": ["Montage en boucle", "Montage en parallèle", "Montage ouvert", "Montage isolé"], "reponse": 1, "explication": "Le montage en dérivation est aussi appelé montage en parallèle."},
        {"id": "q6", "enonce": "Dans un montage en dérivation, les dipôles sont reliés...", "choix": ["Sur une seule boucle successive", "Sur des branches différentes reliées aux mêmes deux points", "Ils ne sont jamais reliés entre eux", "Uniquement au générateur"], "reponse": 1, "explication": "En dérivation, les dipôles sont placés sur des branches différentes reliées aux mêmes deux points du circuit."},
        {"id": "q7", "enonce": "Que se passe-t-il si on retire une lampe d'un montage en dérivation ?", "choix": ["Toutes les lampes s'éteignent", "Les autres lampes continuent de fonctionner normalement", "Le générateur s'arrête", "Rien ne peut être prédit"], "reponse": 1, "explication": "En dérivation, chaque branche est indépendante : retirer une lampe n'affecte pas les autres."},
        {"id": "q8", "enonce": "Quel type de montage est utilisé pour l'installation électrique d'une maison ?", "choix": ["Le montage en série", "Le montage en dérivation", "Aucun montage particulier", "Un montage sans générateur"], "reponse": 1, "explication": "L'installation électrique d'une maison utilise un montage en dérivation, pour que chaque appareil fonctionne indépendamment."},
        {"id": "q9", "enonce": "Dans un montage en dérivation, l'éclat des lampes est-il réduit par rapport à une lampe seule ?", "choix": ["Oui, toujours", "Non, chaque lampe brille avec son éclat normal", "Cela dépend de la couleur des fils", "Oui, elles s'éteignent immédiatement"], "reponse": 1, "explication": "En dérivation, chaque lampe fonctionne indépendamment et brille avec son éclat normal."},
        {"id": "q10", "enonce": "Pourquoi dit-on que les dipôles en série dépendent les uns des autres ?", "choix": ["Car ils sont sur une seule boucle : retirer l'un ouvre tout le circuit", "Car ils sont reliés à des générateurs différents", "Ce n'est pas vrai, ils sont indépendants", "Car ils sont de couleurs différentes"], "reponse": 0, "explication": "En série, tous les dipôles partagent la même boucle : en retirer un ouvre tout le circuit."},
    ],
}

MASSE_VOLUME = {
    "slug": "masse-volume-5e",
    "titre": "La masse et le volume",
    "matiere": "physique-chimie", "niveau": "5e", "duree": "20 min",
    "resume": "Mesurer la masse et le volume d'un objet et comprendre la notion de masse volumique.",
    "objectifs": ["Mesurer une masse avec une balance", "Mesurer un volume, notamment par déplacement d'eau", "Comprendre la notion de masse volumique"],
    "contenu": [
        "La masse d'un objet représente la quantité de matière qu'il contient ; elle se mesure avec une balance et s'exprime en kilogrammes (kg) ou en grammes (g) dans le système international. Le volume représente la place occupée par un objet dans l'espace ; il s'exprime en mètres cubes (m³) ou, pour les liquides, en litres (L), sachant que 1 L équivaut à 1 dm³.",
        "Pour mesurer le volume d'un solide de forme régulière, comme un cube ou un pavé droit, on peut utiliser une formule mathématique. Pour un solide de forme irrégulière, on utilise la méthode du déplacement d'eau : on plonge l'objet dans un récipient gradué rempli d'eau, et le volume d'eau déplacé, c'est-à-dire la différence entre le niveau final et le niveau initial, correspond exactement au volume de l'objet.",
        "La masse volumique d'une matière est le rapport entre sa masse et son volume ; elle se calcule avec la formule masse volumique = masse ÷ volume, et s'exprime en kg/m³ ou en g/cm³. Elle permet de comparer des matières entre elles : la masse volumique de l'eau est d'environ 1 g/cm³, alors que celle du fer est d'environ 7,9 g/cm³, ce qui explique pourquoi le fer coule dans l'eau alors que certains bois flottent.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<rect x="30" y="100" width="90" height="50" fill="none" stroke="#22303f" stroke-width="2"/>\n<line x1="35" y1="115" x2="115" y2="115" stroke="#3b7bd6" stroke-width="2" stroke-dasharray="3,2"/>\n<line x1="35" y1="90" x2="115" y2="90" stroke="#3b7bd6" stroke-width="2"/>\n<text x="75" y="170" text-anchor="middle" font-size="9" fill="#22303f">Volume par déplacement d\'eau</text>\n<rect x="200" y="60" width="60" height="20" fill="#22303f"/><polygon points="180,90 280,90 260,100 200,100" fill="#22303f"/>\n<text x="230" y="130" text-anchor="middle" font-size="9" fill="#22303f">Balance</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Que représente la masse d'un objet ?", "choix": ["La place qu'il occupe dans l'espace", "La quantité de matière qu'il contient", "Sa couleur", "Sa température"], "reponse": 1, "explication": "La masse représente la quantité de matière contenue dans un objet."},
        {"id": "q2", "enonce": "Avec quel instrument mesure-t-on une masse ?", "choix": ["Un thermomètre", "Une balance", "Un chronomètre", "Une règle"], "reponse": 1, "explication": "On mesure une masse avec une balance."},
        {"id": "q3", "enonce": "Dans quelle unité exprime-t-on généralement une masse ?", "choix": ["Le mètre", "Le kilogramme", "Le litre", "Le degré"], "reponse": 1, "explication": "La masse s'exprime en kilogrammes (kg) ou en grammes (g)."},
        {"id": "q4", "enonce": "Que représente le volume d'un objet ?", "choix": ["Sa masse", "La place qu'il occupe dans l'espace", "Sa vitesse", "Sa couleur"], "reponse": 1, "explication": "Le volume représente la place occupée par un objet dans l'espace."},
        {"id": "q5", "enonce": "À combien de litres correspond 1 dm³ ?", "choix": ["1 L", "10 L", "0,1 L", "100 L"], "reponse": 0, "explication": "1 litre équivaut exactement à 1 décimètre cube (1 dm³)."},
        {"id": "q6", "enonce": "Comment mesure-t-on le volume d'un objet de forme irrégulière ?", "choix": ["Avec une formule mathématique uniquement", "Par déplacement d'eau dans un récipient gradué", "C'est impossible", "Avec un thermomètre"], "reponse": 1, "explication": "On utilise la méthode du déplacement d'eau pour mesurer le volume d'un objet de forme irrégulière."},
        {"id": "q7", "enonce": "Comment calcule-t-on la masse volumique ?", "choix": ["Masse × volume", "Masse ÷ volume", "Volume ÷ masse", "Masse + volume"], "reponse": 1, "explication": "La masse volumique se calcule en divisant la masse par le volume."},
        {"id": "q8", "enonce": "Quelle est approximativement la masse volumique de l'eau ?", "choix": ["1 g/cm³", "7,9 g/cm³", "0,1 g/cm³", "100 g/cm³"], "reponse": 0, "explication": "La masse volumique de l'eau est d'environ 1 g/cm³."},
        {"id": "q9", "enonce": "Pourquoi le fer coule-t-il dans l'eau ?", "choix": ["Car sa masse volumique est plus faible que celle de l'eau", "Car sa masse volumique est plus grande que celle de l'eau", "Car il est magnétique", "Car il est chaud"], "reponse": 1, "explication": "Le fer, avec une masse volumique d'environ 7,9 g/cm³, est plus dense que l'eau : il coule."},
        {"id": "q10", "enonce": "En quelle unité peut s'exprimer une masse volumique ?", "choix": ["kg/m³ ou g/cm³", "Uniquement en kg", "Uniquement en litres", "En degrés Celsius"], "reponse": 0, "explication": "La masse volumique s'exprime en kg/m³ ou en g/cm³."},
    ],
}

SYSTEME_SOLAIRE_MVT = {
    "slug": "mouvements-interactions-systeme-solaire-5e",
    "titre": "Les mouvements et les interactions dans le système solaire",
    "matiere": "physique-chimie", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre les mouvements des astres du système solaire et le rôle de la gravitation.",
    "objectifs": ["Décrire les mouvements des planètes autour du Soleil", "Comprendre le rôle de la gravitation dans ces mouvements", "Distinguer rotation et révolution"],
    "contenu": [
        "Le système solaire est composé du Soleil et de tous les objets qui gravitent autour de lui : les huit planètes, leurs satellites naturels, les astéroïdes et les comètes. Chaque planète tourne autour du Soleil en suivant une trajectoire appelée orbite, généralement presque circulaire ; ce mouvement de révolution prend un temps différent pour chaque planète, appelé période de révolution. La Terre met environ 365 jours pour effectuer une révolution complète.",
        "En plus de tourner autour du Soleil, chaque planète tourne aussi sur elle-même : c'est le mouvement de rotation. La Terre effectue une rotation complète en environ 24 heures, ce qui explique l'alternance des jours et des nuits. La rotation et la révolution sont deux mouvements différents mais simultanés.",
        "Ces mouvements sont régis par la gravitation, une force d'attraction qui s'exerce entre tous les objets possédant une masse, et qui est d'autant plus forte que les objets sont massifs et proches l'un de l'autre. C'est la gravitation exercée par le Soleil, très massif, qui maintient les planètes sur leur orbite au lieu de s'échapper dans l'espace ; c'est aussi la gravitation de la Terre qui retient la Lune en orbite autour d'elle.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="160" cy="95" r="22" fill="#f4b942"/>\n<ellipse cx="160" cy="95" rx="90" ry="45" fill="none" stroke="#22303f" stroke-width="1"/>\n<circle cx="250" cy="95" r="8" fill="#3b7bd6"/>\n<ellipse cx="160" cy="95" rx="130" ry="65" fill="none" stroke="#22303f" stroke-width="1"/>\n<circle cx="30" cy="95" r="6" fill="#3ba55d"/>\n<text x="160" y="175" text-anchor="middle" font-size="10" fill="#22303f">Les planètes orbitent autour du Soleil</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que le système solaire ?", "choix": ["Uniquement la Terre et la Lune", "Le Soleil et tous les objets qui gravitent autour de lui", "Uniquement les étoiles lointaines", "Un ensemble de galaxies"], "reponse": 1, "explication": "Le système solaire est composé du Soleil et de tous les objets qui gravitent autour de lui."},
        {"id": "q2", "enonce": "Comment appelle-t-on la trajectoire suivie par une planète autour du Soleil ?", "choix": ["Une rotation", "Une orbite", "Un satellite", "Une éclipse"], "reponse": 1, "explication": "L'orbite est la trajectoire suivie par une planète autour du Soleil."},
        {"id": "q3", "enonce": "Combien de temps met la Terre pour effectuer une révolution complète autour du Soleil ?", "choix": ["24 heures", "Environ 365 jours", "1 mois", "10 ans"], "reponse": 1, "explication": "La Terre met environ 365 jours (une année) pour faire le tour complet du Soleil."},
        {"id": "q4", "enonce": "Qu'est-ce que le mouvement de rotation d'une planète ?", "choix": ["Son déplacement autour du Soleil", "Son mouvement sur elle-même", "Son changement de couleur", "Son rapprochement du Soleil"], "reponse": 1, "explication": "La rotation est le mouvement d'une planète sur elle-même."},
        {"id": "q5", "enonce": "Combien de temps met la Terre pour effectuer une rotation complète sur elle-même ?", "choix": ["Environ 24 heures", "Environ 365 jours", "1 heure", "1 semaine"], "reponse": 0, "explication": "La Terre tourne sur elle-même en environ 24 heures, ce qui donne l'alternance jour/nuit."},
        {"id": "q6", "enonce": "Qu'est-ce qui explique l'alternance des jours et des nuits ?", "choix": ["La révolution de la Terre", "La rotation de la Terre sur elle-même", "Le mouvement de la Lune uniquement", "Le mouvement des étoiles"], "reponse": 1, "explication": "C'est la rotation de la Terre sur elle-même qui provoque l'alternance des jours et des nuits."},
        {"id": "q7", "enonce": "Qu'est-ce que la gravitation ?", "choix": ["Une force de répulsion entre les objets", "Une force d'attraction entre tous les objets possédant une masse", "Un phénomène lumineux", "Un type de vent"], "reponse": 1, "explication": "La gravitation est une force d'attraction qui s'exerce entre tous les objets possédant une masse."},
        {"id": "q8", "enonce": "De quoi dépend l'intensité de la gravitation entre deux objets ?", "choix": ["De leur couleur", "De leur masse et de leur distance", "De leur température uniquement", "De leur vitesse uniquement"], "reponse": 1, "explication": "La gravitation est d'autant plus forte que les objets sont massifs et proches l'un de l'autre."},
        {"id": "q9", "enonce": "Pourquoi les planètes restent-elles sur leur orbite autour du Soleil ?", "choix": ["Grâce à la gravitation exercée par le Soleil", "Elles sont attachées par des cordes invisibles", "Grâce au vent solaire uniquement", "Sans raison particulière"], "reponse": 0, "explication": "La gravitation exercée par le Soleil, très massif, maintient les planètes sur leur orbite."},
        {"id": "q10", "enonce": "Qu'est-ce qui retient la Lune en orbite autour de la Terre ?", "choix": ["La gravitation de la Terre", "Le vent", "La lumière du Soleil", "Rien, elle flotte librement"], "reponse": 0, "explication": "C'est la gravitation exercée par la Terre qui retient la Lune en orbite autour d'elle."},
    ],
}

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "lumiere-vision-image-5e", [CIRCUIT, DIPOLES, MASSE_VOLUME, SYSTEME_SOLAIRE_MVT])

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print("4 leçons Physique-Chimie 5e ajoutées.")
