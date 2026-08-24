# -*- coding: utf-8 -*-
PATH = "src/content/lessons.ts"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def lesson_block(d):
    obj = ", ".join('"' + esc(o) + '"' for o in d["objectifs"])
    cont = ", ".join('"' + esc(c) + '"' for c in d["contenu"])
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
        f'    objectifs: [{obj}],\n    contenu: [{cont}],\n    {quiz_block}\n  }},'
    )

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

L = []

# --- Grammaire et civilisation ---

L.append({
    "slug": "quatrieme-declinaison-latin-4e", "titre": "La 4e déclinaison (manus, manus)",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir la 4e déclinaison latine, moins fréquente mais présente dans des mots courants comme manus.",
    "objectifs": ["Reconnaître le génitif singulier -us de la 4e déclinaison", "Décliner un nom de la 4e déclinaison", "Connaître quelques noms fréquents de cette déclinaison"],
    "contenu": [
        "La 4e déclinaison se reconnaît à son génitif singulier en -us, comme manus, manus (la main). Elle regroupe surtout des noms féminins (manus, la main ; domus, la maison) et quelques noms masculins (exercitus, l'armée ; senatus, le sénat).",
        "Au nominatif singulier, ces noms se terminent souvent par -us, ce qui peut prêter à confusion avec la 2e déclinaison : seul le génitif singulier (-us au lieu de -i) permet de les distinguer avec certitude. Manus, manus (la main) ; exercitus, exercitus (l'armée).",
        "Le mot domus (la maison) est particulier : il emprunte certaines formes à la 2e déclinaison. On retient surtout l'expression domi, qui signifie « à la maison », un locatif qui s'utilise sans préposition, comme pour les noms de villes.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "À quoi reconnaît-on la 4e déclinaison ?", "choix": ["À son génitif singulier en -us", "À son génitif singulier en -i", "À son nominatif en -a", "À son accusatif en -em"], "reponse": 0, "explication": "La 4e déclinaison se reconnaît à son génitif singulier en -us."},
        {"id": "q2", "enonce": "Que signifie manus ?", "choix": ["La main", "La maison", "L'armée", "Le sénat"], "reponse": 0, "explication": "Manus, manus signifie « la main »."},
        {"id": "q3", "enonce": "Que signifie exercitus ?", "choix": ["L'armée", "La main", "La maison", "Le peuple"], "reponse": 0, "explication": "Exercitus, exercitus signifie « l'armée »."},
        {"id": "q4", "enonce": "Pourquoi la 4e déclinaison peut-elle être confondue avec la 2e ?", "choix": ["Car le nominatif singulier se termine souvent aussi par -us", "Car elles ont le même génitif", "Elles ne peuvent jamais être confondues", "Car les deux sont toujours neutres"], "reponse": 0, "explication": "Le nominatif singulier en -us est commun aux deux déclinaisons, seul le génitif permet de les distinguer."},
        {"id": "q5", "enonce": "Quel genre domine dans la 4e déclinaison ?", "choix": ["Le féminin, avec quelques masculins", "Le masculin uniquement", "Le neutre uniquement", "Aucun genre n'est possible"], "reponse": 0, "explication": "La 4e déclinaison regroupe surtout des noms féminins, avec quelques masculins comme exercitus."},
        {"id": "q6", "enonce": "Que signifie domus ?", "choix": ["La maison", "La main", "L'armée", "Le sénat"], "reponse": 0, "explication": "Domus, domus signifie « la maison »."},
        {"id": "q7", "enonce": "Que signifie l'expression domi ?", "choix": ["À la maison", "Vers la maison", "Loin de la maison", "Dans l'armée"], "reponse": 0, "explication": "Domi est un locatif signifiant « à la maison », utilisé sans préposition."},
        {"id": "q8", "enonce": "Domus emprunte-t-il des formes à une autre déclinaison ?", "choix": ["Oui, à la 2e déclinaison", "Non, jamais", "Oui, à la 3e déclinaison", "Oui, à la 5e déclinaison"], "reponse": 0, "explication": "Domus emprunte certaines formes à la 2e déclinaison, ce qui en fait un mot particulier."},
        {"id": "q9", "enonce": "Que signifie senatus ?", "choix": ["Le sénat", "L'armée", "La main", "La maison"], "reponse": 0, "explication": "Senatus, senatus signifie « le sénat »."},
        {"id": "q10", "enonce": "Quel est le génitif singulier de manus ?", "choix": ["Manus", "Mani", "Manui", "Manuum"], "reponse": 0, "explication": "Le génitif singulier de manus est manus, identique au nominatif, typique de la 4e déclinaison."},
    ],
})

