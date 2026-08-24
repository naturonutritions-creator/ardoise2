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

lessons_out.append(lesson_block(
    "etats-changements-matiere-cm2", "Les états et changements d'état de la matière", "physique-chimie", "cm2", "20 min",
    "Approfondir les trois états de la matière, leurs changements, et découvrir les mélanges et solutions.",
    ["Nommer les changements d'état et les conditions qui les provoquent", "Distinguer un mélange homogène d'un mélange hétérogène", "Expliquer ce qu'est une dissolution"],
    [
        "La matière existe sous trois états : solide (forme et volume fixes), liquide (volume fixe mais qui prend la forme du récipient), gazeux (ni forme ni volume fixes, occupe tout l'espace disponible). Le passage d'un état à un autre s'appelle un changement d'état : fusion (solide → liquide), solidification (liquide → solide), vaporisation (liquide → gaz), condensation (gaz → liquide).",
        "Un mélange est l'association de plusieurs substances. Un mélange homogène ne laisse voir qu'une seule substance à l'œil nu, même s'il en contient plusieurs (eau salée, eau sucrée) : on ne distingue plus les composants. Un mélange hétérogène laisse voir plusieurs substances distinctes (eau et huile, eau et sable), qui peuvent parfois se séparer par décantation ou filtration.",
        "Dissoudre du sel ou du sucre dans l'eau crée une solution : le solide disparaît à l'œil mais n'a pas disparu, il s'est simplement mélangé intimement à l'eau (on peut le retrouver en faisant évaporer l'eau). Il existe une limite : au-delà d'une certaine quantité, le sel ou le sucre ne se dissout plus et reste visible au fond du récipient, on dit que la solution est saturée."
    ],
    svg_etats, "quiz-etats-changements-matiere-cm2", "Quiz — Les états et changements d'état de la matière",
    [
        q("q1", "Quels sont les trois états de la matière ?", ["Chaud, froid, tiède", "Solide, liquide, gazeux", "Grand, moyen, petit", "Dur, mou, élastique"], 1, "La matière existe à l'état solide, liquide ou gazeux."),
        q("q2", "Comment appelle-t-on le passage du solide au liquide ?", ["La solidification", "La fusion", "La vaporisation", "La condensation"], 1, "La fusion est le passage de l'état solide à l'état liquide."),
        q("q3", "Comment appelle-t-on le passage du gaz au liquide ?", ["La condensation", "La fusion", "La solidification", "L'évaporation"], 0, "La condensation est le passage de l'état gazeux à l'état liquide."),
        q("q4", "Qu'est-ce qu'un mélange homogène ?", ["On voit plusieurs substances distinctes", "On ne distingue plus les substances à l'œil nu", "Un mélange qui n'existe pas", "Un mélange toujours solide"], 1, "Dans un mélange homogène, les substances sont mélangées si intimement qu'on ne les distingue plus."),
        q("q5", "L'eau et l'huile forment-elles un mélange homogène ou hétérogène ?", ["Homogène", "Hétérogène", "Ni l'un ni l'autre", "Cela dépend de la couleur"], 1, "L'eau et l'huile ne se mélangent pas et restent visibles séparément : c'est un mélange hétérogène."),
        q("q6", "Que devient le sel quand on le dissout dans l'eau ?", ["Il disparaît définitivement", "Il se mélange intimement à l'eau, on peut le retrouver par évaporation", "Il devient un gaz", "Rien ne se passe"], 1, "Le sel dissous n'a pas disparu : on peut le retrouver en faisant évaporer l'eau."),
        q("q7", "Que signifie qu'une solution est « saturée » ?", ["Elle est trop froide", "Le solide ne se dissout plus au-delà d'une certaine quantité", "Elle est devenue un gaz", "Elle a changé de couleur"], 1, "Une solution saturée ne peut plus dissoudre de solide supplémentaire, qui reste visible au fond."),
        q("q8", "Comment peut-on séparer un mélange hétérogène comme l'eau et le sable ?", ["Impossible de les séparer", "Par filtration ou décantation", "En les chauffant uniquement", "En les congelant"], 1, "On peut séparer un mélange hétérogène par filtration ou décantation."),
        q("q9", "Quel état de la matière n'a ni forme ni volume fixes ?", ["Solide", "Liquide", "Gazeux", "Aucun"], 2, "L'état gazeux n'a ni forme ni volume fixes : il occupe tout l'espace disponible."),
        q("q10", "La vaporisation est le passage de quel état à quel état ?", ["Solide à liquide", "Liquide à gaz", "Gaz à liquide", "Liquide à solide"], 1, "La vaporisation est le passage de l'état liquide à l'état gazeux."),
    ]
))

