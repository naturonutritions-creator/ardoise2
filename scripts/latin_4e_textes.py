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

L.append({
    "slug": "version-1-familia-romana-latin-4e", "titre": "Version n°1 — Familia Romana",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant une matinée dans une famille romaine.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire de la famille et de la vie quotidienne", "Identifier les verbes conjugués au présent et à l'imparfait"],
    "contenu": [
        "Texte latin : « Marcus, filius Aulii, mane surgit. Pater in tablino epistulas scribit. Mater cum ancillis in horto laborat. Soror parva, Julia, cum cane ludit. Familia tota domi manet, quia hodie dies festus est. »",
        "Vocabulaire : filius (fils), mane (le matin), surgit (il se lève), tablinum (le bureau), epistula (la lettre), ancilla (la servante), hortus (le jardin), soror (la sœur), canis (le chien), ludit (il/elle joue), domi (à la maison), dies festus (jour de fête).",
        "Traduction proposée : « Marcus, le fils d'Aulus, se lève le matin. Le père écrit des lettres dans son bureau. La mère travaille dans le jardin avec les servantes. La petite sœur, Julia, joue avec le chien. Toute la famille reste à la maison, car aujourd'hui c'est un jour de fête. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « filius » ?", "choix": ["Le fils", "La fille", "Le père", "La mère"], "reponse": 0, "explication": "Filius signifie « le fils »."},
        {"id": "q2", "enonce": "Que fait Marcus le matin ?", "choix": ["Il se lève", "Il dort", "Il part en voyage", "Il écrit des lettres"], "reponse": 0, "explication": "Le texte dit « Marcus... mane surgit », Marcus se lève le matin."},
        {"id": "q3", "enonce": "Où le père écrit-il ses lettres ?", "choix": ["Dans le tablinum (le bureau)", "Dans le jardin", "Dans la rue", "Au marché"], "reponse": 0, "explication": "Pater in tablino epistulas scribit : le père écrit ses lettres dans le bureau."},
        {"id": "q4", "enonce": "Avec qui la mère travaille-t-elle dans le jardin ?", "choix": ["Les servantes (ancillae)", "Les esclaves masculins", "Le père", "Les voisins"], "reponse": 0, "explication": "Mater cum ancillis in horto laborat : la mère travaille avec les servantes dans le jardin."},
        {"id": "q5", "enonce": "Que fait Julia, la petite sœur ?", "choix": ["Elle joue avec le chien", "Elle écrit des lettres", "Elle travaille dans le jardin", "Elle dort"], "reponse": 0, "explication": "Soror parva, Julia, cum cane ludit : Julia joue avec le chien."},
        {"id": "q6", "enonce": "Pourquoi la famille reste-t-elle à la maison ?", "choix": ["Car c'est un jour de fête", "Car il pleut", "Car ils sont malades", "Car c'est interdit de sortir"], "reponse": 0, "explication": "Familia tota domi manet, quia hodie dies festus est : c'est un jour de fête."},
        {"id": "q7", "enonce": "Que signifie « domi » ?", "choix": ["À la maison", "Au marché", "Au jardin", "À l'école"], "reponse": 0, "explication": "Domi est le locatif de domus, signifiant « à la maison »."},
        {"id": "q8", "enonce": "À quel temps est conjugué « surgit » ?", "choix": ["Au présent", "Au futur", "Au parfait", "Au plus-que-parfait"], "reponse": 0, "explication": "Surgit est au présent de l'indicatif, 3e personne du singulier."},
        {"id": "q9", "enonce": "Que signifie « hortus » ?", "choix": ["Le jardin", "La maison", "La lettre", "Le chien"], "reponse": 0, "explication": "Hortus signifie « le jardin »."},
        {"id": "q10", "enonce": "Que signifie « dies festus » ?", "choix": ["Un jour de fête", "Un jour de travail", "Un jour de pluie", "Un jour d'école"], "reponse": 0, "explication": "Dies festus signifie « un jour de fête »."},
    ],
})

