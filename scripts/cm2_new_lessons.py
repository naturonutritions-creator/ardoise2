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

# ---------- SVG illustrations ----------
svg_classification = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="110" y="8" width="100" height="30" rx="8" fill="#2f9e6f"/><text x="160" y="27" text-anchor="middle" fill="#fff" font-size="12">Êtres vivants</text>
<line x1="160" y1="38" x2="80" y2="66" stroke="#5b6470" stroke-width="2"/>
<line x1="160" y1="38" x2="240" y2="66" stroke="#5b6470" stroke-width="2"/>
<rect x="30" y="66" width="100" height="30" rx="8" fill="#3b7bd6"/><text x="80" y="85" text-anchor="middle" fill="#fff" font-size="12">Animaux</text>
<rect x="190" y="66" width="100" height="30" rx="8" fill="#e08a2a"/><text x="240" y="85" text-anchor="middle" fill="#fff" font-size="12">Végétaux</text>
<line x1="80" y1="96" x2="45" y2="130" stroke="#5b6470" stroke-width="2"/>
<line x1="80" y1="96" x2="115" y2="130" stroke="#5b6470" stroke-width="2"/>
<rect x="8" y="130" width="90" height="30" rx="8" fill="#cfe3fb"/><text x="53" y="149" text-anchor="middle" fill="#22303f" font-size="11">Vertébrés</text>
<rect x="108" y="130" width="90" height="30" rx="8" fill="#cfe3fb"/><text x="153" y="149" text-anchor="middle" fill="#22303f" font-size="11">Invertébrés</text>
</svg>'''

svg_milieux = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="0" y="0" width="320" height="190" fill="#eef3f6"/>
<rect x="10" y="20" width="90" height="150" rx="10" fill="#fbe4c4"/><circle cx="55" cy="60" r="14" fill="#f2c94c"/><text x="55" y="150" text-anchor="middle" font-size="11" fill="#22303f">Désert</text>
<rect x="115" y="20" width="90" height="150" rx="10" fill="#c8ecdc"/><path d="M160 130 v-45" stroke="#2f9e6f" stroke-width="6"/><circle cx="160" cy="75" r="16" fill="#2f9e6f"/><text x="160" y="150" text-anchor="middle" font-size="11" fill="#22303f">Forêt</text>
<rect x="220" y="20" width="90" height="150" rx="10" fill="#cfe3fb"/><path d="M240 100 q10 -14 20 0 t20 0" stroke="#3b7bd6" stroke-width="3" fill="none"/><text x="265" y="150" text-anchor="middle" font-size="11" fill="#22303f">Océan</text>
</svg>'''

svg_assiette = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="140" cy="95" r="80" fill="#e7e9ec"/>
<path d="M140 95 L140 15 A80 80 0 0 1 209.3 135 Z" fill="#c8ecdc"/>
<path d="M140 95 L209.3 135 A80 80 0 0 1 140 175 Z" fill="#fbe4c4"/>
<path d="M140 95 L140 175 A80 80 0 0 1 140 15 Z" fill="#f3c9ce"/>
<circle cx="270" cy="40" r="18" fill="#cfe3fb"/>
<text x="140" y="185" text-anchor="middle" font-size="11" fill="#22303f">Assiette équilibrée</text>
<text x="270" y="70" text-anchor="middle" font-size="10" fill="#22303f">Laitier</text>
</svg>'''

svg_etats = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="20" y="120" width="70" height="50" fill="#3b7bd6"/><text x="55" y="150" text-anchor="middle" fill="#fff" font-size="11">Solide</text>
<circle cx="270" cy="145" r="45" fill="#cfe3fb"/><text x="270" y="150" text-anchor="middle" font-size="11" fill="#22303f">Liquide</text>
<g fill="#e08a2a"><circle cx="140" cy="35" r="4"/><circle cx="160" cy="20" r="4"/><circle cx="180" cy="45" r="4"/><circle cx="120" cy="55" r="4"/><circle cx="165" cy="60" r="4"/></g>
<text x="155" y="15" text-anchor="middle" font-size="11" fill="#22303f">Gaz</text>
<path d="M95 130 L135 60" stroke="#5b6470" stroke-width="2" marker-end="url(#a)"/><text x="80" y="95" font-size="9" fill="#22303f">fusion</text>
<path d="M155 65 L230 125" stroke="#5b6470" stroke-width="2"/><text x="200" y="90" font-size="9" fill="#22303f">vaporisation</text>
<defs><marker id="a" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

svg_mouvement = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<path d="M30 150 Q120 20 290 100" stroke="#3b7bd6" stroke-width="3" fill="none" stroke-dasharray="6 6"/>
<circle cx="30" cy="150" r="8" fill="#2f9e6f"/><text x="30" y="172" text-anchor="middle" font-size="10" fill="#22303f">Départ</text>
<circle cx="290" cy="100" r="8" fill="#d1495b"/><text x="290" y="122" text-anchor="middle" font-size="10" fill="#22303f">Arrivée</text>
<rect x="150" y="150" width="14" height="14" fill="#5b6470"/><text x="157" y="180" text-anchor="middle" font-size="10" fill="#22303f">Repère fixe</text>
</svg>'''

