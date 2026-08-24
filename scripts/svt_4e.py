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

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

L = []

L.append({
    "slug": "ecosystemes-biodiversite-4e", "titre": "Les écosystèmes et la biodiversité",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre l'organisation d'un écosystème et les enjeux de la préservation de la biodiversité.",
    "objectifs": ["Définir un écosystème et ses composantes", "Comprendre les relations entre les êtres vivants d'un écosystème", "Comprendre les menaces qui pèsent sur la biodiversité"],
    "contenu": [
        "Un écosystème est un ensemble formé par un milieu (le biotope, avec ses caractéristiques physiques comme le climat, le sol, l'eau) et l'ensemble des êtres vivants qui y habitent (la biocénose), en interaction constante les uns avec les autres et avec leur milieu. Une forêt, un lac ou un récif corallien sont des exemples d'écosystèmes.",
        "Au sein d'un écosystème, les êtres vivants entretiennent des relations variées : relations alimentaires organisées en chaînes et réseaux alimentaires, relations de compétition pour les ressources, ou relations de coopération comme la pollinisation entre une fleur et un insecte. La biodiversité désigne la diversité de ces êtres vivants et de leurs interactions, à tous les niveaux : gènes, espèces, écosystèmes.",
        "Cette biodiversité est aujourd'hui menacée par de nombreuses actions humaines : destruction et fragmentation des habitats naturels, pollution, surexploitation des ressources (surpêche, déforestation), introduction d'espèces invasives et changement climatique. La disparition d'une seule espèce peut fragiliser tout un écosystème, car les interactions entre espèces sont souvent essentielles à son équilibre.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><rect x=\"0\" y=\"120\" width=\"320\" height=\"70\" fill=\"#a8d5a2\"/><circle cx=\"60\" cy=\"100\" r=\"30\" fill=\"#3ba55d\"/><rect x=\"55\" y=\"120\" width=\"10\" height=\"30\" fill=\"#7a5230\"/><circle cx=\"150\" cy=\"90\" r=\"25\" fill=\"#3ba55d\"/><rect x=\"145\" y=\"110\" width=\"8\" height=\"30\" fill=\"#7a5230\"/><circle cx=\"240\" cy=\"105\" r=\"20\" fill=\"#e08a2a\"/><text x=\"160\" y=\"175\" text-anchor=\"middle\" font-size=\"10\" fill=\"#22303f\">Un ecosysteme : biotope + biocenose</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un écosystème ?", "choix": ["Un milieu et les êtres vivants qui y habitent, en interaction", "Uniquement un milieu physique", "Uniquement des êtres vivants", "Un objet technique"], "reponse": 0, "explication": "Un écosystème associe un milieu (biotope) et les êtres vivants (biocénose) en interaction."},
        {"id": "q2", "enonce": "Comment appelle-t-on le milieu physique d'un écosystème ?", "choix": ["La biocénose", "Le biotope", "La biodiversité", "L'écologie"], "reponse": 1, "explication": "Le biotope désigne le milieu physique (climat, sol, eau) d'un écosystème."},
        {"id": "q3", "enonce": "Comment appelle-t-on l'ensemble des êtres vivants d'un écosystème ?", "choix": ["Le biotope", "La biocénose", "L'atmosphère", "Le climat"], "reponse": 1, "explication": "La biocénose désigne l'ensemble des êtres vivants d'un écosystème."},
        {"id": "q4", "enonce": "Citez une relation de coopération entre deux espèces.", "choix": ["La pollinisation entre une fleur et un insecte", "La compétition alimentaire", "La prédation uniquement", "Aucune coopération n'existe entre espèces"], "reponse": 0, "explication": "La pollinisation est un exemple de coopération entre une fleur et un insecte pollinisateur."},
        {"id": "q5", "enonce": "Que désigne la biodiversité ?", "choix": ["La diversité des êtres vivants et de leurs interactions", "Uniquement le nombre d'espèces animales", "Uniquement les plantes", "L'absence de vie"], "reponse": 0, "explication": "La biodiversité désigne la diversité des êtres vivants, des gènes aux écosystèmes."},
        {"id": "q6", "enonce": "Citez une menace humaine sur la biodiversité.", "choix": ["La destruction des habitats naturels", "La protection des forêts uniquement", "Aucune menace n'existe", "La conservation des espèces uniquement"], "reponse": 0, "explication": "La destruction et la fragmentation des habitats naturels menacent fortement la biodiversité."},
        {"id": "q7", "enonce": "Qu'est-ce qu'une espèce invasive ?", "choix": ["Une espèce protégée", "Une espèce introduite qui perturbe l'écosystème local", "Une espèce disparue", "Une espèce en voie d'extinction uniquement"], "reponse": 1, "explication": "Une espèce invasive est une espèce introduite qui perturbe l'équilibre d'un écosystème local."},
        {"id": "q8", "enonce": "La disparition d'une seule espèce peut-elle affecter tout un écosystème ?", "choix": ["Non, jamais", "Oui, car les interactions entre espèces sont souvent essentielles", "Uniquement si c'est une plante", "Uniquement si c'est un prédateur"], "reponse": 1, "explication": "La disparition d'une espèce peut fragiliser tout l'écosystème à cause des interactions entre espèces."},
        {"id": "q9", "enonce": "Citez un exemple d'écosystème.", "choix": ["Une forêt", "Une voiture", "Un ordinateur", "Une pièce de monnaie"], "reponse": 0, "explication": "Une forêt, un lac ou un récif corallien sont des exemples d'écosystèmes."},
        {"id": "q10", "enonce": "La surpêche est-elle une menace pour la biodiversité marine ?", "choix": ["Oui, une surexploitation des ressources", "Non, elle n'a aucun effet", "Elle augmente la biodiversité", "Elle ne concerne pas les écosystèmes"], "reponse": 0, "explication": "La surpêche est une forme de surexploitation qui menace la biodiversité marine."},
    ],
})

