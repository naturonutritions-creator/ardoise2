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

VOIX = {
    "slug": "voix-active-passive-5e",
    "titre": "La voix active et la voix passive",
    "matiere": "francais", "niveau": "5e", "duree": "20 min",
    "resume": "Distinguer la voix active de la voix passive et savoir transformer une phrase de l'une à l'autre.",
    "objectifs": ["Reconnaître une phrase à la voix active et à la voix passive", "Identifier le complément d'agent", "Transformer une phrase active en phrase passive et inversement"],
    "contenu": [
        "À la voix active, le sujet fait l'action exprimée par le verbe : dans « Le chat mange la souris », le chat est actif, il accomplit l'action. À la voix passive, c'est le sujet qui subit l'action : dans « La souris est mangée par le chat », la souris ne fait rien, elle subit l'action du chat.",
        "Pour transformer une phrase active en phrase passive, le complément d'objet direct (COD) de la phrase active devient le sujet de la phrase passive, le sujet actif devient un complément d'agent introduit par « par » (parfois « de »), et le verbe se conjugue avec l'auxiliaire être suivi du participe passé du verbe. Seuls les verbes qui ont un COD, appelés verbes transitifs directs, peuvent être mis à la voix passive.",
        "Le complément d'agent n'est pas toujours exprimé : on peut dire « La maison a été construite » sans préciser par qui, quand cette information est inconnue, évidente ou sans importance pour le sens de la phrase. La voix passive est souvent utilisée pour mettre en valeur celui qui subit l'action plutôt que celui qui l'accomplit, ou dans un style plus formel, notamment scientifique ou administratif.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Dans « Le chat mange la souris », à quelle voix est le verbe ?", "choix": ["La voix passive", "La voix active", "Aucune des deux", "Le mode subjonctif"], "reponse": 1, "explication": "Le sujet « le chat » fait l'action : la phrase est à la voix active."},
        {"id": "q2", "enonce": "Dans « La souris est mangée par le chat », que devient le sujet ?", "choix": ["Il fait l'action", "Il subit l'action", "Il disparaît", "Il devient un complément circonstanciel"], "reponse": 1, "explication": "À la voix passive, le sujet subit l'action au lieu de la faire."},
        {"id": "q3", "enonce": "Comment appelle-t-on le groupe introduit par « par » qui indique qui fait l'action à la voix passive ?", "choix": ["Le sujet", "Le complément d'agent", "Le COD", "L'attribut du sujet"], "reponse": 1, "explication": "Le complément d'agent, introduit par « par » (parfois « de »), indique qui accomplit l'action à la voix passive."},
        {"id": "q4", "enonce": "Que devient le COD de la phrase active dans la phrase passive ?", "choix": ["Il disparaît", "Il devient le sujet de la phrase passive", "Il devient le complément d'agent", "Il reste COD"], "reponse": 1, "explication": "Le COD de la phrase active devient le sujet de la phrase passive."},
        {"id": "q5", "enonce": "Avec quel auxiliaire conjugue-t-on un verbe à la voix passive ?", "choix": ["Avoir", "Être", "Aller", "Aucun auxiliaire"], "reponse": 1, "explication": "Le verbe à la voix passive se conjugue avec l'auxiliaire être suivi du participe passé."},
        {"id": "q6", "enonce": "Tous les verbes peuvent-ils être mis à la voix passive ?", "choix": ["Oui, tous les verbes", "Non, seuls les verbes transitifs directs (avec COD)", "Non, aucun verbe ne le peut", "Seulement les verbes du premier groupe"], "reponse": 1, "explication": "Seuls les verbes ayant un COD, appelés verbes transitifs directs, peuvent être mis au passif."},
        {"id": "q7", "enonce": "Le complément d'agent est-il toujours exprimé ?", "choix": ["Oui, toujours obligatoirement", "Non, il peut être omis", "Il n'existe jamais", "Il remplace toujours le sujet"], "reponse": 1, "explication": "Le complément d'agent peut être omis quand l'information est inconnue, évidente ou sans importance."},
        {"id": "q8", "enonce": "Pourquoi utilise-t-on parfois la voix passive ?", "choix": ["Pour mettre en valeur celui qui subit l'action", "Pour rendre la phrase plus courte toujours", "Pour éviter d'utiliser un verbe", "Cela n'a aucun intérêt"], "reponse": 0, "explication": "La voix passive permet de mettre en valeur celui qui subit l'action plutôt que celui qui l'accomplit."},
        {"id": "q9", "enonce": "Quelle est la forme passive de « Le boulanger fait le pain » ?", "choix": ["Le pain fait le boulanger", "Le pain est fait par le boulanger", "Le boulanger est fait par le pain", "Le pain a fait le boulanger"], "reponse": 1, "explication": "Le COD « le pain » devient sujet, et « le boulanger » devient complément d'agent introduit par « par »."},
        {"id": "q10", "enonce": "La voix passive est souvent utilisée dans quel type de style ?", "choix": ["Le style familier uniquement", "Un style plus formel, scientifique ou administratif", "Le langage des textos", "Elle n'est jamais utilisée à l'écrit"], "reponse": 1, "explication": "La voix passive est fréquente dans un style formel, notamment scientifique ou administratif."},
    ],
}