lessons_out.append(lesson_block(
    "mouvement-objet-cm2", "Décrire le mouvement d'un objet", "physique-chimie", "cm2", "20 min",
    "Apprendre à décrire la trajectoire, la vitesse et le sens du mouvement d'un objet selon un point de repère.",
    ["Décrire une trajectoire (rectiligne, circulaire, quelconque)", "Comparer des vitesses de déplacement", "Comprendre qu'un mouvement se décrit par rapport à un repère"],
    [
        "Un objet est en mouvement quand sa position change au cours du temps, par rapport à un point de repère fixe. Le chemin suivi par l'objet s'appelle sa trajectoire : elle peut être rectiligne (une ligne droite, comme une bille qui roule sur une table), circulaire (un cercle, comme la pointe d'une aiguille d'horloge) ou quelconque (une forme irrégulière, comme le trajet d'un ballon lancé).",
        "La vitesse d'un objet indique la distance parcourue en un temps donné : plus un objet parcourt une grande distance en peu de temps, plus il est rapide. On peut comparer deux vitesses en observant qui arrive le premier sur une même distance, ou qui parcourt la plus grande distance dans le même temps.",
        "Le mouvement dépend toujours du point de vue : un passager assis dans un train est immobile par rapport au train, mais en mouvement par rapport au paysage qui défile dehors. C'est pourquoi on dit toujours qu'un objet est en mouvement (ou immobile) « par rapport à » un repère précis."
    ],
    svg_mouvement, "quiz-mouvement-objet-cm2", "Quiz — Décrire le mouvement d'un objet",
    [
        q("q1", "Quand dit-on qu'un objet est en mouvement ?", ["Quand il est très lourd", "Quand sa position change au cours du temps par rapport à un repère", "Quand il est de couleur vive", "Jamais"], 1, "Un objet est en mouvement quand sa position change au cours du temps par rapport à un repère fixe."),
        q("q2", "Comment appelle-t-on le chemin suivi par un objet en mouvement ?", ["Sa vitesse", "Sa trajectoire", "Son poids", "Sa masse"], 1, "Le chemin suivi par un objet en mouvement s'appelle sa trajectoire."),
        q("q3", "Quel est un exemple de trajectoire circulaire ?", ["Une bille qui roule en ligne droite", "La pointe d'une aiguille d'horloge", "Un ballon lancé au hasard", "Une voiture à l'arrêt"], 1, "La pointe d'une aiguille d'horloge suit une trajectoire circulaire."),
        q("q4", "Qu'indique la vitesse d'un objet ?", ["Sa couleur", "La distance parcourue en un temps donné", "Son poids", "Sa forme"], 1, "La vitesse indique la distance parcourue par un objet en un temps donné."),
        q("q5", "Un passager assis dans un train est-il immobile par rapport au train ?", ["Oui", "Non", "Cela dépend de la vitesse du train", "Impossible à dire"], 0, "Le passager assis ne bouge pas par rapport au train : il est immobile par rapport à ce repère."),
        q("q6", "Ce même passager est-il en mouvement par rapport au paysage extérieur ?", ["Non, jamais", "Oui, car le paysage défile", "Seulement s'il se lève", "Impossible à dire"], 1, "Par rapport au paysage extérieur qui défile, le passager est en mouvement."),
        q("q7", "Pourquoi dit-on toujours qu'un mouvement est « par rapport à » un repère ?", ["Par habitude sans raison", "Car le mouvement dépend du point de vue choisi", "Car les objets ne bougent jamais vraiment", "Ce n'est pas vrai"], 1, "Le mouvement ou l'immobilité d'un objet dépend toujours du repère par rapport auquel on l'observe."),
        q("q8", "Comment qualifie-t-on une trajectoire en ligne droite ?", ["Circulaire", "Rectiligne", "Quelconque", "Ondulée"], 1, "Une trajectoire en ligne droite est dite rectiligne."),
        q("q9", "Comment comparer les vitesses de deux objets sur la même distance ?", ["En regardant leur couleur", "En observant lequel arrive le premier", "C'est impossible", "En les pesant"], 1, "Sur une même distance, l'objet le plus rapide est celui qui arrive le premier."),
        q("q10", "Une trajectoire quelconque peut-elle être irrégulière ?", ["Non, jamais", "Oui, comme le trajet d'un ballon lancé", "Seulement en ligne droite", "Seulement en cercle"], 1, "Une trajectoire quelconque a une forme irrégulière, comme celle d'un ballon lancé."),
    ]
))