L.append({
    "slug": "cinquieme-declinaison-latin-4e", "titre": "La 5e déclinaison (dies, diei)",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir la 5e déclinaison latine, illustrée par des mots courants comme dies (le jour) et res (la chose).",
    "objectifs": ["Reconnaître le génitif singulier -ei de la 5e déclinaison", "Décliner dies et res", "Connaître des expressions latines formées avec res"],
    "contenu": [
        "La 5e déclinaison se reconnaît à son génitif singulier en -ei, comme dies, diei (le jour). Elle regroupe peu de noms, presque tous féminins, à l'exception de dies qui peut être masculin ou féminin selon le sens.",
        "Le nom res, rei (la chose, l'affaire) est l'un des plus fréquents de cette déclinaison, et il entre dans de nombreuses expressions : res publica (la chose publique, d'où vient le mot « république »), res gestae (les hauts faits, littéralement « les choses accomplies »).",
        "Dies, diei (le jour) a donné de nombreux mots français : diurne, journal (via le latin médiéval diurnalis), ou encore le mot « jour » lui-même, issu d'une évolution du latin populaire. On retient aussi meridies (midi), littéralement « le milieu du jour ».",
    ],
    "quiz": [
        {"id": "q1", "enonce": "À quoi reconnaît-on la 5e déclinaison ?", "choix": ["À son génitif singulier en -ei", "À son génitif singulier en -us", "À son nominatif en -a", "À son accusatif en -um"], "reponse": 0, "explication": "La 5e déclinaison se reconnaît à son génitif singulier en -ei."},
        {"id": "q2", "enonce": "Que signifie dies ?", "choix": ["Le jour", "La chose", "La main", "L'armée"], "reponse": 0, "explication": "Dies, diei signifie « le jour »."},
        {"id": "q3", "enonce": "Que signifie res ?", "choix": ["La chose, l'affaire", "Le jour", "Le sénat", "L'armée"], "reponse": 0, "explication": "Res, rei signifie « la chose » ou « l'affaire »."},
        {"id": "q4", "enonce": "D'où vient le mot français « république » ?", "choix": ["De res publica, « la chose publique »", "De rex, « le roi »", "De regnum, « le royaume »", "De civitas, « la cité »"], "reponse": 0, "explication": "République vient de l'expression latine res publica, « la chose publique »."},
        {"id": "q5", "enonce": "Que signifie littéralement res gestae ?", "choix": ["Les choses accomplies, les hauts faits", "Les choses publiques", "Le jour accompli", "Les affaires du sénat"], "reponse": 0, "explication": "Res gestae signifie littéralement « les choses accomplies », c'est-à-dire les hauts faits."},
        {"id": "q6", "enonce": "Quel genre a généralement dies ?", "choix": ["Masculin ou féminin selon le sens", "Toujours neutre", "Toujours féminin", "Toujours masculin"], "reponse": 0, "explication": "Dies peut être masculin ou féminin selon le sens de la phrase."},
        {"id": "q7", "enonce": "Que signifie meridies ?", "choix": ["Midi", "Minuit", "Le matin", "Le soir"], "reponse": 0, "explication": "Meridies signifie « midi », littéralement « le milieu du jour »."},
        {"id": "q8", "enonce": "Combien de noms fréquents compte environ la 5e déclinaison ?", "choix": ["Peu de noms, presque tous féminins", "Des centaines de noms", "Uniquement des noms masculins", "Autant que la 1ère déclinaison"], "reponse": 0, "explication": "La 5e déclinaison regroupe peu de noms, presque tous féminins."},
        {"id": "q9", "enonce": "Quel mot français dérive de dies ?", "choix": ["Diurne", "Nocturne", "Solaire", "Lunaire"], "reponse": 0, "explication": "Diurne dérive du latin dies, « le jour »."},
        {"id": "q10", "enonce": "Quel est le génitif singulier de dies ?", "choix": ["Diei", "Dii", "Diorum", "Diebus"], "reponse": 0, "explication": "Le génitif singulier de dies est diei, caractéristique de la 5e déclinaison."},
    ],
})

