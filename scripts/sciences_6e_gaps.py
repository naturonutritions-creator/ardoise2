# -*- coding: utf-8 -*-
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

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

SEPARATION = {
    "slug": "separation-constituants-melange-6e",
    "titre": "La séparation des constituants d'un mélange",
    "matiere": "physique-chimie", "niveau": "6e", "duree": "20 min",
    "resume": "Découvrir les techniques simples pour séparer les constituants d'un mélange.",
    "objectifs": ["Distinguer mélange homogène et mélange hétérogène", "Connaître les techniques de filtration et de décantation", "Comprendre le principe de l'évaporation et de la distillation simple"],
    "contenu": [
        "Un mélange est hétérogène quand on distingue à l'œil nu ses différents constituants, comme l'eau et le sable ou l'huile et l'eau. Il est homogène quand on ne les distingue plus, même au microscope, comme l'eau salée ou l'air. Pour séparer les constituants d'un mélange hétérogène solide-liquide, on utilise la décantation (les particules les plus denses se déposent au fond par gravité) ou la filtration (le mélange passe à travers un filtre en papier qui retient les particules solides et laisse passer le liquide).",
        "Pour séparer les constituants d'un mélange homogène comme l'eau salée, la filtration ne suffit pas car le sel est dissous dans l'eau : il faut utiliser l'évaporation. En chauffant le mélange, l'eau se transforme en vapeur et s'échappe, tandis que le sel, non volatil, reste au fond du récipient sous forme de cristaux.",
        "La distillation permet de séparer les constituants d'un mélange homogène liquide-liquide, comme l'eau et l'alcool, en exploitant leurs températures d'ébullition différentes. En chauffant le mélange, le constituant qui s'évapore à la température la plus basse se vaporise en premier, puis se recondense en refroidissant dans un tube appelé réfrigérant, ce qui permet de le recueillir séparément.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<path d="M40 40 L60 100 Q60 130 90 130 L100 130 Q130 130 130 100 L150 40 Z" fill="none" stroke="#22303f" stroke-width="2"/>\n<path d="M45 55 L145 55" stroke="#3b7bd6" stroke-width="2"/>\n<circle cx="70" cy="75" r="3" fill="#7a5230"/><circle cx="90" cy="90" r="3" fill="#7a5230"/><circle cx="110" cy="80" r="3" fill="#7a5230"/>\n<text x="95" y="150" text-anchor="middle" font-size="9" fill="#22303f">Filtration</text>\n<rect x="200" y="60" width="90" height="60" fill="#cfe3fb"/>\n<circle cx="220" cy="95" r="3" fill="#22303f"/><circle cx="240" cy="90" r="3" fill="#22303f"/><circle cx="260" cy="100" r="3" fill="#22303f"/>\n<text x="245" y="140" text-anchor="middle" font-size="9" fill="#22303f">Décantation</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Quand un mélange est-il dit hétérogène ?", "choix": ["Quand on distingue ses constituants à l'œil nu", "Quand on ne distingue plus ses constituants", "Quand il ne contient qu'un seul constituant", "Quand il est liquide"], "reponse": 0, "explication": "Un mélange hétérogène est un mélange dont on distingue les différents constituants à l'œil nu."},
        {"id": "q2", "enonce": "Quelle technique permet de retenir des particules solides grâce à un filtre en papier ?", "choix": ["La décantation", "La filtration", "L'évaporation", "La distillation"], "reponse": 1, "explication": "La filtration fait passer le mélange à travers un filtre qui retient les particules solides."},
        {"id": "q3", "enonce": "Sur quel principe repose la décantation ?", "choix": ["L'évaporation de l'eau", "Le dépôt des particules les plus denses par gravité", "Le chauffage du mélange", "La différence de couleur"], "reponse": 1, "explication": "La décantation repose sur le fait que les particules les plus denses se déposent au fond par gravité."},
        {"id": "q4", "enonce": "Pourquoi la filtration ne suffit-elle pas pour séparer l'eau et le sel dissous ?", "choix": ["Car le sel est un solide visible", "Car le sel est dissous dans l'eau, on ne peut pas le filtrer", "Car l'eau salée est un mélange hétérogène", "Car le filtre retient l'eau"], "reponse": 1, "explication": "Le sel étant dissous, il traverse le filtre avec l'eau : la filtration est inefficace."},
        {"id": "q5", "enonce": "Quelle technique permet de récupérer le sel dissous dans l'eau ?", "choix": ["La décantation", "La filtration", "L'évaporation", "L'aimantation"], "reponse": 2, "explication": "En chauffant, l'eau s'évapore et le sel, non volatil, reste au fond sous forme de cristaux."},
        {"id": "q6", "enonce": "La distillation sert à séparer...", "choix": ["Un solide d'un liquide", "Deux liquides mélangés de façon homogène", "Deux gaz", "Deux solides"], "reponse": 1, "explication": "La distillation sépare les constituants d'un mélange homogène liquide-liquide grâce à leurs températures d'ébullition différentes."},
        {"id": "q7", "enonce": "Dans une distillation, quel constituant se vaporise en premier ?", "choix": ["Celui qui a la température d'ébullition la plus haute", "Celui qui a la température d'ébullition la plus basse", "Les deux en même temps", "Cela dépend de la couleur"], "reponse": 1, "explication": "Le constituant dont la température d'ébullition est la plus basse se vaporise en premier."},
        {"id": "q8", "enonce": "Comment appelle-t-on le tube qui refroidit la vapeur lors d'une distillation ?", "choix": ["Le filtre", "Le réfrigérant", "Le décanteur", "Le bécher"], "reponse": 1, "explication": "La vapeur se recondense en refroidissant dans un tube appelé réfrigérant."},
        {"id": "q9", "enonce": "L'eau salée est un exemple de mélange...", "choix": ["Hétérogène", "Homogène", "Solide", "Gazeux"], "reponse": 1, "explication": "L'eau salée est homogène : on ne distingue pas le sel dissous, même au microscope."},
        {"id": "q10", "enonce": "L'eau et le sable forment un mélange...", "choix": ["Homogène", "Hétérogène", "Gazeux uniquement", "Impossible à séparer"], "reponse": 1, "explication": "On distingue le sable dans l'eau à l'œil nu : c'est un mélange hétérogène."},
    ],
}