svg_energie = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<circle cx="60" cy="55" r="30" fill="#f2c94c"/><text x="60" y="105" text-anchor="middle" font-size="11" fill="#22303f">Soleil</text>
<g stroke="#5b6470" stroke-width="4"><line x1="160" y1="40" x2="160" y2="120"/><line x1="160" y1="40" x2="140" y2="80"/><line x1="160" y1="40" x2="180" y2="90"/><line x1="160" y1="40" x2="155" y2="60"/></g>
<text x="160" y="145" text-anchor="middle" font-size="11" fill="#22303f">Éolienne</text>
<circle cx="260" cy="60" r="24" fill="#fbe4c4" stroke="#e08a2a" stroke-width="3"/><text x="260" y="105" text-anchor="middle" font-size="11" fill="#22303f">Ampoule</text>
</svg>'''

svg_signal = '''<svg viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
<rect x="10" y="80" width="85" height="40" rx="8" fill="#3b7bd6"/><text x="52" y="104" text-anchor="middle" fill="#fff" font-size="11">Capteur</text>
<path d="M95 100 H130" stroke="#5b6470" stroke-width="2" marker-end="url(#b)"/>
<rect x="130" y="80" width="85" height="40" rx="8" fill="#2f9e6f"/><text x="172" y="104" text-anchor="middle" fill="#fff" font-size="11">Traitement</text>
<path d="M215 100 H250" stroke="#5b6470" stroke-width="2" marker-end="url(#b)"/>
<rect x="250" y="80" width="65" height="40" rx="8" fill="#e08a2a"/><text x="282" y="104" text-anchor="middle" fill="#fff" font-size="10">Action</text>
<defs><marker id="b" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#5b6470"/></marker></defs>
</svg>'''

lessons_out = []

# ===================== SVT CM2 =====================
lessons_out.append(lesson_block(
    "classification-vivant-cm2", "Classer les êtres vivants", "svt", "cm2", "20 min",
    "Apprendre à classer les êtres vivants selon des critères communs : animaux, végétaux, vertébrés, invertébrés.",
    ["Distinguer le règne animal et le règne végétal", "Classer les animaux en vertébrés et invertébrés", "Utiliser des critères communs pour classer des êtres vivants"],
    [
        "On classe les êtres vivants selon des critères communs (des points communs précis), et non selon leur ressemblance apparente ou leur milieu de vie. Le monde vivant se divise d'abord en grands groupes : les animaux (qui se nourrissent d'autres êtres vivants) et les végétaux (qui produisent leur propre matière grâce à la lumière du soleil, la photosynthèse).",
        "Parmi les animaux, on distingue les vertébrés (qui possèdent un squelette interne avec une colonne vertébrale : mammifères, oiseaux, poissons, reptiles, amphibiens) et les invertébrés (sans squelette interne : insectes, mollusques, vers, crustacés), qui représentent en réalité la majorité des espèces animales connues sur Terre.",
        "Pour classer un être vivant, les scientifiques utilisent des attributs précis (présence de poils, de plumes, nombre de pattes, mode de reproduction...) et non son environnement ou son utilité pour l'être humain : une baleine est un mammifère (elle allaite ses petits et respire avec des poumons) même si elle vit dans l'eau comme un poisson."
    ],
    svg_classification, "quiz-classification-vivant-cm2", "Quiz — Classer les êtres vivants",
    [
        q("q1", "Sur quoi se base-t-on pour classer les êtres vivants ?", ["Leur couleur préférée", "Des critères communs précis", "Leur nom en français", "Leur taille uniquement"], 1, "On classe les êtres vivants selon des critères communs précis (attributs partagés), pas selon des impressions."),
        q("q2", "Comment les végétaux produisent-ils leur matière ?", ["En mangeant d'autres êtres vivants", "Grâce à la photosynthèse et la lumière du soleil", "Ils ne produisent rien", "En absorbant uniquement de l'air"], 1, "Les végétaux produisent leur propre matière grâce à la photosynthèse, un processus qui utilise la lumière du soleil."),
        q("q3", "Qu'est-ce qu'un animal vertébré ?", ["Un animal sans squelette", "Un animal avec un squelette interne et une colonne vertébrale", "Un animal qui vole", "Un animal aquatique uniquement"], 1, "Un vertébré possède un squelette interne avec une colonne vertébrale."),
        q("q4", "Lequel de ces animaux est un invertébré ?", ["Le chat", "L'escargot", "Le pigeon", "La grenouille"], 1, "L'escargot est un mollusque, donc un invertébré (sans squelette interne)."),
        q("q5", "Quel groupe représente la majorité des espèces animales connues ?", ["Les vertébrés", "Les invertébrés", "Les mammifères uniquement", "Les oiseaux uniquement"], 1, "Les invertébrés (insectes, mollusques, vers...) représentent la majorité des espèces animales connues."),
        q("q6", "Pourquoi la baleine est-elle un mammifère et non un poisson ?", ["Parce qu'elle nage vite", "Parce qu'elle allaite ses petits et respire avec des poumons", "Parce qu'elle est très grande", "Parce qu'elle vit dans l'océan"], 1, "La baleine allaite ses petits et respire avec des poumons, ce sont des critères de mammifère, malgré son milieu de vie aquatique."),
        q("q7", "Les reptiles sont-ils des vertébrés ou des invertébrés ?", ["Des vertébrés", "Des invertébrés", "Ni l'un ni l'autre", "Cela dépend de l'espèce"], 0, "Les reptiles possèdent un squelette interne avec une colonne vertébrale : ce sont des vertébrés."),
        q("q8", "Quel critère ne sert PAS à classer les êtres vivants scientifiquement ?", ["Le nombre de pattes", "Le mode de reproduction", "L'utilité pour l'être humain", "La présence de poils ou de plumes"], 2, "L'utilité pour l'être humain n'est pas un critère scientifique de classification du vivant."),
        q("q9", "Les insectes appartiennent-ils au règne animal ou végétal ?", ["Au règne végétal", "Au règne animal", "Ni l'un ni l'autre", "Aux deux à la fois"], 1, "Les insectes se nourrissent d'autres êtres vivants ou de matière organique : ils appartiennent au règne animal."),
        q("q10", "Que signifie « classer » les êtres vivants ?", ["Les ranger par ordre alphabétique", "Les regrouper selon des points communs précis", "Les compter", "Les dessiner"], 1, "Classer les êtres vivants, c'est les regrouper en fonction de critères et de points communs précis."),
    ]
))

lessons_out.append(lesson_block(
    "peuplement-milieux-biodiversite-cm2", "Le peuplement des milieux et la biodiversité", "svt", "cm2", "20 min",
    "Comprendre comment les êtres vivants se répartissent selon les milieux, et pourquoi protéger la biodiversité.",
    ["Comprendre ce qu'est un milieu de vie", "Expliquer pourquoi les espèces ne vivent pas partout de la même façon", "Identifier des gestes qui protègent la biodiversité"],
    [
        "Un milieu de vie est l'endroit où vivent des êtres vivants, avec ses caractéristiques propres (température, présence d'eau, lumière, nourriture disponible). Chaque espèce est adaptée à certains milieux précis : le chameau supporte la chaleur et le manque d'eau du désert, le poisson des grands fonds marins vit sans lumière et sous une pression très forte.",
        "La biodiversité désigne la diversité de tous les êtres vivants sur Terre : la diversité des espèces, mais aussi la diversité au sein d'une même espèce et la diversité des milieux (écosystèmes). Cette biodiversité est aujourd'hui menacée par la destruction des milieux naturels (déforestation, pollution), le changement climatique et la surexploitation de certaines espèces.",
        "Chacun peut agir pour protéger la biodiversité : trier ses déchets et recycler, limiter le gaspillage, planter des espèces locales dans son jardin, ne pas ramasser certaines plantes protégées ou capturer des animaux sauvages, et respecter les espaces naturels protégés comme les parcs nationaux et les réserves naturelles."
    ],
    svg_milieux, "quiz-peuplement-milieux-biodiversite-cm2", "Quiz — Le peuplement des milieux et la biodiversité",
    [
        q("q1", "Qu'est-ce qu'un milieu de vie ?", ["Un pays", "L'endroit où vivent des êtres vivants, avec ses caractéristiques propres", "Une école", "Un zoo uniquement"], 1, "Un milieu de vie est l'endroit où vivent des êtres vivants, avec ses propres caractéristiques (température, eau, lumière...)."),
        q("q2", "Pourquoi le chameau peut-il vivre dans le désert ?", ["Il n'a pas besoin d'eau du tout", "Il est adapté à la chaleur et au manque d'eau", "Il vit en réalité dans l'eau", "Il n'a pas besoin de nourriture"], 1, "Le chameau est adapté aux conditions du désert : il supporte la chaleur et peut se passer d'eau longtemps."),
        q("q3", "Que désigne le mot « biodiversité » ?", ["Uniquement le nombre d'animaux dans un zoo", "La diversité de tous les êtres vivants sur Terre", "Un seul type de plante", "Le climat d'une région"], 1, "La biodiversité désigne la diversité de tous les êtres vivants (espèces, individus, milieux)."),
        q("q4", "Quelle est une menace pour la biodiversité ?", ["Planter des arbres", "La déforestation et la pollution", "Recycler ses déchets", "Créer des réserves naturelles"], 1, "La déforestation et la pollution détruisent les milieux naturels et menacent la biodiversité."),
        q("q5", "Citez un geste qui protège la biodiversité.", ["Jeter ses déchets dans la nature", "Trier ses déchets et recycler", "Capturer des animaux sauvages", "Cueillir toutes les fleurs rencontrées"], 1, "Trier ses déchets et recycler limite la pollution et protège les milieux naturels."),
        q("q6", "Qu'est-ce qu'une réserve naturelle ?", ["Un magasin", "Un espace naturel protégé", "Une ferme", "Un parc d'attractions"], 1, "Une réserve naturelle est un espace protégé où la nature et les espèces sont préservées."),
        q("q7", "Le changement climatique menace-t-il la biodiversité ?", ["Non, aucun rapport", "Oui, il modifie les milieux de vie des espèces", "Seulement en hiver", "Uniquement dans les océans"], 1, "Le changement climatique modifie les conditions des milieux, ce qui menace de nombreuses espèces."),
        q("q8", "Pourquoi ne faut-il pas capturer d'animaux sauvages ?", ["Cela perturbe les milieux et les populations d'espèces", "Cela n'a aucune conséquence", "C'est toujours autorisé", "Les animaux sauvages ne vivent nulle part en particulier"], 0, "Capturer des animaux sauvages perturbe les écosystèmes et peut menacer certaines espèces."),
        q("q9", "La biodiversité concerne-t-elle uniquement les espèces différentes ?", ["Oui, uniquement", "Non, aussi la diversité au sein d'une même espèce et des milieux", "Non, seulement les milieux", "Non, seulement les individus"], 1, "La biodiversité inclut la diversité des espèces, mais aussi au sein d'une même espèce et celle des milieux."),
        q("q10", "Pourquoi planter des espèces locales aide-t-il la biodiversité ?", ["Cela ne sert à rien", "Cela convient mieux aux milieux et aux espèces locales", "Cela coûte moins cher uniquement", "Cela empêche toute pollution"], 1, "Les espèces locales sont adaptées au milieu et profitent mieux à la faune et à la flore locales."),
    ]
))

lessons_out.append(lesson_block(
    "alimentation-equilibree-cm2", "L'alimentation équilibrée", "svt", "cm2", "20 min",
    "Découvrir les groupes d'aliments et composer un repas équilibré pour rester en bonne santé.",
    ["Connaître les grandes familles d'aliments", "Composer une assiette équilibrée", "Comprendre les besoins de l'organisme en énergie"],
    [
        "Les aliments se répartissent en plusieurs familles selon ce qu'ils apportent à l'organisme : les féculents (pain, pâtes, riz, pommes de terre) fournissent de l'énergie ; les fruits et légumes apportent des vitamines, des minéraux et des fibres ; les produits laitiers apportent du calcium ; la viande, le poisson et les œufs apportent des protéines qui construisent et réparent les muscles.",
        "Une assiette équilibrée respecte des proportions : environ la moitié de fruits et légumes, un quart de féculents, un quart de protéines, complétée par un produit laitier et de l'eau à volonté (à privilégier par rapport aux boissons sucrées). Manger varié permet de couvrir tous les besoins de l'organisme sans excès.",
        "Les besoins énergétiques dépendent de l'activité physique : un enfant qui fait du sport ou qui grandit a besoin de plus d'énergie qu'une personne peu active. Manger trop gras, trop sucré ou trop salé de façon répétée peut nuire à la santé, tout comme sauter des repas ; l'équilibre alimentaire se construit sur la semaine entière, pas sur un seul repas."
    ],
    svg_assiette, "quiz-alimentation-equilibree-cm2", "Quiz — L'alimentation équilibrée",
    [
        q("q1", "Que fournissent principalement les féculents à l'organisme ?", ["Des vitamines", "De l'énergie", "Du calcium", "Rien de particulier"], 1, "Les féculents (pain, pâtes, riz, pommes de terre) fournissent principalement de l'énergie."),
        q("q2", "Que apportent les fruits et légumes ?", ["Des protéines uniquement", "Des vitamines, minéraux et fibres", "Du sucre uniquement", "Rien d'utile"], 1, "Les fruits et légumes apportent vitamines, minéraux et fibres."),
        q("q3", "Quel groupe d'aliments apporte des protéines pour les muscles ?", ["Les féculents", "La viande, le poisson et les œufs", "Les produits laitiers uniquement", "Les fruits"], 1, "La viande, le poisson et les œufs apportent des protéines qui construisent et réparent les muscles."),
        q("q4", "Quelle proportion de l'assiette devrait être composée de fruits et légumes ?", ["Un dixième", "Environ la moitié", "La totalité", "Aucune"], 1, "Une assiette équilibrée contient environ la moitié de fruits et légumes."),
        q("q5", "Quelle boisson faut-il privilégier au quotidien ?", ["Les sodas", "L'eau", "Les jus très sucrés", "Aucune boisson n'est nécessaire"], 1, "L'eau doit être privilégiée par rapport aux boissons sucrées."),
        q("q6", "Qu'apportent les produits laitiers ?", ["Des fibres", "Du calcium", "Uniquement de l'eau", "Rien d'utile"], 1, "Les produits laitiers apportent du calcium, important pour les os."),
        q("q7", "Un enfant qui fait beaucoup de sport a-t-il besoin de plus d'énergie ?", ["Non, moins", "Oui, plus", "Cela ne change rien", "Seulement en hiver"], 1, "L'activité physique augmente les besoins énergétiques de l'organisme."),
        q("q8", "Est-il conseillé de manger trop gras, trop sucré ou trop salé régulièrement ?", ["Oui, c'est recommandé", "Non, cela peut nuire à la santé", "Cela n'a aucune conséquence", "Seulement le week-end"], 1, "Manger trop gras, trop sucré ou trop salé de façon répétée peut nuire à la santé."),
        q("q9", "Sur quelle période faut-il évaluer l'équilibre alimentaire ?", ["Un seul repas", "La semaine entière", "Une seule journée", "Une seule minute"], 1, "L'équilibre alimentaire se construit sur la semaine entière, pas sur un seul repas."),
        q("q10", "Sauter des repas est-il bon pour la santé ?", ["Oui, c'est recommandé", "Non, cela peut nuire à l'équilibre alimentaire", "Cela n'a aucun effet", "Seulement pour les féculents"], 1, "Sauter des repas peut nuire à l'équilibre alimentaire et aux apports nécessaires à l'organisme."),
    ]
))

with open(path, 'w') as f:
    f.write(txt)

import re
marker_svt = 'slug: "squelette-muscles-cm2"'
idx = txt.index(marker_svt)
insert_marker = "\n  {\n    "
pos = txt.rindex(insert_marker, 0, idx) + 1
# find end of this lesson block (next "\n  {\n    ")
next_pos = txt.index(insert_marker, idx) + 1
new_block = "".join(lessons_out)
txt = txt[:next_pos] + new_block + txt[next_pos:]

with open(path, 'w') as f:
    f.write(txt)
print("SVT CM2 lessons inserted:", len(lessons_out))