L.append({
    "slug": "evolution-especes-darwin-4e", "titre": "L'évolution des espèces et Charles Darwin",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre le mécanisme de l'évolution des espèces par sélection naturelle, théorisé par Charles Darwin.",
    "objectifs": ["Comprendre ce qu'est l'évolution des espèces", "Connaître le principe de la sélection naturelle", "Comprendre le rôle des fossiles comme preuves de l'évolution"],
    "contenu": [
        "L'évolution est le processus par lequel les caractéristiques des espèces vivantes se transforment au fil des générations, sous l'effet de modifications du matériel génétique et de la pression du milieu. Ce processus explique la grande diversité actuelle du vivant, ainsi que la parenté entre toutes les espèces, qui descendent d'ancêtres communs plus ou moins lointains.",
        "Charles Darwin, naturaliste britannique du XIXe siècle, a théorisé le mécanisme de la sélection naturelle dans son ouvrage L'Origine des espèces (1859). Selon ce principe, au sein d'une population, les individus présentent des variations naturelles ; ceux dont les caractéristiques sont les mieux adaptées à leur environnement survivent et se reproduisent davantage, transmettant ainsi ces caractéristiques avantageuses aux générations suivantes.",
        "Les fossiles, restes ou traces d'êtres vivants conservés dans les roches, constituent une preuve importante de l'évolution : ils permettent d'observer des espèces disparues et de retracer les grandes étapes de la diversification du vivant au cours des temps géologiques. D'autres preuves de l'évolution viennent de la comparaison de l'ADN entre espèces actuelles, qui confirme les liens de parenté déjà suggérés par l'anatomie comparée.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><path d=\"M30 150 L100 100\" stroke=\"#22303f\" stroke-width=\"2\"/><path d=\"M100 100 L160 60\" stroke=\"#22303f\" stroke-width=\"2\"/><path d=\"M100 100 L160 130\" stroke=\"#22303f\" stroke-width=\"2\"/><path d=\"M160 60 L220 30\" stroke=\"#22303f\" stroke-width=\"2\"/><path d=\"M160 60 L220 80\" stroke=\"#22303f\" stroke-width=\"2\"/><circle cx=\"30\" cy=\"150\" r=\"6\" fill=\"#3ba55d\"/><circle cx=\"220\" cy=\"30\" r=\"6\" fill=\"#3b7bd6\"/><circle cx=\"220\" cy=\"80\" r=\"6\" fill=\"#e08a2a\"/><circle cx=\"160\" cy=\"130\" r=\"6\" fill=\"#c1552e\"/><text x=\"160\" y=\"175\" text-anchor=\"middle\" font-size=\"10\" fill=\"#22303f\">Arbre de l'evolution des especes</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que l'évolution des espèces ?", "choix": ["La transformation des caractéristiques des espèces au fil des générations", "L'apparition instantanée de nouvelles espèces", "La disparition de toute vie", "Un phénomène qui ne concerne que les plantes"], "reponse": 0, "explication": "L'évolution est la transformation progressive des caractéristiques des espèces au fil des générations."},
        {"id": "q2", "enonce": "Qui a théorisé la sélection naturelle ?", "choix": ["Charles Darwin", "Isaac Newton", "Louis Pasteur", "Albert Einstein"], "reponse": 0, "explication": "Charles Darwin a théorisé le mécanisme de la sélection naturelle."},
        {"id": "q3", "enonce": "Dans quel ouvrage Darwin expose-t-il sa théorie ?", "choix": ["L'Origine des espèces", "Le Discours de la méthode", "Les Fables", "L'Encyclopédie"], "reponse": 0, "explication": "Darwin publie L'Origine des espèces en 1859."},
        {"id": "q4", "enonce": "Que se passe-t-il pour les individus les mieux adaptés selon la sélection naturelle ?", "choix": ["Ils disparaissent plus vite", "Ils survivent et se reproduisent davantage", "Rien de particulier", "Ils deviennent stériles"], "reponse": 1, "explication": "Les individus les mieux adaptés survivent et se reproduisent davantage, transmettant leurs caractéristiques."},
        {"id": "q5", "enonce": "D'où viennent les variations sur lesquelles agit la sélection naturelle ?", "choix": ["De variations naturelles entre individus d'une population", "Elles n'existent pas", "Uniquement de l'environnement", "Uniquement du hasard total sans lien génétique"], "reponse": 0, "explication": "Les individus d'une population présentent des variations naturelles, sur lesquelles agit la sélection naturelle."},
        {"id": "q6", "enonce": "Qu'est-ce qu'un fossile ?", "choix": ["Un reste ou une trace d'être vivant conservé dans la roche", "Un animal vivant aujourd'hui", "Un type de roche sans lien avec le vivant", "Un instrument scientifique"], "reponse": 0, "explication": "Un fossile est un reste ou une trace d'être vivant conservé dans les roches."},
        {"id": "q7", "enonce": "À quoi servent les fossiles pour l'étude de l'évolution ?", "choix": ["À rien de particulier", "À observer des espèces disparues et retracer les étapes de l'évolution", "Uniquement à la décoration", "Uniquement à dater les roches"], "reponse": 1, "explication": "Les fossiles permettent d'observer des espèces disparues et de retracer les grandes étapes de l'évolution."},
        {"id": "q8", "enonce": "Que confirme la comparaison de l'ADN entre espèces actuelles ?", "choix": ["Rien du tout", "Les liens de parenté entre espèces", "Que les espèces n'ont aucun lien", "Que l'évolution n'existe pas"], "reponse": 1, "explication": "La comparaison de l'ADN confirme les liens de parenté entre espèces, déjà suggérés par l'anatomie comparée."},
        {"id": "q9", "enonce": "Toutes les espèces actuelles descendent-elles d'ancêtres communs ?", "choix": ["Non, chaque espèce est apparue indépendamment", "Oui, plus ou moins lointains selon les espèces", "Uniquement les mammifères", "Cela n'a jamais été démontré"], "reponse": 1, "explication": "Toutes les espèces vivantes descendent d'ancêtres communs plus ou moins lointains."},
        {"id": "q10", "enonce": "À quel siècle appartient Charles Darwin ?", "choix": ["Le XVIIe siècle", "Le XVIIIe siècle", "Le XIXe siècle", "Le XXe siècle"], "reponse": 2, "explication": "Charles Darwin est un naturaliste du XIXe siècle."},
    ],
})