L.append({
    "slug": "version-2-schola-latin-4e", "titre": "Version n°2 — In Schola",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin sur une journée d'école dans la Rome antique.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire scolaire romain", "Identifier les compléments circonstanciels de lieu"],
    "contenu": [
        "Texte latin : « Pueri mane ad scholam ambulant. Magister severus est et discipulos vigilat. Discipuli in tabulis litteras scribunt et fabulas legunt. Qui bene laborat, laudatur ; qui male laborat, punitur. Post scholam, pueri domum laeti currunt. »",
        "Vocabulaire : puer (le garçon, l'enfant), schola (l'école), ambulant (ils marchent), magister (le maître), severus (sévère), discipulus (l'élève), tabula (la tablette), littera (la lettre), fabula (l'histoire, la fable), laudatur (il est loué), punitur (il est puni), laetus (joyeux), currunt (ils courent).",
        "Traduction proposée : « Les garçons marchent vers l'école le matin. Le maître est sévère et surveille les élèves. Les élèves écrivent des lettres sur leurs tablettes et lisent des fables. Celui qui travaille bien est loué ; celui qui travaille mal est puni. Après l'école, les garçons courent joyeusement vers la maison. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « puer » ?", "choix": ["Le garçon, l'enfant", "Le maître", "L'élève", "La lettre"], "reponse": 0, "explication": "Puer signifie « le garçon » ou « l'enfant »."},
        {"id": "q2", "enonce": "Où les garçons marchent-ils le matin ?", "choix": ["Vers l'école", "Vers le marché", "Vers le forum", "Vers le temple"], "reponse": 0, "explication": "Pueri mane ad schola ambulant : les garçons marchent vers l'école le matin."},
        {"id": "q3", "enonce": "Comment est décrit le maître ?", "choix": ["Sévère", "Doux", "Absent", "Malade"], "reponse": 0, "explication": "Magister severus est : le maître est sévère."},
        {"id": "q4", "enonce": "Sur quoi les élèves écrivent-ils des lettres ?", "choix": ["Sur des tablettes (tabulae)", "Sur du papier", "Sur des murs", "Sur le sable"], "reponse": 0, "explication": "Discipuli in tabulis litteras scribunt : les élèves écrivent sur des tablettes."},
        {"id": "q5", "enonce": "Que lisent aussi les élèves ?", "choix": ["Des fables (fabulae)", "Des lettres de leurs parents", "Des lois romaines", "Rien du tout"], "reponse": 0, "explication": "Le texte précise que les élèves lisent aussi des fabulae, des fables."},
        {"id": "q6", "enonce": "Que se passe-t-il pour celui qui travaille bien ?", "choix": ["Il est loué (laudatur)", "Il est puni", "Il rentre plus tôt", "Rien de particulier"], "reponse": 0, "explication": "Qui bene laborat, laudatur : celui qui travaille bien est loué."},
        {"id": "q7", "enonce": "Que se passe-t-il pour celui qui travaille mal ?", "choix": ["Il est puni (punitur)", "Il est loué", "Il rentre plus tôt", "Rien de particulier"], "reponse": 0, "explication": "Qui male laborat, punitur : celui qui travaille mal est puni."},
        {"id": "q8", "enonce": "Que font les garçons après l'école ?", "choix": ["Ils courent joyeusement vers la maison", "Ils restent à l'école", "Ils vont au marché", "Ils dorment sur place"], "reponse": 0, "explication": "Post scholam, pueri domum laeti currunt : les garçons courent joyeusement vers la maison."},
        {"id": "q9", "enonce": "À quelle voix sont laudatur et punitur ?", "choix": ["La voix passive", "La voix active", "L'impératif", "Le subjonctif"], "reponse": 0, "explication": "Laudatur et punitur sont des formes passives (« il est loué », « il est puni »)."},
        {"id": "q10", "enonce": "Que signifie « laetus » ?", "choix": ["Joyeux", "Triste", "Fatigué", "Sévère"], "reponse": 0, "explication": "Laetus signifie « joyeux »."},
    ],
})

L.append({
    "slug": "version-3-forum-mercatus-latin-4e", "titre": "Version n°3 — Forum et Mercatus",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant l'animation du forum et du marché romain.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire du commerce", "Identifier les noms de la 1ère, 2e et 3e déclinaison dans un texte"],
    "contenu": [
        "Texte latin : « In foro magna turba est. Mercatores fructus, panem et vinum vendunt. Emptores pecuniam numerant et cibum emunt. Prope forum, senatores ad curiam ambulant, nam consilium hodie habetur. Pueri inter homines currunt et clamant. »",
        "Vocabulaire : forum (le forum), turba (la foule), mercator (le marchand), fructus (le fruit), panis (le pain), vinum (le vin), vendunt (ils vendent), emptor (l'acheteur), pecunia (l'argent), numerant (ils comptent), emunt (ils achètent), curia (la curie, le lieu de réunion du Sénat), consilium (le conseil, la délibération), clamant (ils crient).",
        "Traduction proposée : « Il y a une grande foule sur le forum. Les marchands vendent des fruits, du pain et du vin. Les acheteurs comptent leur argent et achètent de la nourriture. Près du forum, les sénateurs marchent vers la curie, car une délibération a lieu aujourd'hui. Les enfants courent et crient parmi les gens. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « forum » ?", "choix": ["Le forum, la place publique", "Le temple", "La maison", "L'école"], "reponse": 0, "explication": "Forum désigne la place publique centrale de la ville romaine."},
        {"id": "q2", "enonce": "Que vendent les mercatores ?", "choix": ["Des fruits, du pain et du vin", "Uniquement des vêtements", "Des armes", "Des animaux uniquement"], "reponse": 0, "explication": "Mercatores fructus, panem et vinum vendunt : les marchands vendent fruits, pain et vin."},
        {"id": "q3", "enonce": "Que font les emptores ?", "choix": ["Ils comptent leur argent et achètent de la nourriture", "Ils vendent des marchandises", "Ils dorment", "Ils écrivent des lettres"], "reponse": 0, "explication": "Emptores pecuniam numerant et cibum emunt : les acheteurs comptent leur argent et achètent de la nourriture."},
        {"id": "q4", "enonce": "Où les sénateurs se rendent-ils ?", "choix": ["À la curie", "Au temple", "Au théâtre", "Aux thermes"], "reponse": 0, "explication": "Senatores ad curiam ambulant : les sénateurs marchent vers la curie."},
        {"id": "q5", "enonce": "Pourquoi les sénateurs vont-ils à la curie ?", "choix": ["Car une délibération (consilium) a lieu aujourd'hui", "Pour acheter du pain", "Pour se reposer", "Pour assister à des jeux"], "reponse": 0, "explication": "Nam consilium hodie habetur : une délibération a lieu aujourd'hui."},
        {"id": "q6", "enonce": "Que font les enfants (pueri) dans le texte ?", "choix": ["Ils courent et crient parmi les gens", "Ils vendent des fruits", "Ils comptent l'argent", "Ils restent silencieux"], "reponse": 0, "explication": "Pueri inter homines currunt et clamant : les enfants courent et crient parmi les gens."},
        {"id": "q7", "enonce": "Que signifie « pecunia » ?", "choix": ["L'argent", "Le pain", "Le vin", "Le fruit"], "reponse": 0, "explication": "Pecunia signifie « l'argent »."},
        {"id": "q8", "enonce": "À quelle déclinaison appartient turba, turbae ?", "choix": ["La 1ère déclinaison", "La 2e déclinaison", "La 3e déclinaison", "La 4e déclinaison"], "reponse": 0, "explication": "Turba, turbae (la foule) est un nom féminin de la 1ère déclinaison."},
        {"id": "q9", "enonce": "À quelle déclinaison appartient panis, panis ?", "choix": ["La 3e déclinaison", "La 1ère déclinaison", "La 2e déclinaison", "La 5e déclinaison"], "reponse": 0, "explication": "Panis, panis (le pain) est un nom de la 3e déclinaison."},
        {"id": "q10", "enonce": "Que signifie « vinum » ?", "choix": ["Le vin", "L'eau", "Le pain", "L'argent"], "reponse": 0, "explication": "Vinum signifie « le vin »."},
    ],
})

