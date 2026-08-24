# -*- coding: utf-8 -*-
PATH = "src/content/lessons.ts"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def lesson_block(d):
    obj = ", ".join('"' + esc(o) + '"' for o in d["objectifs"])
    cont = ", ".join('"' + esc(c) + '"' for c in d["contenu"])
    mots = ", ".join('"' + esc(m) + '"' for m in d["motsAEcouter"])
    q_items = []
    for q in d["quiz"]:
        choix = ", ".join('"' + esc(c) + '"' for c in q["choix"])
        expl = esc(q["explication"])
        enonce = esc(q["enonce"])
        q_items.append(
            '      {\n        id: "' + q["id"] + '",\n        enonce: "' + enonce + '",\n'
            '        choix: [' + choix + '],\n        reponse: ' + str(q["reponse"]) + ',\n'
            '        explication: "' + expl + '",\n      }'
        )
    quiz_block = (
        'quiz: {\n    slug: "quiz-' + d["slug"] + '",\n    titre: "Quiz — ' + esc(d["titre"]) + '",\n'
        '    questions: [\n' + ",\n".join(q_items) + "\n    ],\n  },"
    )
    return (
        '  {\n    slug: "' + d["slug"] + '",\n    titre: "' + esc(d["titre"]) + '",\n'
        '    matiere: "' + d["matiere"] + '",\n    niveau: "' + d["niveau"] + '",\n'
        '    duree: "' + d["duree"] + '",\n    resume: "' + esc(d["resume"]) + '",\n'
        '    motsAEcouter: [' + mots + '],\n'
        '    objectifs: [' + obj + '],\n    contenu: [' + cont + '],\n    ' + quiz_block + '\n  },'
    )

def insert_after(txt, anchor_slug, new_dicts):
    start = txt.index('  {\n    slug: "' + anchor_slug + '",')
    nxt = txt.index('\n  {\n    slug:', start + 10)
    insertion = "\n" + "\n".join(lesson_block(d) for d in new_dicts)
    return txt[:nxt] + insertion + txt[nxt:]

L = []

L.append({
    "slug": "le-son-oin", "titre": "Le son [oin]",
    "matiere": "francais", "niveau": "cp", "duree": "15 min",
    "resume": "Apprendre à reconnaître et écrire le son [oin].",
    "motsAEcouter": ["coin", "point", "foin", "loin", "pointu"],
    "objectifs": ["Reconnaître le son [oin] à l'oral", "Associer le son [oin] à sa graphie", "Lire et écrire des mots simples contenant ce son"],
    "contenu": [
        "Le son [oin] se retrouve dans plusieurs mots du quotidien : coin, point, foin, loin, pointu.",
        "On entend [oin] dans « Le coin du jardin est loin, près du foin. »",
        "Clique sur le bouton d'écoute pour entendre chaque mot et bien entraîner ton oreille à repérer ce son.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quel mot contient le son [oin] ?", "choix": ["Coin", "Chat", "Lune", "Robot"], "reponse": 0, "explication": "« Coin » contient le son [oin]."},
        {"id": "q2", "enonce": "Combien de fois entend-on [oin] dans « Le point est loin du coin » ?", "choix": ["1", "2", "3", "4"], "reponse": 2, "explication": "On l'entend dans « point », « loin » et « coin », soit 3 fois."},
        {"id": "extra_q3", "enonce": "Quel mot ne contient PAS le son [oin] ?", "choix": ["Coin", "Point", "Chat", "Foin"], "reponse": 2, "explication": "« Chat » ne contient pas le son [oin]."},
        {"id": "extra_q4", "enonce": "Le son [oin] s'écrit avec quelles lettres ?", "choix": ["oin", "on", "in", "an"], "reponse": 0, "explication": "Le son [oin] s'écrit « oin », comme dans « coin »."},
        {"id": "extra_q5", "enonce": "Dans « pointu », où entend-on le son [oin] ?", "choix": ["Au début", "Au milieu", "À la fin", "Nulle part"], "reponse": 0, "explication": "Dans « pointu », le son [oin] est au début du mot."},
        {"id": "extra_q6", "enonce": "Quel mot contient le son [oin] ?", "choix": ["Loin", "Lune", "Lapin", "Loup"], "reponse": 0, "explication": "« Loin » contient le son [oin]."},
        {"id": "extra_q7", "enonce": "Quel est le mot correctement écrit ?", "choix": ["coin", "coint", "quoin"], "reponse": 0, "explication": "« coin » est le mot correctement écrit ; les autres graphies n'existent pas."},
        {"id": "extra_q8", "enonce": "Quel est le mot correctement écrit ?", "choix": ["fouin", "foin", "foint"], "reponse": 1, "explication": "« foin » est le mot correctement écrit ; les autres graphies n'existent pas."},
    ],
})