L.append({
    "slug": "pronoms-personnels-latin-4e", "titre": "Les pronoms personnels : ego, tu, is, ea, id",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Apprendre à décliner les pronoms personnels latins et à les utiliser pour désigner les personnes.",
    "objectifs": ["Décliner ego et tu aux principaux cas", "Connaître is, ea, id pour la 3e personne", "Comprendre pourquoi le pronom sujet est souvent omis en latin"],
    "contenu": [
        "Le pronom de la première personne, ego (je), se décline ainsi aux cas principaux : nominatif ego, génitif mei, datif mihi, accusatif me, ablatif me. Le pronom de la deuxième personne, tu (tu), suit un schéma similaire : nominatif tu, génitif tui, datif tibi, accusatif te, ablatif te.",
        "Pour la troisième personne, le latin utilise is (masculin), ea (féminin), id (neutre), qui signifient à la fois « il/elle » et « celui-ci/celle-ci ». Ils se déclinent comme des adjectifs, en s'accordant en genre, nombre et cas avec le nom qu'ils remplacent : is la vidit (lui, il l'a vue) ; eam vidit (il l'a vue, elle).",
        "En latin, le verbe porte déjà l'information de la personne grâce à sa terminaison (amo = j'aime, amas = tu aimes), c'est pourquoi le pronom sujet (ego, tu) est très souvent omis, sauf pour insister ou marquer une opposition : Ego lego, tu scribis (Moi, je lis, toi, tu écris).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie ego ?", "choix": ["Je", "Tu", "Il", "Nous"], "reponse": 0, "explication": "Ego est le pronom personnel de la première personne du singulier, « je »."},
        {"id": "q2", "enonce": "Quel est l'accusatif de ego ?", "choix": ["Me", "Mei", "Mihi", "Ego"], "reponse": 0, "explication": "L'accusatif de ego est me."},
        {"id": "q3", "enonce": "Quel est le datif de tu ?", "choix": ["Tibi", "Te", "Tui", "Tu"], "reponse": 0, "explication": "Le datif de tu est tibi."},
        {"id": "q4", "enonce": "Que signifie is, ea, id ?", "choix": ["Il, elle, cela (3e personne)", "Je, tu, il", "Nous, vous, eux", "Ceci, cela (démonstratif uniquement)"], "reponse": 0, "explication": "Is, ea, id signifie « il, elle, cela », pronom de la 3e personne."},
        {"id": "q5", "enonce": "Comment se déclinent is, ea, id ?", "choix": ["Comme des adjectifs, en s'accordant en genre, nombre et cas", "Ils ne se déclinent jamais", "Uniquement au nominatif", "Comme des verbes"], "reponse": 0, "explication": "Is, ea, id se déclinent comme des adjectifs, en s'accordant avec le nom qu'ils remplacent."},
        {"id": "q6", "enonce": "Pourquoi le pronom sujet est-il souvent omis en latin ?", "choix": ["Car le verbe porte déjà l'information de la personne", "Car le latin n'a pas de pronoms", "Par erreur des scribes", "Car c'est interdit par la grammaire"], "reponse": 0, "explication": "Le verbe latin porte l'information de la personne dans sa terminaison, rendant le pronom souvent inutile."},
        {"id": "q7", "enonce": "Quand utilise-t-on quand même le pronom sujet en latin ?", "choix": ["Pour insister ou marquer une opposition", "Jamais, il est toujours omis", "Uniquement à l'impératif", "Uniquement au pluriel"], "reponse": 0, "explication": "Le pronom sujet s'utilise pour insister ou marquer une opposition, comme dans « ego lego, tu scribis »."},
        {"id": "q8", "enonce": "Que signifie amas ?", "choix": ["Tu aimes", "J'aime", "Il aime", "Nous aimons"], "reponse": 0, "explication": "Amas signifie « tu aimes », la terminaison -as indiquant la 2e personne du singulier."},
        {"id": "q9", "enonce": "Quel est le génitif de ego ?", "choix": ["Mei", "Me", "Mihi", "Meus"], "reponse": 0, "explication": "Le génitif de ego est mei."},
        {"id": "q10", "enonce": "Quel est l'ablatif de tu ?", "choix": ["Te", "Tui", "Tibi", "Tu"], "reponse": 0, "explication": "L'ablatif de tu est te, identique à l'accusatif."},
    ],
})

