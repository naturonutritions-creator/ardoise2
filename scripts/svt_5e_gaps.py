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

TERRE_SOLAIRE = {
    "slug": "terre-systeme-solaire-5e",
    "titre": "La Terre dans le système solaire",
    "matiere": "svt", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre la place de la Terre dans le système solaire et les conditions qui y rendent la vie possible.",
    "objectifs": ["Situer la Terre parmi les planètes du système solaire", "Identifier les caractéristiques qui rendent la Terre habitable", "Comprendre la notion de zone habitable"],
    "contenu": [
        "La Terre est la troisième planète du système solaire en partant du Soleil, après Mercure et Vénus. C'est une planète rocheuse, comme Mercure, Vénus et Mars, contrairement aux planètes gazeuses plus éloignées comme Jupiter ou Saturne. Elle est actuellement la seule planète connue à abriter la vie.",
        "Plusieurs conditions rendent la Terre habitable : elle se situe dans la « zone habitable » du système solaire, une distance du Soleil ni trop proche ni trop éloignée, qui permet à l'eau d'exister à l'état liquide à sa surface, condition indispensable à la vie telle que nous la connaissons. Son atmosphère la protège des rayonnements dangereux et maintient une température moyenne compatible avec la vie, tandis que son champ magnétique la protège du vent solaire.",
        "La Terre possède également un satellite naturel, la Lune, dont la gravitation stabilise l'inclinaison de l'axe terrestre et provoque les marées. Cette stabilité de l'inclinaison contribue à la régularité des saisons sur de longues durées, un facteur supplémentaire favorable au maintien de la vie sur notre planète.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="60" cy="95" r="22" fill="#f4b942"/>\n<circle cx="120" cy="95" r="6" fill="#c9847a"/><circle cx="150" cy="95" r="8" fill="#e0c48a"/>\n<circle cx="190" cy="95" r="10" fill="#3b7bd6"/><circle cx="205" cy="88" r="3" fill="#9aa5b1"/>\n<circle cx="230" cy="95" r="9" fill="#c1552e"/>\n<text x="190" y="130" text-anchor="middle" font-size="9" fill="#22303f">Terre (zone habitable)</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Quelle est la position de la Terre dans le système solaire par rapport au Soleil ?", "choix": ["1re planète", "2e planète", "3e planète", "5e planète"], "reponse": 2, "explication": "La Terre est la troisième planète en partant du Soleil, après Mercure et Vénus."},
        {"id": "q2", "enonce": "Quel type de planète est la Terre ?", "choix": ["Une planète gazeuse", "Une planète rocheuse", "Une étoile", "Un astéroïde"], "reponse": 1, "explication": "La Terre est une planète rocheuse, comme Mercure, Vénus et Mars."},
        {"id": "q3", "enonce": "Qu'est-ce que la « zone habitable » ?", "choix": ["Une zone où il n'y a pas de planètes", "Une distance au Soleil permettant à l'eau d'exister à l'état liquide", "Une zone uniquement sur Mars", "Une zone sans atmosphère"], "reponse": 1, "explication": "La zone habitable est une distance au Soleil ni trop proche ni trop éloignée, permettant à l'eau liquide d'exister."},
        {"id": "q4", "enonce": "Pourquoi l'eau liquide est-elle importante pour la vie ?", "choix": ["Elle n'a aucune importance", "C'est une condition indispensable à la vie telle que nous la connaissons", "Elle empêche la vie d'exister", "Elle sert uniquement à refroidir la planète"], "reponse": 1, "explication": "L'eau liquide est une condition indispensable à la vie telle que nous la connaissons."},
        {"id": "q5", "enonce": "Que fait l'atmosphère terrestre ?", "choix": ["Elle empêche toute lumière de passer", "Elle protège des rayonnements dangereux et maintient une température compatible avec la vie", "Elle n'a aucun rôle", "Elle attire les astéroïdes"], "reponse": 1, "explication": "L'atmosphère protège des rayonnements dangereux et régule la température."},
        {"id": "q6", "enonce": "Que fait le champ magnétique terrestre ?", "choix": ["Il protège la Terre du vent solaire", "Il attire les météorites", "Il réchauffe la planète", "Il n'existe pas"], "reponse": 0, "explication": "Le champ magnétique terrestre protège la planète du vent solaire."},
        {"id": "q7", "enonce": "Quel est le satellite naturel de la Terre ?", "choix": ["Mars", "La Lune", "Vénus", "Le Soleil"], "reponse": 1, "explication": "La Lune est le satellite naturel de la Terre."},
        {"id": "q8", "enonce": "Que stabilise la gravitation de la Lune sur la Terre ?", "choix": ["La couleur du ciel", "L'inclinaison de l'axe terrestre", "La température du Soleil", "Le nombre de continents"], "reponse": 1, "explication": "La gravitation de la Lune stabilise l'inclinaison de l'axe terrestre."},
        {"id": "q9", "enonce": "Quel phénomène la Lune provoque-t-elle sur Terre ?", "choix": ["Les saisons uniquement", "Les marées", "Les éruptions volcaniques", "Les séismes"], "reponse": 1, "explication": "La gravitation de la Lune provoque les marées sur Terre."},
        {"id": "q10", "enonce": "La Terre est-elle actuellement la seule planète connue à abriter la vie ?", "choix": ["Non, Mars aussi", "Oui, à ce jour", "Non, toutes les planètes ont la vie", "On ne sait pas du tout"], "reponse": 1, "explication": "À ce jour, la Terre est la seule planète connue à abriter la vie."},
    ],
}