L.append({
    "slug": "version-4-gladiatores-arena-latin-4e", "titre": "Version n°4 — Gladiatores in Arena",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant un combat de gladiateurs dans l'amphithéâtre.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire des jeux du cirque", "Identifier des verbes au parfait"],
    "contenu": [
        "Texte latin : « Hodie in amphitheatro magnus ludus est. Populus Romanus spectat. Duo gladiatores in arenam intraverunt : unus retiarius, alter secutor. Diu pugnaverunt. Tandem retiarius secutorem vicit. Populus clamavit et gladiatori victori coronam dedit. »",
        "Vocabulaire : amphitheatrum (l'amphithéâtre), ludus (le jeu, le spectacle), populus (le peuple), spectat (il regarde), gladiator (le gladiateur), arena (l'arène), retiarius (le rétiaire, gladiateur au filet), secutor (le secuteur, gladiateur au glaive), pugnaverunt (ils combattirent), vicit (il vainquit), corona (la couronne).",
        "Traduction proposée : « Aujourd'hui, il y a un grand spectacle dans l'amphithéâtre. Le peuple romain regarde. Deux gladiateurs sont entrés dans l'arène : l'un rétiaire, l'autre secuteur. Ils combattirent longtemps. Finalement, le rétiaire vainquit le secuteur. Le peuple cria et donna une couronne au gladiateur vainqueur. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Où se déroule le spectacle ?", "choix": ["Dans l'amphithéâtre", "Au forum", "Au temple", "Sur la voie Appienne"], "reponse": 0, "explication": "Hodie in amphitheatro magnus ludus est : le spectacle a lieu dans l'amphithéâtre."},
        {"id": "q2", "enonce": "Qui regarde le spectacle ?", "choix": ["Le peuple romain (populus Romanus)", "Uniquement les sénateurs", "Uniquement les enfants", "Personne"], "reponse": 0, "explication": "Populus Romanus spectat : le peuple romain regarde le spectacle."},
        {"id": "q3", "enonce": "Combien de gladiateurs entrent dans l'arène ?", "choix": ["Deux", "Un seul", "Quatre", "Dix"], "reponse": 0, "explication": "Duo gladiatores in arenam intraverunt : deux gladiateurs entrent dans l'arène."},
        {"id": "q4", "enonce": "Que signifie « retiarius » ?", "choix": ["Un gladiateur combattant au filet", "Un sénateur", "Un marchand", "Un esclave"], "reponse": 0, "explication": "Le retiarius est un type de gladiateur combattant avec un filet et un trident."},
        {"id": "q5", "enonce": "Combien de temps dure le combat ?", "choix": ["Longtemps (diu)", "Une minute", "Toute la journée uniquement", "Le texte ne le précise pas clairement, mais diu signifie longtemps"], "reponse": 0, "explication": "Diu pugnaverunt : ils combattirent longtemps."},
        {"id": "q6", "enonce": "Qui remporte le combat ?", "choix": ["Le retiarius", "Le secutor", "Aucun des deux", "Les deux ex-aequo"], "reponse": 0, "explication": "Tandem retiarius secutorem vicit : le retiarius vainquit le secutor."},
        {"id": "q7", "enonce": "Que fait le peuple à la fin du combat ?", "choix": ["Il crie et donne une couronne au vainqueur", "Il quitte l'amphithéâtre en silence", "Il pleure", "Il attaque les gladiateurs"], "reponse": 0, "explication": "Populus clamavit et gladiatori victori coronam dedit : le peuple cria et donna une couronne au vainqueur."},
        {"id": "q8", "enonce": "À quel temps sont pugnaverunt, vicit et dedit ?", "choix": ["Au parfait", "Au présent", "À l'imparfait", "Au futur"], "reponse": 0, "explication": "Pugnaverunt, vicit et dedit sont des formes du parfait, exprimant des actions passées et achevées."},
        {"id": "q9", "enonce": "Que signifie « corona » ?", "choix": ["La couronne", "Le filet", "Le glaive", "L'arène"], "reponse": 0, "explication": "Corona signifie « la couronne »."},
        {"id": "q10", "enonce": "Que signifie « tandem » dans ce texte ?", "choix": ["Finalement", "Immédiatement", "Jamais", "Souvent"], "reponse": 0, "explication": "Tandem signifie « finalement, à la fin »."},
    ],
})