L.append({
    "slug": "pronoms-relatifs-latin-4e", "titre": "Les pronoms relatifs qui, quae, quod",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Apprendre à utiliser le pronom relatif latin qui, quae, quod pour relier deux propositions.",
    "objectifs": ["Décliner le pronom relatif qui, quae, quod", "Identifier son antécédent dans une phrase", "Traduire une proposition relative latine"],
    "contenu": [
        "Le pronom relatif latin qui (masculin), quae (féminin), quod (neutre) correspond au français « qui », « que » ou « lequel ». Il s'accorde en genre et en nombre avec son antécédent (le nom qu'il remplace), mais son cas dépend de sa fonction dans la proposition relative.",
        "Exemple : Puella quam video pulchra est (La jeune fille que je vois est belle). Ici, quam est à l'accusatif féminin singulier, car elle est complément d'objet direct du verbe video, tout en s'accordant en genre et en nombre avec son antécédent puella (féminin singulier).",
        "Autre exemple, au nominatif : Vir qui venit dominus est (L'homme qui vient est le maître). Ici, qui est sujet du verbe venit, donc au nominatif, mais il s'accorde avec son antécédent vir (masculin singulier). Il faut donc toujours distinguer le genre/nombre (donnés par l'antécédent) du cas (donné par la fonction dans la relative).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie qui, quae, quod ?", "choix": ["Qui, que, lequel", "Je, tu, il", "Ceci, cela", "Le, la, les"], "reponse": 0, "explication": "Qui, quae, quod est le pronom relatif latin, correspondant à « qui », « que » ou « lequel »."},
        {"id": "q2", "enonce": "Avec quoi le pronom relatif s'accorde-t-il en genre et en nombre ?", "choix": ["Son antécédent", "Le verbe de la relative", "Le sujet de la phrase principale", "Il ne s'accorde jamais"], "reponse": 0, "explication": "Le pronom relatif s'accorde en genre et en nombre avec son antécédent."},
        {"id": "q3", "enonce": "De quoi dépend le cas du pronom relatif ?", "choix": ["De sa fonction dans la proposition relative", "Toujours du nominatif", "Du genre de l'antécédent uniquement", "Du nombre de mots de la phrase"], "reponse": 0, "explication": "Le cas du pronom relatif dépend de sa fonction (sujet, complément...) dans la proposition relative."},
        {"id": "q4", "enonce": "Dans « Puella quam video pulchra est », quelle est la fonction de quam ?", "choix": ["Complément d'objet direct de video", "Sujet de video", "Complément du nom", "Attribut du sujet"], "reponse": 0, "explication": "Quam est complément d'objet direct de video, d'où l'accusatif."},
        {"id": "q5", "enonce": "Traduisez : Puella quam video pulchra est.", "choix": ["La jeune fille que je vois est belle.", "La jeune fille qui voit est belle.", "Je vois la belle jeune fille.", "La jeune fille est vue et belle."], "reponse": 0, "explication": "Puella quam video pulchra est se traduit par « La jeune fille que je vois est belle »."},
        {"id": "q6", "enonce": "Dans « Vir qui venit dominus est », quelle est la fonction de qui ?", "choix": ["Sujet de venit", "Complément d'objet de venit", "Complément du nom", "Attribut"], "reponse": 0, "explication": "Qui est sujet du verbe venit, il est donc au nominatif."},
        {"id": "q7", "enonce": "Traduisez : Vir qui venit dominus est.", "choix": ["L'homme qui vient est le maître.", "L'homme que je vois est le maître.", "Le maître qui vient est un homme.", "L'homme vient chez le maître."], "reponse": 0, "explication": "Vir qui venit dominus est se traduit par « L'homme qui vient est le maître »."},
        {"id": "q8", "enonce": "Quel est le genre de quae ?", "choix": ["Féminin", "Masculin", "Neutre", "Il n'a pas de genre"], "reponse": 0, "explication": "Quae est la forme féminine du pronom relatif au nominatif singulier (ou neutre pluriel)."},
        {"id": "q9", "enonce": "Quel est le genre de quod ?", "choix": ["Neutre", "Masculin", "Féminin", "Il n'a pas de genre"], "reponse": 0, "explication": "Quod est la forme neutre du pronom relatif au nominatif et accusatif singulier."},
        {"id": "q10", "enonce": "Le cas et le genre/nombre du pronom relatif dépendent-ils toujours de la même chose ?", "choix": ["Non : le genre/nombre vient de l'antécédent, le cas de la fonction dans la relative", "Oui, toujours de l'antécédent", "Oui, toujours de la fonction", "Le pronom relatif ne varie jamais"], "reponse": 0, "explication": "Il faut distinguer le genre/nombre (donné par l'antécédent) du cas (donné par la fonction dans la proposition relative)."},
    ],
})