DISCOURS = {
    "slug": "discours-direct-indirect-5e",
    "titre": "Le discours direct et le discours indirect",
    "matiere": "francais", "niveau": "5e", "duree": "20 min",
    "resume": "Distinguer le discours direct du discours indirect et savoir passer de l'un à l'autre.",
    "objectifs": ["Reconnaître le discours direct et ses marques typographiques", "Reconnaître le discours indirect", "Transformer une phrase au discours direct en discours indirect"],
    "contenu": [
        "Le discours direct rapporte les paroles de quelqu'un telles qu'elles ont été prononcées, en les insérant dans le texte avec des marques typographiques précises : guillemets, deux-points, tirets de dialogue, et des verbes introducteurs comme « dire », « demander », « répondre ». Par exemple : Marie a dit : « Je suis fatiguée. »",
        "Le discours indirect rapporte les mêmes paroles mais de façon intégrée dans la phrase, sans guillemets, généralement à l'aide d'une proposition subordonnée introduite par « que », « si » ou un mot interrogatif. La phrase précédente devient : Marie a dit qu'elle était fatiguée. On observe que le pronom « je » devient « elle » et que le temps du verbe change, du présent à l'imparfait : c'est ce qu'on appelle la concordance des temps.",
        "Passer du discours direct au discours indirect entraîne plusieurs transformations : les pronoms personnels et les déterminants possessifs changent de personne (je devient il ou elle, mon devient son), les temps verbaux reculent d'un cran quand le verbe introducteur est au passé (présent devenu imparfait, passé composé devenu plus-que-parfait, futur devenu conditionnel), et certains marqueurs de temps et de lieu changent aussi (aujourd'hui devient ce jour-là, ici devient là, demain devient le lendemain).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Comment rapporte-t-on des paroles au discours direct ?", "choix": ["Telles qu'elles ont été prononcées, avec des guillemets", "En les résumant sans guillemets", "En changeant tous les pronoms", "On ne peut pas rapporter des paroles au discours direct"], "reponse": 0, "explication": "Le discours direct rapporte les paroles telles quelles, avec des marques typographiques comme les guillemets."},
        {"id": "q2", "enonce": "Quelle ponctuation utilise-t-on typiquement au discours direct ?", "choix": ["Le point d'exclamation uniquement", "Les guillemets et les deux-points", "La virgule uniquement", "Aucune ponctuation particulière"], "reponse": 1, "explication": "Le discours direct utilise souvent des guillemets et des deux-points, avec un verbe introducteur."},
        {"id": "q3", "enonce": "Comment rapporte-t-on des paroles au discours indirect ?", "choix": ["Avec des guillemets", "De façon intégrée dans la phrase, sans guillemets", "En criant", "On ne peut pas le faire"], "reponse": 1, "explication": "Le discours indirect intègre les paroles rapportées dans la phrase, sans guillemets."},
        {"id": "q4", "enonce": "Quel mot introduit souvent une proposition au discours indirect ?", "choix": ["Que", "Alors", "Donc", "Mais"], "reponse": 0, "explication": "Le discours indirect utilise souvent une subordonnée introduite par « que », « si » ou un mot interrogatif."},
        {"id": "q5", "enonce": "Dans « Marie a dit : “Je suis fatiguée” » transformé en discours indirect, que devient « je » ?", "choix": ["Il reste « je »", "Il devient « elle »", "Il devient « nous »", "Il disparaît"], "reponse": 1, "explication": "Au discours indirect, les pronoms changent de personne : « je » devient « elle »."},
        {"id": "q6", "enonce": "Comment appelle-t-on le changement de temps verbal lors du passage au discours indirect ?", "choix": ["La conjugaison libre", "La concordance des temps", "L'accord du participe", "La voix passive"], "reponse": 1, "explication": "Ce phénomène s'appelle la concordance des temps."},
        {"id": "q7", "enonce": "Si le verbe introducteur est au passé, que devient un présent au discours indirect ?", "choix": ["Il reste au présent", "Il devient un imparfait", "Il devient un futur", "Il devient un passé simple"], "reponse": 1, "explication": "Après un verbe introducteur au passé, le présent devient un imparfait au discours indirect."},
        {"id": "q8", "enonce": "Que devient « demain » au discours indirect après un verbe introducteur au passé ?", "choix": ["Aujourd'hui", "Le lendemain", "Hier", "Il reste « demain »"], "reponse": 1, "explication": "Le marqueur de temps « demain » devient « le lendemain » au discours indirect."},
        {"id": "q9", "enonce": "Que devient « ici » au discours indirect ?", "choix": ["Là", "Maintenant", "Ailleurs", "Il reste « ici »"], "reponse": 0, "explication": "Le marqueur de lieu « ici » devient généralement « là » au discours indirect."},
        {"id": "q10", "enonce": "Que devient le déterminant possessif « mon » au discours indirect si le locuteur change ?", "choix": ["Il reste « mon »", "Il devient « son »", "Il devient « leur »", "Il disparaît"], "reponse": 1, "explication": "Les déterminants possessifs changent de personne, « mon » pouvant devenir « son »."},
    ],
}