TRANSMISSION = {
    "slug": "transmission-signal-6e",
    "titre": "La transmission de l'information par un signal",
    "matiere": "physique-chimie", "niveau": "6e", "duree": "20 min",
    "resume": "Comprendre ce qu'est un signal et comment l'information est transmise et codée.",
    "objectifs": ["Définir ce qu'est un signal", "Distinguer signal analogique et signal numérique", "Identifier différents moyens de transmission de l'information"],
    "contenu": [
        "Un signal est un phénomène physique, lumineux, sonore ou électrique, qui transporte une information d'un émetteur vers un récepteur. La voix est un signal sonore transmis dans l'air ; un feu tricolore envoie un signal lumineux ; un smartphone envoie des signaux électriques ou des ondes radio pour communiquer.",
        "Un signal peut être analogique, c'est-à-dire qu'il varie de façon continue, comme le son capté par un microphone, ou numérique, c'est-à-dire codé sous forme de nombres, le plus souvent en binaire, une suite de 0 et de 1. La plupart des appareils actuels convertissent les signaux analogiques en signaux numériques pour les traiter, les stocker et les transmettre plus facilement, avec moins de pertes de qualité.",
        "L'information peut être transmise par différents supports : câbles électriques, fibre optique grâce à la lumière, ondes radio comme le Wi-Fi, le Bluetooth ou la téléphonie mobile, ou encore ondes sonores. Chaque support a une portée, une vitesse et une capacité de transmission différentes ; la fibre optique, par exemple, permet de transmettre énormément d'informations très rapidement sur de longues distances.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="40" cy="95" r="18" fill="#3b7bd6"/><text x="40" y="99" text-anchor="middle" font-size="9" fill="#fff">Emetteur</text>\n<path d="M70 95 Q100 60 130 95 Q160 130 190 95 Q220 60 250 95" fill="none" stroke="#e08a2a" stroke-width="3"/>\n<circle cx="280" cy="95" r="18" fill="#3ba55d"/><text x="280" y="99" text-anchor="middle" font-size="8" fill="#fff">Recepteur</text>\n<text x="160" y="150" text-anchor="middle" font-size="10" fill="#22303f">Un signal transporte une information</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un signal ?", "choix": ["Un phénomène physique qui transporte une information", "Un objet solide", "Une couleur uniquement", "Un mélange chimique"], "reponse": 0, "explication": "Un signal est un phénomène physique (lumineux, sonore, électrique) qui transporte une information."},
        {"id": "q2", "enonce": "La voix est un exemple de signal...", "choix": ["Lumineux", "Sonore", "Électrique uniquement", "Numérique uniquement"], "reponse": 1, "explication": "La voix est un signal sonore transmis dans l'air."},
        {"id": "q3", "enonce": "Un signal analogique varie...", "choix": ["De façon continue", "Uniquement en 0 et 1", "Il ne varie jamais", "De façon aléatoire seulement"], "reponse": 0, "explication": "Un signal analogique varie de façon continue, comme le son capté par un microphone."},
        {"id": "q4", "enonce": "Un signal numérique est codé sous forme de...", "choix": ["Couleurs", "Nombres, le plus souvent en binaire", "Sons uniquement", "Odeurs"], "reponse": 1, "explication": "Un signal numérique est codé sous forme de nombres, en général en binaire (suite de 0 et de 1)."},
        {"id": "q5", "enonce": "Pourquoi convertit-on souvent un signal analogique en signal numérique ?", "choix": ["Pour le rendre invisible", "Pour le traiter, le stocker et le transmettre plus facilement", "Pour le détruire", "Ce n'est jamais fait"], "reponse": 1, "explication": "La conversion en numérique facilite le traitement, le stockage et la transmission avec moins de pertes."},
        {"id": "q6", "enonce": "Quel support de transmission utilise la lumière ?", "choix": ["Le câble électrique", "La fibre optique", "L'onde sonore", "Le papier"], "reponse": 1, "explication": "La fibre optique transmet l'information grâce à la lumière."},
        {"id": "q7", "enonce": "Le Wi-Fi et le Bluetooth transmettent l'information par...", "choix": ["Des câbles", "Des ondes radio", "Des ondes sonores uniquement", "De la lumière visible"], "reponse": 1, "explication": "Le Wi-Fi et le Bluetooth utilisent des ondes radio pour transmettre l'information."},
        {"id": "q8", "enonce": "Quel support permet de transmettre très rapidement de grandes quantités d'informations sur de longues distances ?", "choix": ["Le papier", "La fibre optique", "La voix", "Le feu tricolore"], "reponse": 1, "explication": "La fibre optique permet une transmission très rapide et à grande capacité sur de longues distances."},
        {"id": "q9", "enonce": "Un feu tricolore transmet un signal...", "choix": ["Sonore", "Lumineux", "Numérique uniquement", "Chimique"], "reponse": 1, "explication": "Le feu tricolore envoie un signal lumineux pour transmettre une information aux usagers."},
        {"id": "q10", "enonce": "Dans la transmission d'un signal, qui reçoit l'information ?", "choix": ["L'émetteur", "Le récepteur", "Le support uniquement", "Personne"], "reponse": 1, "explication": "Le récepteur est celui qui reçoit l'information transportée par le signal."},
    ],
}