L.append({
    "slug": "futur-simple-indicatif-latin-4e", "titre": "Le futur simple de l'indicatif",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Apprendre à former le futur simple latin pour les quatre conjugaisons.",
    "objectifs": ["Former le futur des verbes en -are et -ere avec -bo", "Former le futur des verbes en -ere (3e conj.) et -ire avec -am", "Traduire des phrases au futur"],
    "contenu": [
        "Pour les verbes de la 1ère conjugaison (-are) et de la 2e conjugaison (-ere long), le futur se forme avec l'infixe -b- suivi des terminaisons personnelles : amabo (j'aimerai), amabis, amabit, amabimus, amabitis, amabunt. De même pour la 2e conjugaison : monebo (j'avertirai), monebis...",
        "Pour les verbes de la 3e conjugaison (-ere bref) et de la 4e conjugaison (-ire), le futur se forme différemment, avec les voyelles -a-/-e- : legam, leges, leget, legemus, legetis, legent (je lirai...) ; audiam, audies, audiet... (j'entendrai...).",
        "Le verbe esse (être) a un futur irrégulier à mémoriser : ero (je serai), eris, erit, erimus, eritis, erunt. Ce futur d'esse sert aussi à former le futur antérieur d'autres verbes, comme amavero (j'aurai aimé).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Avec quel infixe se forme le futur des verbes en -are ?", "choix": ["-b-", "-a-", "-s-", "-v-"], "reponse": 0, "explication": "Le futur des verbes en -are se forme avec l'infixe -b- : amabo."},
        {"id": "q2", "enonce": "Que signifie amabo ?", "choix": ["J'aimerai", "J'aimais", "J'ai aimé", "J'aime"], "reponse": 0, "explication": "Amabo est la première personne du futur d'amare, « j'aimerai »."},
        {"id": "q3", "enonce": "Comment se forme le futur des verbes de la 3e conjugaison (-ere bref) ?", "choix": ["Avec les voyelles -a-/-e-", "Avec l'infixe -b-", "Il n'existe pas de futur pour ces verbes", "Avec l'infixe -v-"], "reponse": 0, "explication": "Les verbes de la 3e conjugaison forment leur futur avec les voyelles -a-/-e- : legam, leges..."},
        {"id": "q4", "enonce": "Que signifie legam ?", "choix": ["Je lirai", "Je lisais", "J'ai lu", "Je lis"], "reponse": 0, "explication": "Legam est la première personne du futur de legere, « je lirai »."},
        {"id": "q5", "enonce": "Que signifie audiam ?", "choix": ["J'entendrai", "J'entendais", "J'ai entendu", "J'entends"], "reponse": 0, "explication": "Audiam est la première personne du futur de audire, « j'entendrai »."},
        {"id": "q6", "enonce": "Quel est le futur du verbe esse à la première personne ?", "choix": ["Ero", "Sum", "Eram", "Fui"], "reponse": 0, "explication": "Le futur d'esse est irrégulier : ero, « je serai »."},
        {"id": "q7", "enonce": "Le futur d'esse est-il régulier ?", "choix": ["Non, il est irrégulier", "Oui, parfaitement régulier", "Il n'a pas de futur", "Il suit la 3e conjugaison"], "reponse": 0, "explication": "Le futur d'esse est irrégulier et doit être mémorisé : ero, eris, erit..."},
        {"id": "q8", "enonce": "Que sert à former le futur d'esse, en plus de son propre futur ?", "choix": ["Le futur antérieur d'autres verbes", "L'imparfait des autres verbes", "Le présent des autres verbes", "Rien d'autre"], "reponse": 0, "explication": "Le futur d'esse sert aussi à former le futur antérieur, comme amavero (j'aurai aimé)."},
        {"id": "q9", "enonce": "Quelle est la terminaison de la 3e personne du pluriel au futur (1ère conjugaison) ?", "choix": ["-bunt", "-bant", "-nt", "-bimus"], "reponse": 0, "explication": "La 3e personne du pluriel du futur en -are se termine par -bunt : amabunt."},
        {"id": "q10", "enonce": "Que signifie monebis ?", "choix": ["Tu avertiras", "Tu avertissais", "Tu as averti", "Tu avertis"], "reponse": 0, "explication": "Monebis est la deuxième personne du futur de monere, « tu avertiras »."},
    ],
})

