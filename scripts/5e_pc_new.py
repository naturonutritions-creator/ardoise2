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

svg_molecules = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="10" y="40" width="90" height="120" fill="#e7e9ec"/><text x="55" y="175" text-anchor="middle" font-size="9" fill="#22303f">Solide</text>
<g fill="#3b7bd6">
<circle cx="30" cy="55" r="5"/><circle cx="50" cy="55" r="5"/><circle cx="70" cy="55" r="5"/><circle cx="30" cy="75" r="5"/><circle cx="50" cy="75" r="5"/><circle cx="70" cy="75" r="5"/>
<circle cx="30" cy="95" r="5"/><circle cx="50" cy="95" r="5"/><circle cx="70" cy="95" r="5"/></g>
<rect x="115" y="40" width="90" height="120" fill="#cfe3fb"/><text x="160" y="175" text-anchor="middle" font-size="9" fill="#22303f">Liquide</text>
<g fill="#3b7bd6"><circle cx="135" cy="70" r="5"/><circle cx="160" cy="60" r="5"/><circle cx="180" cy="85" r="5"/><circle cx="140" cy="110" r="5"/><circle cx="175" cy="120" r="5"/></g>
<rect x="220" y="40" width="90" height="120" fill="#fbe4c4"/><text x="265" y="175" text-anchor="middle" font-size="9" fill="#22303f">Gaz</text>
<g fill="#e08a2a"><circle cx="235" cy="55" r="5"/><circle cx="290" cy="150" r="5"/><circle cx="260" cy="100" r="5"/><circle cx="300" cy="65" r="5"/><circle cx="240" cy="130" r="5"/></g>
</svg>'''

svg_corps_purs = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="30" y="30" width="20" height="140" fill="#e7e9ec"/>
<line x1="10" y1="60" x2="50" y2="60" stroke="#5b6470" stroke-width="2"/><text x="0" y="55" font-size="9" fill="#22303f">100°C</text>
<line x1="10" y1="140" x2="50" y2="140" stroke="#5b6470" stroke-width="2"/><text x="0" y="135" font-size="9" fill="#22303f">0°C</text>
<text x="40" y="185" text-anchor="middle" font-size="9" fill="#22303f">Eau pure</text>
<rect x="220" y="30" width="20" height="140" fill="#fbe4c4"/>
<line x1="200" y1="50" x2="260" y2="50" stroke="#d1495b" stroke-width="2" stroke-dasharray="3 3"/>
<line x1="200" y1="150" x2="260" y2="150" stroke="#d1495b" stroke-width="2" stroke-dasharray="3 3"/>
<text x="230" y="185" text-anchor="middle" font-size="9" fill="#22303f">Mélange (plage variable)</text>
</svg>'''

svg_transfo_chimique = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M60 60 L60 140 Q60 160 90 160 Q120 160 120 140 L120 60 Z" fill="#cfe3fb" stroke="#3b7bd6" stroke-width="3"/>
<circle cx="80" cy="120" r="5" fill="#fff"/><circle cx="100" cy="100" r="4" fill="#fff"/><circle cx="90" cy="140" r="6" fill="#fff"/>
<path d="M200 60 L200 140 Q200 160 230 160 Q260 160 260 140 L260 60 Z" fill="#f3c9ce" stroke="#d1495b" stroke-width="3"/>
<circle cx="220" cy="115" r="4" fill="#fff"/><circle cx="240" cy="90" r="5" fill="#fff"/><circle cx="230" cy="70" r="4" fill="#fff"/>
<path d="M130 100 H190" stroke="#5b6470" stroke-width="2" marker-end="url(#g1)"/>
<text x="160" y="30" text-anchor="middle" font-size="9" fill="#22303f">Réactifs → Produits (transformation chimique)</text>
<defs><marker id="g1" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

svg_mouvement5 = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<line x1="20" y1="70" x2="300" y2="70" stroke="#5b6470" stroke-width="2"/>
<g fill="#3b7bd6"><circle cx="30" cy="70" r="5"/><circle cx="70" cy="70" r="5"/><circle cx="110" cy="70" r="5"/><circle cx="150" cy="70" r="5"/><circle cx="190" cy="70" r="5"/></g>
<text x="110" y="55" text-anchor="middle" font-size="9" fill="#22303f">Vitesse constante</text>
<line x1="20" y1="140" x2="300" y2="140" stroke="#5b6470" stroke-width="2"/>
<g fill="#e08a2a"><circle cx="30" cy="140" r="5"/><circle cx="50" cy="140" r="5"/><circle cx="80" cy="140" r="5"/><circle cx="130" cy="140" r="5"/><circle cx="200" cy="140" r="5"/></g>
<text x="150" y="165" text-anchor="middle" font-size="9" fill="#22303f">Vitesse variable (accélération)</text>
</svg>'''

svg_forces = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="130" y="70" width="60" height="40" fill="#5b6470"/>
<path d="M160 110 V170" stroke="#d1495b" stroke-width="4" marker-end="url(#g2)"/>
<text x="200" y="150" font-size="10" fill="#22303f">Poids (force vers le bas)</text>
<rect x="30" y="150" width="40" height="10" fill="#3b7bd6"/><text x="50" y="180" text-anchor="middle" font-size="8" fill="#22303f">Balance (masse)</text>
<line x1="250" y1="30" x2="250" y2="80" stroke="#2f9e6f" stroke-width="3"/><rect x="240" y="80" width="20" height="15" fill="#2f9e6f"/><text x="250" y="105" text-anchor="middle" font-size="8" fill="#22303f">Dynamomètre (poids)</text>
<defs><marker id="g2" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#d1495b"/></marker></defs>
</svg>'''

