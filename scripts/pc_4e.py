# -*- coding: utf-8 -*-
PATH = "src/content/lessons.ts"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def lesson_block(d):
    obj = ", ".join('"' + esc(o) + '"' for o in d["objectifs"])
    cont = ", ".join('"' + esc(c) + '"' for c in d["contenu"])
    illus = ""
    if d.get("illustration"):
        illus = f'\n    illustration: `{d["illustration"]}`,'
    q_items = []
    for q in d["quiz"]:
        choix = ", ".join('"' + esc(c) + '"' for c in q["choix"])
        expl = esc(q["explication"])
        enonce = esc(q["enonce"])
        q_items.append(
            f'      {{\n        id: "{q["id"]}",\n        enonce: "{enonce}",\n'
            f'        choix: [{choix}],\n        reponse: {q["reponse"]},\n'
            f'        explication: "{expl}",\n      }}'
        )
    quiz_block = (
        f'quiz: {{\n    slug: "quiz-{d["slug"]}",\n    titre: "Quiz — {esc(d["titre"])}",\n'
        f'    questions: [\n' + ",\n".join(q_items) + "\n    ],\n  },"
    )
    return (
        f'  {{\n    slug: "{d["slug"]}",\n    titre: "{esc(d["titre"])}",\n'
        f'    matiere: "{d["matiere"]}",\n    niveau: "{d["niveau"]}",\n'
        f'    duree: "{d["duree"]}",\n    resume: "{esc(d["resume"])}",\n'
        f'    objectifs: [{obj}],\n    contenu: [{cont}],{illus}\n    {quiz_block}\n  }},'
    )

def insert_before(txt, anchor_slug, new_dicts):
    idx = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    insertion = "\n".join(lesson_block(d) for d in new_dicts) + "\n"
    return txt[:idx] + insertion + txt[idx:]

L = []

L.append({
    "slug": "ions-charge-electrique-4e", "titre": "Les ions et la charge électrique",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre ce qu'est un ion et comment il se forme à partir d'un atome.",
    "objectifs": ["Définir ce qu'est un ion", "Distinguer cation et anion", "Connaître quelques ions courants"],
    "contenu": [
        "Un atome est électriquement neutre : il possède autant d'électrons (charge négative) que de protons (charge positive) dans son noyau. Un ion est une espèce chimique qui s'est formée à partir d'un atome (ou d'un groupe d'atomes) ayant gagné ou perdu un ou plusieurs électrons, ce qui lui donne une charge électrique globale non nulle.",
        "Lorsqu'un atome perd un ou plusieurs électrons, il devient un ion chargé positivement, appelé cation (par exemple, l'ion sodium Na+ ou l'ion cuivre Cu2+). Lorsqu'un atome gagne un ou plusieurs électrons, il devient un ion chargé négativement, appelé anion (par exemple, l'ion chlorure Cl- ou l'ion sulfate SO4 2-).",
        "Les ions sont présents dans nos gestes quotidiens : l'eau du robinet contient de nombreux ions dissous (calcium, chlorure, sulfate...), le sel de cuisine est constitué d'ions sodium et d'ions chlorure, et les ions jouent un rôle essentiel dans le fonctionnement du corps humain, notamment dans la transmission des messages nerveux.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"90\" cy=\"90\" r=\"30\" fill=\"#3b7bd6\"/><text x=\"90\" y=\"96\" text-anchor=\"middle\" font-size=\"14\" fill=\"#fff\">Na+</text><text x=\"90\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Cation (perte d electron)</text><circle cx=\"230\" cy=\"90\" r=\"30\" fill=\"#c1552e\"/><text x=\"230\" y=\"96\" text-anchor=\"middle\" font-size=\"14\" fill=\"#fff\">Cl-</text><text x=\"230\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Anion (gain d electron)</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un atome électriquement neutre ?", "choix": ["Un atome ayant autant d'électrons que de protons", "Un atome sans électrons", "Un atome sans protons", "Un atome radioactif"], "reponse": 0, "explication": "Un atome neutre possède autant d'électrons (charge négative) que de protons (charge positive)."},
        {"id": "q2", "enonce": "Qu'est-ce qu'un ion ?", "choix": ["Une espèce chimique ayant gagné ou perdu des électrons", "Un atome toujours neutre", "Un type de molécule d'eau", "Un noyau atomique isolé"], "reponse": 0, "explication": "Un ion est une espèce chimique chargée, formée par gain ou perte d'électrons."},
        {"id": "q3", "enonce": "Comment appelle-t-on un ion chargé positivement ?", "choix": ["Un anion", "Un cation", "Un neutron", "Un isotope"], "reponse": 1, "explication": "Un ion chargé positivement, formé par perte d'électrons, est appelé cation."},
        {"id": "q4", "enonce": "Comment appelle-t-on un ion chargé négativement ?", "choix": ["Un cation", "Un anion", "Un proton", "Un atome neutre"], "reponse": 1, "explication": "Un ion chargé négativement, formé par gain d'électrons, est appelé anion."},
        {"id": "q5", "enonce": "Comment se forme un cation ?", "choix": ["Par perte d'un ou plusieurs électrons", "Par gain d'un ou plusieurs électrons", "Par fusion de deux atomes", "Par perte de protons"], "reponse": 0, "explication": "Un cation se forme lorsqu'un atome perd un ou plusieurs électrons."},
        {"id": "q6", "enonce": "L'ion sodium Na+ est-il un cation ou un anion ?", "choix": ["Un cation", "Un anion", "Ni l'un ni l'autre", "Un atome neutre"], "reponse": 0, "explication": "L'ion sodium Na+ est chargé positivement, c'est donc un cation."},
        {"id": "q7", "enonce": "L'ion chlorure Cl- est-il un cation ou un anion ?", "choix": ["Un cation", "Un anion", "Ni l'un ni l'autre", "Un atome neutre"], "reponse": 1, "explication": "L'ion chlorure Cl- est chargé négativement, c'est donc un anion."},
        {"id": "q8", "enonce": "De quels ions est constitué le sel de cuisine ?", "choix": ["Ions sodium et ions chlorure", "Ions calcium et ions sulfate", "Ions cuivre uniquement", "Aucun ion"], "reponse": 0, "explication": "Le sel de cuisine est constitué d'ions sodium (Na+) et d'ions chlorure (Cl-)."},
        {"id": "q9", "enonce": "L'eau du robinet contient-elle des ions dissous ?", "choix": ["Non, jamais", "Oui, comme le calcium, le chlorure ou le sulfate", "Uniquement des atomes neutres", "Uniquement de l'oxygène"], "reponse": 1, "explication": "L'eau du robinet contient de nombreux ions dissous comme le calcium, le chlorure ou le sulfate."},
        {"id": "q10", "enonce": "Les ions jouent-ils un rôle dans le corps humain ?", "choix": ["Non, aucun rôle", "Oui, notamment dans la transmission des messages nerveux", "Uniquement dans la digestion", "Uniquement dans la respiration"], "reponse": 1, "explication": "Les ions jouent un rôle essentiel, notamment dans la transmission des messages nerveux."},
    ],
})

