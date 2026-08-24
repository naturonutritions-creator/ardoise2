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

svg_peuplement = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="0" y="0" width="320" height="190" fill="#eef3f6"/>
<rect x="10" y="100" width="90" height="80" fill="#fbe4c4"/><circle cx="55" cy="60" r="18" fill="#f2c94c"/><text x="55" y="175" text-anchor="middle" font-size="10" fill="#22303f">Désert chaud</text>
<rect x="115" y="100" width="90" height="80" fill="#cfe3fb"/><path d="M140 175 v-40" stroke="#3b7bd6" stroke-width="4"/><path d="M180 175 v-30" stroke="#3b7bd6" stroke-width="4"/><text x="160" y="95" text-anchor="middle" font-size="10" fill="#22303f">Zone tempérée</text>
<rect x="220" y="100" width="90" height="80" fill="#e7e9ec"/><circle cx="265" cy="140" r="10" fill="#fff"/><text x="265" y="175" text-anchor="middle" font-size="10" fill="#22303f">Pôle froid</text>
</svg>'''

svg_terre_saisons = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="160" cy="95" r="24" fill="#f2c94c"/><text x="160" y="60" text-anchor="middle" font-size="10" fill="#22303f">Soleil</text>
<ellipse cx="160" cy="95" rx="120" ry="55" fill="none" stroke="#cfe3fb" stroke-width="2"/>
<circle cx="280" cy="95" r="10" fill="#3b7bd6" transform="rotate(-20 160 95)"/>
<circle cx="40" cy="95" r="10" fill="#2f9e6f" transform="rotate(20 160 95)"/>
<text x="160" y="175" text-anchor="middle" font-size="10" fill="#22303f">Révolution de la Terre autour du Soleil</text>
</svg>'''

svg_melanges = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="20" y="60" width="110" height="100" rx="8" fill="#cfe3fb"/><text x="75" y="180" text-anchor="middle" font-size="10" fill="#22303f">Mélange homogène</text>
<rect x="190" y="60" width="110" height="100" rx="8" fill="#e7e9ec"/>
<circle cx="220" cy="90" r="6" fill="#3b7bd6"/><circle cx="250" cy="120" r="10" fill="#e08a2a"/><circle cx="280" cy="80" r="7" fill="#3b7bd6"/><circle cx="230" cy="140" r="5" fill="#e08a2a"/>
<text x="245" y="180" text-anchor="middle" font-size="10" fill="#22303f">Mélange hétérogène</text>
</svg>'''

svg_mouvement6 = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M30 150 Q120 20 290 100" stroke="#3b7bd6" stroke-width="3" fill="none" stroke-dasharray="6 6"/>
<circle cx="30" cy="150" r="8" fill="#2f9e6f"/><circle cx="160" cy="60" r="8" fill="#e08a2a"/><circle cx="290" cy="100" r="8" fill="#d1495b"/>
<text x="160" y="185" text-anchor="middle" font-size="10" fill="#22303f">Trajectoire et positions successives</text>
</svg>'''

svg_materiaux = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="15" y="60" width="70" height="70" fill="#5b6470"/><text x="50" y="145" text-anchor="middle" font-size="9" fill="#22303f">Métal</text>
<rect x="105" y="60" width="70" height="70" fill="#e08a2a"/><text x="140" y="145" text-anchor="middle" font-size="9" fill="#22303f">Bois</text>
<rect x="195" y="60" width="70" height="70" fill="#cfe3fb"/><text x="230" y="145" text-anchor="middle" font-size="9" fill="#22303f">Plastique</text>
<rect x="285" y="60" width="30" height="70" fill="#c8ecdc"/><text x="300" y="145" text-anchor="middle" font-size="8" fill="#22303f">Verre</text>
</svg>'''

svg_lumiere = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="50" cy="95" r="22" fill="#f2c94c"/>
<line x1="72" y1="95" x2="200" y2="95" stroke="#f2c94c" stroke-width="2"/>
<rect x="200" y="60" width="18" height="70" fill="#5b6470"/>
<path d="M218 60 L260 150 L260 60 Z" fill="#c8c8c8" opacity="0.7"/>
<text x="50" y="130" text-anchor="middle" font-size="9" fill="#22303f">Source</text>
<text x="209" y="145" text-anchor="middle" font-size="9" fill="#22303f">Objet</text>
<text x="245" y="165" text-anchor="middle" font-size="9" fill="#22303f">Ombre</text>
</svg>'''