L.append({
    "slug": "reproduction-developpement-animaux-4e", "titre": "La reproduction sexuée et le développement des animaux",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre les mécanismes de la reproduction sexuée et les étapes du développement chez les animaux.",
    "objectifs": ["Comprendre le principe de la fécondation", "Distinguer développement direct et développement indirect", "Comprendre l'influence du milieu sur la reproduction"],
    "contenu": [
        "La reproduction sexuée nécessite la rencontre d'une cellule reproductrice mâle (spermatozoïde) et d'une cellule reproductrice femelle (ovule) : c'est la fécondation, qui donne naissance à une nouvelle cellule, l'œuf, à l'origine d'un nouvel individu. Cette fécondation peut être externe, dans le milieu extérieur comme chez de nombreux poissons, ou interne, à l'intérieur du corps de la femelle comme chez les mammifères.",
        "Après la fécondation, le développement d'un animal peut suivre deux grandes voies : le développement direct, où le jeune ressemble déjà à l'adulte en miniature dès sa naissance, comme chez les mammifères ou les oiseaux ; ou le développement indirect, avec métamorphose, où le jeune passe par des stades très différents de l'adulte, comme la chenille qui devient papillon, ou le têtard qui devient grenouille.",
        "La réussite de la reproduction dépend fortement des conditions du milieu : température, disponibilité en nourriture, présence de partenaires. De nombreuses espèces synchronisent leur reproduction avec des périodes favorables de l'année (saison des amours), et certaines adoptent des comportements complexes, comme les parades nuptiales, pour favoriser la rencontre entre partenaires et le succès de la reproduction.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"60\" cy=\"80\" r=\"15\" fill=\"#3ba55d\"/><text x=\"60\" y=\"110\" text-anchor=\"middle\" font-size=\"8\" fill=\"#22303f\">Oeuf</text><path d=\"M90 80 L140 80\" stroke=\"#22303f\" stroke-width=\"2\"/><ellipse cx=\"170\" cy=\"80\" rx=\"25\" ry=\"14\" fill=\"#7a5230\"/><text x=\"170\" y=\"110\" text-anchor=\"middle\" font-size=\"8\" fill=\"#22303f\">Chenille</text><path d=\"M200 80 L250 80\" stroke=\"#22303f\" stroke-width=\"2\"/><ellipse cx=\"280\" cy=\"70\" rx=\"16\" ry=\"10\" fill=\"#e08a2a\"/><path d=\"M270 65 L255 55 M290 65 L305 55\" stroke=\"#c1552e\" stroke-width=\"3\"/><text x=\"160\" y=\"170\" text-anchor=\"middle\" font-size=\"10\" fill=\"#22303f\">Developpement indirect : metamorphose</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que la fécondation ?", "choix": ["La rencontre d'un spermatozoïde et d'un ovule", "La naissance d'un animal", "La mort d'une cellule", "Un type de nutrition"], "reponse": 0, "explication": "La fécondation est la rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle."},
        {"id": "q2", "enonce": "Que donne la fécondation ?", "choix": ["Un œuf, à l'origine d'un nouvel individu", "Rien de particulier", "Un adulte immédiatement", "Une cellule morte"], "reponse": 0, "explication": "La fécondation donne naissance à l'œuf, cellule à l'origine d'un nouvel individu."},
        {"id": "q3", "enonce": "Qu'est-ce que la fécondation externe ?", "choix": ["Elle se produit dans le milieu extérieur", "Elle se produit toujours à l'intérieur du corps", "Elle n'existe pas chez les animaux", "Elle concerne uniquement les mammifères"], "reponse": 0, "explication": "La fécondation externe se produit dans le milieu extérieur, comme chez de nombreux poissons."},
        {"id": "q4", "enonce": "Chez quels animaux la fécondation est-elle généralement interne ?", "choix": ["Les mammifères", "Tous les poissons", "Aucun animal", "Uniquement les insectes"], "reponse": 0, "explication": "La fécondation interne se produit à l'intérieur du corps de la femelle, comme chez les mammifères."},
        {"id": "q5", "enonce": "Qu'est-ce que le développement direct ?", "choix": ["Le jeune ressemble déjà à l'adulte en miniature", "Le jeune passe par une métamorphose complète", "Il n'existe pas chez les animaux", "Il concerne uniquement les insectes"], "reponse": 0, "explication": "Dans le développement direct, le jeune ressemble déjà à l'adulte en miniature dès la naissance."},
        {"id": "q6", "enonce": "Qu'est-ce que le développement indirect ?", "choix": ["Le jeune passe par des stades très différents de l'adulte", "Le jeune est identique à l'adulte", "Il n'existe pas", "Il concerne uniquement les mammifères"], "reponse": 0, "explication": "Le développement indirect implique une métamorphose, avec des stades très différents de l'adulte."},
        {"id": "q7", "enonce": "Citez un exemple de métamorphose.", "choix": ["La chenille qui devient papillon", "Le chaton qui devient chat", "Le poussin qui devient poule", "L'agneau qui devient mouton"], "reponse": 0, "explication": "La métamorphose de la chenille en papillon est un exemple classique de développement indirect."},
        {"id": "q8", "enonce": "Le têtard devient-il une grenouille par développement direct ou indirect ?", "choix": ["Direct", "Indirect, avec métamorphose", "Ni l'un ni l'autre", "Il ne se transforme jamais"], "reponse": 1, "explication": "Le têtard se transforme en grenouille par métamorphose, un développement indirect."},
        {"id": "q9", "enonce": "Qu'est-ce qu'une parade nuptiale ?", "choix": ["Un comportement favorisant la rencontre entre partenaires", "Une maladie animale", "Un type de nutrition", "Un phénomène météorologique"], "reponse": 0, "explication": "La parade nuptiale est un comportement complexe qui favorise la rencontre entre partenaires reproducteurs."},
        {"id": "q10", "enonce": "Le succès de la reproduction dépend-il des conditions du milieu ?", "choix": ["Non, jamais", "Oui, comme la température ou la disponibilité en nourriture", "Uniquement de la couleur des animaux", "Uniquement de la saison en hiver"], "reponse": 1, "explication": "Le succès de la reproduction dépend fortement des conditions du milieu."},
    ],
})