L.append({
    "slug": "conductivite-solutions-ioniques-4e", "titre": "La conductivité électrique des solutions ioniques",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre pourquoi certaines solutions conduisent le courant électrique grâce aux ions qu'elles contiennent.",
    "objectifs": ["Comprendre le rôle des ions dans la conduction du courant", "Distinguer une solution conductrice d'une solution non conductrice", "Connaître le principe du test de conductivité"],
    "contenu": [
        "L'eau pure ne conduit pratiquement pas le courant électrique, car elle contient très peu d'ions. En revanche, une solution contenant des ions dissous, comme l'eau salée, conduit le courant électrique : ce sont les ions, chargés électriquement et mobiles dans la solution, qui assurent le déplacement des charges et donc le passage du courant.",
        "Pour tester la conductivité d'une solution, on utilise un conductimètre ou un circuit électrique simple comportant une lampe ou un ampèremètre : plus la solution contient d'ions, plus elle conduit facilement le courant, et plus l'intensité mesurée est élevée. Une solution sans ions, comme l'eau distillée pure, n'allume pas la lampe du circuit test.",
        "Cette propriété a de nombreuses applications : elle permet par exemple de mesurer la salinité de l'eau de mer, de contrôler la qualité de l'eau potable, ou d'expliquer pourquoi il est dangereux d'utiliser un appareil électrique près de l'eau, celle-ci contenant souvent des ions dissous qui la rendent conductrice.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"40\" y=\"70\" width=\"100\" height=\"70\" fill=\"#a9d6f5\" stroke=\"#22303f\"/><circle cx=\"70\" cy=\"100\" r=\"4\" fill=\"#3b7bd6\"/><circle cx=\"100\" cy=\"110\" r=\"4\" fill=\"#c1552e\"/><circle cx=\"120\" cy=\"90\" r=\"4\" fill=\"#3b7bd6\"/><path d=\"M140 105 L220 105\" stroke=\"#22303f\" stroke-width=\"2\"/><circle cx=\"245\" cy=\"105\" r=\"20\" fill=\"#e08a2a\"/><text x=\"245\" y=\"111\" text-anchor=\"middle\" font-size=\"10\" fill=\"#fff\">ON</text><text x=\"160\" y=\"170\" text-anchor=\"middle\" font-size=\"10\" fill=\"#22303f\">Solution ionique : la lampe s allume</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "L'eau pure conduit-elle bien le courant électrique ?", "choix": ["Oui, très bien", "Non, elle conduit très peu le courant", "Elle ne conduit jamais rien", "Cela dépend de sa couleur"], "reponse": 1, "explication": "L'eau pure conduit très peu le courant car elle contient très peu d'ions."},
        {"id": "q2", "enonce": "Qu'est-ce qui permet à une solution de conduire le courant électrique ?", "choix": ["Les ions dissous", "La couleur de la solution", "La température uniquement", "Le volume de la solution"], "reponse": 0, "explication": "Ce sont les ions dissous, chargés et mobiles, qui assurent le passage du courant électrique."},
        {"id": "q3", "enonce": "L'eau salée conduit-elle le courant électrique ?", "choix": ["Non, jamais", "Oui, car elle contient des ions sodium et chlorure dissous", "Uniquement si elle est chaude", "Uniquement si elle est glacée"], "reponse": 1, "explication": "L'eau salée conduit le courant grâce aux ions sodium et chlorure qu'elle contient."},
        {"id": "q4", "enonce": "Que se passe-t-il si on teste l'eau distillée pure dans un circuit avec une lampe ?", "choix": ["La lampe s'allume fortement", "La lampe ne s'allume pas", "Le circuit explose", "La lampe clignote"], "reponse": 1, "explication": "L'eau distillée pure ne contenant quasiment pas d'ions, la lampe ne s'allume pas."},
        {"id": "q5", "enonce": "Plus une solution contient d'ions, que se passe-t-il pour sa conductivité ?", "choix": ["Elle diminue", "Elle augmente", "Elle reste identique", "Elle devient nulle"], "reponse": 1, "explication": "Plus une solution contient d'ions, plus elle conduit facilement le courant électrique."},
        {"id": "q6", "enonce": "Quel appareil permet de mesurer la conductivité d'une solution ?", "choix": ["Un conductimètre", "Un thermomètre", "Une balance", "Un microscope"], "reponse": 0, "explication": "Un conductimètre permet de mesurer la conductivité électrique d'une solution."},
        {"id": "q7", "enonce": "Pourquoi est-il dangereux d'utiliser un appareil électrique près de l'eau ?", "choix": ["Ce n'est pas dangereux", "Car l'eau contient souvent des ions qui la rendent conductrice", "Car l'eau est toujours froide", "Car l'eau est transparente"], "reponse": 1, "explication": "L'eau contient souvent des ions dissous qui la rendent conductrice, ce qui présente un risque électrique."},
        {"id": "q8", "enonce": "À quoi sert la mesure de conductivité de l'eau de mer ?", "choix": ["À rien de particulier", "À mesurer sa salinité", "À mesurer sa température uniquement", "À mesurer sa couleur"], "reponse": 1, "explication": "La conductivité permet de mesurer la salinité de l'eau de mer, liée à sa teneur en ions."},
        {"id": "q9", "enonce": "La conductivité électrique permet-elle de contrôler la qualité de l'eau potable ?", "choix": ["Non, jamais", "Oui, c'est l'une de ses applications", "Uniquement pour l'eau de mer", "Uniquement pour l'eau glacée"], "reponse": 1, "explication": "La mesure de conductivité permet notamment de contrôler la qualité de l'eau potable."},
        {"id": "q10", "enonce": "Une solution sans ions dissous peut-elle conduire le courant ?", "choix": ["Oui, très bien", "Non, ou très mal", "Cela dépend de sa couleur", "Toujours parfaitement"], "reponse": 1, "explication": "Sans ions dissous, une solution conduit très mal, voire pas du tout, le courant électrique."},
    ],
})