RISQUES_LOCAUX = {
    "slug": "risques-echelle-locale-5e",
    "titre": "Les risques à l'échelle locale",
    "matiere": "svt", "niveau": "5e", "duree": "20 min",
    "resume": "Identifier les risques naturels à l'échelle locale et les moyens de s'en protéger.",
    "objectifs": ["Distinguer aléa et risque", "Identifier différents risques naturels locaux", "Comprendre les moyens de prévention et de protection"],
    "contenu": [
        "Un aléa est un phénomène naturel potentiellement dangereux, comme une inondation, un séisme, une tempête ou un glissement de terrain. Un risque existe lorsque cet aléa se produit dans une zone où vivent des populations ou se trouvent des biens, comme des habitations ou des infrastructures, susceptibles d'être touchés : sans présence humaine, un aléa reste sans conséquence, il n'y a donc pas de risque.",
        "À l'échelle locale, certains risques sont plus fréquents selon la géographie du territoire : les zones proches d'un cours d'eau sont exposées aux inondations, les régions montagneuses aux glissements de terrain et aux avalanches, les zones côtières aux submersions marines et à l'érosion du littoral. Connaître les risques propres à son territoire permet de mieux s'y préparer.",
        "Pour limiter les conséquences de ces risques, plusieurs moyens de prévention existent : construire des digues ou des bassins de rétention contre les inondations, respecter des normes de construction anti-sismiques dans les zones à risque, ou établir des plans de prévention des risques qui interdisent ou encadrent la construction dans les zones les plus exposées. L'information et l'alerte des populations, par exemple grâce à des systèmes d'alerte précoce, jouent aussi un rôle essentiel.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<path d="M20 150 L80 60 L140 150 Z" fill="#c1552e"/><text x="80" y="170" text-anchor="middle" font-size="9" fill="#22303f">Montagne</text>\n<rect x="180" y="110" width="110" height="40" fill="#3b7bd6"/><text x="235" y="165" text-anchor="middle" font-size="9" fill="#22303f">Inondation</text>\n<polygon points="60,55 70,40 80,55 90,35 100,55" fill="none" stroke="#e08a2a" stroke-width="2"/>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un aléa ?", "choix": ["Une population exposée", "Un phénomène naturel potentiellement dangereux", "Une construction anti-sismique", "Un système d'alerte"], "reponse": 1, "explication": "Un aléa est un phénomène naturel potentiellement dangereux, comme un séisme ou une inondation."},
        {"id": "q2", "enonce": "Quand parle-t-on de risque ?", "choix": ["Dès qu'un aléa existe, même sans présence humaine", "Quand un aléa touche une zone où vivent des populations ou se trouvent des biens", "Uniquement lors d'un séisme", "Jamais, le risque n'existe pas"], "reponse": 1, "explication": "Un risque existe quand un aléa touche une zone habitée ou des biens susceptibles d'être touchés."},
        {"id": "q3", "enonce": "Un aléa sans présence humaine constitue-t-il un risque ?", "choix": ["Oui, toujours", "Non, il reste sans conséquence", "Cela dépend de sa couleur", "Oui, mais seulement la nuit"], "reponse": 1, "explication": "Sans présence humaine ni biens exposés, un aléa reste sans conséquence : il n'y a pas de risque."},
        {"id": "q4", "enonce": "Quelles zones sont particulièrement exposées aux inondations ?", "choix": ["Les zones proches d'un cours d'eau", "Les sommets des montagnes", "Le centre des déserts", "Aucune zone en particulier"], "reponse": 0, "explication": "Les zones proches d'un cours d'eau sont particulièrement exposées au risque d'inondation."},
        {"id": "q5", "enonce": "Quel risque est fréquent dans les régions montagneuses ?", "choix": ["La submersion marine", "Les glissements de terrain et avalanches", "La sécheresse uniquement", "Aucun risque"], "reponse": 1, "explication": "Les régions montagneuses sont exposées aux glissements de terrain et aux avalanches."},
        {"id": "q6", "enonce": "Quel risque concerne particulièrement les zones côtières ?", "choix": ["Les avalanches", "La submersion marine et l'érosion du littoral", "Les glissements de terrain uniquement", "Aucun risque particulier"], "reponse": 1, "explication": "Les zones côtières sont exposées à la submersion marine et à l'érosion du littoral."},
        {"id": "q7", "enonce": "Quel ouvrage permet de se protéger des inondations ?", "choix": ["Une digue", "Un pont uniquement décoratif", "Une tour", "Rien ne peut protéger des inondations"], "reponse": 0, "explication": "Les digues et bassins de rétention permettent de limiter les conséquences des inondations."},
        {"id": "q8", "enonce": "Que permettent les normes de construction anti-sismiques ?", "choix": ["D'empêcher totalement les séismes", "De limiter les dégâts causés par un séisme sur les bâtiments", "De prévoir la date exacte d'un séisme", "Rien du tout"], "reponse": 1, "explication": "Les normes anti-sismiques limitent les dégâts sur les bâtiments en cas de séisme, sans empêcher le séisme lui-même."},
        {"id": "q9", "enonce": "Qu'est-ce qu'un plan de prévention des risques ?", "choix": ["Un document qui encadre ou interdit la construction dans les zones exposées", "Un plan de vacances", "Une carte touristique", "Un règlement sportif"], "reponse": 0, "explication": "Un plan de prévention des risques encadre ou interdit la construction dans les zones les plus exposées."},
        {"id": "q10", "enonce": "Pourquoi les systèmes d'alerte précoce sont-ils importants ?", "choix": ["Ils empêchent les catastrophes", "Ils permettent d'informer et d'alerter les populations pour limiter les conséquences", "Ils ne servent à rien", "Ils remplacent les digues"], "reponse": 1, "explication": "Les systèmes d'alerte précoce permettent d'informer les populations pour qu'elles se protègent à temps."},
    ],
}