CONVERSIONS = {
    "slug": "conversions-stockage-energie-6e",
    "titre": "Les conversions et le stockage de l'énergie",
    "matiere": "physique-chimie", "niveau": "6e", "duree": "20 min",
    "resume": "Comprendre comment l'énergie change de forme et comment elle peut être stockée.",
    "objectifs": ["Identifier différentes formes d'énergie", "Comprendre qu'une conversion d'énergie transforme une forme en une autre", "Connaître quelques moyens de stocker l'énergie"],
    "contenu": [
        "L'énergie existe sous plusieurs formes : énergie électrique, mécanique liée au mouvement, thermique liée à la chaleur, chimique stockée dans les aliments ou les combustibles, ou encore lumineuse. Un dispositif convertit souvent une forme d'énergie en une autre : un panneau solaire convertit l'énergie lumineuse en énergie électrique, un moteur convertit l'énergie électrique en énergie mécanique, une ampoule convertit l'énergie électrique en lumière et en chaleur.",
        "Lors de chaque conversion, une partie de l'énergie est généralement perdue sous forme de chaleur non utile : c'est pourquoi aucun appareil n'a un rendement de 100 %. Économiser l'énergie consiste notamment à choisir des appareils qui convertissent l'énergie avec le moins de pertes possible.",
        "L'énergie peut être stockée pour être utilisée plus tard : une pile ou une batterie stocke de l'énergie chimique qui se convertit en énergie électrique à l'usage ; un barrage stocke de l'énergie sous forme d'eau retenue en hauteur, convertie en électricité quand l'eau descend et fait tourner une turbine ; les aliments stockent de l'énergie chimique que le corps humain convertit en énergie pour bouger et fonctionner.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<rect x="20" y="70" width="70" height="45" rx="6" fill="#f4b942"/><text x="55" y="97" text-anchor="middle" font-size="9" fill="#22303f">Solaire</text>\n<path d="M95 92 L135 92" stroke="#22303f" stroke-width="2" marker-end="url(#arrow)"/>\n<rect x="140" y="70" width="70" height="45" rx="6" fill="#3b7bd6"/><text x="175" y="97" text-anchor="middle" font-size="9" fill="#fff">Electrique</text>\n<path d="M215 92 L255 92" stroke="#22303f" stroke-width="2"/>\n<rect x="260" y="70" width="50" height="45" rx="6" fill="#3ba55d"/><text x="285" y="97" text-anchor="middle" font-size="9" fill="#fff">Mecanique</text>\n<text x="160" y="150" text-anchor="middle" font-size="10" fill="#22303f">L\'énergie se convertit d\'une forme à une autre</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Que convertit un panneau solaire ?", "choix": ["L'énergie mécanique en énergie chimique", "L'énergie lumineuse en énergie électrique", "L'énergie électrique en lumière", "Rien, il stocke seulement"], "reponse": 1, "explication": "Un panneau solaire convertit l'énergie lumineuse du Soleil en énergie électrique."},
        {"id": "q2", "enonce": "Que convertit un moteur électrique ?", "choix": ["L'énergie électrique en énergie mécanique", "L'énergie chimique en lumière", "L'énergie thermique en énergie électrique", "Rien"], "reponse": 0, "explication": "Un moteur électrique convertit l'énergie électrique en énergie mécanique (mouvement)."},
        {"id": "q3", "enonce": "Une ampoule convertit l'énergie électrique en...", "choix": ["Énergie chimique uniquement", "Lumière et chaleur", "Énergie mécanique uniquement", "Rien, elle ne convertit rien"], "reponse": 1, "explication": "Une ampoule convertit l'énergie électrique en lumière, mais aussi en chaleur (perte)."},
        {"id": "q4", "enonce": "Pourquoi aucun appareil n'a un rendement de 100 % ?", "choix": ["Car une partie de l'énergie est toujours perdue en chaleur non utile", "Car les appareils sont mal fabriqués", "Car l'énergie disparaît complètement", "Ce n'est pas vrai, certains ont 100 %"], "reponse": 0, "explication": "Lors de chaque conversion, une partie de l'énergie se perd toujours sous forme de chaleur non utile."},
        {"id": "q5", "enonce": "Que stocke une pile ou une batterie ?", "choix": ["De l'énergie mécanique", "De l'énergie chimique", "De la lumière", "Rien, elle produit l'énergie elle-même"], "reponse": 1, "explication": "Une pile ou une batterie stocke de l'énergie chimique, convertie en électricité à l'usage."},
        {"id": "q6", "enonce": "Comment un barrage stocke-t-il de l'énergie ?", "choix": ["Sous forme d'eau retenue en hauteur", "Sous forme de chaleur uniquement", "Sous forme de lumière", "Il ne stocke rien"], "reponse": 0, "explication": "Un barrage stocke de l'énergie sous forme d'eau retenue en hauteur, convertie en électricité."},
        {"id": "q7", "enonce": "Qu'est-ce qui fait tourner la turbine d'un barrage ?", "choix": ["Le vent", "L'eau qui descend", "Le soleil", "Rien, elle tourne toute seule"], "reponse": 1, "explication": "L'eau qui descend du barrage fait tourner la turbine, produisant de l'électricité."},
        {"id": "q8", "enonce": "Quelle forme d'énergie est stockée dans les aliments ?", "choix": ["Énergie électrique", "Énergie chimique", "Énergie lumineuse", "Énergie sonore"], "reponse": 1, "explication": "Les aliments stockent de l'énergie chimique, que le corps convertit en énergie pour fonctionner."},
        {"id": "q9", "enonce": "Économiser l'énergie consiste notamment à...", "choix": ["Choisir des appareils qui convertissent l'énergie avec le moins de pertes possible", "Utiliser uniquement des piles", "Éviter toute conversion d'énergie", "Ne jamais utiliser d'électricité"], "reponse": 0, "explication": "Choisir des appareils efficaces limite les pertes d'énergie lors des conversions."},
        {"id": "q10", "enonce": "L'énergie thermique est liée à...", "choix": ["La lumière", "La chaleur", "Le mouvement", "Le son"], "reponse": 1, "explication": "L'énergie thermique est l'énergie liée à la chaleur."},
    ],
}