L.append({
    "slug": "plus-que-parfait-indicatif-latin-4e", "titre": "Le plus-que-parfait de l'indicatif",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Apprendre à former et traduire le plus-que-parfait latin, qui exprime une action antérieure à une autre action passée.",
    "objectifs": ["Former le plus-que-parfait à partir du radical du parfait", "Comprendre l'usage du plus-que-parfait", "Traduire des phrases au plus-que-parfait"],
    "contenu": [
        "Le plus-que-parfait se forme à partir du radical du parfait, auquel on ajoute les terminaisons -eram, -eras, -erat, -eramus, -eratis, -erant. Pour amare (parfait amav-), cela donne : amaveram (j'avais aimé), amaveras, amaverat, amaveramus, amaveratis, amaverant.",
        "Ces terminaisons rappellent l'imparfait du verbe esse (eram, eras, erat...), ce qui facilite leur mémorisation : le plus-que-parfait s'analyse d'ailleurs historiquement comme le radical du parfait suivi de l'imparfait de esse.",
        "Le plus-que-parfait exprime une action antérieure à une autre action déjà passée : Cum Roma venerat, oppidum jam captum erat (Quand il était arrivé à Rome, la ville avait déjà été prise). On l'utilise donc pour marquer un ordre chronologique entre deux événements du passé.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "À partir de quel radical se forme le plus-que-parfait ?", "choix": ["Le radical du parfait", "Le radical du présent", "L'infinitif complet", "Le radical du futur"], "reponse": 0, "explication": "Le plus-que-parfait se forme à partir du radical du parfait."},
        {"id": "q2", "enonce": "Quelles terminaisons s'ajoutent au radical du parfait ?", "choix": ["-eram, -eras, -erat...", "-bam, -bas, -bat...", "-bo, -bis, -bit...", "-o, -s, -t..."], "reponse": 0, "explication": "Les terminaisons du plus-que-parfait sont -eram, -eras, -erat, -eramus, -eratis, -erant."},
        {"id": "q3", "enonce": "Que signifie amaveram ?", "choix": ["J'avais aimé", "J'aimerai", "J'aime", "J'ai aimé"], "reponse": 0, "explication": "Amaveram est la première personne du plus-que-parfait d'amare, « j'avais aimé »."},
        {"id": "q4", "enonce": "À quel autre temps ressemblent les terminaisons du plus-que-parfait ?", "choix": ["L'imparfait du verbe esse", "Le présent du verbe esse", "Le futur du verbe esse", "Le parfait du verbe esse"], "reponse": 0, "explication": "Les terminaisons du plus-que-parfait rappellent l'imparfait d'esse (eram, eras, erat...)."},
        {"id": "q5", "enonce": "Qu'exprime le plus-que-parfait ?", "choix": ["Une action antérieure à une autre action passée", "Une action future", "Une action présente habituelle", "Un ordre"], "reponse": 0, "explication": "Le plus-que-parfait exprime une action antérieure à une autre action déjà passée."},
        {"id": "q6", "enonce": "Traduisez : Cum Roma venerat, oppidum jam captum erat.", "choix": ["Quand il était arrivé à Rome, la ville avait déjà été prise.", "Quand il arrive à Rome, la ville est prise.", "Il arrivera à Rome quand la ville sera prise.", "Rome avait pris la ville."], "reponse": 0, "explication": "Cette phrase exprime deux actions passées, l'une antérieure à l'autre grâce au plus-que-parfait."},
        {"id": "q7", "enonce": "Le plus-que-parfait marque-t-il un ordre chronologique entre deux événements passés ?", "choix": ["Oui", "Non, jamais", "Uniquement au pluriel", "Uniquement à la voix passive"], "reponse": 0, "explication": "Le plus-que-parfait sert précisément à marquer qu'une action est antérieure à une autre action passée."},
        {"id": "q8", "enonce": "Quelle est la terminaison de la 1ère personne du pluriel au plus-que-parfait ?", "choix": ["-eramus", "-erimus", "-abamus", "-bimus"], "reponse": 0, "explication": "La 1ère personne du pluriel du plus-que-parfait a la terminaison -eramus."},
        {"id": "q9", "enonce": "Que signifie amaveratis ?", "choix": ["Vous aviez aimé", "Vous aimerez", "Vous aimez", "Vous avez aimé"], "reponse": 0, "explication": "Amaveratis est la 2e personne du pluriel du plus-que-parfait, « vous aviez aimé »."},
        {"id": "q10", "enonce": "Le plus-que-parfait se forme-t-il sur le radical du présent ?", "choix": ["Non, sur le radical du parfait", "Oui, toujours", "Uniquement pour les verbes en -are", "Uniquement au pluriel"], "reponse": 0, "explication": "Le plus-que-parfait se forme toujours sur le radical du parfait, jamais sur celui du présent."},
    ],
})