L.append({
    "slug": "tests-identification-ions-4e", "titre": "Les tests d'identification des ions",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Connaître les tests chimiques permettant d'identifier certains ions en solution.",
    "objectifs": ["Connaître le test de reconnaissance de l'ion chlorure", "Connaître le test de reconnaissance de l'ion cuivre", "Comprendre le principe d'un test caractéristique"],
    "contenu": [
        "Un test caractéristique est une réaction chimique qui permet d'identifier la présence d'un ion précis dans une solution, en observant un changement visible : apparition d'un précipité (solide qui se forme dans la solution) ou changement de couleur. Chaque ion possède son propre réactif caractéristique.",
        "Pour identifier l'ion chlorure (Cl-), on ajoute quelques gouttes de nitrate d'argent : en présence d'ions chlorure, un précipité blanc de chlorure d'argent se forme immédiatement, qui noircit ensuite à la lumière. Pour identifier l'ion cuivre (Cu2+), on ajoute quelques gouttes de solution d'hydroxyde de sodium (soude) : un précipité bleu caractéristique se forme.",
        "D'autres ions ont leurs propres tests : l'ion fer II donne un précipité vert avec la soude, l'ion fer III donne un précipité rouille, et l'ion sulfate donne un précipité blanc avec le chlorure de baryum. Ces tests sont largement utilisés en laboratoire et en analyse de l'eau pour identifier rapidement la composition chimique d'une solution.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"50\" y=\"60\" width=\"50\" height=\"90\" fill=\"#e8f0f8\" stroke=\"#22303f\"/><circle cx=\"75\" cy=\"130\" r=\"8\" fill=\"#f5f2e8\"/><text x=\"75\" y=\"170\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Cl- + precipite blanc</text><rect x=\"200\" y=\"60\" width=\"50\" height=\"90\" fill=\"#e8f0f8\" stroke=\"#22303f\"/><circle cx=\"225\" cy=\"130\" r=\"8\" fill=\"#3b7bd6\"/><text x=\"225\" y=\"170\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Cu2+ + precipite bleu</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un test caractéristique ?", "choix": ["Une réaction chimique permettant d'identifier un ion précis", "Un test de couleur sans lien avec la chimie", "Un test de température", "Un test de masse"], "reponse": 0, "explication": "Un test caractéristique permet d'identifier un ion précis grâce à un changement observable."},
        {"id": "q2", "enonce": "Quel réactif permet d'identifier l'ion chlorure ?", "choix": ["Le nitrate d'argent", "L'hydroxyde de sodium", "Le chlorure de baryum", "L'eau pure"], "reponse": 0, "explication": "Le nitrate d'argent permet d'identifier l'ion chlorure par formation d'un précipité blanc."},
        {"id": "q3", "enonce": "Quelle couleur a le précipité obtenu avec l'ion chlorure et le nitrate d'argent ?", "choix": ["Bleu", "Blanc", "Rouille", "Vert"], "reponse": 1, "explication": "Le test à l'ion chlorure avec le nitrate d'argent donne un précipité blanc, qui noircit à la lumière."},
        {"id": "q4", "enonce": "Quel réactif permet d'identifier l'ion cuivre ?", "choix": ["Le nitrate d'argent", "L'hydroxyde de sodium (soude)", "Le chlorure de baryum", "L'acide chlorhydrique"], "reponse": 1, "explication": "L'hydroxyde de sodium (soude) permet d'identifier l'ion cuivre par formation d'un précipité bleu."},
        {"id": "q5", "enonce": "Quelle couleur a le précipité obtenu avec l'ion cuivre et la soude ?", "choix": ["Bleu", "Blanc", "Rouille", "Jaune"], "reponse": 0, "explication": "Le test à l'ion cuivre avec la soude donne un précipité bleu caractéristique."},
        {"id": "q6", "enonce": "Quelle couleur donne l'ion fer III avec la soude ?", "choix": ["Bleu", "Rouille", "Blanc", "Vert"], "reponse": 1, "explication": "L'ion fer III donne un précipité de couleur rouille avec la soude."},
        {"id": "q7", "enonce": "Quelle couleur donne l'ion fer II avec la soude ?", "choix": ["Vert", "Bleu", "Rouille", "Blanc"], "reponse": 0, "explication": "L'ion fer II donne un précipité vert avec la soude."},
        {"id": "q8", "enonce": "Quel réactif permet d'identifier l'ion sulfate ?", "choix": ["Le chlorure de baryum", "Le nitrate d'argent", "La soude", "L'eau distillée"], "reponse": 0, "explication": "Le chlorure de baryum permet d'identifier l'ion sulfate par formation d'un précipité blanc."},
        {"id": "q9", "enonce": "À quoi servent ces tests d'identification dans la vie réelle ?", "choix": ["À rien de particulier", "À l'analyse de l'eau et en laboratoire", "Uniquement à la décoration", "Uniquement à la cuisine"], "reponse": 1, "explication": "Ces tests sont largement utilisés en laboratoire et en analyse de l'eau."},
        {"id": "q10", "enonce": "Comment observe-t-on généralement le résultat d'un test caractéristique ?", "choix": ["Par l'apparition d'un précipité ou un changement de couleur", "Par un changement de température uniquement", "Par un bruit particulier", "Par une odeur uniquement"], "reponse": 0, "explication": "Un test caractéristique se manifeste par l'apparition d'un précipité ou un changement de couleur visible."},
    ],
})

L.append({
    "slug": "vitesse-mouvement-4e", "titre": "La vitesse d'un mouvement",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre la notion de vitesse et savoir la calculer à partir d'une distance et d'une durée.",
    "objectifs": ["Définir la vitesse moyenne d'un mouvement", "Savoir calculer une vitesse à partir d'une distance et d'une durée", "Connaître les unités de vitesse usuelles"],
    "contenu": [
        "Le mouvement d'un objet est toujours décrit par rapport à un référentiel, c'est-à-dire un objet ou un point fixe choisi comme référence. La vitesse moyenne d'un objet en mouvement caractérise la rapidité de son déplacement : elle se calcule en divisant la distance parcourue par la durée du parcours, selon la formule v = d / t.",
        "L'unité légale de vitesse dans le système international est le mètre par seconde (m/s), mais dans la vie courante, on utilise très souvent le kilomètre par heure (km/h), notamment pour les déplacements routiers. Pour convertir une vitesse de m/s en km/h, on multiplie par 3,6 ; pour convertir de km/h en m/s, on divise par 3,6.",
        "Un mouvement est dit uniforme lorsque la vitesse reste constante au cours du temps ; il est dit varié lorsque la vitesse change, en accélérant ou en ralentissant. La vitesse instantanée, indiquée par exemple par le compteur d'une voiture, peut différer de la vitesse moyenne calculée sur l'ensemble du trajet, notamment à cause des arrêts et changements d'allure.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><path d=\"M30 140 L280 140\" stroke=\"#22303f\" stroke-width=\"2\"/><circle cx=\"60\" cy=\"140\" r=\"8\" fill=\"#3b7bd6\"/><circle cx=\"220\" cy=\"140\" r=\"8\" fill=\"#c1552e\"/><path d=\"M60 120 L220 120\" stroke=\"#e08a2a\" stroke-width=\"2\" marker-end=\"url(#arrow)\"/><text x=\"140\" y=\"110\" text-anchor=\"middle\" font-size=\"10\" fill=\"#22303f\">distance d</text><text x=\"140\" y=\"170\" text-anchor=\"middle\" font-size=\"12\" fill=\"#22303f\">v = d / t</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Par rapport à quoi décrit-on le mouvement d'un objet ?", "choix": ["Un référentiel", "Sa couleur", "Sa masse", "Sa température"], "reponse": 0, "explication": "Le mouvement d'un objet se décrit toujours par rapport à un référentiel, un point fixe choisi comme référence."},
        {"id": "q2", "enonce": "Quelle est la formule de la vitesse moyenne ?", "choix": ["v = d / t", "v = d x t", "v = t / d", "v = d + t"], "reponse": 0, "explication": "La vitesse moyenne se calcule en divisant la distance parcourue par la durée du parcours (v = d / t)."},
        {"id": "q3", "enonce": "Quelle est l'unité légale de vitesse dans le système international ?", "choix": ["Le kilomètre par heure", "Le mètre par seconde", "Le mètre par heure", "Le kilomètre par seconde"], "reponse": 1, "explication": "L'unité légale de vitesse est le mètre par seconde (m/s)."},
        {"id": "q4", "enonce": "Quelle unité de vitesse utilise-t-on couramment pour les déplacements routiers ?", "choix": ["Le mètre par seconde", "Le kilomètre par heure", "Le centimètre par minute", "Le mètre par minute"], "reponse": 1, "explication": "Le kilomètre par heure (km/h) est couramment utilisé pour les déplacements routiers."},
        {"id": "q5", "enonce": "Par quel nombre multiplie-t-on une vitesse en m/s pour l'obtenir en km/h ?", "choix": ["3,6", "10", "100", "1000"], "reponse": 0, "explication": "On multiplie par 3,6 pour convertir une vitesse de m/s en km/h."},
        {"id": "q6", "enonce": "Par quel nombre divise-t-on une vitesse en km/h pour l'obtenir en m/s ?", "choix": ["3,6", "10", "60", "1000"], "reponse": 0, "explication": "On divise par 3,6 pour convertir une vitesse de km/h en m/s."},
        {"id": "q7", "enonce": "Qu'est-ce qu'un mouvement uniforme ?", "choix": ["Un mouvement où la vitesse reste constante", "Un mouvement où la vitesse change tout le temps", "Un mouvement sans vitesse", "Un mouvement uniquement circulaire"], "reponse": 0, "explication": "Un mouvement est uniforme lorsque la vitesse reste constante au cours du temps."},
        {"id": "q8", "enonce": "Qu'est-ce qu'un mouvement varié ?", "choix": ["Un mouvement où la vitesse change, en accélérant ou en ralentissant", "Un mouvement toujours à vitesse constante", "Un mouvement immobile", "Un mouvement sans référentiel"], "reponse": 0, "explication": "Un mouvement varié se caractérise par un changement de vitesse, accélération ou ralentissement."},
        {"id": "q9", "enonce": "Que peut indiquer le compteur d'une voiture ?", "choix": ["La vitesse instantanée", "Uniquement la distance totale", "Uniquement la couleur de la route", "Rien de particulier"], "reponse": 0, "explication": "Le compteur d'une voiture indique généralement la vitesse instantanée."},
        {"id": "q10", "enonce": "La vitesse moyenne d'un trajet peut-elle différer de la vitesse instantanée ?", "choix": ["Non, elles sont toujours identiques", "Oui, notamment à cause des arrêts et changements d'allure", "Cela n'a aucun sens", "Uniquement en cas de panne"], "reponse": 1, "explication": "La vitesse moyenne peut différer de la vitesse instantanée à cause des arrêts et variations d'allure."},
    ],
})