L.append({
    "slug": "version-5-caesar-gallia-latin-4e", "titre": "Version n°5 — Caesar in Gallia",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin simplifié inspiré de la guerre des Gaules.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire militaire romain", "Identifier une proposition relative dans un texte"],
    "contenu": [
        "Texte latin : « Caesar, dux Romanus, cum exercitu in Galliam venit. Galli, qui in oppidis habitabant, contra Romanos pugnaverunt. Sed legiones Romanae fortiores erant. Post multa proelia, Caesar Galliam vicit et pacem dedit. Incolae novas leges Romanas acceperunt. »",
        "Vocabulaire : dux (le chef, le général), exercitus (l'armée), Gallia (la Gaule), Galli (les Gaulois), oppidum (la ville fortifiée), contra (contre), legio (la légion), fortis (fort, courageux), proelium (la bataille), pax (la paix), incola (l'habitant), lex (la loi).",
        "Traduction proposée : « César, général romain, vint en Gaule avec son armée. Les Gaulois, qui habitaient dans des villes fortifiées, combattirent contre les Romains. Mais les légions romaines étaient plus fortes. Après de nombreuses batailles, César vainquit la Gaule et donna la paix. Les habitants reçurent de nouvelles lois romaines. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qui est Caesar dans ce texte ?", "choix": ["Un général romain (dux Romanus)", "Un sénateur", "Un marchand", "Un gladiateur"], "reponse": 0, "explication": "Caesar, dux Romanus : César est présenté comme un général romain."},
        {"id": "q2", "enonce": "Avec quoi César vient-il en Gaule ?", "choix": ["Avec son armée (exercitu)", "Seul", "Avec des marchands", "Avec le Sénat entier"], "reponse": 0, "explication": "Caesar... cum exercitu in Galliam venit : César vient avec son armée."},
        {"id": "q3", "enonce": "Où habitaient les Gaulois ?", "choix": ["Dans des villes fortifiées (oppida)", "Dans des grottes", "Sur des bateaux", "Dans le désert"], "reponse": 0, "explication": "Galli, qui in oppidis habitabant : les Gaulois habitaient dans des oppida, des villes fortifiées."},
        {"id": "q4", "enonce": "Quel est le pronom relatif dans « Galli, qui in oppidis habitabant »?", "choix": ["Qui", "Quae", "Quod", "Quem"], "reponse": 0, "explication": "Qui est le pronom relatif, sujet de habitabant, s'accordant avec Galli (masculin pluriel)."},
        {"id": "q5", "enonce": "Contre qui les Gaulois combattent-ils ?", "choix": ["Contre les Romains", "Contre les Grecs", "Contre les Égyptiens", "Contre d'autres Gaulois uniquement"], "reponse": 0, "explication": "Contra Romanos pugnaverunt : ils combattirent contre les Romains."},
        {"id": "q6", "enonce": "Qui était le plus fort selon le texte ?", "choix": ["Les légions romaines", "Les Gaulois", "Aucun des deux", "Impossible à dire"], "reponse": 0, "explication": "Legiones Romanae fortiores erant : les légions romaines étaient plus fortes."},
        {"id": "q7", "enonce": "Que se passe-t-il après de nombreuses batailles ?", "choix": ["César vainquit la Gaule et donna la paix", "Les Gaulois gagnèrent la guerre", "Rien ne changea", "César quitta la Gaule sans combattre"], "reponse": 0, "explication": "Post multa proelia, Caesar Galliam vicit et pacem dedit."},
        {"id": "q8", "enonce": "Que reçurent les habitants après la conquête ?", "choix": ["De nouvelles lois romaines", "De nouvelles terres uniquement", "Rien du tout", "La liberté totale"], "reponse": 0, "explication": "Incolae novas leges Romanas acceperunt : les habitants reçurent de nouvelles lois romaines."},
        {"id": "q9", "enonce": "Que signifie « proelium » ?", "choix": ["La bataille", "La paix", "La loi", "La ville"], "reponse": 0, "explication": "Proelium signifie « la bataille »."},
        {"id": "q10", "enonce": "Que signifie « pax » ?", "choix": ["La paix", "La guerre", "La loi", "L'armée"], "reponse": 0, "explication": "Pax, pacis signifie « la paix »."},
    ],
})