L.append({
    "slug": "republique-romaine-institutions-latin-4e", "titre": "La République romaine et ses institutions",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir le fonctionnement de la République romaine et ses principales institutions politiques.",
    "objectifs": ["Connaître le rôle du Sénat", "Connaître les principaux magistrats romains", "Comprendre le principe de la collégialité et de l'annualité des charges"],
    "contenu": [
        "La République romaine (de 509 à 27 avant J.-C. environ) repose sur un partage du pouvoir entre plusieurs institutions. Le Sénat (senatus), composé d'anciens magistrats, conseille les dirigeants et gère notamment les affaires étrangères et les finances publiques, sans détenir formellement le pouvoir exécutif.",
        "Les magistrats sont élus chaque année par le peuple : les deux consuls dirigent l'État et commandent les armées, les préteurs rendent la justice, les édiles s'occupent de l'entretien de la ville et de l'organisation des jeux, les questeurs gèrent les finances publiques.",
        "Deux principes fondamentaux organisent ces charges : la collégialité (chaque magistrature est occupée par au moins deux personnes, qui peuvent se contrôler mutuellement) et l'annualité (les charges durent un an, ce qui limite les risques de prise de pouvoir personnel). Les tribuns de la plèbe, quant à eux, protègent spécifiquement les intérêts du peuple et disposent d'un droit de veto.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "De quand à quand s'étend approximativement la République romaine ?", "choix": ["De 509 à 27 avant J.-C. environ", "De 27 avant J.-C. à 476 après J.-C.", "De 753 à 509 avant J.-C.", "Du Ve au XVe siècle après J.-C."], "reponse": 0, "explication": "La République romaine s'étend approximativement de 509 à 27 avant J.-C."},
        {"id": "q2", "enonce": "De quoi est composé le Sénat ?", "choix": ["D'anciens magistrats", "Du peuple entier", "Uniquement des consuls", "Uniquement des esclaves affranchis"], "reponse": 0, "explication": "Le Sénat est composé d'anciens magistrats romains."},
        {"id": "q3", "enonce": "Combien y a-t-il de consuls en même temps ?", "choix": ["Deux", "Un seul", "Quatre", "Dix"], "reponse": 0, "explication": "Il y a toujours deux consuls en même temps, élus pour un an."},
        {"id": "q4", "enonce": "Que font les préteurs ?", "choix": ["Ils rendent la justice", "Ils gèrent les finances", "Ils organisent les jeux", "Ils commandent l'armée uniquement"], "reponse": 0, "explication": "Les préteurs sont chargés de rendre la justice."},
        {"id": "q5", "enonce": "Que font les édiles ?", "choix": ["Ils s'occupent de l'entretien de la ville et des jeux", "Ils dirigent l'armée", "Ils rendent la justice", "Ils président le Sénat"], "reponse": 0, "explication": "Les édiles s'occupent de l'entretien de la ville et de l'organisation des jeux."},
        {"id": "q6", "enonce": "Que gèrent les questeurs ?", "choix": ["Les finances publiques", "La justice", "Les jeux du cirque", "L'armée uniquement"], "reponse": 0, "explication": "Les questeurs gèrent les finances publiques."},
        {"id": "q7", "enonce": "Qu'est-ce que la collégialité ?", "choix": ["Chaque magistrature est occupée par au moins deux personnes", "Une seule personne détient tout le pouvoir", "Les magistrats sont élus à vie", "Le Sénat gouverne seul"], "reponse": 0, "explication": "La collégialité signifie que chaque magistrature est partagée entre au moins deux personnes."},
        {"id": "q8", "enonce": "Qu'est-ce que l'annualité des charges ?", "choix": ["Les magistratures durent un an", "Les magistratures sont à vie", "Les magistratures durent dix ans", "Il n'y a pas de durée définie"], "reponse": 0, "explication": "L'annualité signifie que les charges de magistrat durent un an, limitant les risques de prise de pouvoir personnel."},
        {"id": "q9", "enonce": "Qui protège spécifiquement les intérêts du peuple ?", "choix": ["Les tribuns de la plèbe", "Les consuls", "Le Sénat", "Les préteurs"], "reponse": 0, "explication": "Les tribuns de la plèbe protègent spécifiquement les intérêts du peuple."},
        {"id": "q10", "enonce": "Que possèdent les tribuns de la plèbe ?", "choix": ["Un droit de veto", "Le commandement de l'armée", "Le pouvoir judiciaire suprême", "La présidence du Sénat"], "reponse": 0, "explication": "Les tribuns de la plèbe disposent d'un droit de veto pour protéger le peuple."},
    ],
})