L.append({
    "slug": "actions-mecaniques-effets-4e", "titre": "Les actions mécaniques et leurs effets",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre ce qu'est une force et modéliser ses effets sur un objet.",
    "objectifs": ["Identifier différents types d'actions mécaniques", "Comprendre les effets possibles d'une force sur un objet", "Savoir modéliser une force par un vecteur"],
    "contenu": [
        "Une action mécanique est une action exercée par un objet ou un phénomène sur un autre objet, capable de modifier son mouvement ou sa forme. On distingue les actions de contact, comme pousser ou tirer un objet directement, des actions à distance, comme l'attraction gravitationnelle ou l'attraction magnétique, qui s'exercent sans contact physique.",
        "Les effets d'une action mécanique, appelée aussi force, peuvent être variés : mettre un objet immobile en mouvement, modifier la vitesse ou la direction d'un objet déjà en mouvement, ou déformer un objet (comme comprimer un ressort). Une force peut aussi maintenir un objet immobile en équilibre, en compensant d'autres forces qui s'exercent sur lui.",
        "Une force se représente par un vecteur, une flèche caractérisée par son point d'application (où elle s'exerce), sa direction, son sens et sa valeur (exprimée en newtons, symbole N). Plus la flèche est longue, plus la force représentée est intense. Le poids d'un objet, force exercée par la Terre, est un exemple important de force à distance.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"120\" y=\"80\" width=\"60\" height=\"40\" fill=\"#7a5230\"/><path d=\"M180 100 L250 100\" stroke=\"#c1552e\" stroke-width=\"3\"/><path d=\"M250 100 L235 92 M250 100 L235 108\" stroke=\"#c1552e\" stroke-width=\"3\"/><text x=\"215\" y=\"85\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Force F</text><text x=\"150\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Objet</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'une action mécanique ?", "choix": ["Une action capable de modifier le mouvement ou la forme d'un objet", "Une réaction chimique", "Une action sans aucun effet", "Un phénomène uniquement sonore"], "reponse": 0, "explication": "Une action mécanique modifie le mouvement ou la forme d'un objet sur lequel elle s'exerce."},
        {"id": "q2", "enonce": "Qu'est-ce qu'une action de contact ?", "choix": ["Une action qui nécessite un contact direct entre objets", "Une action qui s'exerce toujours à distance", "Une action uniquement électrique", "Une action inexistante en physique"], "reponse": 0, "explication": "Une action de contact nécessite un contact direct entre deux objets, comme pousser ou tirer."},
        {"id": "q3", "enonce": "Citez un exemple d'action à distance.", "choix": ["L'attraction gravitationnelle", "Pousser une chaise", "Tirer une corde", "Frapper un ballon"], "reponse": 0, "explication": "L'attraction gravitationnelle est une action à distance, s'exerçant sans contact physique."},
        {"id": "q4", "enonce": "Une force peut-elle mettre un objet immobile en mouvement ?", "choix": ["Non, jamais", "Oui", "Uniquement si l'objet est très léger", "Uniquement en apesanteur"], "reponse": 1, "explication": "Une force peut mettre en mouvement un objet initialement immobile."},
        {"id": "q5", "enonce": "Une force peut-elle déformer un objet ?", "choix": ["Non, jamais", "Oui, comme comprimer un ressort", "Uniquement les objets liquides", "Uniquement les objets gazeux"], "reponse": 1, "explication": "Une force peut déformer un objet, par exemple en comprimant un ressort."},
        {"id": "q6", "enonce": "Comment représente-t-on une force ?", "choix": ["Par un vecteur (une flèche)", "Par un simple point", "Par une couleur", "Par un son"], "reponse": 0, "explication": "Une force se représente par un vecteur, caractérisé par son point d'application, sa direction, son sens et sa valeur."},
        {"id": "q7", "enonce": "Dans quelle unité s'exprime la valeur d'une force ?", "choix": ["Le newton (N)", "Le mètre (m)", "Le kilogramme (kg)", "La seconde (s)"], "reponse": 0, "explication": "La valeur d'une force s'exprime en newtons, de symbole N."},
        {"id": "q8", "enonce": "Qu'est-ce que le poids d'un objet ?", "choix": ["Une force exercée par la Terre sur l'objet", "Une action de contact uniquement", "Une couleur physique", "Une unité de longueur"], "reponse": 0, "explication": "Le poids est la force exercée par la Terre sur un objet, un exemple de force à distance."},
        {"id": "q9", "enonce": "Une force peut-elle maintenir un objet immobile en équilibre ?", "choix": ["Non, jamais", "Oui, en compensant d'autres forces", "Uniquement si l'objet est très lourd", "Uniquement dans le vide"], "reponse": 1, "explication": "Une force peut maintenir un objet en équilibre en compensant d'autres forces qui s'exercent sur lui."},
        {"id": "q10", "enonce": "Que signifie une flèche plus longue représentant une force ?", "choix": ["Une force plus faible", "Une force plus intense", "Aucune différence", "Une force à distance uniquement"], "reponse": 1, "explication": "Plus la flèche représentant une force est longue, plus la force est intense."},
    ],
})