L.append({
    "slug": "version-6-dei-olympi-latin-4e", "titre": "Version n°6 — Dei Olympi",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin de mythologie sur les dieux de l'Olympe.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître les noms des principaux dieux romains", "Identifier les compléments au génitif exprimant la possession"],
    "contenu": [
        "Texte latin : « Jupiter, rex deorum, in Olympo habitat. Juno, uxor Jupiteris, dea matrimonii est. Neptunus, frater Jupiteris, mare regit ; Pluto, alter frater, mortuos in inferis regit. Minerva, filia Jupiteris, sapientiae dea est. Omnes dei mortalibus auxilium vel poenas dant. »",
        "Vocabulaire : rex (le roi), deus/dea (le dieu/la déesse), Olympus (l'Olympe), uxor (l'épouse), matrimonium (le mariage), frater (le frère), mare (la mer), regit (il règne sur, il gouverne), inferi (les enfers), sapientia (la sagesse), mortalis (le mortel), auxilium (l'aide), poena (la punition).",
        "Traduction proposée : « Jupiter, roi des dieux, habite sur l'Olympe. Junon, épouse de Jupiter, est la déesse du mariage. Neptune, frère de Jupiter, règne sur la mer ; Pluton, l'autre frère, règne sur les morts aux enfers. Minerve, fille de Jupiter, est la déesse de la sagesse. Tous les dieux donnent aux mortels de l'aide ou des punitions. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qui est le roi des dieux ?", "choix": ["Jupiter", "Neptune", "Pluton", "Minerve"], "reponse": 0, "explication": "Jupiter, rex deorum : Jupiter est présenté comme le roi des dieux."},
        {"id": "q2", "enonce": "Où habite Jupiter ?", "choix": ["Sur l'Olympe", "Dans la mer", "Aux enfers", "Sur Terre parmi les hommes"], "reponse": 0, "explication": "Jupiter... in Olympo habitat : Jupiter habite sur l'Olympe."},
        {"id": "q3", "enonce": "Qui est Junon (Juno) par rapport à Jupiter ?", "choix": ["Son épouse (uxor)", "Sa fille", "Sa sœur uniquement", "Sa mère"], "reponse": 0, "explication": "Juno, uxor Jupiteris : Junon est l'épouse de Jupiter."},
        {"id": "q4", "enonce": "De quoi Junon est-elle la déesse ?", "choix": ["Du mariage (matrimonium)", "De la mer", "De la sagesse", "De la guerre"], "reponse": 0, "explication": "Dea matrimonii est : Junon est la déesse du mariage."},
        {"id": "q5", "enonce": "Sur quoi règne Neptune ?", "choix": ["La mer (mare)", "Les enfers", "L'Olympe", "La sagesse"], "reponse": 0, "explication": "Neptunus... mare regit : Neptune règne sur la mer."},
        {"id": "q6", "enonce": "Sur quoi règne Pluton ?", "choix": ["Les morts, aux enfers (inferi)", "La mer", "L'Olympe", "Le mariage"], "reponse": 0, "explication": "Pluto... mortuos in inferis regit : Pluton règne sur les morts aux enfers."},
        {"id": "q7", "enonce": "Qui est Minerve par rapport à Jupiter ?", "choix": ["Sa fille (filia)", "Son épouse", "Sa sœur", "Sa mère"], "reponse": 0, "explication": "Minerva, filia Jupiteris : Minerve est la fille de Jupiter."},
        {"id": "q8", "enonce": "De quoi Minerve est-elle la déesse ?", "choix": ["De la sagesse (sapientia)", "De la mer", "Du mariage", "De la guerre uniquement"], "reponse": 0, "explication": "Sapientiae dea est : Minerve est la déesse de la sagesse."},
        {"id": "q9", "enonce": "À quel cas est « Jupiteris » dans « uxor Jupiteris » ?", "choix": ["Le génitif, exprimant la possession", "Le nominatif", "L'accusatif", "L'ablatif"], "reponse": 0, "explication": "Jupiteris est au génitif, exprimant la possession : « l'épouse de Jupiter »."},
        {"id": "q10", "enonce": "Que donnent les dieux aux mortels selon le texte ?", "choix": ["De l'aide ou des punitions", "Uniquement de l'argent", "Rien du tout", "Uniquement des lois"], "reponse": 0, "explication": "Omnes dei mortalibus auxilium vel poenas dant : les dieux donnent aide ou punitions aux mortels."},
    ],
})