L.append({
    "slug": "systeme-nerveux-communication-4e", "titre": "Le système nerveux et la communication nerveuse",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre l'organisation du système nerveux et le trajet d'un message nerveux.",
    "objectifs": ["Identifier les organes du système nerveux", "Comprendre le trajet d'un message nerveux lors d'un réflexe", "Comprendre les effets de certaines substances sur le système nerveux"],
    "contenu": [
        "Le système nerveux est organisé autour du système nerveux central, composé du cerveau et de la moelle épinière, protégés respectivement par le crâne et la colonne vertébrale, et du système nerveux périphérique, formé des nerfs qui relient ce centre à tous les organes du corps. Le cerveau, organe le plus complexe du corps humain, coordonne la plupart des fonctions volontaires et involontaires.",
        "Lors d'un réflexe, comme retirer sa main d'une surface brûlante, un message nerveux part d'un récepteur sensoriel (la peau), remonte par un nerf sensitif jusqu'à la moelle épinière, qui traite l'information très rapidement sans passer par le cerveau, puis un nerf moteur transmet la commande jusqu'au muscle qui se contracte. Ce circuit court explique la très grande rapidité des réflexes.",
        "Certaines substances peuvent perturber le fonctionnement du système nerveux : l'alcool ralentit la transmission des messages nerveux et altère les réflexes et le jugement ; certaines drogues modifient artificiellement l'activité du cerveau, créant des sensations de plaisir mais aussi des risques de dépendance et des dommages durables, particulièrement graves sur un cerveau encore en développement, comme celui d'un adolescent.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><ellipse cx=\"80\" cy=\"60\" rx=\"35\" ry=\"28\" fill=\"#e08a2a\"/><text x=\"80\" y=\"105\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Cerveau</text><path d=\"M80 88 L80 150\" stroke=\"#3b7bd6\" stroke-width=\"6\"/><text x=\"80\" y=\"170\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Moelle epiniere</text><path d=\"M80 130 Q180 130 220 100\" stroke=\"#c1552e\" stroke-width=\"2\" fill=\"none\"/><circle cx=\"240\" cy=\"90\" r=\"8\" fill=\"#c1552e\"/><text x=\"240\" y=\"115\" text-anchor=\"middle\" font-size=\"8\" fill=\"#22303f\">Muscle</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "De quoi est composé le système nerveux central ?", "choix": ["Du cerveau et de la moelle épinière", "Uniquement des nerfs", "Uniquement du cœur", "Des muscles uniquement"], "reponse": 0, "explication": "Le système nerveux central est composé du cerveau et de la moelle épinière."},
        {"id": "q2", "enonce": "Qu'est-ce qui protège le cerveau ?", "choix": ["La colonne vertébrale", "Le crâne", "La peau uniquement", "Rien ne le protège"], "reponse": 1, "explication": "Le crâne protège le cerveau, tandis que la colonne vertébrale protège la moelle épinière."},
        {"id": "q3", "enonce": "Qu'est-ce que le système nerveux périphérique ?", "choix": ["Le cerveau uniquement", "Les nerfs qui relient le système central aux organes", "La moelle épinière uniquement", "Un organe séparé du système nerveux"], "reponse": 1, "explication": "Le système nerveux périphérique est formé des nerfs qui relient le système central à tout le corps."},
        {"id": "q4", "enonce": "Lors d'un réflexe, où part le message nerveux en premier ?", "choix": ["Du cerveau", "D'un récepteur sensoriel comme la peau", "Du cœur", "Des poumons"], "reponse": 1, "explication": "Le message nerveux part d'un récepteur sensoriel, comme la peau, lors d'un réflexe."},
        {"id": "q5", "enonce": "Le message d'un réflexe passe-t-il par le cerveau ?", "choix": ["Oui, toujours", "Non, la moelle épinière traite l'information directement", "Cela dépend du réflexe", "Il ne passe par aucun organe"], "reponse": 1, "explication": "Lors d'un réflexe, la moelle épinière traite l'information rapidement, sans passer par le cerveau."},
        {"id": "q6", "enonce": "Pourquoi les réflexes sont-ils très rapides ?", "choix": ["Grâce au circuit court passant par la moelle épinière", "Ils ne sont pas rapides du tout", "Car ils passent toujours par le cerveau", "Grâce aux muscles uniquement"], "reponse": 0, "explication": "Le circuit court, sans passer par le cerveau, explique la grande rapidité des réflexes."},
        {"id": "q7", "enonce": "Quel effet l'alcool a-t-il sur le système nerveux ?", "choix": ["Il l'améliore", "Il ralentit la transmission des messages nerveux", "Il n'a aucun effet", "Il accélère les réflexes"], "reponse": 1, "explication": "L'alcool ralentit la transmission des messages nerveux et altère réflexes et jugement."},
        {"id": "q8", "enonce": "Pourquoi les drogues sont-elles particulièrement dangereuses pour un adolescent ?", "choix": ["Elles n'ont aucun effet particulier", "Le cerveau adolescent est encore en développement", "Elles ne concernent que les adultes", "Elles n'affectent jamais le cerveau"], "reponse": 1, "explication": "Le cerveau d'un adolescent est encore en développement, ce qui le rend plus vulnérable aux effets des drogues."},
        {"id": "q9", "enonce": "Quel nerf transmet la commande du système nerveux vers le muscle ?", "choix": ["Le nerf sensitif", "Le nerf moteur", "Aucun nerf", "Le nerf optique uniquement"], "reponse": 1, "explication": "Le nerf moteur transmet la commande jusqu'au muscle qui se contracte."},
        {"id": "q10", "enonce": "Qu'est-ce qui peut créer une dépendance en modifiant l'activité du cerveau ?", "choix": ["Certaines drogues", "L'eau", "Les fruits", "Le sommeil"], "reponse": 0, "explication": "Certaines drogues modifient artificiellement l'activité du cerveau, créant des risques de dépendance."},
    ],
})