L.append({
    "slug": "poids-masse-gravitation-4e", "titre": "Le poids, la masse et la gravitation universelle",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Distinguer le poids et la masse d'un objet et comprendre le principe de la gravitation universelle.",
    "objectifs": ["Distinguer la masse et le poids d'un objet", "Connaître la relation entre poids et masse", "Comprendre le principe de la gravitation universelle"],
    "contenu": [
        "La masse d'un objet, exprimée en kilogrammes (kg), mesure la quantité de matière qu'il contient : elle est constante, quel que soit l'endroit de l'univers où se trouve l'objet. Le poids, exprimé en newtons (N), est une force, celle exercée par un astre (comme la Terre) sur l'objet du fait de la gravitation : il dépend donc du lieu où se trouve l'objet.",
        "Sur Terre, le poids et la masse d'un objet sont reliés par la relation P = m x g, où g est appelé intensité de la pesanteur, environ égale à 9,8 N/kg sur Terre. Sur la Lune, où la gravité est plus faible (environ 1,6 N/kg), un même objet aurait la même masse mais un poids nettement plus faible que sur Terre.",
        "Isaac Newton a théorisé la loi de la gravitation universelle : tous les objets massifs s'attirent mutuellement, avec une force d'autant plus grande que leur masse est importante et que la distance qui les sépare est faible. C'est cette force qui maintient les planètes en orbite autour du Soleil et la Lune en orbite autour de la Terre.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"160\" cy=\"110\" r=\"45\" fill=\"#3b7bd6\"/><text x=\"160\" y=\"115\" text-anchor=\"middle\" font-size=\"10\" fill=\"#fff\">Terre</text><circle cx=\"280\" cy=\"60\" r=\"12\" fill=\"#9aa5b1\"/><path d=\"M270 68 L200 100\" stroke=\"#c1552e\" stroke-width=\"2\" fill=\"none\"/><text x=\"280\" y=\"40\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Lune</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Que mesure la masse d'un objet ?", "choix": ["La quantité de matière qu'il contient", "La force exercée par la Terre sur l'objet", "Sa couleur", "Sa vitesse"], "reponse": 0, "explication": "La masse mesure la quantité de matière contenue dans un objet."},
        {"id": "q2", "enonce": "Dans quelle unité s'exprime la masse ?", "choix": ["Le kilogramme (kg)", "Le newton (N)", "Le mètre (m)", "La seconde (s)"], "reponse": 0, "explication": "La masse s'exprime en kilogrammes (kg)."},
        {"id": "q3", "enonce": "Dans quelle unité s'exprime le poids ?", "choix": ["Le kilogramme (kg)", "Le newton (N)", "Le mètre (m)", "Le litre (L)"], "reponse": 1, "explication": "Le poids, étant une force, s'exprime en newtons (N)."},
        {"id": "q4", "enonce": "Le poids d'un objet change-t-il selon le lieu où il se trouve ?", "choix": ["Non, jamais", "Oui, car il dépend de la gravitation locale", "Uniquement s'il est mouillé", "Uniquement s'il est chaud"], "reponse": 1, "explication": "Le poids dépend de l'intensité de la pesanteur du lieu, donc il varie selon l'endroit."},
        {"id": "q5", "enonce": "La masse d'un objet change-t-elle selon le lieu où il se trouve ?", "choix": ["Oui, énormément", "Non, elle reste constante", "Uniquement sur la Lune", "Uniquement dans l'espace"], "reponse": 1, "explication": "La masse d'un objet reste constante, quel que soit l'endroit où il se trouve."},
        {"id": "q6", "enonce": "Quelle est la relation entre le poids et la masse ?", "choix": ["P = m x g", "P = m + g", "P = m / g", "P = g / m"], "reponse": 0, "explication": "Le poids se calcule par la relation P = m x g, où g est l'intensité de la pesanteur."},
        {"id": "q7", "enonce": "Quelle est approximativement l'intensité de la pesanteur sur Terre ?", "choix": ["9,8 N/kg", "1,6 N/kg", "100 N/kg", "0 N/kg"], "reponse": 0, "explication": "L'intensité de la pesanteur sur Terre est d'environ 9,8 N/kg."},
        {"id": "q8", "enonce": "Le poids d'un objet sur la Lune est-il plus faible que sur Terre ?", "choix": ["Non, plus élevé", "Oui, car la gravité lunaire est plus faible", "Il est identique", "Cela dépend de la couleur de l'objet"], "reponse": 1, "explication": "La gravité lunaire étant plus faible (environ 1,6 N/kg), le poids y est plus faible que sur Terre."},
        {"id": "q9", "enonce": "Qui a théorisé la loi de la gravitation universelle ?", "choix": ["Isaac Newton", "Charles Darwin", "Albert Einstein", "Louis Pasteur"], "reponse": 0, "explication": "Isaac Newton a théorisé la loi de la gravitation universelle."},
        {"id": "q10", "enonce": "Qu'est-ce qui maintient la Lune en orbite autour de la Terre ?", "choix": ["La force de gravitation", "Le vent", "La lumière du Soleil", "Le champ magnétique terrestre uniquement"], "reponse": 0, "explication": "La force de gravitation maintient la Lune en orbite autour de la Terre."},
    ],
})

L.append({
    "slug": "formes-conversions-energie-4e", "titre": "Les formes et conversions d'énergie",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Identifier les différentes formes d'énergie et comprendre le principe de leur conversion.",
    "objectifs": ["Identifier différentes formes d'énergie", "Comprendre le principe d'une conversion d'énergie", "Connaître l'unité de l'énergie"],
    "contenu": [
        "L'énergie existe sous de nombreuses formes : l'énergie cinétique (liée au mouvement d'un objet), l'énergie potentielle (liée à la position d'un objet, comme l'altitude), l'énergie électrique, l'énergie thermique (chaleur), l'énergie chimique (stockée dans les combustibles ou les aliments), l'énergie lumineuse et l'énergie nucléaire.",
        "L'énergie ne peut ni être créée ni disparaître : elle se transforme d'une forme à une autre, c'est ce qu'on appelle une conversion d'énergie. Par exemple, un panneau solaire convertit l'énergie lumineuse en énergie électrique ; une centrale hydraulique convertit l'énergie potentielle de l'eau en énergie électrique ; le corps humain convertit l'énergie chimique des aliments en énergie mécanique et thermique.",
        "L'unité légale de l'énergie est le joule (J), mais dans la vie courante, on utilise souvent le kilowattheure (kWh) pour l'énergie électrique, notamment sur les factures d'électricité. Lors de chaque conversion, une partie de l'énergie est généralement dissipée sous forme de chaleur, ce qui explique pourquoi aucun appareil n'a un rendement énergétique parfait de 100 %.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"40\" y=\"70\" width=\"70\" height=\"40\" fill=\"#e08a2a\"/><text x=\"75\" y=\"95\" text-anchor=\"middle\" font-size=\"9\" fill=\"#fff\">Lumineuse</text><path d=\"M110 90 L200 90\" stroke=\"#22303f\" stroke-width=\"2\"/><path d=\"M200 90 L188 84 M200 90 L188 96\" stroke=\"#22303f\" stroke-width=\"2\"/><rect x=\"210\" y=\"70\" width=\"70\" height=\"40\" fill=\"#3b7bd6\"/><text x=\"245\" y=\"95\" text-anchor=\"middle\" font-size=\"9\" fill=\"#fff\">Electrique</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Citez une forme d'énergie.", "choix": ["L'énergie cinétique", "La couleur", "La masse", "Le volume"], "reponse": 0, "explication": "L'énergie cinétique, liée au mouvement, est une des nombreuses formes d'énergie."},
        {"id": "q2", "enonce": "À quoi est liée l'énergie potentielle ?", "choix": ["À la position d'un objet, comme l'altitude", "Uniquement à la couleur d'un objet", "Uniquement à sa vitesse", "Elle n'existe pas"], "reponse": 0, "explication": "L'énergie potentielle est liée à la position d'un objet, notamment à son altitude."},
        {"id": "q3", "enonce": "Où est stockée l'énergie chimique ?", "choix": ["Dans les combustibles ou les aliments", "Dans la lumière uniquement", "Dans le vide", "Dans le son"], "reponse": 0, "explication": "L'énergie chimique est stockée dans les combustibles ou les aliments."},
        {"id": "q4", "enonce": "L'énergie peut-elle être créée ou détruite ?", "choix": ["Oui, facilement", "Non, elle se transforme seulement d'une forme à une autre", "Uniquement dans l'espace", "Uniquement par l'homme"], "reponse": 1, "explication": "L'énergie ne peut ni être créée ni disparaître, elle se transforme seulement."},
        {"id": "q5", "enonce": "Que convertit un panneau solaire ?", "choix": ["L'énergie lumineuse en énergie électrique", "L'énergie électrique en énergie lumineuse", "L'énergie chimique en énergie nucléaire", "Rien du tout"], "reponse": 0, "explication": "Un panneau solaire convertit l'énergie lumineuse en énergie électrique."},
        {"id": "q6", "enonce": "Que convertit une centrale hydraulique ?", "choix": ["L'énergie potentielle de l'eau en énergie électrique", "L'énergie lumineuse en énergie chimique", "L'énergie nucléaire en énergie potentielle", "Rien du tout"], "reponse": 0, "explication": "Une centrale hydraulique convertit l'énergie potentielle de l'eau en énergie électrique."},
        {"id": "q7", "enonce": "Quelle est l'unité légale de l'énergie ?", "choix": ["Le joule (J)", "Le newton (N)", "Le watt (W)", "Le kilogramme (kg)"], "reponse": 0, "explication": "L'unité légale de l'énergie est le joule (J)."},
        {"id": "q8", "enonce": "Quelle unité d'énergie électrique apparaît sur les factures d'électricité ?", "choix": ["Le kilowattheure (kWh)", "Le mètre par seconde", "Le newton", "Le degré Celsius"], "reponse": 0, "explication": "Le kilowattheure (kWh) est couramment utilisé pour l'énergie électrique sur les factures."},
        {"id": "q9", "enonce": "Que se passe-t-il souvent lors d'une conversion d'énergie ?", "choix": ["Toute l'énergie est parfaitement conservée sans perte", "Une partie de l'énergie est dissipée sous forme de chaleur", "L'énergie disparaît totalement", "L'énergie se multiplie"], "reponse": 1, "explication": "Une partie de l'énergie est généralement dissipée sous forme de chaleur lors d'une conversion."},
        {"id": "q10", "enonce": "Un appareil peut-il avoir un rendement énergétique de 100% ?", "choix": ["Oui, toujours", "Non, à cause des pertes sous forme de chaleur", "Uniquement les appareils électriques", "Uniquement dans le vide"], "reponse": 1, "explication": "Aucun appareil n'a un rendement parfait de 100% à cause des pertes d'énergie sous forme de chaleur."},
    ],
})