L.append({
    "slug": "version-7-via-appia-latin-4e", "titre": "Version n°7 — Iter per Viam Appiam",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant un voyage sur la voie Appienne.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire du voyage et des routes romaines", "Identifier des verbes au futur"],
    "contenu": [
        "Texte latin : « Cras Marcus et pater eius iter per Viam Appiam facient. Via longa et recta est ; Romani eam optime aedificaverunt. Viatores per multa oppida transibunt et in tabernis cibum emeni. Si tempus bonum erit, Capuam ante noctem pervenient. »",
        "Vocabulaire : cras (demain), iter (le voyage, la route), via (la route, la voie), longus (long), rectus (droit), aedificaverunt (ils construisirent), viator (le voyageur), taberna (l'auberge, la boutique), tempus (le temps), nox (la nuit), pervenient (ils arriveront).",
        "Traduction proposée : « Demain, Marcus et son père feront un voyage par la voie Appienne. La route est longue et droite ; les Romains l'ont très bien construite. Les voyageurs traverseront de nombreuses villes et achèteront de la nourriture dans les auberges. S'il fait beau temps, ils arriveront à Capoue avant la nuit. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que vont faire Marcus et son père demain ?", "choix": ["Un voyage par la voie Appienne", "Une bataille", "Un spectacle de gladiateurs", "Un repas de fête"], "reponse": 0, "explication": "Cras Marcus et pater eius iter per Viam Appiam facient : ils feront un voyage par la voie Appienne."},
        {"id": "q2", "enonce": "Comment est décrite la voie Appienne ?", "choix": ["Longue et droite (longa et recta)", "Courte et sinueuse", "Étroite et dangereuse", "Détruite"], "reponse": 0, "explication": "Via longa et recta est : la route est longue et droite."},
        {"id": "q3", "enonce": "Qui a construit cette route ?", "choix": ["Les Romains", "Les Gaulois", "Les Grecs", "Personne, elle est naturelle"], "reponse": 0, "explication": "Romani eam optime aedificaverunt : les Romains l'ont très bien construite."},
        {"id": "q4", "enonce": "Que traverseront les voyageurs ?", "choix": ["De nombreuses villes (oppida)", "Des déserts", "Des océans", "Des montagnes uniquement"], "reponse": 0, "explication": "Viatores per multa oppida transibunt : les voyageurs traverseront de nombreuses villes."},
        {"id": "q5", "enonce": "Où les voyageurs achèteront-ils de la nourriture ?", "choix": ["Dans les auberges (tabernae)", "Au temple", "Chez le sénateur", "Ils n'achèteront rien"], "reponse": 0, "explication": "In tabernis cibum ement : ils achèteront de la nourriture dans les auberges."},
        {"id": "q6", "enonce": "À quelle ville les voyageurs espèrent-ils arriver ?", "choix": ["Capoue (Capua)", "Rome", "Pompéi", "Athènes"], "reponse": 0, "explication": "Capuam ante noctem pervenient : ils arriveront à Capoue avant la nuit."},
        {"id": "q7", "enonce": "À quelle condition arriveront-ils avant la nuit ?", "choix": ["S'il fait beau temps (si tempus bonum erit)", "S'ils partent très tôt uniquement", "Peu importe la condition", "S'ils prennent un bateau"], "reponse": 0, "explication": "Si tempus bonum erit : la condition posée est qu'il fasse beau temps."},
        {"id": "q8", "enonce": "À quel temps est le verbe « facient » ?", "choix": ["Au futur", "Au présent", "À l'imparfait", "Au parfait"], "reponse": 0, "explication": "Facient est au futur, 3e personne du pluriel de facere."},
        {"id": "q9", "enonce": "Que signifie « cras » ?", "choix": ["Demain", "Hier", "Aujourd'hui", "Bientôt, dans un mois"], "reponse": 0, "explication": "Cras signifie « demain »."},
        {"id": "q10", "enonce": "Que signifie « viator » ?", "choix": ["Le voyageur", "Le marchand", "Le soldat", "Le sénateur"], "reponse": 0, "explication": "Viator signifie « le voyageur »."},
    ],
})

L.append({
    "slug": "version-8-pompeii-ante-eruptionem-latin-4e", "titre": "Version n°8 — Pompeii ante Eruptionem",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant la ville de Pompéi avant l'éruption du Vésuve.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire de la ville romaine", "Identifier un verbe au plus-que-parfait"],
    "contenu": [
        "Texte latin : « Pompeii, urbs pulchra prope mare, multos incolas habebat. Cives in foro negotia agebant, in thermis lavabant, in theatro fabulas spectabant. Vesuvius mons prope urbem stabat ; incolae eum non timebant, quia antea numquam eruperat. »",
        "Vocabulaire : urbs (la ville), incola (l'habitant), civis (le citoyen), negotium (l'affaire, le commerce), thermae (les thermes), lavabant (ils se lavaient), theatrum (le théâtre), mons (la montagne, le mont), timebant (ils craignaient), antea (auparavant), numquam (jamais), eruperat (il était entré en éruption).",
        "Traduction proposée : « Pompéi, belle ville proche de la mer, avait de nombreux habitants. Les citoyens faisaient des affaires sur le forum, se lavaient aux thermes, regardaient des pièces au théâtre. Le mont Vésuve se dressait près de la ville ; les habitants ne le craignaient pas, car il n'était jamais entré en éruption auparavant. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Comment est décrite Pompéi ?", "choix": ["Belle ville proche de la mer", "Petit village de montagne", "Ville déserte", "Ville fortifiée en guerre"], "reponse": 0, "explication": "Pompeii, urbs pulchra prope mare : Pompéi est une belle ville proche de la mer."},
        {"id": "q2", "enonce": "Où les citoyens faisaient-ils des affaires ?", "choix": ["Sur le forum", "Au théâtre", "Aux thermes", "Sur le Vésuve"], "reponse": 0, "explication": "Cives in foro negotia agebant : les citoyens faisaient des affaires sur le forum."},
        {"id": "q3", "enonce": "Où les citoyens se lavaient-ils ?", "choix": ["Aux thermes", "Dans la mer uniquement", "Au forum", "Au théâtre"], "reponse": 0, "explication": "In thermis lavabant : ils se lavaient aux thermes."},
        {"id": "q4", "enonce": "Que regardaient les citoyens au théâtre ?", "choix": ["Des pièces (fabulae)", "Des combats de gladiateurs", "Des courses de chars", "Rien, le théâtre était fermé"], "reponse": 0, "explication": "In theatro fabulas spectabant : ils regardaient des pièces au théâtre."},
        {"id": "q5", "enonce": "Quelle montagne se trouvait près de Pompéi ?", "choix": ["Le Vésuve", "L'Etna", "Le Vulcano", "Le Stromboli"], "reponse": 0, "explication": "Vesuvius mons prope urbem stabat : le mont Vésuve se dressait près de la ville."},
        {"id": "q6", "enonce": "Les habitants craignaient-ils le Vésuve ?", "choix": ["Non, ils ne le craignaient pas", "Oui, énormément", "Ils l'ignoraient totalement", "Ils avaient déjà fui la ville"], "reponse": 0, "explication": "Incolae eum non timebant : les habitants ne craignaient pas le Vésuve."},
        {"id": "q7", "enonce": "Pourquoi les habitants ne craignaient-ils pas le Vésuve ?", "choix": ["Car il n'était jamais entré en éruption auparavant", "Car ils ne savaient pas que c'était un volcan", "Car des prêtres l'avaient béni", "Car ils étaient très courageux"], "reponse": 0, "explication": "Quia antea numquam eruperat : car il n'était jamais entré en éruption auparavant."},
        {"id": "q8", "enonce": "À quel temps est « eruperat » ?", "choix": ["Au plus-que-parfait", "Au présent", "Au futur", "À l'imparfait"], "reponse": 0, "explication": "Eruperat est au plus-que-parfait, exprimant une action antérieure à une autre action passée."},
        {"id": "q9", "enonce": "Que signifie « incola » ?", "choix": ["L'habitant", "Le voyageur", "Le sénateur", "Le marchand"], "reponse": 0, "explication": "Incola signifie « l'habitant »."},
        {"id": "q10", "enonce": "Que signifie « numquam » ?", "choix": ["Jamais", "Toujours", "Souvent", "Parfois"], "reponse": 0, "explication": "Numquam signifie « jamais »."},
    ],
})