L.append({
    "slug": "reproduction-humaine-puberte-4e", "titre": "La reproduction humaine et la puberté",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre les transformations de la puberté et le fonctionnement des appareils reproducteurs humains.",
    "objectifs": ["Comprendre les transformations physiques et hormonales de la puberté", "Décrire le fonctionnement de l'appareil reproducteur féminin et masculin", "Comprendre le principe de la fécondation chez l'être humain"],
    "contenu": [
        "La puberté est la période de transformations physiques et hormonales qui marque le passage de l'enfance à l'adolescence, généralement entre 10 et 15 ans. Elle est déclenchée par le cerveau, qui stimule la production d'hormones sexuelles : les testicules produisent de la testostérone chez le garçon, les ovaires produisent des œstrogènes et de la progestérone chez la fille, entraînant l'apparition des caractères sexuels secondaires.",
        "Chez la fille, les ovaires libèrent chaque mois un ovule, ce qui déclenche le cycle menstruel : si l'ovule n'est pas fécondé, les règles surviennent environ 14 jours plus tard. Chez le garçon, les testicules produisent en continu des spermatozoïdes à partir de la puberté, stockés puis libérés lors de l'éjaculation.",
        "La fécondation se produit lorsqu'un spermatozoïde rencontre un ovule dans les voies génitales féminines, généralement dans une trompe utérine. L'œuf ainsi formé se divise puis s'implante dans la paroi de l'utérus, où il se développe pendant environ neuf mois de grossesse avant la naissance. Ce processus nécessite une bonne connaissance du corps pour permettre des choix éclairés en matière de contraception et de santé reproductive.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que la puberté ?", "choix": ["La période de transformations physiques et hormonales entre enfance et adolescence", "Une maladie", "La naissance d'un enfant", "Un phénomène qui ne concerne que les adultes"], "reponse": 0, "explication": "La puberté marque le passage de l'enfance à l'adolescence par des transformations physiques et hormonales."},
        {"id": "q2", "enonce": "Qu'est-ce qui déclenche la puberté ?", "choix": ["Le cœur", "Le cerveau, qui stimule la production d'hormones", "Les poumons", "Aucun organe en particulier"], "reponse": 1, "explication": "Le cerveau déclenche la puberté en stimulant la production d'hormones sexuelles."},
        {"id": "q3", "enonce": "Quelle hormone produisent les testicules chez le garçon ?", "choix": ["Les œstrogènes", "La testostérone", "La progestérone", "L'insuline"], "reponse": 1, "explication": "Les testicules produisent la testostérone, hormone sexuelle masculine."},
        {"id": "q4", "enonce": "Quelles hormones produisent les ovaires chez la fille ?", "choix": ["La testostérone uniquement", "Les œstrogènes et la progestérone", "L'insuline", "Aucune hormone"], "reponse": 1, "explication": "Les ovaires produisent les œstrogènes et la progestérone."},
        {"id": "q5", "enonce": "Que se passe-t-il si l'ovule libéré n'est pas fécondé ?", "choix": ["Les règles surviennent environ 14 jours plus tard", "Rien ne se passe", "Une grossesse commence quand même", "L'ovaire cesse de fonctionner"], "reponse": 0, "explication": "Si l'ovule n'est pas fécondé, les règles surviennent environ 14 jours plus tard."},
        {"id": "q6", "enonce": "Que produisent en continu les testicules à partir de la puberté ?", "choix": ["Des ovules", "Des spermatozoïdes", "De la progestérone", "Rien de particulier"], "reponse": 1, "explication": "Les testicules produisent en continu des spermatozoïdes à partir de la puberté."},
        {"id": "q7", "enonce": "Où se produit généralement la fécondation chez l'être humain ?", "choix": ["Dans une trompe utérine", "Dans l'estomac", "Dans les poumons", "Dans le cerveau"], "reponse": 0, "explication": "La fécondation se produit généralement dans une trompe utérine."},
        {"id": "q8", "enonce": "Où s'implante l'œuf après la fécondation ?", "choix": ["Dans la paroi de l'utérus", "Dans l'estomac", "Dans les ovaires", "Dans les poumons"], "reponse": 0, "explication": "L'œuf se divise puis s'implante dans la paroi de l'utérus."},
        {"id": "q9", "enonce": "Combien de temps dure environ une grossesse humaine ?", "choix": ["Environ un mois", "Environ neuf mois", "Environ deux ans", "Environ une semaine"], "reponse": 1, "explication": "Une grossesse humaine dure environ neuf mois."},
        {"id": "q10", "enonce": "Pourquoi est-il important de bien connaître son corps à la puberté ?", "choix": ["Ce n'est pas important", "Pour permettre des choix éclairés en matière de contraception et de santé", "Uniquement pour le sport", "Uniquement pour l'alimentation"], "reponse": 1, "explication": "Une bonne connaissance du corps permet des choix éclairés en matière de contraception et de santé reproductive."},
    ],
})