NERVEUX_CARDIO = {
    "slug": "systeme-nerveux-cardio-respiratoire-5e",
    "titre": "Les systèmes nerveux, cardio-respiratoire et l'effort musculaire",
    "matiere": "svt", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre comment le système nerveux et le système cardio-respiratoire permettent l'effort musculaire.",
    "objectifs": ["Comprendre le rôle du système nerveux dans le mouvement", "Comprendre comment le système cardio-respiratoire répond à l'effort", "Identifier les besoins des muscles pendant un effort"],
    "contenu": [
        "Le mouvement volontaire est commandé par le système nerveux : le cerveau élabore une commande motrice qui est transmise par les nerfs jusqu'aux muscles concernés, provoquant leur contraction. Ce trajet, du cerveau au muscle, est très rapide, ce qui permet des réactions quasi instantanées, comme retirer sa main d'une surface brûlante.",
        "Pendant un effort physique, les muscles ont besoin de davantage de dioxygène et de nutriments pour produire l'énergie nécessaire à leur contraction. Le système cardio-respiratoire s'adapte alors : la fréquence cardiaque et la fréquence respiratoire augmentent, ce qui permet d'apporter plus rapidement le sang oxygéné aux muscles qui travaillent.",
        "Cette adaptation est mesurable et progressive : plus l'effort est intense, plus la fréquence cardiaque et respiratoire augmentent, jusqu'à un certain maximum. Après l'effort, ces fréquences reviennent progressivement à leur valeur de repos ; plus une personne est entraînée physiquement, plus ce retour au calme est rapide, ce qui traduit une meilleure efficacité du système cardio-respiratoire.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="80" cy="60" r="22" fill="#e7c07a"/>\n<path d="M80 82 L80 150" stroke="#22303f" stroke-width="4"/>\n<path d="M80 100 L50 130 M80 100 L110 130" stroke="#22303f" stroke-width="4"/>\n<path d="M100 65 Q150 65 150 100 Q150 130 200 130" fill="none" stroke="#c1552e" stroke-width="2"/>\n<path d="M230 90 L245 60 L255 100 L265 50 L280 90" fill="none" stroke="#c1552e" stroke-width="2"/>\n<text x="255" y="140" text-anchor="middle" font-size="9" fill="#22303f">Fréquence cardiaque ↑ à l\'effort</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Quel organe commande le mouvement volontaire ?", "choix": ["Le cœur", "Le cerveau", "L'estomac", "Le foie"], "reponse": 1, "explication": "Le cerveau élabore la commande motrice à l'origine du mouvement volontaire."},
        {"id": "q2", "enonce": "Comment la commande motrice du cerveau atteint-elle les muscles ?", "choix": ["Par le sang uniquement", "Par les nerfs", "Par la respiration", "Elle n'atteint jamais les muscles"], "reponse": 1, "explication": "La commande motrice est transmise par les nerfs jusqu'aux muscles."},
        {"id": "q3", "enonce": "Pourquoi le trajet cerveau-muscle est-il très rapide ?", "choix": ["Pour permettre des réactions quasi instantanées", "Cela n'a aucune utilité particulière", "Pour ralentir le mouvement", "Ce n'est pas rapide du tout"], "reponse": 0, "explication": "La rapidité du trajet nerveux permet des réactions quasi instantanées, comme retirer sa main d'une surface brûlante."},
        {"id": "q4", "enonce": "De quoi les muscles ont-ils davantage besoin pendant un effort ?", "choix": ["De dioxygène et de nutriments", "De rien de plus qu'au repos", "Uniquement d'eau", "De moins d'énergie"], "reponse": 0, "explication": "Pendant un effort, les muscles ont besoin de plus de dioxygène et de nutriments pour produire de l'énergie."},
        {"id": "q5", "enonce": "Que fait la fréquence cardiaque pendant un effort ?", "choix": ["Elle diminue", "Elle augmente", "Elle reste identique", "Elle s'arrête"], "reponse": 1, "explication": "La fréquence cardiaque augmente pendant l'effort pour apporter plus de sang oxygéné aux muscles."},
        {"id": "q6", "enonce": "Que fait la fréquence respiratoire pendant un effort ?", "choix": ["Elle diminue", "Elle augmente aussi", "Elle reste identique", "Elle disparaît"], "reponse": 1, "explication": "La fréquence respiratoire augmente également pendant l'effort, pour apporter plus de dioxygène."},
        {"id": "q7", "enonce": "Pourquoi le cœur bat-il plus vite à l'effort ?", "choix": ["Pour apporter plus rapidement le sang oxygéné aux muscles", "Pour ralentir le corps", "Sans raison particulière", "Pour refroidir le corps"], "reponse": 0, "explication": "Le cœur accélère pour apporter plus rapidement le sang oxygéné aux muscles qui travaillent."},
        {"id": "q8", "enonce": "Que se passe-t-il pour les fréquences cardiaque et respiratoire après l'effort ?", "choix": ["Elles restent élevées pour toujours", "Elles reviennent progressivement à leur valeur de repos", "Elles s'arrêtent immédiatement", "Elles augmentent encore plus"], "reponse": 1, "explication": "Après l'effort, les fréquences reviennent progressivement à leur valeur de repos."},
        {"id": "q9", "enonce": "Chez une personne entraînée, le retour au calme après l'effort est...", "choix": ["Plus lent que chez une personne non entraînée", "Plus rapide, signe d'une meilleure efficacité cardio-respiratoire", "Identique dans tous les cas", "Impossible à observer"], "reponse": 1, "explication": "Une meilleure condition physique se traduit par un retour au calme plus rapide après l'effort."},
        {"id": "q10", "enonce": "Quel système du corps est particulièrement sollicité pendant un effort musculaire ?", "choix": ["Le système digestif uniquement", "Le système cardio-respiratoire", "Le système auditif", "Aucun système particulier"], "reponse": 1, "explication": "Le système cardio-respiratoire s'adapte fortement à l'effort musculaire pour répondre aux besoins des muscles."},
    ],
}