L.append({
    "slug": "version-9-senatus-deliberat-latin-4e", "titre": "Version n°9 — Senatus Deliberat",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant une séance de délibération au Sénat romain.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire politique romain", "Identifier une proposition subordonnée introduite par quia ou si"],
    "contenu": [
        "Texte latin : « Senatores in curia conveniunt. Consul, qui hodie praesidet, de bello loquitur. « Si hostes Italiam intrabunt, » inquit, « exercitum novum mittere debemus. » Senatores diu disputant ; alii pacem malunt, alii bellum. Tandem consilium sumitur : legiones ad fines mittentur. »",
        "Vocabulaire : senator (le sénateur), curia (la curie), consul (le consul), praesidet (il préside), bellum (la guerre), hostis (l'ennemi), Italia (l'Italie), mittere (envoyer), disputant (ils discutent), pax (la paix), malunt (ils préfèrent), consilium sumitur (une décision est prise), finis (la frontière).",
        "Traduction proposée : « Les sénateurs se réunissent dans la curie. Le consul, qui préside aujourd'hui, parle de la guerre. « Si les ennemis entrent en Italie, » dit-il, « nous devons envoyer une nouvelle armée. » Les sénateurs discutent longtemps ; les uns préfèrent la paix, les autres la guerre. Finalement, une décision est prise : les légions seront envoyées aux frontières. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Où se réunissent les sénateurs ?", "choix": ["Dans la curie", "Au forum", "Au théâtre", "Aux thermes"], "reponse": 0, "explication": "Senatores in curia conveniunt : les sénateurs se réunissent dans la curie."},
        {"id": "q2", "enonce": "Qui préside la séance ?", "choix": ["Le consul", "Un préteur", "Un tribun de la plèbe", "Un questeur"], "reponse": 0, "explication": "Consul, qui hodie praesidet : le consul préside la séance."},
        {"id": "q3", "enonce": "De quoi parle le consul ?", "choix": ["De la guerre (bellum)", "Du commerce", "Des jeux du cirque", "De l'agriculture"], "reponse": 0, "explication": "De bello loquitur : le consul parle de la guerre."},
        {"id": "q4", "enonce": "Que dit le consul si les ennemis entrent en Italie ?", "choix": ["Il faut envoyer une nouvelle armée", "Il faut fuir la ville", "Il ne faut rien faire", "Il faut négocier immédiatement la paix"], "reponse": 0, "explication": "Exercitum novum mittere debemus : il faut envoyer une nouvelle armée."},
        {"id": "q5", "enonce": "Que préfèrent certains sénateurs ?", "choix": ["La paix (pax)", "La guerre uniquement", "Rien de précis", "De quitter le Sénat"], "reponse": 0, "explication": "Alii pacem malunt : certains sénateurs préfèrent la paix."},
        {"id": "q6", "enonce": "Que préfèrent d'autres sénateurs ?", "choix": ["La guerre (bellum)", "La paix uniquement", "Le commerce", "Les jeux du cirque"], "reponse": 0, "explication": "Alii bellum (malunt) : d'autres préfèrent la guerre."},
        {"id": "q7", "enonce": "Quelle décision est finalement prise ?", "choix": ["Les légions seront envoyées aux frontières", "Le Sénat est dissous", "La paix est immédiatement signée", "Rien n'est décidé"], "reponse": 0, "explication": "Legiones ad fines mittentur : les légions seront envoyées aux frontières."},
        {"id": "q8", "enonce": "Quelle conjonction introduit la condition « si les ennemis entrent » ?", "choix": ["Si", "Quia", "Nam", "Cum"], "reponse": 0, "explication": "Si introduit la proposition conditionnelle « si hostes Italiam intrabunt »."},
        {"id": "q9", "enonce": "Que signifie « hostis » ?", "choix": ["L'ennemi", "Le sénateur", "Le consul", "Le citoyen"], "reponse": 0, "explication": "Hostis signifie « l'ennemi »."},
        {"id": "q10", "enonce": "Que signifie « bellum » ?", "choix": ["La guerre", "La paix", "La loi", "La ville"], "reponse": 0, "explication": "Bellum signifie « la guerre »."},
    ],
})