svg_energie_conv = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="40" cy="50" r="20" fill="#f2c94c"/><text x="40" y="90" text-anchor="middle" font-size="9" fill="#22303f">Lumineuse</text>
<path d="M62 55 H105" stroke="#5b6470" stroke-width="2" marker-end="url(#g3)"/>
<rect x="105" y="30" width="50" height="50" fill="#3b7bd6"/><text x="130" y="95" text-anchor="middle" font-size="9" fill="#22303f">Électrique</text>
<path d="M157 55 H200" stroke="#5b6470" stroke-width="2" marker-end="url(#g3)"/>
<circle cx="230" cy="55" r="25" fill="#2f9e6f"/><text x="230" y="95" text-anchor="middle" font-size="9" fill="#22303f">Cinétique</text>
<text x="270" y="140" font-size="9" fill="#22303f">+ chaleur perdue</text>
<defs><marker id="g3" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

svg_oeil = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<ellipse cx="160" cy="95" rx="130" ry="70" fill="#cfe3fb" stroke="#3b7bd6" stroke-width="2"/>
<circle cx="70" cy="95" r="25" fill="#22303f"/><circle cx="70" cy="95" r="10" fill="#fff"/>
<ellipse cx="270" cy="95" rx="15" ry="35" fill="#d1495b"/>
<text x="70" y="140" text-anchor="middle" font-size="9" fill="#22303f">Pupille / cristallin</text>
<text x="270" y="140" text-anchor="middle" font-size="9" fill="#22303f">Rétine</text>
<path d="M10 95 H55" stroke="#f2c94c" stroke-width="2" marker-end="url(#g4)"/>
<defs><marker id="g4" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#f2c94c"/></marker></defs>
</svg>'''

lessons_out = []

lessons_out.append(lesson_block(
    "etats-matiere-constitution-5e", "Les états de la matière et leur constitution", "physique-chimie", "5e", "20 min",
    "Découvrir que la matière est constituée de molécules et comprendre l'organisation de ces molécules selon l'état physique.",
    ["Comprendre que la matière est constituée de molécules", "Décrire l'organisation des molécules dans les trois états", "Relier changement d'état et agitation des molécules"],
    [
        "Toute matière est constituée de molécules, des particules extrêmement petites, invisibles même au meilleur microscope optique. Les molécules sont elles-mêmes constituées d'atomes, les plus petites particules de matière, assemblés entre eux selon un modèle précis propre à chaque substance : par exemple, une molécule d'eau est constituée de deux atomes d'hydrogène et un atome d'oxygène.",
        "L'état physique d'une matière (solide, liquide ou gazeux) dépend de la façon dont ses molécules sont organisées et de leur agitation. Dans un solide, les molécules sont serrées et rangées de façon ordonnée, avec très peu de mouvement : la matière garde une forme fixe. Dans un liquide, les molécules restent proches mais peuvent glisser les unes sur les autres. Dans un gaz, les molécules sont très éloignées les unes des autres et se déplacent librement à grande vitesse : le gaz occupe tout l'espace disponible.",
        "Un changement d'état correspond à une modification de l'organisation et de l'agitation des molécules, provoquée par un changement de température : chauffer une matière augmente l'agitation de ses molécules (fusion, vaporisation), la refroidir la diminue (solidification, condensation). Le nombre de molécules et leur nature ne changent pas lors d'un changement d'état : seule leur organisation est modifiée."
    ],
    svg_molecules, "quiz-etats-matiere-constitution-5e", "Quiz — Les états de la matière et leur constitution",
    [
        q("q1", "De quoi toute matière est-elle constituée ?", ["De vide uniquement", "De molécules", "De lumière", "De rien de particulier"], 1, "Toute matière est constituée de molécules, des particules extrêmement petites."),
        q("q2", "De quoi une molécule est-elle elle-même constituée ?", ["D'atomes", "De cellules", "De lumière", "De rien"], 0, "Une molécule est constituée d'atomes assemblés selon un modèle précis."),
        q("q3", "Comment sont organisées les molécules dans un solide ?", ["Très éloignées et libres", "Serrées et rangées de façon ordonnée", "Elles n'existent pas dans un solide", "Aléatoirement dispersées dans tout l'espace"], 1, "Dans un solide, les molécules sont serrées et organisées de façon ordonnée, avec peu de mouvement."),
        q("q4", "Comment sont organisées les molécules dans un gaz ?", ["Serrées et immobiles", "Très éloignées les unes des autres, en mouvement libre", "Elles n'existent pas dans un gaz", "Organisées en rangées fixes"], 1, "Dans un gaz, les molécules sont très éloignées et se déplacent librement à grande vitesse."),
        q("q5", "Qu'est-ce qui provoque un changement d'état ?", ["Un changement de couleur", "Un changement de température qui modifie l'agitation des molécules", "Le hasard", "Un changement d'odeur"], 1, "Un changement de température modifie l'agitation des molécules et provoque un changement d'état."),
        q("q6", "Le nombre de molécules change-t-il lors d'un changement d'état ?", ["Oui, il change beaucoup", "Non, seule leur organisation est modifiée", "Oui, elles disparaissent", "Cela dépend de la substance"], 1, "Lors d'un changement d'état, le nombre de molécules ne change pas : seule leur organisation est modifiée."),
        q("q7", "Que se passe-t-il pour l'agitation des molécules quand on chauffe une matière ?", ["Elle diminue", "Elle augmente", "Elle reste identique", "Les molécules disparaissent"], 1, "Chauffer une matière augmente l'agitation de ses molécules."),
        q("q8", "Combien d'atomes composent une molécule d'eau ?", ["Un seul atome", "Deux atomes d'hydrogène et un atome d'oxygène", "Trois atomes d'oxygène", "Aucun atome"], 1, "Une molécule d'eau est constituée de deux atomes d'hydrogène et un atome d'oxygène."),
        q("q9", "Dans quel état les molécules peuvent-elles glisser les unes sur les autres tout en restant proches ?", ["Solide", "Liquide", "Gazeux", "Aucun état"], 1, "Dans un liquide, les molécules restent proches mais peuvent glisser les unes sur les autres."),
        q("q10", "Refroidir une matière augmente-t-il ou diminue-t-il l'agitation de ses molécules ?", ["Elle l'augmente", "Elle la diminue", "Cela n'a aucun effet", "Les molécules s'arrêtent complètement toujours"], 1, "Refroidir une matière diminue l'agitation de ses molécules."),
    ]
))

lessons_out.append(lesson_block(
    "melanges-corps-purs-5e", "Mélanges et corps purs", "physique-chimie", "5e", "20 min",
    "Distinguer un corps pur d'un mélange, et savoir identifier une eau pure grâce à sa température de changement d'état.",
    ["Définir un corps pur et un mélange", "Identifier un corps pur grâce à sa température de changement d'état", "Comprendre la notion de concentration dans une solution"],
    [
        "Un corps pur est une substance constituée d'un seul type de molécule (l'eau distillée, le dioxygène pur, le sel pur). Un mélange, à l'inverse, est constitué de plusieurs corps purs différents : l'eau du robinet, qui contient de l'eau et divers minéraux dissous, ou l'air, qui est un mélange de plusieurs gaz.",
        "On peut identifier un corps pur grâce à ses températures de changement d'état, qui sont fixes et caractéristiques : l'eau pure fond à 0°C et bout à 100°C sous une pression normale, quelle que soit la quantité d'eau. Un mélange, en revanche, n'a pas de température de changement d'état unique et fixe : elle varie selon les proportions du mélange.",
        "Dans une solution (mélange homogène d'un solide dissous dans un liquide), la concentration indique la quantité de soluté dissoute dans un volume donné de solution : plus on ajoute de sel dans un même volume d'eau, plus la concentration en sel augmente, jusqu'à atteindre la saturation, où plus aucun sel supplémentaire ne peut se dissoudre."
    ],
    svg_corps_purs, "quiz-melanges-corps-purs-5e", "Quiz — Mélanges et corps purs",
    [
        q("q1", "Qu'est-ce qu'un corps pur ?", ["Une substance constituée d'un seul type de molécule", "Un mélange de plusieurs substances", "De l'eau du robinet", "De l'air"], 0, "Un corps pur est une substance constituée d'un seul type de molécule."),
        q("q2", "L'eau du robinet est-elle un corps pur ?", ["Oui, toujours", "Non, c'est un mélange (eau et minéraux dissous)", "Oui, car elle est transparente", "Cela dépend de sa couleur"], 1, "L'eau du robinet contient des minéraux dissous : c'est un mélange, pas un corps pur."),
        q("q3", "À quelle température l'eau pure fond-elle sous une pression normale ?", ["100°C", "0°C", "50°C", "-10°C"], 1, "L'eau pure fond à 0°C sous une pression normale."),
        q("q4", "À quelle température l'eau pure bout-elle sous une pression normale ?", ["0°C", "50°C", "100°C", "200°C"], 2, "L'eau pure bout à 100°C sous une pression normale."),
        q("q5", "Un mélange a-t-il une température de changement d'état fixe comme un corps pur ?", ["Oui, toujours identique", "Non, elle varie selon les proportions du mélange", "Un mélange ne change jamais d'état", "Cela dépend uniquement de sa couleur"], 1, "Un mélange n'a pas de température de changement d'état fixe : elle varie selon ses proportions."),
        q("q6", "Comment identifier un corps pur en laboratoire ?", ["Par sa couleur uniquement", "Grâce à ses températures de changement d'état, fixes et caractéristiques", "Impossible de l'identifier", "Par son odeur uniquement"], 1, "Les températures de changement d'état, fixes pour un corps pur, permettent de l'identifier."),
        q("q7", "Qu'indique la concentration d'une solution ?", ["La couleur de la solution", "La quantité de soluté dissoute dans un volume donné de solution", "La température de la solution", "Le poids du récipient"], 1, "La concentration indique la quantité de soluté dissoute dans un volume donné de solution."),
        q("q8", "Que se passe-t-il quand une solution atteint la saturation ?", ["Elle peut encore dissoudre du soluté à l'infini", "Plus aucun soluté supplémentaire ne peut se dissoudre", "Elle devient un corps pur", "Elle change de couleur automatiquement"], 1, "À saturation, la solution ne peut plus dissoudre de soluté supplémentaire."),
        q("q9", "L'air est-il un corps pur ou un mélange ?", ["Un corps pur", "Un mélange de plusieurs gaz", "Ni l'un ni l'autre", "Un solide"], 1, "L'air est un mélange homogène de plusieurs gaz (azote, oxygène...)."),
        q("q10", "Le dioxygène pur est-il un exemple de corps pur ?", ["Non, c'est un mélange", "Oui, il est constitué d'un seul type de molécule", "Ce n'est pas une substance chimique", "Il n'existe pas à l'état pur"], 1, "Le dioxygène pur est un exemple de corps pur, constitué d'un seul type de molécule."),
    ]
))

lessons_out.append(lesson_block(
    "transformations-chimiques-5e", "Identifier une transformation chimique", "physique-chimie", "5e", "20 min",
    "Distinguer une transformation physique d'une transformation chimique, et reconnaître les signes d'une réaction chimique.",
    ["Distinguer transformation physique et transformation chimique", "Identifier les signes visibles d'une transformation chimique", "Citer des exemples de transformations chimiques du quotidien"],
    [
        "Une transformation physique change l'état ou la forme d'une matière sans changer sa nature : faire fondre de la glace, casser un morceau de craie, ou dissoudre du sel dans l'eau sont des transformations physiques, car la substance de départ existe toujours et peut souvent être récupérée.",
        "Une transformation chimique, en revanche, transforme une ou plusieurs substances de départ (les réactifs) en une ou plusieurs substances différentes (les produits), avec des propriétés nouvelles : la combustion du bois transforme le bois et le dioxygène en cendres, fumée et dioxyde de carbone ; la rouille transforme le fer et le dioxygène en oxyde de fer. Ces nouvelles substances ne peuvent pas redevenir facilement les substances de départ.",
        "Plusieurs signes permettent souvent de repérer une transformation chimique : un changement de couleur, un dégagement de gaz (bulles), la formation d'un solide qui n'était pas présent avant (précipité), un dégagement de chaleur ou de lumière (comme une flamme). Ces observations aident à distinguer une transformation chimique d'une simple transformation physique."
    ],
    svg_transfo_chimique, "quiz-transformations-chimiques-5e", "Quiz — Identifier une transformation chimique",
    [
        q("q1", "Faire fondre de la glace est-il une transformation physique ou chimique ?", ["Physique", "Chimique", "Ni l'une ni l'autre", "Les deux à la fois"], 0, "Faire fondre de la glace change l'état sans changer la nature de la substance : c'est une transformation physique."),
        q("q2", "Comment appelle-t-on les substances de départ d'une transformation chimique ?", ["Les produits", "Les réactifs", "Les solutés", "Les solvants"], 1, "Les substances de départ d'une transformation chimique s'appellent les réactifs."),
        q("q3", "Comment appelle-t-on les nouvelles substances formées lors d'une transformation chimique ?", ["Les réactifs", "Les produits", "Les corps purs uniquement", "Les mélanges uniquement"], 1, "Les nouvelles substances formées s'appellent les produits de la transformation chimique."),
        q("q4", "La combustion du bois est-elle une transformation chimique ?", ["Non, c'est une transformation physique", "Oui, elle forme de nouvelles substances (cendres, fumée, CO₂)", "Ce n'est pas une transformation", "Le bois ne change jamais"], 1, "La combustion transforme le bois et le dioxygène en nouvelles substances : c'est une transformation chimique."),
        q("q5", "La rouille du fer est-elle une transformation chimique ?", ["Non, c'est réversible facilement", "Oui, elle forme de l'oxyde de fer à partir du fer et du dioxygène", "Le fer ne rouille jamais", "C'est une transformation physique"], 1, "La rouille est une transformation chimique qui forme de l'oxyde de fer à partir du fer et du dioxygène."),
        q("q6", "Citez un signe qui peut indiquer une transformation chimique.", ["Un simple changement de forme", "Un dégagement de gaz (bulles)", "Un changement de température ambiante sans lien", "Rien de visible n'indique une transformation chimique"], 1, "Un dégagement de gaz (bulles) peut indiquer une transformation chimique en cours."),
        q("q7", "Qu'est-ce qu'un précipité ?", ["Un liquide qui s'évapore", "Un solide qui se forme dans un liquide lors d'une réaction chimique", "Un gaz uniquement", "Une simple coloration"], 1, "Un précipité est un solide qui se forme dans un liquide lors d'une transformation chimique."),
        q("q8", "Dissoudre du sel dans l'eau est-il une transformation chimique ?", ["Oui, le sel change de nature", "Non, c'est une transformation physique, le sel reste du sel", "Cela dépend de la température", "Le sel disparaît définitivement"], 1, "Dissoudre du sel est une transformation physique : le sel garde sa nature et peut être récupéré par évaporation."),
        q("q9", "Les substances produites par une transformation chimique peuvent-elles facilement redevenir les substances de départ ?", ["Oui, très facilement", "Non, ce n'est pas facile, contrairement à une transformation physique", "Toujours instantanément", "Cela n'a aucune importance"], 1, "Contrairement à une transformation physique, les produits d'une transformation chimique ne redeviennent pas facilement les réactifs de départ."),
        q("q10", "Un dégagement de chaleur ou de lumière peut-il signaler une transformation chimique ?", ["Non, jamais", "Oui, comme dans le cas d'une flamme", "Uniquement pour les liquides", "Cela n'a aucun rapport"], 1, "Un dégagement de chaleur ou de lumière (comme une flamme) est un signe possible de transformation chimique."),
    ]
))

lessons_out.append(lesson_block(
    "mouvement-caracteriser-5e", "Caractériser un mouvement", "physique-chimie", "5e", "20 min",
    "Approfondir la description d'un mouvement : trajectoire, vitesse constante ou variable, et vitesse instantanée.",
    ["Distinguer mouvement à vitesse constante et mouvement à vitesse variable", "Interpréter une trajectoire à partir de positions successives à intervalles réguliers", "Calculer une vitesse à partir de mesures de distance et de durée"],
    [
        "Un mouvement est dit uniforme, ou à vitesse constante, lorsque l'objet parcourt des distances égales pendant des durées égales : sur un enregistrement de ses positions successives à intervalles de temps réguliers, les points sont alors régulièrement espacés. Un mouvement est dit varié lorsque la vitesse change au cours du temps : les points sont alors inégalement espacés, plus resserrés quand l'objet ralentit, plus espacés quand il accélère.",
        "On appelle vitesse moyenne le rapport entre la distance totale parcourue et la durée totale du parcours (vitesse = distance ÷ durée). Elle ne renseigne pas sur les variations de vitesse au cours du trajet : un objet peut avoir une vitesse moyenne de 50 km/h tout en ayant roulé plus vite à certains moments et plus lentement à d'autres.",
        "Pour étudier un mouvement plus précisément, on peut mesurer des vitesses sur de courts intervalles de temps (vitesses instantanées), qui donnent une idée plus fine de la façon dont l'objet accélère, ralentit, ou se déplace à vitesse constante à un instant donné. Ces mesures sont utilisées par exemple en sécurité routière pour étudier le freinage d'un véhicule."
    ],
    svg_mouvement5, "quiz-mouvement-caracteriser-5e", "Quiz — Caractériser un mouvement",
    [
        q("q1", "Qu'est-ce qu'un mouvement uniforme ?", ["Un mouvement à vitesse variable", "Un mouvement à vitesse constante", "Un objet immobile", "Un mouvement circulaire uniquement"], 1, "Un mouvement uniforme se fait à vitesse constante : distances égales en durées égales."),
        q("q2", "Sur un enregistrement à intervalles réguliers, comment reconnaît-on un mouvement uniforme ?", ["Les points sont régulièrement espacés", "Les points sont très resserrés puis très espacés", "Il n'y a qu'un seul point", "Les points changent de couleur"], 0, "Dans un mouvement uniforme, les points enregistrés à intervalles réguliers sont régulièrement espacés."),
        q("q3", "Que signifie un resserrement des points enregistrés sur une trajectoire ?", ["L'objet accélère", "L'objet ralentit", "L'objet est à vitesse constante", "Rien de particulier"], 1, "Un resserrement des points indique que l'objet parcourt moins de distance par intervalle de temps : il ralentit."),
        q("q4", "Comment calcule-t-on la vitesse moyenne d'un objet ?", ["Distance × durée", "Distance ÷ durée", "Durée ÷ distance", "Distance − durée"], 1, "La vitesse moyenne se calcule en divisant la distance parcourue par la durée du parcours."),
        q("q5", "La vitesse moyenne renseigne-t-elle sur les variations de vitesse au cours du trajet ?", ["Oui, précisément", "Non, elle ne renseigne pas sur ces variations", "Elle n'a aucun rapport avec le trajet", "Elle est toujours égale à la vitesse instantanée"], 1, "La vitesse moyenne ne renseigne pas sur les variations de vitesse au cours du trajet."),
        q("q6", "Qu'est-ce qu'une vitesse instantanée ?", ["La vitesse moyenne sur tout le trajet", "Une vitesse mesurée sur un très court intervalle de temps", "Une vitesse qui ne varie jamais", "Une unité de distance"], 1, "La vitesse instantanée est mesurée sur un très court intervalle de temps, donnant une idée précise du mouvement à cet instant."),
        q("q7", "Dans quel domaine utilise-t-on des mesures de vitesses instantanées ?", ["La cuisine", "La sécurité routière (étude du freinage)", "La musique", "La peinture"], 1, "La sécurité routière utilise des mesures de vitesses instantanées pour étudier le freinage d'un véhicule."),
        q("q8", "Un objet à vitesse moyenne de 50 km/h a-t-il forcément roulé à 50 km/h tout le trajet ?", ["Oui, obligatoirement", "Non, il peut avoir varié sa vitesse tout en ayant cette moyenne", "Non, c'est impossible d'avoir une moyenne", "Cela ne concerne que les avions"], 1, "Un objet peut avoir varié sa vitesse au cours du trajet tout en ayant une vitesse moyenne de 50 km/h."),
        q("q9", "Qu'est-ce qu'un mouvement varié ?", ["Un mouvement dont la vitesse change au cours du temps", "Un mouvement toujours à vitesse constante", "Un objet immobile", "Un mouvement qui n'existe pas"], 0, "Un mouvement varié est un mouvement dont la vitesse change au cours du temps."),
        q("q10", "Sur un enregistrement, des points très espacés indiquent-ils une vitesse faible ou élevée ?", ["Une vitesse faible", "Une vitesse élevée", "Un objet immobile", "Rien de particulier"], 1, "Des points très espacés à intervalles de temps réguliers indiquent une grande distance parcourue : une vitesse élevée."),
    ]
))

lessons_out.append(lesson_block(
    "forces-actions-poids-5e", "Modéliser une action : le poids et les forces", "physique-chimie", "5e", "20 min",
    "Comprendre ce qu'est une force, comment elle agit sur un objet, et distinguer poids et masse.",
    ["Définir ce qu'est une force et ses effets possibles", "Distinguer la masse et le poids d'un objet", "Représenter une force par une flèche"],
    [
        "Une force représente une action mécanique exercée par un objet ou un phénomène sur un autre objet : elle peut mettre en mouvement un objet immobile, modifier sa trajectoire ou sa vitesse, ou encore le déformer. Une force possède un point d'application, une direction, un sens et une intensité (une valeur) : elle peut donc être représentée par une flèche.",
        "Le poids d'un objet est la force exercée par la Terre sur cet objet, qui l'attire vers son centre : c'est la force de gravité. Le poids se mesure en newtons (N) à l'aide d'un dynamomètre. La masse d'un objet, elle, se mesure en kilogrammes (kg) à l'aide d'une balance, et représente la quantité de matière qui le compose : elle ne change pas selon le lieu où se trouve l'objet, contrairement au poids.",
        "Sur la Lune, la force de gravité est environ 6 fois plus faible que sur Terre : un objet y a donc la même masse que sur Terre (la quantité de matière ne change pas), mais un poids 6 fois plus faible, la Lune l'attirant beaucoup moins fort, ce qui explique pourquoi les astronautes semblent « bondir » à la surface de la Lune."
    ],
    svg_forces, "quiz-forces-actions-poids-5e", "Quiz — Modéliser une action : le poids et les forces",
    [
        q("q1", "Qu'est-ce qu'une force ?", ["Une couleur", "Une action mécanique exercée par un objet sur un autre", "Une unité de masse", "Un état de la matière"], 1, "Une force représente une action mécanique exercée par un objet ou un phénomène sur un autre objet."),
        q("q2", "Par quoi peut-on représenter une force ?", ["Un point", "Une flèche", "Un cercle", "Une couleur"], 1, "Une force peut être représentée par une flèche, indiquant direction, sens et intensité."),
        q("q3", "Qu'est-ce que le poids d'un objet ?", ["La quantité de matière qui le compose", "La force exercée par la Terre qui l'attire vers son centre", "Sa couleur", "Sa forme"], 1, "Le poids est la force exercée par la Terre (gravité) qui attire l'objet vers son centre."),
        q("q4", "Dans quelle unité mesure-t-on le poids ?", ["Le kilogramme", "Le newton", "Le litre", "Le mètre"], 1, "Le poids se mesure en newtons (N)."),
        q("q5", "Dans quelle unité mesure-t-on la masse ?", ["Le newton", "Le kilogramme", "Le litre", "Le mètre carré"], 1, "La masse se mesure en kilogrammes (kg)."),
        q("q6", "Avec quel instrument mesure-t-on le poids d'un objet ?", ["Une balance", "Un dynamomètre", "Un thermomètre", "Une règle"], 1, "Le poids se mesure avec un dynamomètre."),
        q("q7", "Avec quel instrument mesure-t-on la masse d'un objet ?", ["Un dynamomètre", "Une balance", "Un chronomètre", "Un thermomètre"], 1, "La masse se mesure avec une balance."),
        q("q8", "La masse d'un objet change-t-elle si on l'emmène sur la Lune ?", ["Oui, elle change beaucoup", "Non, elle reste la même", "Elle devient nulle", "Elle double"], 1, "La masse représente la quantité de matière et ne change pas selon le lieu."),
        q("q9", "Le poids d'un objet change-t-il sur la Lune ?", ["Non, il reste identique", "Oui, il devient environ 6 fois plus faible", "Il devient 6 fois plus grand", "Il devient nul"], 1, "Sur la Lune, la gravité étant plus faible, le poids d'un objet devient environ 6 fois plus faible qu'sur Terre."),
        q("q10", "Une force peut-elle uniquement mettre un objet en mouvement ?", ["Oui, uniquement cela", "Non, elle peut aussi modifier une trajectoire, une vitesse, ou déformer un objet", "Non, une force ne fait jamais rien", "Elle change uniquement la couleur des objets"], 1, "Une force peut mettre en mouvement, modifier une trajectoire ou une vitesse, ou déformer un objet."),
    ]
))

lessons_out.append(lesson_block(
    "energie-sources-conversions-5e", "Sources, formes et conversions de l'énergie", "physique-chimie", "5e", "20 min",
    "Identifier différentes formes d'énergie et comprendre comment un dispositif peut convertir l'énergie d'une forme à une autre.",
    ["Identifier différentes formes d'énergie", "Comprendre ce qu'est une conversion d'énergie", "Citer des exemples de chaînes de conversion d'énergie du quotidien"],
    [
        "L'énergie existe sous plusieurs formes : l'énergie cinétique (liée au mouvement), l'énergie thermique (liée à la chaleur), l'énergie lumineuse, l'énergie chimique (stockée dans les aliments, les combustibles, les piles), l'énergie électrique, et l'énergie mécanique (liée à la position, comme l'eau retenue en haut d'un barrage). L'énergie ne peut jamais être créée ni détruite : elle se transforme seulement d'une forme à une autre.",
        "Un dispositif technique convertit souvent l'énergie d'une forme à une autre pour la rendre utile : un panneau solaire convertit l'énergie lumineuse en énergie électrique ; un moteur électrique convertit l'énergie électrique en énergie cinétique (mouvement) ; une pile convertit de l'énergie chimique en énergie électrique ; une centrale hydroélectrique convertit l'énergie mécanique de l'eau qui tombe en énergie électrique.",
        "Lors de chaque conversion, une partie de l'énergie est souvent perdue sous forme de chaleur non utile (par exemple la chaleur dégagée par une ampoule ou un moteur qui chauffe), ce qui explique pourquoi aucun dispositif ne convertit jamais 100% de l'énergie reçue en énergie utile : on cherche donc à créer des dispositifs les plus efficaces possible pour limiter ces pertes et économiser l'énergie."
    ],
    svg_energie_conv, "quiz-energie-sources-conversions-5e", "Quiz — Sources, formes et conversions de l'énergie",
    [
        q("q1", "L'énergie peut-elle être créée à partir de rien ?", ["Oui, facilement", "Non, elle se transforme seulement d'une forme à une autre", "Oui, dans certains dispositifs seulement", "L'énergie n'existe pas vraiment"], 1, "L'énergie ne peut jamais être créée ni détruite : elle se transforme d'une forme à une autre."),
        q("q2", "Quelle forme d'énergie est liée au mouvement ?", ["L'énergie chimique", "L'énergie cinétique", "L'énergie lumineuse", "L'énergie thermique"], 1, "L'énergie cinétique est liée au mouvement d'un objet."),
        q("q3", "Que convertit un panneau solaire ?", ["L'énergie électrique en énergie chimique", "L'énergie lumineuse en énergie électrique", "L'énergie cinétique en énergie thermique", "Rien du tout"], 1, "Un panneau solaire convertit l'énergie lumineuse du soleil en énergie électrique."),
        q("q4", "Que convertit un moteur électrique ?", ["L'énergie électrique en énergie cinétique", "L'énergie lumineuse en énergie chimique", "L'énergie thermique en énergie électrique", "Rien du tout"], 0, "Un moteur électrique convertit l'énergie électrique en énergie cinétique (mouvement)."),
        q("q5", "Que convertit une pile électrique ?", ["De l'énergie chimique en énergie électrique", "De l'énergie électrique en énergie chimique", "De l'énergie lumineuse en énergie mécanique", "Rien du tout"], 0, "Une pile convertit l'énergie chimique stockée en énergie électrique."),
        q("q6", "Où l'énergie mécanique de l'eau qui tombe est-elle utilisée ?", ["Dans les panneaux solaires", "Dans les centrales hydroélectriques", "Dans les piles", "Dans les moteurs à essence uniquement"], 1, "Les centrales hydroélectriques convertissent l'énergie mécanique de l'eau qui tombe en énergie électrique."),
        q("q7", "Une conversion d'énergie est-elle toujours efficace à 100% ?", ["Oui, toujours", "Non, une partie est souvent perdue sous forme de chaleur", "Oui, sauf pour l'électricité", "L'énergie n'est jamais perdue"], 1, "Aucun dispositif ne convertit 100% de l'énergie en énergie utile : une partie est perdue en chaleur."),
        q("q8", "Pourquoi cherche-t-on à créer des dispositifs efficaces ?", ["Pour perdre plus d'énergie", "Pour limiter les pertes et économiser l'énergie", "Cela n'a aucune importance", "Uniquement pour des raisons esthétiques"], 1, "Des dispositifs efficaces limitent les pertes d'énergie et permettent d'en économiser."),
        q("q9", "L'énergie chimique est-elle stockée dans les aliments ?", ["Non, jamais", "Oui, comme dans les combustibles ou les piles", "Seulement dans l'eau", "Les aliments ne contiennent pas d'énergie"], 1, "L'énergie chimique est stockée dans les aliments, les combustibles et les piles."),
        q("q10", "Quelle forme d'énergie est liée à la position, comme l'eau en haut d'un barrage ?", ["L'énergie chimique", "L'énergie mécanique", "L'énergie lumineuse", "L'énergie électrique"], 1, "L'énergie mécanique est liée à la position, comme celle de l'eau retenue en haut d'un barrage."),
    ]
))

lessons_out.append(lesson_block(
    "lumiere-vision-image-5e", "La propagation de la lumière, la vision et l'image", "physique-chimie", "5e", "20 min",
    "Approfondir la propagation rectiligne de la lumière et comprendre comment se forme une image à travers une lentille.",
    ["Rappeler la propagation rectiligne de la lumière", "Comprendre comment l'œil perçoit une image", "Décrire simplement le rôle d'une lentille convergente"],
    [
        "La lumière se propage en ligne droite dans un milieu transparent et homogène : ce principe permet d'expliquer la formation des ombres, mais aussi le fonctionnement d'appareils optiques simples comme la chambre noire, une boîte percée d'un petit trou qui laisse passer la lumière et forme une image inversée sur la paroi opposée.",
        "L'œil humain fonctionne comme un appareil optique complexe : la lumière entre par la pupille, traverse le cristallin (une lentille naturelle) qui la fait converger, et forme une image sur la rétine, au fond de l'œil. Cette image est transmise au cerveau par le nerf optique, qui la traite pour permettre la vision.",
        "Une lentille convergente est un objet transparent, plus épais au centre que sur les bords, qui fait converger les rayons lumineux qui la traversent vers un point appelé foyer. Ce principe est utilisé dans les loupes, les appareils photo et les lunettes de vue pour corriger certains défauts de la vision, en modifiant la façon dont l'image se forme sur la rétine."
    ],
    svg_oeil, "quiz-lumiere-vision-image-5e", "Quiz — La propagation de la lumière, la vision et l'image",
    [
        q("q1", "Comment la lumière se propage-t-elle dans un milieu transparent homogène ?", ["En ligne courbe", "En ligne droite", "De façon aléatoire", "Elle ne se propage pas"], 1, "La lumière se propage en ligne droite dans un milieu transparent et homogène."),
        q("q2", "Qu'est-ce qu'une chambre noire ?", ["Une pièce sans aucune utilité", "Une boîte percée d'un petit trou qui forme une image inversée", "Un type de lentille", "Un appareil photo moderne uniquement"], 1, "Une chambre noire est une boîte percée d'un petit trou qui laisse passer la lumière et forme une image inversée."),
        q("q3", "Par où la lumière entre-t-elle dans l'œil ?", ["Par la rétine", "Par la pupille", "Par le nerf optique", "Par le cristallin uniquement au début"], 1, "La lumière entre dans l'œil par la pupille."),
        q("q4", "Quel est le rôle du cristallin dans l'œil ?", ["Il transmet l'image au cerveau", "Il fait converger la lumière comme une lentille naturelle", "Il ne sert à rien", "Il produit de la lumière"], 1, "Le cristallin agit comme une lentille naturelle qui fait converger la lumière."),
        q("q5", "Où se forme l'image dans l'œil ?", ["Sur la pupille", "Sur la rétine", "Sur le cristallin", "Elle ne se forme nulle part"], 1, "L'image se forme sur la rétine, au fond de l'œil."),
        q("q6", "Comment l'image formée sur la rétine est-elle transmise au cerveau ?", ["Par le nerf optique", "Par la pupille", "Elle n'est jamais transmise", "Par le cristallin"], 0, "L'image est transmise au cerveau par le nerf optique."),
        q("q7", "Qu'est-ce qu'une lentille convergente ?", ["Un objet opaque qui bloque la lumière", "Un objet transparent, plus épais au centre, qui fait converger les rayons lumineux", "Un miroir", "Une source de lumière"], 1, "Une lentille convergente est un objet transparent, plus épais au centre, qui fait converger les rayons lumineux."),
        q("q8", "Comment appelle-t-on le point où convergent les rayons traversant une lentille convergente ?", ["Le centre", "Le foyer", "La pupille", "La rétine"], 1, "Le point où convergent les rayons s'appelle le foyer de la lentille."),
        q("q9", "Dans quels objets utilise-t-on des lentilles convergentes ?", ["Uniquement dans les livres", "Les loupes, les appareils photo, les lunettes de vue", "Uniquement dans les vêtements", "Elles ne sont jamais utilisées"], 1, "Les lentilles convergentes sont utilisées dans les loupes, appareils photo et lunettes de vue."),
        q("q10", "L'image formée par une chambre noire est-elle à l'endroit ou inversée ?", ["À l'endroit", "Inversée", "Elle ne forme jamais d'image", "Cela dépend de la couleur de la lumière"], 1, "La chambre noire forme une image inversée sur la paroi opposée au trou."),
    ]
))

marker = "\n  {\n    "
idx = txt.index('slug: "ressources-naturelles-terre-5e"')
next_pos = txt.index(marker, idx) + 1
new_block = "".join(lessons_out)
txt = txt[:next_pos] + new_block + txt[next_pos:]

with open(path, 'w') as f:
    f.write(txt)
print("5e Physique-Chimie new lessons inserted:", len(lessons_out))