lessons_out = []

lessons_out.append(lesson_block(
    "peuplement-milieux-6e", "Le peuplement des milieux", "svt", "6e", "20 min",
    "Comprendre pourquoi les êtres vivants ne se répartissent pas de la même façon partout sur Terre.",
    ["Comprendre ce qu'est un peuplement", "Identifier les facteurs qui influencent la répartition des espèces", "Relier les caractéristiques d'un milieu aux espèces qui y vivent"],
    [
        "Le peuplement d'un milieu désigne l'ensemble des êtres vivants qui y habitent. Un même milieu n'est jamais peuplé au hasard : la température, la disponibilité en eau, la lumière et les ressources alimentaires déterminent quelles espèces peuvent s'y installer et s'y reproduire.",
        "Certains milieux sont très contraignants : le désert chaud impose de résister à des températures extrêmes et au manque d'eau, les pôles imposent de résister au grand froid. Seules les espèces adaptées à ces contraintes (par leur physiologie ou leur comportement) peuvent y survivre : le peuplement y est donc souvent moins riche que dans un milieu tempéré aux conditions plus modérées.",
        "Le peuplement d'un milieu évolue aussi avec les saisons (migrations, hibernation) et peut être fortement modifié par l'action humaine : déforestation, urbanisation, pollution ou réchauffement climatique poussent certaines espèces à disparaître d'un milieu ou à en coloniser de nouveaux, parfois au détriment des espèces déjà présentes."
    ],
    svg_peuplement, "quiz-peuplement-milieux-6e", "Quiz — Le peuplement des milieux",
    [
        q("q1", "Que désigne le peuplement d'un milieu ?", ["Le nombre d'habitants humains", "L'ensemble des êtres vivants qui y habitent", "La météo du lieu", "La surface du milieu"], 1, "Le peuplement d'un milieu désigne l'ensemble des êtres vivants qui y vivent."),
        q("q2", "Quels facteurs influencent la répartition des espèces dans un milieu ?", ["Uniquement la couleur du sol", "La température, l'eau, la lumière et les ressources alimentaires", "Le nombre d'habitants humains uniquement", "Aucun facteur particulier"], 1, "La température, l'eau, la lumière et les ressources alimentaires sont des facteurs déterminants."),
        q("q3", "Pourquoi le peuplement du désert est-il souvent moins riche qu'en milieu tempéré ?", ["Car le désert est trop grand", "Car les conditions extrêmes limitent les espèces capables d'y survivre", "Car il n'y a jamais de vie dans le désert", "Ce n'est pas le cas, c'est l'inverse"], 1, "Les conditions extrêmes du désert (chaleur, manque d'eau) limitent le nombre d'espèces adaptées."),
        q("q4", "Le peuplement d'un milieu peut-il changer avec les saisons ?", ["Non, jamais", "Oui, par exemple avec les migrations ou l'hibernation", "Seulement en été", "Seulement dans les océans"], 1, "Le peuplement change avec les saisons : migrations, hibernation, cycles de reproduction."),
        q("q5", "L'action humaine peut-elle modifier le peuplement d'un milieu ?", ["Non, jamais", "Oui, par exemple par la déforestation ou l'urbanisation", "Seulement dans les déserts", "Seulement en mer"], 1, "La déforestation, l'urbanisation ou la pollution modifient le peuplement des milieux."),
        q("q6", "Que peut provoquer le réchauffement climatique sur le peuplement ?", ["Rien du tout", "Certaines espèces disparaissent ou en colonisent de nouveaux milieux", "Toutes les espèces s'adaptent instantanément", "Seulement des effets positifs"], 1, "Le réchauffement climatique pousse certaines espèces à quitter un milieu ou à en coloniser un nouveau."),
        q("q7", "Un même milieu est-il peuplé au hasard ?", ["Oui, totalement au hasard", "Non, les conditions du milieu déterminent quelles espèces peuvent y vivre", "Cela dépend uniquement de la chance", "Oui, toujours de façon identique partout"], 1, "Le peuplement dépend des conditions du milieu, pas du hasard."),
        q("q8", "Quel est un exemple de milieu très contraignant pour les espèces ?", ["Une forêt tempérée", "Le désert chaud ou les pôles", "Un jardin", "Une plaine agricole"], 1, "Le désert chaud et les pôles imposent des conditions extrêmes qui limitent les espèces présentes."),
        q("q9", "Pourquoi certaines espèces migrent-elles ?", ["Par pur hasard", "Pour trouver des conditions plus favorables selon la saison", "Elles ne migrent jamais", "Uniquement pour jouer"], 1, "Les migrations permettent à certaines espèces de trouver des conditions plus favorables selon la saison."),
        q("q10", "La déforestation a-t-elle un impact sur le peuplement des milieux ?", ["Non, aucun impact", "Oui, elle peut faire disparaître des espèces d'un milieu", "Seulement un impact positif", "Uniquement sur les poissons"], 1, "La déforestation détruit l'habitat de nombreuses espèces, modifiant fortement le peuplement du milieu."),
    ]
))