L.append({
    "slug": "puissance-electrique-economies-4e", "titre": "La puissance électrique et les économies d'énergie",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre la notion de puissance électrique et les enjeux des économies d'énergie.",
    "objectifs": ["Définir la puissance électrique", "Savoir calculer une énergie consommée à partir d'une puissance et d'une durée", "Connaître des pistes d'économies d'énergie"],
    "contenu": [
        "La puissance électrique d'un appareil, exprimée en watts (W), indique la quantité d'énergie qu'il consomme (ou produit) chaque seconde. Un appareil de forte puissance, comme un radiateur électrique (souvent plus de 1000 W), consomme beaucoup plus d'énergie par seconde qu'un appareil de faible puissance, comme une ampoule LED (quelques watts).",
        "L'énergie consommée par un appareil se calcule en multipliant sa puissance par la durée de fonctionnement : E = P x t. Si la puissance est exprimée en kilowatts (kW) et la durée en heures (h), l'énergie obtenue s'exprime directement en kilowattheures (kWh), l'unité utilisée sur les factures d'électricité.",
        "Face à l'augmentation de la consommation énergétique mondiale et à ses impacts environnementaux, plusieurs pistes permettent de réaliser des économies d'énergie : utiliser des appareils basse consommation (comme les ampoules LED), bien isoler les bâtiments pour limiter les pertes de chaleur, éteindre les appareils en veille, et adapter ses usages (température de chauffage, durée d'utilisation des appareils).",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"40\" y=\"60\" width=\"90\" height=\"90\" fill=\"#c1552e\"/><text x=\"85\" y=\"110\" text-anchor=\"middle\" font-size=\"11\" fill=\"#fff\">1000 W</text><rect x=\"200\" y=\"110\" width=\"30\" height=\"40\" fill=\"#3ba55d\"/><text x=\"215\" y=\"135\" text-anchor=\"middle\" font-size=\"9\" fill=\"#fff\">8 W</text><text x=\"160\" y=\"170\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Radiateur vs ampoule LED</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Que mesure la puissance électrique d'un appareil ?", "choix": ["La quantité d'énergie consommée chaque seconde", "Sa couleur", "Sa masse", "Sa taille"], "reponse": 0, "explication": "La puissance électrique indique la quantité d'énergie consommée (ou produite) chaque seconde."},
        {"id": "q2", "enonce": "Dans quelle unité s'exprime la puissance électrique ?", "choix": ["Le watt (W)", "Le joule (J)", "Le newton (N)", "L'ampère (A)"], "reponse": 0, "explication": "La puissance électrique s'exprime en watts (W)."},
        {"id": "q3", "enonce": "Un radiateur électrique a-t-il généralement une forte ou une faible puissance ?", "choix": ["Une forte puissance", "Une faible puissance", "Aucune puissance", "Cela dépend uniquement de sa couleur"], "reponse": 0, "explication": "Un radiateur électrique a généralement une forte puissance, souvent plus de 1000 W."},
        {"id": "q4", "enonce": "Quelle est la formule de l'énergie consommée par un appareil ?", "choix": ["E = P x t", "E = P / t", "E = P + t", "E = P - t"], "reponse": 0, "explication": "L'énergie consommée se calcule en multipliant la puissance par la durée de fonctionnement (E = P x t)."},
        {"id": "q5", "enonce": "Quelle unité obtient-on si P est en kW et t en heures ?", "choix": ["Le kilowattheure (kWh)", "Le joule", "Le watt", "Le newton"], "reponse": 0, "explication": "Avec la puissance en kW et la durée en heures, l'énergie s'exprime directement en kWh."},
        {"id": "q6", "enonce": "Une ampoule LED consomme-t-elle plus ou moins qu'une ampoule classique ?", "choix": ["Beaucoup moins", "Beaucoup plus", "Exactement la même chose", "Cela n'a aucun lien"], "reponse": 0, "explication": "Une ampoule LED consomme beaucoup moins d'énergie qu'une ampoule classique pour un éclairage équivalent."},
        {"id": "q7", "enonce": "Citez une piste d'économie d'énergie.", "choix": ["Bien isoler les bâtiments", "Laisser tous les appareils allumés en permanence", "Augmenter le chauffage au maximum", "Utiliser uniquement des appareils de forte puissance"], "reponse": 0, "explication": "Bien isoler les bâtiments permet de limiter les pertes de chaleur et de réaliser des économies d'énergie."},
        {"id": "q8", "enonce": "Éteindre les appareils en veille permet-il des économies d'énergie ?", "choix": ["Non, cela n'a aucun effet", "Oui, car la veille consomme aussi de l'énergie", "Cela augmente la consommation", "Uniquement pour les ordinateurs"], "reponse": 1, "explication": "Les appareils en veille continuent de consommer de l'énergie ; les éteindre permet des économies."},
        {"id": "q9", "enonce": "Pourquoi les économies d'énergie sont-elles importantes aujourd'hui ?", "choix": ["Elles n'ont aucune importance", "À cause de l'augmentation de la consommation mondiale et de ses impacts environnementaux", "Uniquement pour des raisons esthétiques", "Elles ne concernent que les usines"], "reponse": 1, "explication": "Les économies d'énergie répondent à l'augmentation de la consommation mondiale et à ses impacts environnementaux."},
        {"id": "q10", "enonce": "Sur quoi apparaît généralement le kilowattheure consommé ?", "choix": ["Sur les factures d'électricité", "Sur les étiquettes alimentaires", "Sur les cartes routières", "Sur les bulletins scolaires"], "reponse": 0, "explication": "Le kilowattheure (kWh) apparaît sur les factures d'électricité pour indiquer l'énergie consommée."},
    ],
})