MICROORGANISMES = {
    "slug": "micro-organismes-alimentation-6e",
    "titre": "L'utilisation des micro-organismes dans l'alimentation humaine",
    "matiere": "svt", "niveau": "6e", "duree": "20 min",
    "resume": "Découvrir comment certains micro-organismes sont utilisés pour fabriquer des aliments.",
    "objectifs": ["Définir ce qu'est un micro-organisme", "Comprendre le principe de la fermentation", "Citer des exemples d'aliments fabriqués grâce à des micro-organismes"],
    "contenu": [
        "Un micro-organisme est un être vivant si petit qu'il n'est visible qu'au microscope : bactéries, levures et certaines moisissures en sont des exemples. Si certains micro-organismes peuvent provoquer des maladies, beaucoup d'autres sont utiles et même indispensables à la fabrication de nombreux aliments que nous consommons chaque jour.",
        "La fermentation est une transformation d'aliments provoquée par des micro-organismes, qui se nourrissent des sucres présents et produisent en retour d'autres substances comme du gaz, de l'acide ou de l'alcool. Les levures transforment ainsi le sucre de la pâte à pain en gaz carbonique, ce qui fait lever le pain ; les mêmes levures transforment le sucre du raisin en alcool pour fabriquer le vin.",
        "De nombreux aliments du quotidien résultent de fermentations : le yaourt est obtenu grâce à des bactéries lactiques qui transforment le lactose du lait en acide lactique, ce qui épaissit et acidifie le lait ; le fromage utilise aussi des bactéries et parfois des moisissures, comme pour le roquefort ; la choucroute et le vinaigre font également intervenir des micro-organismes utiles.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<ellipse cx="80" cy="110" rx="45" ry="30" fill="#e7c07a"/><text x="80" y="150" text-anchor="middle" font-size="9" fill="#22303f">Pain</text>\n<circle cx="200" cy="90" r="35" fill="#f5f2e8" stroke="#c7bfa6"/><text x="200" y="150" text-anchor="middle" font-size="9" fill="#22303f">Yaourt</text>\n<g fill="#3ba55d"><circle cx="60" cy="90" r="4"/><circle cx="75" cy="80" r="4"/><circle cx="90" cy="88" r="4"/><circle cx="185" cy="75" r="4"/><circle cx="205" cy="65" r="4"/><circle cx="215" cy="80" r="4"/></g>\n<text x="160" y="180" text-anchor="middle" font-size="10" fill="#22303f">Les micro-organismes transforment les aliments</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un micro-organisme ?", "choix": ["Un être vivant visible à l'œil nu", "Un être vivant visible seulement au microscope", "Un objet non vivant", "Un minéral"], "reponse": 1, "explication": "Un micro-organisme est un être vivant si petit qu'il n'est visible qu'au microscope."},
        {"id": "q2", "enonce": "Citez un exemple de micro-organisme.", "choix": ["Une bactérie", "Un chat", "Un arbre", "Une pierre"], "reponse": 0, "explication": "Les bactéries, levures et moisissures sont des exemples de micro-organismes."},
        {"id": "q3", "enonce": "Qu'est-ce que la fermentation ?", "choix": ["Une transformation d'aliments provoquée par des micro-organismes", "Une cuisson à haute température", "Un simple mélange sans transformation", "Une réaction impossible dans les aliments"], "reponse": 0, "explication": "La fermentation est une transformation d'aliments provoquée par des micro-organismes."},
        {"id": "q4", "enonce": "Que produisent les levures dans la pâte à pain ?", "choix": ["De l'eau uniquement", "Du gaz carbonique, qui fait lever le pain", "Du sel", "De l'huile"], "reponse": 1, "explication": "Les levures transforment le sucre de la pâte en gaz carbonique, ce qui fait lever le pain."},
        {"id": "q5", "enonce": "Que transforment les levures pour fabriquer le vin ?", "choix": ["Le sucre du raisin en alcool", "L'eau en sucre", "L'alcool en sucre", "Le raisin en pain"], "reponse": 0, "explication": "Les levures transforment le sucre du raisin en alcool lors de la fermentation."},
        {"id": "q6", "enonce": "Quelles bactéries transforment le lait en yaourt ?", "choix": ["Des bactéries lactiques", "Des levures uniquement", "Aucune, c'est un procédé purement chimique", "Des moisissures uniquement"], "reponse": 0, "explication": "Des bactéries lactiques transforment le lactose du lait en acide lactique pour former le yaourt."},
        {"id": "q7", "enonce": "Qu'est-ce que l'acide lactique produit lors de la fabrication du yaourt ?", "choix": ["Il rend le lait plus liquide", "Il épaissit et acidifie le lait", "Il n'a aucun effet", "Il rend le lait plus sucré"], "reponse": 1, "explication": "L'acide lactique épaissit et acidifie le lait, donnant la texture du yaourt."},
        {"id": "q8", "enonce": "Quel fromage utilise des moisissures dans sa fabrication ?", "choix": ["Le roquefort", "L'emmental uniquement", "Aucun fromage", "Le fromage blanc uniquement"], "reponse": 0, "explication": "Le roquefort est fabriqué grâce à des moisissures particulières."},
        {"id": "q9", "enonce": "Citez un autre aliment fermenté que le pain, le vin, le yaourt ou le fromage.", "choix": ["La choucroute", "Le sel", "L'huile", "Le sucre en poudre"], "reponse": 0, "explication": "La choucroute résulte d'une fermentation par des micro-organismes."},
        {"id": "q10", "enonce": "Tous les micro-organismes sont-ils dangereux pour l'humain ?", "choix": ["Oui, tous", "Non, beaucoup sont utiles, notamment en alimentation", "Non, aucun n'est dangereux", "Cela dépend uniquement de leur couleur"], "reponse": 1, "explication": "Si certains micro-organismes peuvent être pathogènes, beaucoup d'autres sont utiles, notamment dans l'alimentation."},
    ],
}