lessons_out.append(lesson_block(
    "mouvement-terre-saisons-6e", "Le mouvement de la Terre et les saisons", "svt", "6e", "20 min",
    "Comprendre comment la rotation et la révolution de la Terre expliquent le jour, la nuit et les saisons.",
    ["Distinguer rotation et révolution de la Terre", "Expliquer l'alternance jour/nuit", "Expliquer l'origine des saisons"],
    [
        "La Terre effectue deux mouvements en même temps. La rotation est le mouvement de la Terre sur elle-même, autour d'un axe imaginaire passant par les pôles : elle effectue un tour complet en environ 24 heures, ce qui explique l'alternance entre le jour (la partie de la Terre exposée au Soleil) et la nuit (la partie opposée, dans l'ombre).",
        "La révolution est le mouvement de la Terre autour du Soleil : elle effectue un tour complet en environ 365 jours (une année). C'est ce mouvement, combiné à l'inclinaison de l'axe de la Terre, qui provoque les saisons.",
        "L'axe de la Terre est incliné d'environ 23,5° par rapport à son orbite : selon la position de la Terre sur son orbite autour du Soleil, l'hémisphère Nord ou l'hémisphère Sud reçoit plus ou moins directement les rayons du Soleil, ce qui provoque l'alternance des saisons (quand c'est l'été dans l'hémisphère Nord, c'est l'hiver dans l'hémisphère Sud, et inversement)."
    ],
    svg_terre_saisons, "quiz-mouvement-terre-saisons-6e", "Quiz — Le mouvement de la Terre et les saisons",
    [
        q("q1", "Qu'est-ce que la rotation de la Terre ?", ["Son mouvement autour du Soleil", "Son mouvement sur elle-même", "Son mouvement autour de la Lune", "Elle ne bouge jamais"], 1, "La rotation est le mouvement de la Terre sur elle-même, autour de l'axe des pôles."),
        q("q2", "En combien de temps la Terre effectue-t-elle un tour complet sur elle-même ?", ["Environ 1 heure", "Environ 24 heures", "Environ 365 jours", "Environ 1 mois"], 1, "La Terre effectue un tour complet sur elle-même en environ 24 heures."),
        q("q3", "Qu'est-ce que la révolution de la Terre ?", ["Son mouvement sur elle-même", "Son mouvement autour du Soleil", "Son mouvement autour de la Lune", "Un tremblement de terre"], 1, "La révolution est le mouvement de la Terre autour du Soleil."),
        q("q4", "En combien de temps la Terre effectue-t-elle un tour complet autour du Soleil ?", ["24 heures", "Un mois", "Environ 365 jours", "10 ans"], 2, "La Terre effectue un tour complet autour du Soleil en environ 365 jours, soit une année."),
        q("q5", "Qu'est-ce qui explique l'alternance du jour et de la nuit ?", ["La révolution de la Terre", "La rotation de la Terre sur elle-même", "Les saisons", "La distance à la Lune"], 1, "L'alternance jour/nuit est due à la rotation de la Terre sur elle-même."),
        q("q6", "Qu'est-ce qui provoque principalement les saisons ?", ["La rotation rapide de la Terre", "L'inclinaison de l'axe de la Terre combinée à sa révolution", "La distance changeante à la Lune", "Le changement de vitesse du Soleil"], 1, "Les saisons sont dues à l'inclinaison de l'axe terrestre combinée à la révolution autour du Soleil."),
        q("q7", "De combien de degrés l'axe de la Terre est-il incliné environ ?", ["0°", "23,5°", "90°", "180°"], 1, "L'axe de la Terre est incliné d'environ 23,5° par rapport à son orbite."),
        q("q8", "Quand c'est l'été dans l'hémisphère Nord, quelle saison est-ce dans l'hémisphère Sud ?", ["L'été aussi", "L'hiver", "Le printemps", "Il n'y a pas de saisons dans l'hémisphère Sud"], 1, "Les saisons sont inversées entre les deux hémisphères : été au Nord correspond à hiver au Sud."),
        q("q9", "La partie de la Terre exposée au Soleil connaît-elle le jour ou la nuit ?", ["La nuit", "Le jour", "Ni l'un ni l'autre", "Cela dépend de la saison uniquement"], 1, "La partie de la Terre exposée au Soleil connaît le jour, l'autre partie est dans la nuit."),
        q("q10", "La Terre tourne-t-elle uniquement autour du Soleil, sans tourner sur elle-même ?", ["Oui, uniquement autour du Soleil", "Non, elle effectue les deux mouvements en même temps", "Non, elle tourne uniquement sur elle-même", "Elle ne bouge pas du tout"], 1, "La Terre effectue simultanément sa rotation sur elle-même et sa révolution autour du Soleil."),
    ]
))