L.append({
    "slug": "version-10-ludi-circenses-latin-4e", "titre": "Version n°10 — Ludi Circenses",
    "matiere": "latin", "niveau": "4e", "duree": "25 min",
    "resume": "Exercice de version : traduire un court texte latin décrivant une course de chars au Circus Maximus.",
    "objectifs": ["Traduire un texte latin en français (exercice de version)", "Reconnaître le vocabulaire des courses de chars", "Faire la synthèse des acquis grammaticaux du niveau 4e sur un texte complet"],
    "contenu": [
        "Texte latin : « In Circo Maximo, ingens turba spectat. Quattuor factiones — russata, veneta, alba, prasina — quadrigas mittunt. Aurigae equos incitant ; rotae celeriter volvuntur. Populus clamat et faveat aurigae quem amat. Qui primus septem spatia circuit, victor est et praemium magnum accipit. »",
        "Vocabulaire : circus (le cirque), ingens (immense), factio (l'équipe, la faction), quadriga (le char à quatre chevaux), auriga (le cocher), equus (le cheval), incitant (ils excitent, ils lancent), rota (la roue), volvuntur (elles tournent), faveat (qu'il soutienne, subjonctif), spatium (le tour de piste), circuit (il fait le tour), victor (le vainqueur), praemium (la récompense).",
        "Traduction proposée : « Au Circus Maximus, une foule immense regarde. Quatre équipes — la rouge, la bleue, la blanche, la verte — envoient leurs chars à quatre chevaux. Les cochers excitent leurs chevaux ; les roues tournent rapidement. Le peuple crie et soutient le cocher qu'il aime. Celui qui fait le tour de piste sept fois en premier est le vainqueur et reçoit une grande récompense. »",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Où se déroule la course ?", "choix": ["Au Circus Maximus", "Dans l'amphithéâtre", "Au forum", "Au théâtre"], "reponse": 0, "explication": "In Circo Maximo : la course se déroule au Circus Maximus."},
        {"id": "q2", "enonce": "Combien d'équipes (factiones) participent ?", "choix": ["Quatre", "Deux", "Six", "Huit"], "reponse": 0, "explication": "Quattuor factiones : quatre équipes participent à la course."},
        {"id": "q3", "enonce": "Que signifie « quadriga » ?", "choix": ["Un char à quatre chevaux", "Un cheval seul", "Un cocher", "Une roue"], "reponse": 0, "explication": "Quadriga désigne un char tiré par quatre chevaux."},
        {"id": "q4", "enonce": "Que font les aurigae (cochers) ?", "choix": ["Ils excitent leurs chevaux", "Ils regardent depuis les gradins", "Ils construisent les chars", "Ils vendent des billets"], "reponse": 0, "explication": "Aurigae equos incitant : les cochers excitent (lancent) leurs chevaux."},
        {"id": "q5", "enonce": "Que fait le peuple pendant la course ?", "choix": ["Il crie et soutient son cocher favori", "Il reste silencieux", "Il quitte le cirque", "Il dort"], "reponse": 0, "explication": "Populus clamat et faveat aurigae quem amat : le peuple crie et soutient le cocher qu'il aime."},
        {"id": "q6", "enonce": "Combien de tours de piste faut-il faire pour gagner ?", "choix": ["Sept", "Trois", "Dix", "Un seul"], "reponse": 0, "explication": "Qui primus septem spatia circuit : il faut faire sept tours de piste."},
        {"id": "q7", "enonce": "Que reçoit le vainqueur ?", "choix": ["Une grande récompense (praemium magnum)", "Rien du tout", "Une simple couronne de fleurs", "Le droit de recommencer la course"], "reponse": 0, "explication": "Victor est et praemium magnum accipit : le vainqueur reçoit une grande récompense."},
        {"id": "q8", "enonce": "Que signifie « ingens » ?", "choix": ["Immense", "Petit", "Silencieux", "Rapide"], "reponse": 0, "explication": "Ingens signifie « immense »."},
        {"id": "q9", "enonce": "Que signifie « rota » ?", "choix": ["La roue", "Le cheval", "Le char entier", "Le cocher"], "reponse": 0, "explication": "Rota signifie « la roue »."},
        {"id": "q10", "enonce": "Ce texte fait appel à quel type de vocabulaire principalement ?", "choix": ["Le vocabulaire des courses de chars et des spectacles", "Le vocabulaire de l'agriculture", "Le vocabulaire de la guerre uniquement", "Le vocabulaire scolaire"], "reponse": 0, "explication": "Ce texte utilise le vocabulaire des ludi circenses, les courses de chars, spectacle populaire romain."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "pompei-ville-figee-latin-4e", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} versions Latin 4e ajoutees.")