lessons_out.append(lesson_block(
    "energie-economiser-cm2", "Économiser l'énergie", "physique-chimie", "cm2", "20 min",
    "Identifier les sources d'énergie et adopter des gestes pour économiser l'énergie au quotidien.",
    ["Distinguer énergies renouvelables et non renouvelables", "Comprendre pourquoi économiser l'énergie est important", "Citer des gestes simples d'économie d'énergie"],
    [
        "L'énergie est nécessaire pour se déplacer, s'éclairer, se chauffer ou faire fonctionner des appareils. Certaines sources d'énergie sont renouvelables : elles se renouvellent naturellement et ne s'épuisent pas à l'échelle humaine (soleil, vent, eau, bois si replanté). D'autres sont non renouvelables : elles existent en quantité limitée sur Terre et mettent des millions d'années à se former (pétrole, charbon, gaz naturel).",
        "L'utilisation des énergies non renouvelables (énergies fossiles) libère du dioxyde de carbone qui contribue au changement climatique. C'est pourquoi de plus en plus d'énergie est produite grâce à des sources renouvelables : panneaux solaires, éoliennes, barrages hydroélectriques.",
        "Chacun peut économiser l'énergie au quotidien par des gestes simples : éteindre la lumière en quittant une pièce, ne pas laisser les appareils en veille, bien isoler son logement, privilégier la marche, le vélo ou les transports en commun, et baisser légèrement le chauffage en hiver. Ces économies réduisent à la fois la facture d'énergie et l'impact sur l'environnement."
    ],
    svg_energie, "quiz-energie-economiser-cm2", "Quiz — Économiser l'énergie",
    [
        q("q1", "Qu'est-ce qu'une énergie renouvelable ?", ["Une énergie qui s'épuise vite", "Une énergie qui se renouvelle naturellement", "Une énergie interdite", "Une énergie qui n'existe pas"], 1, "Une énergie renouvelable se renouvelle naturellement et ne s'épuise pas à l'échelle humaine."),
        q("q2", "Citez une source d'énergie renouvelable.", ["Le pétrole", "Le soleil", "Le charbon", "Le gaz naturel"], 1, "Le soleil est une source d'énergie renouvelable."),
        q("q3", "Citez une source d'énergie non renouvelable.", ["Le vent", "L'eau", "Le pétrole", "Le soleil"], 2, "Le pétrole est une énergie fossile, non renouvelable."),
        q("q4", "Que libère l'utilisation des énergies fossiles ?", ["De l'eau pure uniquement", "Du dioxyde de carbone qui contribue au changement climatique", "Rien du tout", "De l'oxygène uniquement"], 1, "Les énergies fossiles libèrent du dioxyde de carbone, qui contribue au changement climatique."),
        q("q5", "Quel appareil transforme l'énergie du vent en électricité ?", ["Le panneau solaire", "L'éolienne", "Le barrage", "La bougie"], 1, "L'éolienne transforme l'énergie du vent en électricité."),
        q("q6", "Citez un geste simple pour économiser l'énergie.", ["Laisser toutes les lumières allumées", "Éteindre la lumière en quittant une pièce", "Laisser les appareils toujours en veille", "Chauffer au maximum toute l'année"], 1, "Éteindre la lumière en quittant une pièce est un geste simple d'économie d'énergie."),
        q("q7", "Pourquoi isoler son logement permet-il d'économiser l'énergie ?", ["Cela n'a aucun effet", "Cela limite les pertes de chaleur, donc le besoin de chauffage", "Cela augmente la consommation", "Cela concerne uniquement l'été"], 1, "Une bonne isolation limite les pertes de chaleur et réduit donc les besoins en chauffage."),
        q("q8", "Le bois est-il une énergie renouvelable ?", ["Jamais", "Oui, s'il est replanté", "Seulement en hiver", "Non, jamais renouvelable"], 1, "Le bois est renouvelable si les arbres coupés sont replantés."),
        q("q9", "Quel moyen de transport économise le plus d'énergie ?", ["La voiture individuelle seule", "Le vélo ou la marche", "L'avion", "Le camion"], 1, "Le vélo et la marche ne consomment pas d'énergie fossile, contrairement à la voiture ou l'avion."),
        q("q10", "Pourquoi économiser l'énergie est-il important ?", ["Ce n'est pas important", "Cela réduit la facture et l'impact sur l'environnement", "Cela n'a aucun effet sur le climat", "Uniquement pour le confort"], 1, "Économiser l'énergie réduit à la fois la facture énergétique et l'impact environnemental."),
    ]
))