lessons_out.append(lesson_block(
    "melanges-solutions-6e", "Mélanges et solutions", "physique-chimie", "6e", "20 min",
    "Distinguer mélange homogène et hétérogène, et comprendre ce qu'est une solution.",
    ["Distinguer mélange homogène et mélange hétérogène", "Expliquer ce qu'est une dissolution", "Identifier des méthodes de séparation d'un mélange"],
    [
        "Un mélange est obtenu en associant au moins deux substances différentes. On distingue deux types de mélanges : le mélange homogène, dans lequel on ne distingue plus les différents constituants à l'œil nu (l'eau salée, l'eau sucrée, l'air), et le mélange hétérogène, dans lequel on distingue encore plusieurs phases ou substances (l'eau et l'huile, l'eau et le sable, l'eau boueuse).",
        "Quand un solide se dissout entièrement dans un liquide, on obtient une solution : le solide dissous s'appelle le soluté, et le liquide qui dissout s'appelle le solvant (le plus souvent l'eau). Une solution est un mélange homogène : le sel dissous dans l'eau n'est plus visible, mais il est toujours présent, comme le montre l'évaporation de l'eau qui laisse réapparaître les cristaux de sel.",
        "Pour séparer les constituants d'un mélange hétérogène, on peut utiliser différentes techniques selon les substances : la décantation laisse les particules les plus lourdes se déposer au fond, la filtration retient les particules solides à l'aide d'un filtre (papier filtre, passoire), tandis que pour séparer les constituants d'une solution (mélange homogène), il faut utiliser l'évaporation ou la distillation."
    ],
    svg_melanges, "quiz-melanges-solutions-6e", "Quiz — Mélanges et solutions",
    [
        q("q1", "Qu'est-ce qu'un mélange ?", ["Une substance unique", "L'association d'au moins deux substances différentes", "Un liquide uniquement", "Un solide uniquement"], 1, "Un mélange est obtenu en associant au moins deux substances différentes."),
        q("q2", "Qu'est-ce qu'un mélange homogène ?", ["On distingue plusieurs substances à l'œil nu", "On ne distingue plus les différents constituants à l'œil nu", "Il n'existe pas dans la nature", "Un mélange toujours coloré"], 1, "Dans un mélange homogène, on ne distingue plus les constituants séparément à l'œil nu."),
        q("q3", "L'eau et le sable forment-ils un mélange homogène ou hétérogène ?", ["Homogène", "Hétérogène", "Ni l'un ni l'autre", "Une solution"], 1, "L'eau et le sable restent visibles séparément : c'est un mélange hétérogène."),
        q("q4", "Comment appelle-t-on le solide dissous dans une solution ?", ["Le solvant", "Le soluté", "Le mélange", "Le filtrat"], 1, "Le solide dissous s'appelle le soluté."),
        q("q5", "Comment appelle-t-on le liquide qui dissout le soluté ?", ["Le soluté", "Le solvant", "Le filtre", "Le précipité"], 1, "Le liquide qui dissout le soluté s'appelle le solvant, le plus souvent l'eau."),
        q("q6", "Le sel dissous dans l'eau a-t-il vraiment disparu ?", ["Oui, il a disparu définitivement", "Non, il est toujours présent, on peut le récupérer par évaporation", "Il s'est transformé en eau", "Il devient un gaz"], 1, "Le sel n'a pas disparu : on peut le récupérer en faisant évaporer l'eau."),
        q("q7", "Quelle technique permet de retenir les particules solides d'un mélange hétérogène ?", ["L'évaporation", "La filtration", "La dissolution", "La fusion"], 1, "La filtration retient les particules solides grâce à un filtre."),
        q("q8", "Qu'est-ce que la décantation ?", ["Faire chauffer un liquide", "Laisser les particules les plus lourdes se déposer au fond", "Ajouter du sel dans l'eau", "Mélanger deux gaz"], 1, "La décantation consiste à laisser les particules lourdes se déposer au fond du récipient."),
        q("q9", "Comment séparer le sel de l'eau dans une solution d'eau salée ?", ["Par filtration", "Par évaporation de l'eau", "Impossible de les séparer", "En ajoutant de l'huile"], 1, "L'évaporation de l'eau permet de récupérer le sel, car les constituants d'une solution ne peuvent pas être filtrés."),
        q("q10", "L'air est-il un exemple de mélange homogène ?", ["Non, ce n'est pas un mélange", "Oui, c'est un mélange homogène de plusieurs gaz", "C'est un mélange hétérogène", "L'air n'existe pas vraiment"], 1, "L'air est un mélange homogène de plusieurs gaz (azote, oxygène...) qu'on ne distingue pas séparément."),
    ]
))