L.append({
    "slug": "systeme-immunitaire-microbes-4e", "titre": "Le système immunitaire et les microbes pathogènes",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre comment le corps se défend contre les microbes pathogènes grâce au système immunitaire.",
    "objectifs": ["Distinguer les différents types de microbes pathogènes", "Comprendre les mécanismes de défense de l'organisme", "Comprendre le principe de la vaccination"],
    "contenu": [
        "Certains microbes, appelés pathogènes, peuvent provoquer des maladies infectieuses en pénétrant dans l'organisme : les bactéries, organismes unicellulaires qui peuvent se multiplier rapidement dans le corps, et les virus, particules encore plus petites qui doivent obligatoirement infecter une cellule pour se reproduire, sont les deux principaux types de microbes pathogènes.",
        "Face à ces agressions, l'organisme dispose de plusieurs lignes de défense. La peau et les muqueuses forment une première barrière physique. Si un microbe pénètre malgré tout, le système immunitaire réagit : des cellules appelées globules blancs reconnaissent et détruisent les microbes, notamment grâce à la production d'anticorps, des protéines spécifiques capables de neutraliser un microbe précis.",
        "La vaccination consiste à présenter à l'organisme une forme inoffensive d'un microbe ou de l'un de ses composants, ce qui déclenche une réponse immunitaire sans provoquer la maladie. Le système immunitaire garde en mémoire cette rencontre : en cas d'infection réelle par ce même microbe, il réagit beaucoup plus rapidement et efficacement, empêchant généralement le développement de la maladie.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"80\" cy=\"90\" r=\"30\" fill=\"#f5f2e8\" stroke=\"#22303f\"/><circle cx=\"70\" cy=\"80\" r=\"6\" fill=\"#c1552e\"/><circle cx=\"95\" cy=\"95\" r=\"5\" fill=\"#c1552e\"/><text x=\"80\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Globule blanc</text><path d=\"M170 90 L200 70 M170 90 L200 110\" stroke=\"#3b7bd6\" stroke-width=\"3\"/><circle cx=\"220\" cy=\"90\" r=\"10\" fill=\"#e08a2a\"/><text x=\"220\" y=\"130\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Microbe neutralise</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un microbe pathogène ?", "choix": ["Un microbe qui peut provoquer une maladie", "Un microbe toujours inoffensif", "Un type de cellule humaine", "Un anticorps"], "reponse": 0, "explication": "Un microbe pathogène est un microbe capable de provoquer une maladie infectieuse."},
        {"id": "q2", "enonce": "Qu'est-ce qu'une bactérie ?", "choix": ["Un organisme unicellulaire qui peut se multiplier dans le corps", "Une cellule humaine", "Un anticorps", "Un globule blanc"], "reponse": 0, "explication": "Une bactérie est un organisme unicellulaire capable de se multiplier dans l'organisme."},
        {"id": "q3", "enonce": "Qu'est-ce qu'un virus, contrairement à une bactérie ?", "choix": ["Il doit obligatoirement infecter une cellule pour se reproduire", "Il se reproduit tout seul sans cellule", "Il n'existe pas réellement", "Il est toujours inoffensif"], "reponse": 0, "explication": "Un virus doit infecter une cellule hôte pour pouvoir se reproduire, contrairement à une bactérie."},
        {"id": "q4", "enonce": "Quelle est la première ligne de défense de l'organisme ?", "choix": ["Les anticorps", "La peau et les muqueuses", "Le cerveau", "Le cœur"], "reponse": 1, "explication": "La peau et les muqueuses forment une première barrière physique contre les microbes."},
        {"id": "q5", "enonce": "Quelles cellules reconnaissent et détruisent les microbes dans le corps ?", "choix": ["Les globules rouges", "Les globules blancs", "Les cellules musculaires", "Les cellules nerveuses"], "reponse": 1, "explication": "Les globules blancs reconnaissent et détruisent les microbes pathogènes."},
        {"id": "q6", "enonce": "Qu'est-ce qu'un anticorps ?", "choix": ["Un type de microbe", "Une protéine capable de neutraliser un microbe précis", "Un globule rouge", "Un vaccin"], "reponse": 1, "explication": "Un anticorps est une protéine spécifique produite pour neutraliser un microbe précis."},
        {"id": "q7", "enonce": "Que consiste à faire la vaccination ?", "choix": ["Présenter à l'organisme une forme inoffensive d'un microbe", "Détruire tous les microbes du corps", "Empêcher toute réponse immunitaire", "Guérir une maladie déjà déclarée"], "reponse": 0, "explication": "La vaccination présente à l'organisme une forme inoffensive d'un microbe pour déclencher une réponse immunitaire."},
        {"id": "q8", "enonce": "Que fait le système immunitaire après une vaccination ?", "choix": ["Il oublie immédiatement le microbe", "Il garde en mémoire cette rencontre", "Il ne réagit jamais", "Il détruit toutes les cellules du corps"], "reponse": 1, "explication": "Le système immunitaire garde en mémoire la rencontre avec le microbe présenté par le vaccin."},
        {"id": "q9", "enonce": "Pourquoi une personne vaccinée réagit-elle plus vite face à une infection réelle ?", "choix": ["Grâce à la mémoire immunitaire acquise par la vaccination", "Ce n'est pas le cas", "Car elle ne peut plus être infectée du tout", "Grâce à la chance uniquement"], "reponse": 0, "explication": "La mémoire immunitaire permet une réponse plus rapide et efficace en cas d'infection réelle."},
        {"id": "q10", "enonce": "La vaccination provoque-t-elle la maladie qu'elle prévient ?", "choix": ["Oui, toujours", "Non, elle utilise une forme inoffensive du microbe", "Cela dépend du vaccin uniquement pour les virus", "Oui, systématiquement et gravement"], "reponse": 1, "explication": "La vaccination utilise une forme inoffensive du microbe, sans provoquer la maladie elle-même."},
    ],
})