L.append({
    "slug": "pompei-ville-figee-latin-4e", "titre": "Pompéi : une ville figée dans le temps",
    "matiere": "latin", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir la ville de Pompéi et ce que son ensevelissement par le Vésuve nous apprend sur la vie quotidienne romaine.",
    "objectifs": ["Connaître les circonstances de la destruction de Pompéi", "Comprendre pourquoi Pompéi est une source historique exceptionnelle", "Découvrir des éléments de la vie quotidienne pompéienne"],
    "contenu": [
        "En l'an 79 après J.-C., le volcan Vésuve entre en éruption et ensevelit la ville de Pompéi, ainsi que la ville voisine d'Herculanum, sous plusieurs mètres de cendres et de lapilli (petites pierres volcaniques). Cet événement est connu grâce au témoignage écrit de Pline le Jeune, qui a assisté à la scène depuis l'autre côté du golfe de Naples.",
        "Paradoxalement, cette catastrophe a permis de conserver la ville presque intacte, figée à l'instant de sa destruction : les rues, les maisons, les fresques murales, les objets du quotidien et même les formes laissées par les corps des victimes ont traversé les siècles sans être détruits par le temps ou modifiés par des reconstructions ultérieures.",
        "Les fouilles archéologiques, commencées au XVIIIe siècle et toujours en cours aujourd'hui, ont révélé une mine d'informations sur la vie quotidienne romaine : plans des maisons avec leur atrium et leur péristyle, thermes publics, amphithéâtre, boutiques avec leurs enseignes peintes, et même des graffitis laissés par les habitants sur les murs de la ville.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "En quelle année Pompéi a-t-elle été détruite ?", "choix": ["79 après J.-C.", "509 avant J.-C.", "27 avant J.-C.", "410 après J.-C."], "reponse": 0, "explication": "Pompéi a été détruite en l'an 79 après J.-C. par l'éruption du Vésuve."},
        {"id": "q2", "enonce": "Quel volcan a détruit Pompéi ?", "choix": ["Le Vésuve", "L'Etna", "Le Stromboli", "Le Vulcano"], "reponse": 0, "explication": "Le Vésuve est le volcan qui est entré en éruption en 79 après J.-C."},
        {"id": "q3", "enonce": "Quelle autre ville a été ensevelie en même temps que Pompéi ?", "choix": ["Herculanum", "Rome", "Ostie", "Capoue"], "reponse": 0, "explication": "Herculanum a été ensevelie en même temps que Pompéi lors de l'éruption du Vésuve."},
        {"id": "q4", "enonce": "Qui a laissé un témoignage écrit de cette éruption ?", "choix": ["Pline le Jeune", "Jules César", "Cicéron", "Virgile"], "reponse": 0, "explication": "Pline le Jeune a laissé un témoignage écrit précieux de l'éruption du Vésuve."},
        {"id": "q5", "enonce": "Sous quoi Pompéi a-t-elle été ensevelie ?", "choix": ["Des cendres et des lapilli", "De la lave uniquement", "De l'eau", "De la neige"], "reponse": 0, "explication": "Pompéi a été ensevelie sous plusieurs mètres de cendres et de lapilli (pierres volcaniques)."},
        {"id": "q6", "enonce": "Pourquoi Pompéi est-elle une source historique exceptionnelle ?", "choix": ["Car elle a été figée intacte au moment de sa destruction", "Car elle a été entièrement reconstruite", "Car aucune fouille n'y a jamais été menée", "Car elle n'a jamais existé réellement"], "reponse": 0, "explication": "Pompéi a été conservée quasiment intacte, figée à l'instant de sa destruction, sans reconstruction ultérieure."},
        {"id": "q7", "enonce": "Quand ont commencé les fouilles archéologiques de Pompéi ?", "choix": ["Au XVIIIe siècle", "Au Moyen Âge", "Au XXe siècle uniquement", "Dans l'Antiquité"], "reponse": 0, "explication": "Les fouilles archéologiques de Pompéi ont commencé au XVIIIe siècle."},
        {"id": "q8", "enonce": "Qu'est-ce que l'atrium dans une maison romaine ?", "choix": ["Une partie de la maison, présente à Pompéi", "Un temple", "Un amphithéâtre", "Une place publique"], "reponse": 0, "explication": "L'atrium est une pièce centrale des maisons romaines, visible dans les habitations de Pompéi."},
        {"id": "q9", "enonce": "Quels éléments de la vie quotidienne a-t-on retrouvés à Pompéi ?", "choix": ["Boutiques, thermes, graffitis, amphithéâtre", "Uniquement des tombeaux", "Uniquement des temples", "Rien n'a été retrouvé"], "reponse": 0, "explication": "Les fouilles ont révélé boutiques, thermes, amphithéâtre et graffitis, témoins de la vie quotidienne."},
        {"id": "q10", "enonce": "Les fouilles de Pompéi sont-elles encore en cours aujourd'hui ?", "choix": ["Oui", "Non, elles sont terminées depuis longtemps", "Elles n'ont jamais commencé", "Elles ont été interdites"], "reponse": 0, "explication": "Les fouilles archéologiques de Pompéi se poursuivent encore aujourd'hui."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "jeux-cirque-gladiateurs-latin-5e", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecons grammaire/civilisation Latin 4e ajoutees.")