lessons_out.append(lesson_block(
    "mouvement-objet-6e", "Décrire et caractériser un mouvement", "physique-chimie", "6e", "20 min",
    "Approfondir la description d'un mouvement : trajectoire, vitesse et relativité du mouvement.",
    ["Décrire une trajectoire à l'aide de positions successives", "Calculer une vitesse moyenne simple", "Comprendre que le mouvement dépend du référentiel choisi"],
    [
        "Pour décrire le mouvement d'un objet, on relève ses positions successives au cours du temps par rapport à un repère fixe : en reliant ces positions, on obtient sa trajectoire, qui peut être rectiligne, circulaire ou quelconque. Plus les positions successives sont rapprochées dans le temps, plus le mouvement de l'objet est lent ; plus elles sont éloignées, plus il est rapide.",
        "La vitesse moyenne d'un objet se calcule en divisant la distance parcourue par la durée du parcours : vitesse = distance ÷ durée. Par exemple, un cycliste qui parcourt 20 km en 1 heure a une vitesse moyenne de 20 km/h. Plus la distance parcourue dans un temps donné est grande, plus la vitesse est élevée.",
        "Le référentiel est l'objet ou le point fixe par rapport auquel on décrit un mouvement. Un même objet peut être immobile dans un référentiel et en mouvement dans un autre : un objet posé sur le siège d'une voiture roulante est immobile par rapport à la voiture, mais en mouvement par rapport à la route. Il n'existe donc pas de mouvement « absolu », seulement des mouvements relatifs à un référentiel précis."
    ],
    svg_mouvement6, "quiz-mouvement-objet-6e", "Quiz — Décrire et caractériser un mouvement",
    [
        q("q1", "Comment obtient-on la trajectoire d'un objet ?", ["En le pesant", "En reliant ses positions successives au cours du temps", "En mesurant sa couleur", "En le photographiant une seule fois"], 1, "La trajectoire s'obtient en reliant les positions successives de l'objet au cours du temps."),
        q("q2", "Comment calcule-t-on une vitesse moyenne ?", ["Distance × durée", "Distance ÷ durée", "Durée ÷ distance", "Distance + durée"], 1, "La vitesse moyenne se calcule en divisant la distance parcourue par la durée du parcours."),
        q("q3", "Un cycliste parcourt 20 km en 1 heure. Quelle est sa vitesse moyenne ?", ["10 km/h", "20 km/h", "40 km/h", "60 km/h"], 1, "20 km ÷ 1 h = 20 km/h."),
        q("q4", "Qu'est-ce qu'un référentiel ?", ["Un type de trajectoire", "L'objet ou le point fixe par rapport auquel on décrit un mouvement", "Une unité de vitesse", "Un instrument de mesure"], 1, "Le référentiel est l'objet ou le point fixe par rapport auquel on décrit un mouvement."),
        q("q5", "Un objet peut-il être immobile dans un référentiel et en mouvement dans un autre ?", ["Non, jamais", "Oui, cela dépend du référentiel choisi", "Seulement s'il est très petit", "Seulement dans l'espace"], 1, "Un objet peut être immobile dans un référentiel et en mouvement dans un autre : le mouvement est relatif."),
        q("q6", "Existe-t-il un mouvement « absolu », indépendant de tout référentiel ?", ["Oui, toujours", "Non, tout mouvement est relatif à un référentiel", "Seulement pour les objets très rapides", "Seulement dans l'eau"], 1, "Il n'existe pas de mouvement absolu : tout mouvement se décrit par rapport à un référentiel précis."),
        q("q7", "Un objet posé sur le siège d'une voiture roulante est-il immobile par rapport à la voiture ?", ["Non, jamais", "Oui, il est immobile par rapport à la voiture", "Cela dépend de la vitesse de la voiture", "Impossible à dire"], 1, "Par rapport à la voiture, l'objet posé sur le siège ne bouge pas : il est immobile dans ce référentiel."),
        q("q8", "Plus les positions successives d'un objet sont rapprochées dans le temps, que peut-on en déduire ?", ["Le mouvement est rapide", "Le mouvement est lent", "L'objet est immobile", "Rien du tout"], 1, "Des positions successives rapprochées dans le temps indiquent un mouvement lent."),
        q("q9", "Quelle unité peut-on utiliser pour exprimer une vitesse ?", ["Le kg", "Le km/h", "Le litre", "Le mètre carré"], 1, "Le km/h (kilomètre par heure) est une unité courante de vitesse."),
        q("q10", "Une trajectoire circulaire correspond-elle toujours à un mouvement rapide ?", ["Oui, toujours", "Non, la forme de la trajectoire ne dit rien sur la vitesse", "Oui, car un cercle est plus court", "Non, un cercle est toujours immobile"], 1, "La forme de la trajectoire (circulaire, rectiligne...) ne renseigne pas directement sur la vitesse de l'objet."),
    ]
))