L.append({
    "slug": "conduites-addictives-risques-4e", "titre": "Les conduites addictives et leurs risques",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre le mécanisme des conduites addictives et leurs conséquences sur la santé.",
    "objectifs": ["Définir ce qu'est une conduite addictive", "Comprendre le mécanisme biologique de l'addiction", "Identifier les conséquences des conduites addictives sur la santé"],
    "contenu": [
        "Une conduite addictive est un comportement de consommation répétée d'une substance (tabac, alcool, drogues) ou une pratique (jeux vidéo, écrans) qui devient difficile à contrôler, malgré la connaissance de ses conséquences négatives sur la santé, les relations sociales ou la vie quotidienne. On distingue les addictions avec substance des addictions comportementales, sans substance.",
        "Sur le plan biologique, de nombreuses substances addictives agissent sur le circuit de récompense du cerveau, une zone qui libère naturellement de la dopamine, une molécule associée au plaisir, lors d'activités bénéfiques comme manger ou se sentir en sécurité. Ces substances stimulent artificiellement et de façon excessive ce circuit, ce qui pousse à répéter la consommation pour retrouver cette sensation, malgré une accoutumance qui nécessite des doses toujours plus importantes.",
        "Les conduites addictives ont des conséquences graves sur la santé : le tabac endommage les poumons et augmente fortement le risque de cancers et de maladies cardio-vasculaires ; l'alcool abîme le foie et le système nerveux ; certaines drogues provoquent des troubles psychiques durables. Elles ont aussi des conséquences sociales, comme l'isolement ou des difficultés scolaires et professionnelles, ce qui rend la prévention particulièrement importante, surtout à l'adolescence.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'une conduite addictive ?", "choix": ["Un comportement de consommation devenu difficile à contrôler", "Une activité toujours bénéfique", "Une maladie génétique uniquement", "Un sport"], "reponse": 0, "explication": "Une conduite addictive est un comportement de consommation répétée devenu difficile à contrôler."},
        {"id": "q2", "enonce": "Une addiction concerne-t-elle uniquement des substances ?", "choix": ["Oui, uniquement", "Non, il existe aussi des addictions comportementales sans substance", "Non, uniquement des comportements", "Les addictions n'existent pas"], "reponse": 1, "explication": "On distingue les addictions avec substance des addictions comportementales, comme les jeux vidéo ou les écrans."},
        {"id": "q3", "enonce": "Sur quelle zone du cerveau agissent de nombreuses substances addictives ?", "choix": ["Le circuit de récompense", "Le système digestif", "Les poumons", "Le système osseux"], "reponse": 0, "explication": "Ces substances agissent sur le circuit de récompense du cerveau, lié au plaisir."},
        {"id": "q4", "enonce": "Quelle molécule est associée au plaisir dans le cerveau ?", "choix": ["La dopamine", "L'insuline", "L'oxygène", "Le glucose"], "reponse": 0, "explication": "La dopamine est la molécule associée au plaisir libérée par le circuit de récompense."},
        {"id": "q5", "enonce": "Qu'est-ce que l'accoutumance ?", "choix": ["Le besoin de doses toujours plus importantes pour ressentir le même effet", "L'absence totale d'effet d'une substance", "Une guérison rapide", "Un effet immédiat sans conséquence"], "reponse": 0, "explication": "L'accoutumance est le besoin de doses toujours plus importantes pour retrouver le même effet."},
        {"id": "q6", "enonce": "Quel organe le tabac endommage-t-il particulièrement ?", "choix": ["Les poumons", "Les yeux", "Les oreilles", "Les cheveux"], "reponse": 0, "explication": "Le tabac endommage particulièrement les poumons et augmente le risque de cancers."},
        {"id": "q7", "enonce": "Quel organe l'alcool abîme-t-il particulièrement ?", "choix": ["Le foie et le système nerveux", "Les cheveux", "Les ongles", "Les dents uniquement"], "reponse": 0, "explication": "L'alcool abîme particulièrement le foie et le système nerveux."},
        {"id": "q8", "enonce": "Les conduites addictives ont-elles des conséquences sociales ?", "choix": ["Non, uniquement physiques", "Oui, comme l'isolement ou des difficultés scolaires", "Elles n'ont aucune conséquence", "Uniquement des conséquences positives"], "reponse": 1, "explication": "Les conduites addictives ont aussi des conséquences sociales, comme l'isolement ou des difficultés scolaires."},
        {"id": "q9", "enonce": "Pourquoi la prévention est-elle particulièrement importante à l'adolescence ?", "choix": ["Elle n'a aucune importance", "Car le cerveau adolescent est plus vulnérable", "Uniquement pour des raisons financières", "Les adolescents ne sont jamais concernés"], "reponse": 1, "explication": "Le cerveau adolescent, encore en développement, est particulièrement vulnérable aux effets des substances addictives."},
        {"id": "q10", "enonce": "Une personne consciente des risques peut-elle malgré tout développer une addiction ?", "choix": ["Non, jamais", "Oui, l'addiction devient difficile à contrôler malgré cette connaissance", "Uniquement si elle le souhaite", "Cela n'a aucun lien"], "reponse": 1, "explication": "Une conduite addictive devient difficile à contrôler même en connaissant ses conséquences négatives."},
    ],
})