ALIMENTS_DIGESTIF = {
    "slug": "aliments-systeme-digestif-5e",
    "titre": "Les aliments et le système digestif",
    "matiere": "svt", "niveau": "5e", "duree": "20 min",
    "resume": "Comprendre le trajet des aliments dans le système digestif et le rôle de la digestion.",
    "objectifs": ["Décrire le trajet des aliments dans le tube digestif", "Comprendre le rôle de la digestion", "Comprendre comment les nutriments passent dans le sang"],
    "contenu": [
        "Les aliments que nous consommons ne peuvent pas être utilisés directement par notre corps : ils doivent d'abord être transformés en nutriments, des substances suffisamment petites pour traverser la paroi de l'intestin et passer dans le sang. Ce processus de transformation s'appelle la digestion, et se déroule tout au long du tube digestif : bouche, œsophage, estomac, intestin grêle et gros intestin.",
        "La digestion commence dans la bouche, où les aliments sont découpés et broyés par la mastication et mélangés à la salive, qui commence déjà à transformer certains sucres. Dans l'estomac, les aliments sont brassés et mélangés à des sucs digestifs acides qui poursuivent leur transformation. C'est surtout dans l'intestin grêle que se termine la digestion, grâce à d'autres sucs digestifs produits par le pancréas et le foie.",
        "Les nutriments issus de la digestion traversent la fine paroi de l'intestin grêle, richement irriguée par des vaisseaux sanguins, pour passer dans le sang : c'est l'absorption intestinale. Le sang transporte ensuite ces nutriments jusqu'à toutes les cellules du corps, qui les utilisent pour produire de l'énergie ou pour se construire. Les résidus non digérés poursuivent leur chemin jusqu'au gros intestin, puis sont évacués.",
    ],
    "illustration": '<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n<circle cx="60" cy="30" r="14" fill="#e7c07a"/>\n<path d="M60 44 L60 70" stroke="#22303f" stroke-width="3"/>\n<ellipse cx="90" cy="95" rx="30" ry="22" fill="#c1552e"/>\n<path d="M120 100 Q200 100 200 140 Q200 170 260 170 Q290 170 290 140" fill="none" stroke="#e08a2a" stroke-width="6" stroke-linecap="round"/>\n<text x="180" y="30" text-anchor="middle" font-size="10" fill="#22303f">Bouche → estomac → intestin</text>\n</svg>',
    "quiz": [
        {"id": "q1", "enonce": "Pourquoi les aliments doivent-ils être transformés en nutriments ?", "choix": ["Pour qu'ils soient plus jolis", "Pour qu'ils soient assez petits pour passer dans le sang", "Ce n'est pas nécessaire", "Pour qu'ils changent de couleur"], "reponse": 1, "explication": "Les aliments doivent être transformés en nutriments, assez petits pour traverser la paroi intestinale et passer dans le sang."},
        {"id": "q2", "enonce": "Comment appelle-t-on le processus de transformation des aliments ?", "choix": ["La respiration", "La digestion", "La circulation", "La transpiration"], "reponse": 1, "explication": "Ce processus de transformation des aliments s'appelle la digestion."},
        {"id": "q3", "enonce": "Où commence la digestion ?", "choix": ["Dans l'estomac", "Dans la bouche", "Dans l'intestin grêle", "Dans le gros intestin"], "reponse": 1, "explication": "La digestion commence dans la bouche, avec la mastication et la salive."},
        {"id": "q4", "enonce": "Que fait la mastication ?", "choix": ["Elle découpe et broie les aliments", "Elle les colore", "Elle les refroidit", "Elle ne sert à rien"], "reponse": 0, "explication": "La mastication découpe et broie les aliments dans la bouche."},
        {"id": "q5", "enonce": "Que se passe-t-il dans l'estomac ?", "choix": ["Les aliments sont brassés et mélangés à des sucs digestifs acides", "Rien, l'estomac ne fait que stocker", "Les aliments deviennent des nutriments directement", "Les aliments sont évacués"], "reponse": 0, "explication": "Dans l'estomac, les aliments sont brassés et mélangés à des sucs digestifs acides."},
        {"id": "q6", "enonce": "Où se termine principalement la digestion ?", "choix": ["Dans la bouche", "Dans l'œsophage", "Dans l'intestin grêle", "Dans le gros intestin"], "reponse": 2, "explication": "C'est surtout dans l'intestin grêle que se termine la digestion, grâce aux sucs du pancréas et du foie."},
        {"id": "q7", "enonce": "Comment appelle-t-on le passage des nutriments dans le sang ?", "choix": ["La mastication", "L'absorption intestinale", "La respiration", "La transpiration"], "reponse": 1, "explication": "L'absorption intestinale est le passage des nutriments à travers la paroi de l'intestin grêle vers le sang."},
        {"id": "q8", "enonce": "Pourquoi la paroi de l'intestin grêle est-elle richement irriguée par des vaisseaux sanguins ?", "choix": ["Pour faciliter le passage des nutriments dans le sang", "Pour la rendre plus solide", "Cela n'a aucune utilité", "Pour la refroidir"], "reponse": 0, "explication": "Cette irrigation facilite l'absorption des nutriments directement dans le sang."},
        {"id": "q9", "enonce": "Que transporte le sang après l'absorption intestinale ?", "choix": ["Les nutriments vers toutes les cellules du corps", "Uniquement de l'eau", "Rien de particulier", "Les aliments non digérés"], "reponse": 0, "explication": "Le sang transporte les nutriments absorbés jusqu'à toutes les cellules du corps."},
        {"id": "q10", "enonce": "Que deviennent les résidus non digérés ?", "choix": ["Ils restent dans l'estomac", "Ils poursuivent leur chemin jusqu'au gros intestin, puis sont évacués", "Ils passent directement dans le sang", "Ils disparaissent immédiatement"], "reponse": 1, "explication": "Les résidus non digérés poursuivent leur chemin jusqu'au gros intestin avant d'être évacués."},
    ],
}

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "ressources-naturelles-terre-5e", [TERRE_SOLAIRE, RISQUES_LOCAUX, NERVEUX_CARDIO, ALIMENTS_DIGESTIF])

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print("4 leçons SVT 5e ajoutées.")