lessons_out.append(lesson_block(
    "materiaux-objets-techniques-6e", "Les matériaux et les objets techniques", "physique-chimie", "6e", "20 min",
    "Identifier les matériaux utilisés dans les objets techniques et comprendre pourquoi ils sont choisis.",
    ["Identifier différentes familles de matériaux", "Relier une propriété d'un matériau à son usage", "Comprendre l'évolution des objets techniques dans le temps"],
    [
        "Les objets techniques sont fabriqués à partir de matériaux choisis selon leurs propriétés : les métaux (fer, aluminium, cuivre) sont solides, résistants et souvent bons conducteurs d'électricité et de chaleur ; le bois est léger, facile à travailler et renouvelable ; le plastique est léger, imperméable et peu coûteux à produire en grande quantité ; le verre est transparent, dur, mais fragile aux chocs.",
        "Le choix d'un matériau dépend directement de l'usage prévu pour l'objet : on utilise du métal pour une casserole car il conduit bien la chaleur, du verre pour une fenêtre car il est transparent, du plastique isolant pour la gaine d'un fil électrique car il ne conduit pas l'électricité, contrairement au métal qui la conduit très bien.",
        "Les objets techniques évoluent dans le temps pour mieux répondre aux besoins : le téléphone est passé du téléphone filaire au smartphone, l'éclairage de la bougie à l'ampoule électrique puis à la LED, plus économe en énergie. Cette évolution s'appuie souvent sur la découverte de nouveaux matériaux ou de nouvelles techniques de fabrication."
    ],
    svg_materiaux, "quiz-materiaux-objets-techniques-6e", "Quiz — Les matériaux et les objets techniques",
    [
        q("q1", "Pourquoi utilise-t-on du métal pour fabriquer une casserole ?", ["Car il est très léger", "Car il conduit bien la chaleur", "Car il est transparent", "Car il est peu coûteux uniquement"], 1, "Le métal conduit bien la chaleur, ce qui est utile pour une casserole."),
        q("q2", "Quelle propriété du verre le rend utile pour une fenêtre ?", ["Il est souple", "Il est transparent", "Il conduit l'électricité", "Il est très léger"], 1, "Le verre est transparent, ce qui permet de laisser passer la lumière à travers une fenêtre."),
        q("q3", "Pourquoi utilise-t-on du plastique pour la gaine d'un fil électrique ?", ["Car il conduit très bien l'électricité", "Car il n'est pas conducteur d'électricité (isolant)", "Car il est transparent", "Car il est très lourd"], 1, "Le plastique est isolant électrique, ce qui protège des chocs électriques autour d'un fil conducteur."),
        q("q4", "Quel matériau est renouvelable parmi ceux-ci ?", ["Le métal", "Le plastique", "Le bois", "Le verre"], 2, "Le bois est un matériau renouvelable si les arbres sont replantés."),
        q("q5", "Le verre est-il un matériau fragile aux chocs ?", ["Non, jamais", "Oui, il peut se briser facilement", "Seulement s'il est très épais", "Il ne se brise jamais"], 1, "Le verre est dur mais reste fragile face aux chocs, il peut se briser."),
        q("q6", "Comment a évolué l'éclairage au fil du temps ?", ["Il n'a jamais changé", "De la bougie à l'ampoule électrique puis à la LED", "De la LED à la bougie", "Il n'existe pas d'évolution technique"], 1, "L'éclairage a évolué de la bougie à l'ampoule électrique, puis à la LED, plus économe en énergie."),
        q("q7", "Qu'est-ce qui pousse les objets techniques à évoluer ?", ["Le hasard uniquement", "Mieux répondre aux besoins grâce à de nouveaux matériaux ou techniques", "Ils n'évoluent jamais", "Une décision unique et définitive"], 1, "Les objets techniques évoluent pour mieux répondre aux besoins, souvent grâce à de nouveaux matériaux."),
        q("q8", "Pourquoi le plastique est-il beaucoup utilisé dans l'industrie ?", ["Il est très lourd et coûteux", "Il est léger, imperméable et peu coûteux à produire", "Il est fragile et rare", "Il conduit très bien l'électricité"], 1, "Le plastique est léger, imperméable et peu coûteux à produire en grande quantité."),
        q("q9", "Quel matériau est un bon conducteur d'électricité ?", ["Le bois", "Le plastique", "Le métal", "Le verre"], 2, "Le métal est un bon conducteur d'électricité, contrairement au bois, au plastique ou au verre."),
        q("q10", "Le choix d'un matériau pour un objet technique dépend-il de son usage ?", ["Non, c'est toujours le même matériau utilisé", "Oui, chaque matériau est choisi selon ses propriétés et l'usage prévu", "Non, c'est un choix totalement aléatoire", "Uniquement du prix, jamais des propriétés"], 1, "Le matériau est choisi selon ses propriétés (résistance, conduction, transparence...) adaptées à l'usage prévu."),
    ]
))