L.append({
    "slug": "ressources-naturelles-gestion-environnement-4e", "titre": "Les ressources naturelles et la gestion de l'environnement",
    "matiere": "svt", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre les enjeux liés à l'exploitation des ressources naturelles et à leur gestion durable.",
    "objectifs": ["Distinguer ressources renouvelables et non renouvelables", "Comprendre les impacts de la surexploitation des ressources", "Connaître des pistes de gestion durable des ressources"],
    "contenu": [
        "Les ressources naturelles sont des éléments prélevés dans la nature et utilisés par les êtres humains : eau, bois, minerais, pétrole, poissons. On distingue les ressources renouvelables, qui se régénèrent naturellement à une vitesse comparable à leur utilisation (eau, bois si la forêt est bien gérée, énergie solaire), des ressources non renouvelables, qui existent en quantité limitée et ne se régénèrent pas à l'échelle humaine (pétrole, charbon, minerais).",
        "La surexploitation d'une ressource, même renouvelable, peut compromettre sa capacité de régénération : une forêt coupée plus vite qu'elle ne repousse finit par disparaître, tout comme une espèce de poisson pêchée plus vite qu'elle ne se reproduit peut s'effondrer. Cette surexploitation a des conséquences sur les écosystèmes entiers et sur les activités humaines qui en dépendent.",
        "Pour une gestion plus durable des ressources, plusieurs pistes existent : limiter les prélèvements à un niveau qui permet le renouvellement naturel de la ressource, développer le recyclage et l'économie circulaire pour limiter l'extraction de nouvelles matières premières, et protéger certains espaces naturels particulièrement riches, comme les réserves naturelles, où l'exploitation est réglementée ou interdite.",
    ],
    "illustration": "<svg viewBox=\"0 0 320 190\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"sans-serif\"><circle cx=\"80\" cy=\"90\" r=\"35\" fill=\"#3ba55d\"/><text x=\"80\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Renouvelable</text><path d=\"M60 70 A 20 20 0 1 1 59 70\" fill=\"none\" stroke=\"#fff\" stroke-width=\"3\"/><rect x=\"200\" y=\"55\" width=\"70\" height=\"70\" fill=\"#7a5230\"/><text x=\"235\" y=\"140\" text-anchor=\"middle\" font-size=\"9\" fill=\"#22303f\">Non renouvelable</text></svg>",
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'une ressource naturelle ?", "choix": ["Un élément prélevé dans la nature et utilisé par les humains", "Un objet fabriqué en usine", "Une invention technique", "Un phénomène météorologique uniquement"], "reponse": 0, "explication": "Une ressource naturelle est un élément prélevé dans la nature et utilisé par les êtres humains."},
        {"id": "q2", "enonce": "Qu'est-ce qu'une ressource renouvelable ?", "choix": ["Une ressource qui se régénère naturellement à une vitesse comparable à son usage", "Une ressource qui n'existe jamais en grande quantité", "Une ressource qui disparaît immédiatement", "Une ressource fabriquée par l'homme uniquement"], "reponse": 0, "explication": "Une ressource renouvelable se régénère à une vitesse comparable à son utilisation."},
        {"id": "q3", "enonce": "Citez un exemple de ressource non renouvelable.", "choix": ["Le pétrole", "L'eau de pluie", "Le bois si la forêt est bien gérée", "L'énergie solaire"], "reponse": 0, "explication": "Le pétrole est une ressource non renouvelable, disponible en quantité limitée."},
        {"id": "q4", "enonce": "Citez un exemple de ressource renouvelable.", "choix": ["Le charbon", "L'énergie solaire", "Le pétrole", "Les minerais"], "reponse": 1, "explication": "L'énergie solaire est une ressource renouvelable, disponible en continu."},
        {"id": "q5", "enonce": "Qu'est-ce que la surexploitation d'une ressource ?", "choix": ["Un prélèvement supérieur à sa capacité de régénération", "Un prélèvement nul", "Une protection totale de la ressource", "Un recyclage complet"], "reponse": 0, "explication": "La surexploitation consiste à prélever une ressource plus vite qu'elle ne peut se régénérer."},
        {"id": "q6", "enonce": "Une forêt peut-elle disparaître même si elle est renouvelable ?", "choix": ["Non, jamais", "Oui, si elle est coupée plus vite qu'elle ne repousse", "Uniquement en cas d'incendie", "Elle ne peut jamais être coupée"], "reponse": 1, "explication": "Une forêt renouvelable peut disparaître si elle est surexploitée, coupée plus vite qu'elle ne repousse."},
        {"id": "q7", "enonce": "Qu'est-ce que l'économie circulaire ?", "choix": ["Un modèle qui favorise le recyclage et limite l'extraction de nouvelles ressources", "Un modèle qui gaspille les ressources", "Un modèle sans aucun recyclage", "Une monnaie particulière"], "reponse": 0, "explication": "L'économie circulaire favorise le recyclage pour limiter l'extraction de nouvelles matières premières."},
        {"id": "q8", "enonce": "Qu'est-ce qu'une réserve naturelle ?", "choix": ["Un espace où l'exploitation est réglementée ou interdite", "Une zone entièrement industrielle", "Un espace sans aucune faune", "Une zone urbaine dense"], "reponse": 0, "explication": "Une réserve naturelle est un espace protégé où l'exploitation est réglementée ou interdite."},
        {"id": "q9", "enonce": "La surpêche peut-elle affecter une espèce de poisson ?", "choix": ["Non, jamais", "Oui, si elle est pêchée plus vite qu'elle ne se reproduit", "Elle augmente toujours la population de poissons", "Elle n'a aucun lien avec la reproduction"], "reponse": 1, "explication": "La surpêche peut compromettre la reproduction d'une espèce et provoquer son effondrement."},
        {"id": "q10", "enonce": "Quelle piste permet de limiter l'extraction de nouvelles matières premières ?", "choix": ["Le recyclage", "L'augmentation de la consommation", "L'arrêt total de toute activité humaine", "Le gaspillage"], "reponse": 0, "explication": "Le recyclage permet de limiter l'extraction de nouvelles matières premières."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "activite-interne-globe", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecons SVT 4e ajoutees.")