lessons_out.append(lesson_block(
    "objets-techniques-signal-cm2", "Objets techniques et signaux", "physique-chimie", "cm2", "20 min",
    "Comprendre comment un objet technique fonctionne grâce à des signaux, et s'initier à la logique de la programmation.",
    ["Décrire le fonctionnement d'un objet technique simple", "Comprendre ce qu'est un signal (lumineux, sonore, électrique)", "Relier une consigne simple à une action (logique de programmation)"],
    [
        "Un objet technique est fabriqué par l'être humain pour répondre à un besoin (se déplacer, communiquer, s'éclairer...). Beaucoup d'objets techniques fonctionnent grâce à une chaîne simple : un capteur détecte une information (un bouton pressé, une main devant un détecteur), cette information est traitée, puis un actionneur produit une action (une lumière s'allume, une porte s'ouvre).",
        "Un signal est une information transmise d'un point à un autre : un signal peut être lumineux (un feu tricolore), sonore (une sonnerie), ou électrique (un courant qui circule dans un fil). Les appareils numériques transforment ces signaux en une suite de 0 et de 1 (signal numérique) pour les traiter et les stocker.",
        "Programmer, c'est donner une suite d'instructions précises à une machine pour qu'elle réalise une tâche : par exemple, un robot programmé pour avancer, tourner à droite puis s'arrêter suit ces instructions dans l'ordre exact où elles ont été données. Si l'ordre des instructions change, le résultat change aussi : c'est pourquoi il faut réfléchir avec logique et précision avant de programmer."
    ],
    svg_signal, "quiz-objets-techniques-signal-cm2", "Quiz — Objets techniques et signaux",
    [
        q("q1", "Pourquoi l'être humain fabrique-t-il des objets techniques ?", ["Pour répondre à un besoin", "Par hasard", "Uniquement pour le loisir", "Sans aucune raison"], 0, "Un objet technique est fabriqué pour répondre à un besoin humain."),
        q("q2", "Quel est le rôle d'un capteur dans un objet technique ?", ["Il détecte une information", "Il ne sert à rien", "Il fabrique l'objet", "Il coupe l'électricité"], 0, "Un capteur détecte une information, comme un bouton pressé ou une présence."),
        q("q3", "Que fait un actionneur ?", ["Il détecte une information", "Il produit une action", "Il stocke l'énergie", "Il n'existe pas dans les objets techniques"], 1, "Un actionneur produit une action, comme allumer une lumière ou ouvrir une porte."),
        q("q4", "Qu'est-ce qu'un signal ?", ["Une information transmise d'un point à un autre", "Un objet technique complet", "Une source d'énergie", "Une matière première"], 0, "Un signal est une information transmise d'un point à un autre (lumineuse, sonore, électrique)."),
        q("q5", "Citez un exemple de signal lumineux.", ["Une sonnerie", "Un feu tricolore", "Un courant électrique invisible", "Un capteur de température"], 1, "Un feu tricolore est un exemple de signal lumineux."),
        q("q6", "En quoi les appareils numériques transforment-ils les signaux ?", ["En musique uniquement", "En une suite de 0 et de 1", "En chaleur", "En rien du tout"], 1, "Les appareils numériques transforment les signaux en une suite de 0 et de 1 (signal numérique)."),
        q("q7", "Que signifie « programmer » une machine ?", ["La réparer", "Lui donner une suite d'instructions précises", "La nettoyer", "L'éteindre définitivement"], 1, "Programmer, c'est donner une suite d'instructions précises à une machine pour qu'elle réalise une tâche."),
        q("q8", "L'ordre des instructions a-t-il de l'importance en programmation ?", ["Non, aucune importance", "Oui, si l'ordre change, le résultat change aussi", "Seulement pour les robots", "Jamais"], 1, "L'ordre des instructions est essentiel : le modifier change le résultat de la tâche exécutée."),
        q("q9", "Quel type de signal peut circuler dans un fil électrique ?", ["Un signal sonore uniquement", "Un signal électrique", "Un signal olfactif", "Aucun signal"], 1, "Un courant électrique qui circule dans un fil est un signal électrique."),
        q("q10", "Quelle est la chaîne typique de fonctionnement d'un objet technique automatisé ?", ["Capteur → traitement → actionneur", "Actionneur → capteur uniquement", "Traitement uniquement", "Il n'y a pas de chaîne"], 0, "La chaîne typique est : un capteur détecte, l'information est traitée, puis un actionneur agit."),
    ]
))

marker = "\n  {\n    "
idx = txt.index('slug: "electricite-securite-cm2"')
next_pos = txt.index(marker, idx) + 1
new_block = "".join(lessons_out)
txt = txt[:next_pos] + new_block + txt[next_pos:]

with open(path, 'w') as f:
    f.write(txt)
print("Physique-Chimie CM2 lessons inserted:", len(lessons_out))