lessons_out.append(lesson_block(
    "lumiere-vision-6e", "La lumière, la vision et les ombres", "physique-chimie", "6e", "20 min",
    "Comprendre comment la lumière se propage, comment on voit les objets, et comment se forment les ombres.",
    ["Distinguer une source de lumière d'un objet éclairé", "Comprendre que la lumière se propage en ligne droite", "Expliquer la formation d'une ombre"],
    [
        "Une source de lumière est un objet qui produit sa propre lumière (le Soleil, une ampoule allumée, une flamme). Un objet éclairé, lui, ne produit pas de lumière : il devient visible uniquement parce qu'il renvoie vers nos yeux une partie de la lumière qu'il reçoit d'une source. La Lune, par exemple, n'est pas une source de lumière : elle est visible car elle réfléchit la lumière du Soleil.",
        "La lumière se propage en ligne droite, tant qu'elle ne rencontre pas d'obstacle : c'est ce qui permet de voir un objet uniquement s'il existe un trajet en ligne droite entre cet objet, la source de lumière et notre œil. Un rayon lumineux ne peut pas contourner un obstacle opaque.",
        "Quand un objet opaque (qui ne laisse pas passer la lumière) se trouve entre une source de lumière et un écran, il bloque une partie des rayons lumineux et forme une ombre sur l'écran, à l'opposé de la source. La taille de l'ombre dépend de la distance entre la source, l'objet et l'écran : plus la source est proche de l'objet, plus l'ombre projetée est grande."
    ],
    svg_lumiere, "quiz-lumiere-vision-6e", "Quiz — La lumière, la vision et les ombres",
    [
        q("q1", "Qu'est-ce qu'une source de lumière ?", ["Un objet qui reflète la lumière uniquement", "Un objet qui produit sa propre lumière", "Un objet toujours noir", "Un objet transparent uniquement"], 1, "Une source de lumière produit sa propre lumière, comme le Soleil ou une ampoule allumée."),
        q("q2", "La Lune est-elle une source de lumière ?", ["Oui, elle produit sa propre lumière", "Non, elle réfléchit la lumière du Soleil", "Elle ne produit ni ne réfléchit de lumière", "Oui, seulement la nuit"], 1, "La Lune n'est pas une source de lumière : elle est visible car elle réfléchit la lumière du Soleil."),
        q("q3", "Comment la lumière se propage-t-elle dans un milieu transparent homogène ?", ["En ligne courbe", "En ligne droite", "De façon aléatoire", "Elle ne se propage pas"], 1, "La lumière se propage en ligne droite tant qu'elle ne rencontre pas d'obstacle."),
        q("q4", "Que faut-il pour voir un objet ?", ["Rien de particulier", "Un trajet en ligne droite entre l'objet, une source de lumière et l'œil", "Que l'objet produise sa propre lumière uniquement", "Que l'objet soit très grand"], 1, "On voit un objet grâce à un trajet en ligne droite reliant la source de lumière, l'objet et l'œil."),
        q("q5", "Qu'est-ce qu'un objet opaque ?", ["Un objet qui laisse passer toute la lumière", "Un objet qui ne laisse pas passer la lumière", "Un objet transparent", "Une source de lumière"], 1, "Un objet opaque ne laisse pas passer la lumière, il bloque les rayons lumineux."),
        q("q6", "Où se forme l'ombre d'un objet opaque éclairé ?", ["Du même côté que la source de lumière", "À l'opposé de la source de lumière, sur un écran", "Il n'y a jamais d'ombre", "Uniquement au-dessus de l'objet"], 1, "L'ombre se forme à l'opposé de la source de lumière, là où les rayons sont bloqués par l'objet."),
        q("q7", "Que se passe-t-il si la source de lumière se rapproche de l'objet opaque ?", ["L'ombre projetée devient plus grande", "L'ombre projetée devient plus petite", "L'ombre disparaît", "Rien ne change"], 0, "Plus la source de lumière est proche de l'objet, plus l'ombre projetée sur l'écran est grande."),
        q("q8", "Un rayon lumineux peut-il contourner un obstacle opaque ?", ["Oui, toujours", "Non, il est bloqué par l'obstacle", "Seulement la nuit", "Seulement s'il est très rapide"], 1, "Un rayon lumineux ne peut pas contourner un obstacle opaque : il se propage en ligne droite et est bloqué."),
        q("q9", "Un objet éclairé produit-il sa propre lumière ?", ["Oui, toujours", "Non, il renvoie une partie de la lumière qu'il reçoit", "Oui, mais seulement le jour", "Cela dépend de sa couleur uniquement"], 1, "Un objet éclairé ne produit pas de lumière : il renvoie vers nos yeux une partie de la lumière reçue d'une source."),
        q("q10", "Une flamme de bougie est-elle une source de lumière ?", ["Non, ce n'est jamais une source", "Oui, elle produit sa propre lumière", "Seulement si elle est électrique", "Seulement le jour"], 1, "Une flamme de bougie produit sa propre lumière : c'est bien une source de lumière."),
    ]
))

marker = "\n  {\n    "

# SVT: insert after "sommeil-6e" (last svt lesson of the 6e science block)
idx = txt.index('slug: "sommeil-6e"')
next_pos = txt.index(marker, idx) + 1
svt_block = "".join(lessons_out[0:2])
txt = txt[:next_pos] + svt_block + txt[next_pos:]

# Physique-Chimie: insert after "sources-energie-6e" (last physique-chimie lesson before svt block)
idx2 = txt.index('slug: "sources-energie-6e"')
next_pos2 = txt.index(marker, idx2) + 1
pc_block = "".join(lessons_out[2:6])
txt = txt[:next_pos2] + pc_block + txt[next_pos2:]

with open(path, 'w') as f:
    f.write(txt)
print("6e new lessons inserted:", len(lessons_out))