SUBJONCTIF = {
    "slug": "subjonctif-present-5e",
    "titre": "Le subjonctif présent",
    "matiere": "francais", "niveau": "5e", "duree": "20 min",
    "resume": "Conjuguer et employer le subjonctif présent pour exprimer un souhait, un doute ou une obligation.",
    "objectifs": ["Conjuguer les verbes réguliers et les principaux verbes irréguliers au subjonctif présent", "Reconnaître les situations qui imposent l'emploi du subjonctif", "Distinguer indicatif et subjonctif selon le sens"],
    "contenu": [
        "Le subjonctif présent est un mode qui exprime un fait envisagé, souhaité, redouté ou soumis à une condition, plutôt qu'un fait certain, rôle réservé à l'indicatif. Il est presque toujours employé dans une proposition subordonnée introduite par « que », après des verbes ou expressions comme « il faut que », « je veux que », « je doute que », « bien que », « pour que ».",
        "Pour la plupart des verbes réguliers, le subjonctif présent se forme à partir du radical de la 3e personne du pluriel de l'indicatif présent, comme « ils parlent » qui donne « que je parle », auquel on ajoute les terminaisons -e, -es, -e, -ions, -iez, -ent. Par exemple : que je finisse, que tu finisses, qu'il finisse, que nous finissions, que vous finissiez, qu'ils finissent.",
        "Plusieurs verbes très fréquents ont un subjonctif irrégulier à connaître par cœur : être, comme dans « que je sois » et « que nous soyons » ; avoir, comme dans « que j'aie » et « que nous ayons » ; aller, comme dans « que j'aille » et « que nous allions » ; faire, comme dans « que je fasse » ; pouvoir, comme dans « que je puisse » ; savoir, comme dans « que je sache » ; vouloir, comme dans « que je veuille ». On distingue le subjonctif de l'indicatif au sens de la phrase : « Je pense qu'il vient » exprime un fait certain à l'indicatif, mais « Je doute qu'il vienne » exprime un fait incertain au subjonctif.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que exprime le subjonctif, contrairement à l'indicatif ?", "choix": ["Un fait certain", "Un fait envisagé, souhaité, redouté ou soumis à une condition", "Une question", "Un ordre uniquement"], "reponse": 1, "explication": "Le subjonctif exprime un fait envisagé, souhaité ou incertain, alors que l'indicatif exprime un fait certain."},
        {"id": "q2", "enonce": "Par quel mot le subjonctif est-il presque toujours introduit ?", "choix": ["Que", "Et", "Ou", "Donc"], "reponse": 0, "explication": "Le subjonctif est presque toujours employé dans une subordonnée introduite par « que »."},
        {"id": "q3", "enonce": "À partir de quoi se forme le subjonctif présent des verbes réguliers ?", "choix": ["Le radical de la 1re personne du singulier du futur", "Le radical de la 3e personne du pluriel de l'indicatif présent", "L'infinitif directement", "Le participe passé"], "reponse": 1, "explication": "Le subjonctif présent régulier se forme à partir du radical de « ils » à l'indicatif présent."},
        {"id": "q4", "enonce": "Quelle terminaison a « que je » au subjonctif présent pour un verbe régulier ?", "choix": ["-e", "-s", "-ai", "-ons"], "reponse": 0, "explication": "Le subjonctif présent prend la terminaison -e à la première personne du singulier."},
        {"id": "q5", "enonce": "Comment conjugue-t-on « être » au subjonctif présent, 1re personne du singulier ?", "choix": ["Que je suis", "Que je sois", "Que je serai", "Que je fus"], "reponse": 1, "explication": "Le verbe être est irrégulier au subjonctif : que je sois."},
        {"id": "q6", "enonce": "Comment conjugue-t-on « avoir » au subjonctif présent, 1re personne du singulier ?", "choix": ["Que j'ai", "Que j'aie", "Que j'aurai", "Que j'avais"], "reponse": 1, "explication": "Le verbe avoir est irrégulier au subjonctif : que j'aie."},
        {"id": "q7", "enonce": "Comment conjugue-t-on « aller » au subjonctif présent, 1re personne du pluriel ?", "choix": ["Que nous allons", "Que nous allions", "Que nous irons", "Que nous allâmes"], "reponse": 1, "explication": "Le verbe aller donne « que nous allions » au subjonctif présent."},
        {"id": "q8", "enonce": "Quelle phrase est correctement au subjonctif ?", "choix": ["Il faut que tu viens", "Il faut que tu viennes", "Il faut que tu viendras", "Il faut que tu vins"], "reponse": 1, "explication": "Après « il faut que », le verbe se met au subjonctif : que tu viennes."},
        {"id": "q9", "enonce": "Dans « Je pense qu'il vient », à quel mode est le verbe ?", "choix": ["Au subjonctif, car le fait est incertain", "À l'indicatif, car le fait est présenté comme certain", "À l'impératif", "Au conditionnel"], "reponse": 1, "explication": "« Penser que » exprime généralement un fait certain, donc suivi de l'indicatif."},
        {"id": "q10", "enonce": "Dans « Je doute qu'il vienne », à quel mode est le verbe et pourquoi ?", "choix": ["Au subjonctif, car le fait est incertain", "À l'indicatif, car le fait est certain", "À l'impératif", "Au futur simple"], "reponse": 0, "explication": "« Douter que » exprime l'incertitude, donc suivi du subjonctif : qu'il vienne."},
    ],
}

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "raconter-dialogue-oral-5e", [VOIX, DISCOURS, SUBJONCTIF])

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print("3 leçons Français 5e ajoutées.")