L.append({
    "slug": "propagation-lumiere-4e", "titre": "La propagation de la lumière",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre comment se propage la lumière et ce qui se passe lorsqu'elle rencontre un obstacle.",
    "objectifs": ["Connaître le principe de propagation rectiligne de la lumière", "Distinguer objets transparents, translucides et opaques", "Comprendre la formation des ombres"],
    "contenu": [
        "La lumière se propage en ligne droite dans un milieu homogène et transparent, comme l'air ou le vide : c'est le principe de propagation rectiligne de la lumière. Ce principe explique pourquoi on ne peut pas voir un objet caché derrière un obstacle opaque, et pourquoi les rayons lumineux issus du Soleil ou d'une lampe forment des faisceaux de lignes droites.",
        "Selon leur capacité à laisser passer la lumière, les objets sont classés en trois catégories : les objets transparents (comme le verre clair ou l'air) laissent passer la lumière et permettent de voir nettement à travers ; les objets translucides (comme le verre dépoli) laissent passer une partie de la lumière mais floutent l'image ; les objets opaques (comme le bois ou le métal) ne laissent pas passer la lumière du tout.",
        "Lorsqu'un objet opaque est placé sur le trajet de la lumière issue d'une source, il bloque une partie du faisceau lumineux, créant une zone d'obscurité appelée ombre. On distingue l'ombre propre (la partie de l'objet lui-même non éclairée) de l'ombre portée (la zone sombre projetée sur une surface derrière l'objet).",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"40\" cy=\"60\" r=\"15\" fill=\"#e08a2a\"/><path d=\"M55 60 L150 60\" stroke=\"#e08a2a\" stroke-width=\"2\"/><path d=\"M55 60 L150 100\" stroke=\"#e08a2a\" stroke-width=\"2\"/><path d=\"M55 60 L150 130\" stroke=\"#e08a2a\" stroke-width=\"2\"/><rect x=\"150\" y=\"55\" width=\"20\" height=\"80\" fill=\"#22303f\"/><path d=\"M170 95 L260 150\" stroke=\"#9aa5b1\" stroke-width=\"18\"/><text x=\"215\" y=\"170\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Ombre portee</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Comment se propage la lumière dans un milieu homogène et transparent ?", "choix": ["En ligne droite", "En zigzag", "En cercle", "Elle ne se propage pas"], "reponse": 0, "explication": "La lumière se propage en ligne droite dans un milieu homogène et transparent, c'est la propagation rectiligne."},
        {"id": "q2", "enonce": "Que signifie la propagation rectiligne de la lumière ?", "choix": ["La lumière voyage en ligne droite", "La lumière voyage en spirale", "La lumière ne voyage jamais", "La lumière change constamment de direction"], "reponse": 0, "explication": "La propagation rectiligne signifie que la lumière se déplace en ligne droite."},
        {"id": "q3", "enonce": "Qu'est-ce qu'un objet transparent ?", "choix": ["Un objet qui laisse passer la lumière et permet de voir nettement à travers", "Un objet qui bloque toute la lumière", "Un objet qui ne laisse passer aucune lumière", "Un objet toujours coloré"], "reponse": 0, "explication": "Un objet transparent laisse passer la lumière et permet de voir nettement à travers, comme le verre clair."},
        {"id": "q4", "enonce": "Qu'est-ce qu'un objet translucide ?", "choix": ["Un objet qui laisse passer une partie de la lumière en floutant l'image", "Un objet totalement opaque", "Un objet totalement transparent", "Un objet qui n'existe pas"], "reponse": 0, "explication": "Un objet translucide laisse passer une partie de la lumière, mais floute l'image, comme le verre dépoli."},
        {"id": "q5", "enonce": "Qu'est-ce qu'un objet opaque ?", "choix": ["Un objet qui ne laisse pas passer la lumière", "Un objet qui laisse passer toute la lumière", "Un objet transparent uniquement", "Un objet lumineux"], "reponse": 0, "explication": "Un objet opaque, comme le bois ou le métal, ne laisse pas passer la lumière."},
        {"id": "q6", "enonce": "Que se passe-t-il quand un objet opaque est placé sur le trajet de la lumière ?", "choix": ["Rien ne se passe", "Il crée une zone d'ombre", "La lumière traverse sans problème", "L'objet devient transparent"], "reponse": 1, "explication": "Un objet opaque bloque la lumière et crée une zone d'ombre."},
        {"id": "q7", "enonce": "Qu'est-ce que l'ombre propre ?", "choix": ["La partie de l'objet lui-même non éclairée", "La zone projetée sur une surface derrière l'objet", "La lumière directe du soleil", "Une couleur d'objet"], "reponse": 0, "explication": "L'ombre propre est la partie de l'objet lui-même qui n'est pas éclairée."},
        {"id": "q8", "enonce": "Qu'est-ce que l'ombre portée ?", "choix": ["La zone sombre projetée sur une surface derrière l'objet", "La partie éclairée de l'objet", "Une source de lumière", "Un objet transparent"], "reponse": 0, "explication": "L'ombre portée est la zone sombre projetée sur une surface derrière l'objet opaque."},
        {"id": "q9", "enonce": "Pourquoi ne peut-on pas voir un objet caché derrière un obstacle opaque ?", "choix": ["À cause de la propagation rectiligne de la lumière", "Car les objets opaques sont invisibles", "Car la lumière change toujours de direction", "Ce n'est pas vrai, on peut toujours le voir"], "reponse": 0, "explication": "La propagation rectiligne de la lumière explique pourquoi un obstacle opaque empêche de voir ce qui est caché derrière."},
        {"id": "q10", "enonce": "Le verre dépoli est-il transparent, translucide ou opaque ?", "choix": ["Transparent", "Translucide", "Opaque", "Aucun des trois"], "reponse": 1, "explication": "Le verre dépoli est translucide : il laisse passer une partie de la lumière en floutant l'image."},
    ],
})

L.append({
    "slug": "vitesse-lumiere-son-4e", "titre": "La vitesse de la lumière et la vitesse du son",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comparer la vitesse de propagation de la lumière et celle du son dans différents milieux.",
    "objectifs": ["Connaître l'ordre de grandeur de la vitesse de la lumière", "Connaître l'ordre de grandeur de la vitesse du son dans l'air", "Comprendre pourquoi on voit l'éclair avant d'entendre le tonnerre"],
    "contenu": [
        "La lumière se propage extrêmement vite : dans le vide, sa vitesse est d'environ 300 000 kilomètres par seconde (km/s), ce qui correspond à la vitesse maximale connue dans l'univers. À cette vitesse, la lumière du Soleil met un peu plus de 8 minutes pour atteindre la Terre, malgré une distance moyenne d'environ 150 millions de kilomètres.",
        "Le son se propage beaucoup plus lentement que la lumière : dans l'air, à température ambiante, sa vitesse est d'environ 340 mètres par seconde (m/s), soit environ un million de fois plus lent que la lumière. Le son a besoin d'un support matériel (air, eau, solide) pour se propager : contrairement à la lumière, il ne peut pas se propager dans le vide.",
        "Cette différence de vitesse explique pourquoi, lors d'un orage, on voit l'éclair avant d'entendre le tonnerre, même si les deux phénomènes se produisent au même instant : la lumière de l'éclair nous parvient quasiment instantanément, tandis que le son du tonnerre met plusieurs secondes à parcourir la même distance. On peut ainsi estimer la distance d'un orage en comptant le nombre de secondes entre l'éclair et le tonnerre.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><path d=\"M60 40 L100 90 L80 90 L120 150\" stroke=\"#e08a2a\" stroke-width=\"4\" fill=\"none\"/><text x=\"80\" y=\"30\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Eclair : lumiere (rapide)</text><path d=\"M200 100 Q220 80 240 100 Q260 120 280 100\" stroke=\"#3b7bd6\" stroke-width=\"3\" fill=\"none\"/><text x=\"240\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Tonnerre : son (lent)</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Quelle est approximativement la vitesse de la lumière dans le vide ?", "choix": ["300 000 km/s", "340 m/s", "100 km/h", "3 000 km/s"], "reponse": 0, "explication": "La vitesse de la lumière dans le vide est d'environ 300 000 km/s."},
        {"id": "q2", "enonce": "Quelle est approximativement la vitesse du son dans l'air ?", "choix": ["300 000 km/s", "340 m/s", "1000 km/s", "3 m/s"], "reponse": 1, "explication": "La vitesse du son dans l'air à température ambiante est d'environ 340 m/s."},
        {"id": "q3", "enonce": "Combien de temps met la lumière du Soleil pour atteindre la Terre ?", "choix": ["Un peu plus de 8 minutes", "8 secondes", "8 heures", "8 jours"], "reponse": 0, "explication": "La lumière du Soleil met un peu plus de 8 minutes pour atteindre la Terre."},
        {"id": "q4", "enonce": "Le son peut-il se propager dans le vide ?", "choix": ["Oui, très bien", "Non, il a besoin d'un support matériel", "Uniquement dans l'espace", "Uniquement la nuit"], "reponse": 1, "explication": "Le son a besoin d'un support matériel (air, eau, solide) et ne peut pas se propager dans le vide."},
        {"id": "q5", "enonce": "La lumière peut-elle se propager dans le vide ?", "choix": ["Non, jamais", "Oui, contrairement au son", "Uniquement dans l'eau", "Uniquement dans l'air"], "reponse": 1, "explication": "Contrairement au son, la lumière peut se propager dans le vide."},
        {"id": "q6", "enonce": "Pourquoi voit-on l'éclair avant d'entendre le tonnerre ?", "choix": ["Car la lumière est beaucoup plus rapide que le son", "Car le son arrive avant la lumière", "Ce n'est pas vrai, ils arrivent en même temps", "Car l'éclair est plus proche"], "reponse": 0, "explication": "La lumière étant beaucoup plus rapide que le son, l'éclair est perçu avant le tonnerre."},
        {"id": "q7", "enonce": "Environ combien de fois la lumière est-elle plus rapide que le son dans l'air ?", "choix": ["Environ un million de fois", "Deux fois", "Dix fois", "Elles ont la même vitesse"], "reponse": 0, "explication": "La lumière est environ un million de fois plus rapide que le son dans l'air."},
        {"id": "q8", "enonce": "Comment peut-on estimer la distance d'un orage ?", "choix": ["En comptant les secondes entre l'éclair et le tonnerre", "En comptant le nombre d'éclairs", "C'est impossible à estimer", "En mesurant la température"], "reponse": 0, "explication": "On peut estimer la distance d'un orage en comptant les secondes entre l'éclair et le tonnerre."},
        {"id": "q9", "enonce": "La vitesse de la lumière dans le vide est-elle la vitesse maximale connue dans l'univers ?", "choix": ["Non, il existe des vitesses plus rapides", "Oui, c'est la vitesse maximale connue", "Cela n'a jamais été démontré", "Uniquement sur Terre"], "reponse": 1, "explication": "La vitesse de la lumière dans le vide est la vitesse maximale connue dans l'univers."},
        {"id": "q10", "enonce": "Quelle est environ la distance moyenne entre le Soleil et la Terre ?", "choix": ["150 millions de kilomètres", "150 000 kilomètres", "1,5 million de kilomètres", "15 milliards de kilomètres"], "reponse": 0, "explication": "La distance moyenne entre le Soleil et la Terre est d'environ 150 millions de kilomètres."},
    ],
})