L.append({
    "slug": "le-son-ien", "titre": "Le son [ien]",
    "matiere": "francais", "niveau": "cp", "duree": "15 min",
    "resume": "Apprendre à reconnaître et écrire le son [ien].",
    "motsAEcouter": ["chien", "bien", "rien", "chirurgien", "musicien"],
    "objectifs": ["Reconnaître le son [ien] à l'oral", "Associer le son [ien] à sa graphie", "Lire et écrire des mots simples contenant ce son"],
    "contenu": [
        "Le son [ien] se retrouve dans plusieurs mots du quotidien : chien, bien, rien, chirurgien, musicien.",
        "On entend [ien] dans « Le chien du musicien ne fait rien de mal. »",
        "Clique sur le bouton d'écoute pour entendre chaque mot et bien entraîner ton oreille à repérer ce son.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quel mot contient le son [ien] ?", "choix": ["Chien", "Chat", "Robot", "Lune"], "reponse": 0, "explication": "« Chien » contient le son [ien]."},
        {"id": "q2", "enonce": "Combien de fois entend-on [ien] dans « Le chien du musicien dit bien » ?", "choix": ["1", "2", "3", "4"], "reponse": 2, "explication": "On l'entend dans « chien », « musicien » et « bien », soit 3 fois."},
        {"id": "extra_q3", "enonce": "Quel mot ne contient PAS le son [ien] ?", "choix": ["Chien", "Bien", "Chat", "Rien"], "reponse": 2, "explication": "« Chat » ne contient pas le son [ien]."},
        {"id": "extra_q4", "enonce": "Le son [ien] s'écrit avec quelles lettres ?", "choix": ["ien", "in", "an", "on"], "reponse": 0, "explication": "Le son [ien] s'écrit « ien », comme dans « chien »."},
        {"id": "extra_q5", "enonce": "Dans « musicien », où entend-on le son [ien] ?", "choix": ["Au début", "Au milieu", "À la fin", "Nulle part"], "reponse": 2, "explication": "Dans « musicien », le son [ien] est à la fin du mot."},
        {"id": "extra_q6", "enonce": "Quel métier contient le son [ien] ?", "choix": ["Chirurgien", "Boulanger", "Docteur", "Facteur"], "reponse": 0, "explication": "« Chirurgien » contient le son [ien]."},
        {"id": "extra_q7", "enonce": "Quel est le mot correctement écrit ?", "choix": ["chien", "chian", "quien"], "reponse": 0, "explication": "« chien » est le mot correctement écrit ; les autres graphies n'existent pas."},
        {"id": "extra_q8", "enonce": "Quel est le mot correctement écrit ?", "choix": ["bian", "biens", "bien"], "reponse": 2, "explication": "« bien » est le mot correctement écrit ; les autres graphies n'existent pas."},
    ],
})

L.append({
    "slug": "le-son-ai-ei", "titre": "Le son [ai/ei]",
    "matiere": "francais", "niveau": "cp", "duree": "15 min",
    "resume": "Apprendre à reconnaître et écrire le son [ai/ei].",
    "motsAEcouter": ["lait", "neige", "fraise", "maison", "reine"],
    "objectifs": ["Reconnaître le son [ai/ei] à l'oral", "Associer le son [ai/ei] à ses deux graphies", "Lire et écrire des mots simples contenant ce son"],
    "contenu": [
        "Le son [ai/ei] se retrouve dans plusieurs mots du quotidien : lait, neige, fraise, maison, reine.",
        "On entend [ai/ei] dans « La reine mange une fraise sous la neige. »",
        "Ce son peut s'écrire de deux façons : « ai » comme dans « lait », ou « ei » comme dans « neige ». Clique sur le bouton d'écoute pour entendre chaque mot et bien entraîner ton oreille à repérer ce son.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quel mot contient le son [ai/ei] ?", "choix": ["Lait", "Chat", "Robot", "Lune"], "reponse": 0, "explication": "« Lait » contient le son [ai/ei]."},
        {"id": "q2", "enonce": "Combien de fois entend-on [ai/ei] dans « La fraise et le lait sont sous la neige » ?", "choix": ["1", "2", "3", "4"], "reponse": 2, "explication": "On l'entend dans « fraise », « lait » et « neige », soit 3 fois."},
        {"id": "extra_q3", "enonce": "Quel mot ne contient PAS le son [ai/ei] ?", "choix": ["Lait", "Neige", "Chat", "Fraise"], "reponse": 2, "explication": "« Chat » ne contient pas le son [ai/ei]."},
        {"id": "extra_q4", "enonce": "Le son [ai/ei] peut s'écrire de deux façons, lesquelles ?", "choix": ["ai et ei", "on et an", "oi et oin", "ou et on"], "reponse": 0, "explication": "Le son [ai/ei] s'écrit « ai » (lait) ou « ei » (neige)."},
        {"id": "extra_q5", "enonce": "Dans « maison », où entend-on le son [ai/ei] ?", "choix": ["Au début", "Au milieu", "À la fin", "Nulle part"], "reponse": 1, "explication": "Dans « maison », le son [ai] est au milieu du mot."},
        {"id": "extra_q6", "enonce": "Quel mot s'écrit avec « ei » ?", "choix": ["Neige", "Lait", "Maison", "Fraise"], "reponse": 0, "explication": "« Neige » s'écrit avec « ei »."},
        {"id": "extra_q7", "enonce": "Quel est le mot correctement écrit ?", "choix": ["lait", "lai", "let"], "reponse": 0, "explication": "« lait » est le mot correctement écrit ; les autres graphies n'existent pas."},
        {"id": "extra_q8", "enonce": "Quel est le mot correctement écrit ?", "choix": ["neje", "neige", "naige"], "reponse": 1, "explication": "« neige » est le mot correctement écrit ; les autres graphies n'existent pas."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

# Insertion en fin de la série "sons" du CP, juste après le-son-f-v (dernier son avant les leçons de lecture de phrases)
txt = insert_after(txt, "le-son-f-v", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(str(len(L)) + " nouveaux sons CP ajoutes.")