TRI_RECYCLAGE = {
    "slug": "tri-recyclage-materiaux-6e",
    "titre": "Le tri et le recyclage des matériaux",
    "matiere": "svt", "niveau": "6e", "duree": "20 min",
    "resume": "Comprendre pourquoi et comment on trie et recycle les matériaux pour limiter leur impact environnemental.",
    "objectifs": ["Identifier les principaux matériaux recyclables", "Comprendre le principe du recyclage", "Comprendre l'intérêt environnemental du tri des déchets"],
    "contenu": [
        "Les objets que nous utilisons sont fabriqués à partir de matériaux comme le verre, le papier, le plastique, le métal ou le bois. Extraire et fabriquer ces matériaux consomme des ressources naturelles, eau, énergie, matières premières, souvent non renouvelables ou disponibles en quantité limitée. Trier les déchets permet de séparer les matériaux recyclables des autres déchets, pour leur donner une seconde vie plutôt que de les jeter.",
        "Le recyclage consiste à transformer un déchet en matière première réutilisable pour fabriquer un nouvel objet. Le verre peut être fondu et refondu presque à l'infini sans perdre en qualité ; le papier et le carton peuvent être recyclés plusieurs fois, mais leurs fibres s'usent progressivement ; certains plastiques sont recyclables, d'autres beaucoup moins facilement, ce qui rend le tri du plastique plus complexe.",
        "Recycler présente plusieurs avantages : cela limite l'extraction de nouvelles ressources naturelles, réduit la quantité de déchets envoyés en décharge ou incinérés, et consomme généralement moins d'énergie que la fabrication à partir de matières premières neuves. Recycler l'aluminium, par exemple, consomme environ 20 fois moins d'énergie que d'en produire à partir du minerai. C'est pourquoi le tri sélectif à la maison ou au collège est un geste simple mais utile pour l'environnement.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<rect x="30" y="80" width="60" height="70" fill="#3b7bd6"/><text x="60" y="120" text-anchor="middle" font-size="9" fill="#fff">Verre</text>\n<rect x="130" y="80" width="60" height="70" fill="#e7c07a"/><text x="160" y="120" text-anchor="middle" font-size="9" fill="#22303f">Papier</text>\n<rect x="230" y="80" width="60" height="70" fill="#3ba55d"/><text x="260" y="120" text-anchor="middle" font-size="9" fill="#fff">Plastique</text>\n<path d="M60 60 A 30 30 0 1 1 59 60" fill="none" stroke="#22303f" stroke-width="2"/>\n<text x="160" y="175" text-anchor="middle" font-size="10" fill="#22303f">Trier pour recycler</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Pourquoi trie-t-on les déchets ?", "choix": ["Pour les rendre plus jolis", "Pour séparer les matériaux recyclables des autres déchets", "Cela ne sert à rien", "Pour les brûler plus vite"], "reponse": 1, "explication": "Le tri sépare les matériaux recyclables des autres déchets afin de leur donner une seconde vie."},
        {"id": "q2", "enonce": "Qu'est-ce que le recyclage ?", "choix": ["Jeter un déchet définitivement", "Transformer un déchet en matière première réutilisable", "Brûler tous les déchets", "Enterrer les déchets"], "reponse": 1, "explication": "Le recyclage transforme un déchet en matière première pour fabriquer un nouvel objet."},
        {"id": "q3", "enonce": "Le verre peut-il être recyclé à l'infini ?", "choix": ["Non, jamais", "Oui, presque à l'infini sans perdre en qualité", "Une seule fois", "Cela dépend de sa couleur uniquement"], "reponse": 1, "explication": "Le verre peut être fondu et refondu presque à l'infini sans perdre en qualité."},
        {"id": "q4", "enonce": "Que se passe-t-il aux fibres du papier à chaque recyclage ?", "choix": ["Rien, elles restent identiques", "Elles s'usent progressivement", "Elles deviennent plus solides", "Elles disparaissent immédiatement"], "reponse": 1, "explication": "Les fibres du papier et du carton s'usent progressivement à chaque recyclage."},
        {"id": "q5", "enonce": "Pourquoi le tri du plastique est-il plus complexe ?", "choix": ["Car tous les plastiques se recyclent facilement", "Car certains plastiques sont difficiles à recycler", "Car le plastique n'existe pas en plusieurs types", "Ce n'est pas complexe"], "reponse": 1, "explication": "Certains plastiques sont recyclables, d'autres beaucoup moins facilement, ce qui complique le tri."},
        {"id": "q6", "enonce": "Recycler l'aluminium par rapport à en produire à partir du minerai consomme...", "choix": ["Beaucoup plus d'énergie", "Environ 20 fois moins d'énergie", "Exactement la même énergie", "Il est impossible de recycler l'aluminium"], "reponse": 1, "explication": "Recycler l'aluminium consomme environ 20 fois moins d'énergie que d'en produire à partir du minerai."},
        {"id": "q7", "enonce": "Le recyclage permet de limiter...", "choix": ["L'extraction de nouvelles ressources naturelles", "La quantité d'objets fabriqués", "Le nombre d'usines", "Rien du tout"], "reponse": 0, "explication": "Le recyclage limite l'extraction de nouvelles ressources naturelles."},
        {"id": "q8", "enonce": "Quel est un des matériaux couramment recyclés ?", "choix": ["Le verre", "L'air", "L'eau de pluie", "Le sable de plage"], "reponse": 0, "explication": "Le verre, le papier, le métal et certains plastiques sont couramment recyclés."},
        {"id": "q9", "enonce": "Le tri sélectif au collège ou à la maison est un geste...", "choix": ["Inutile", "Simple mais utile pour l'environnement", "Dangereux", "Interdit"], "reponse": 1, "explication": "Le tri sélectif est un geste simple qui a un réel intérêt pour l'environnement."},
        {"id": "q10", "enonce": "Fabriquer un matériau à partir de matières premières neuves consomme en général...", "choix": ["Moins d'énergie que le recyclage", "Plus d'énergie que le recyclage", "Exactement autant d'énergie", "Aucune énergie"], "reponse": 1, "explication": "Fabriquer à partir de matières premières neuves consomme en général plus d'énergie que le recyclage."},
    ],
}

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "lumiere-vision-6e", [SEPARATION, TRANSMISSION, CONVERSIONS])
txt = insert_after(txt, "mouvement-terre-saisons-6e", [MICROORGANISMES, TRI_RECYCLAGE])

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print("5 leçons Sciences 6e ajoutées.")