L.append({
    "slug": "ondes-sonores-caracteristiques-4e", "titre": "Les ondes sonores et leurs caractéristiques",
    "matiere": "physique-chimie", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre comment se produit et se caractérise un son.",
    "objectifs": ["Comprendre comment se produit un son", "Distinguer hauteur et intensité d'un son", "Connaître les limites de l'audition humaine"],
    "contenu": [
        "Un son est produit par la vibration d'un objet, appelé source sonore : les cordes d'une guitare, les cordes vocales, ou la membrane d'un haut-parleur vibrent et transmettent cette vibration aux molécules du milieu environnant (généralement l'air), créant une onde sonore qui se propage jusqu'à notre oreille.",
        "Un son se caractérise par deux grandeurs principales : sa hauteur, liée à la fréquence de vibration (exprimée en hertz, Hz) — plus la fréquence est élevée, plus le son est aigu, plus elle est basse, plus le son est grave ; et son intensité, liée à l'amplitude de la vibration (exprimée en décibels, dB) — plus l'amplitude est grande, plus le son est fort.",
        "L'oreille humaine ne perçoit qu'une gamme limitée de fréquences, généralement entre 20 Hz et 20 000 Hz : en dessous, on parle d'infrasons, au-dessus, d'ultrasons, tous deux inaudibles pour l'être humain mais parfois perçus par certains animaux. Une exposition prolongée à des sons de forte intensité (au-delà de 85 dB) peut endommager durablement l'audition.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><path d=\"M30 100 Q50 60 70 100 Q90 140 110 100 Q130 60 150 100\" stroke=\"#3b7bd6\" stroke-width=\"3\" fill=\"none\"/><text x=\"90\" y=\"130\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Son aigu (haute frequence)</text><path d=\"M190 100 Q220 85 250 100 Q280 115 310 100\" stroke=\"#c1552e\" stroke-width=\"3\" fill=\"none\"/><text x=\"250\" y=\"130\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Son grave (basse frequence)</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Comment se produit un son ?", "choix": ["Par la vibration d'une source sonore", "Par la lumière", "Par la chaleur uniquement", "Par le mouvement des atomes uniquement"], "reponse": 0, "explication": "Un son est produit par la vibration d'une source sonore, comme des cordes ou une membrane."},
        {"id": "q2", "enonce": "Qu'est-ce qui caractérise la hauteur d'un son ?", "choix": ["La fréquence de vibration", "La couleur", "La température", "La masse"], "reponse": 0, "explication": "La hauteur d'un son est liée à sa fréquence de vibration, exprimée en hertz."},
        {"id": "q3", "enonce": "Dans quelle unité s'exprime la fréquence d'un son ?", "choix": ["Le hertz (Hz)", "Le décibel (dB)", "Le watt (W)", "Le mètre (m)"], "reponse": 0, "explication": "La fréquence d'un son s'exprime en hertz (Hz)."},
        {"id": "q4", "enonce": "Un son de fréquence élevée est-il aigu ou grave ?", "choix": ["Aigu", "Grave", "Ni l'un ni l'autre", "Cela dépend de sa couleur"], "reponse": 0, "explication": "Plus la fréquence est élevée, plus le son est aigu."},
        {"id": "q5", "enonce": "Qu'est-ce qui caractérise l'intensité d'un son ?", "choix": ["L'amplitude de la vibration", "Sa fréquence uniquement", "Sa couleur", "Sa vitesse de propagation"], "reponse": 0, "explication": "L'intensité d'un son est liée à l'amplitude de sa vibration, exprimée en décibels."},
        {"id": "q6", "enonce": "Dans quelle unité s'exprime l'intensité sonore ?", "choix": ["Le hertz (Hz)", "Le décibel (dB)", "Le mètre (m)", "Le kilogramme (kg)"], "reponse": 1, "explication": "L'intensité sonore s'exprime en décibels (dB)."},
        {"id": "q7", "enonce": "Quelle est la gamme de fréquences généralement audible par l'être humain ?", "choix": ["Entre 20 Hz et 20 000 Hz", "Entre 0 Hz et 1 Hz", "Entre 1 000 000 Hz et 2 000 000 Hz", "Aucune limite"], "reponse": 0, "explication": "L'oreille humaine perçoit généralement les fréquences entre 20 Hz et 20 000 Hz."},
        {"id": "q8", "enonce": "Comment appelle-t-on les sons de fréquence inférieure à 20 Hz ?", "choix": ["Des ultrasons", "Des infrasons", "Des sons aigus", "Des sons normaux"], "reponse": 1, "explication": "Les sons de fréquence inférieure à 20 Hz sont appelés infrasons, inaudibles pour l'être humain."},
        {"id": "q9", "enonce": "Comment appelle-t-on les sons de fréquence supérieure à 20 000 Hz ?", "choix": ["Des infrasons", "Des ultrasons", "Des sons graves", "Des sons normaux"], "reponse": 1, "explication": "Les sons de fréquence supérieure à 20 000 Hz sont appelés ultrasons, inaudibles pour l'être humain."},
        {"id": "q10", "enonce": "Une exposition prolongée à des sons de plus de 85 dB peut-elle endommager l'audition ?", "choix": ["Non, jamais", "Oui, cela peut l'endommager durablement", "Uniquement pour les animaux", "Uniquement en dessous de 20 Hz"], "reponse": 1, "explication": "Une exposition prolongée à des sons de forte intensité (plus de 85 dB) peut endommager durablement l'audition."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_before(txt, "preterit-anglais", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecons Physique-Chimie 4e ajoutees.")
