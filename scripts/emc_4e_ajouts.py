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
    "slug": "numerique-responsable-citoyennete-4e", "titre": "Le numérique responsable : droits et devoirs en ligne",
    "matiere": "emc", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre les enjeux citoyens du numérique : identité numérique, données personnelles et usages responsables.",
    "objectifs": ["Comprendre ce qu'est l'identité numérique", "Connaître les droits liés à la protection des données personnelles", "Adopter des usages responsables des outils numériques et des réseaux sociaux"],
    "contenu": [
        "L'identité numérique est l'ensemble des traces que nous laissons en ligne : messages, photos publiées, commentaires, historique de navigation. Ces traces, une fois publiées, sont très difficiles à effacer totalement et peuvent être vues par un grand nombre de personnes, y compris dans le futur (recruteurs, établissements scolaires...). Il est donc essentiel de réfléchir avant de publier un contenu.",
        "Le RGPD (Règlement général sur la protection des données), en vigueur dans l'Union européenne depuis 2018, protège les données personnelles des citoyens : il oblige les entreprises à demander le consentement avant de collecter des données, et donne à chacun le droit d'accéder à ses données, de les faire corriger, ou de demander leur suppression (droit à l'oubli).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que l'identité numérique ?", "choix": ["L'ensemble des traces que l'on laisse en ligne", "Uniquement son nom légal", "Une carte d'identité électronique officielle", "Un mot de passe"], "reponse": 0, "explication": "L'identité numérique désigne l'ensemble des traces (photos, messages, commentaires) laissées en ligne."},
        {"id": "q2", "enonce": "Est-il facile d'effacer totalement un contenu publié en ligne ?", "choix": ["Oui, très facilement", "Non, c'est souvent très difficile", "Cela dépend uniquement de l'heure de publication", "Les contenus disparaissent automatiquement après un jour"], "reponse": 1, "explication": "Une fois publié, un contenu en ligne est souvent très difficile à effacer totalement, car il peut avoir été copié ou partagé."},
        {"id": "q3", "enonce": "Que signifie le sigle RGPD ?", "choix": ["Règlement général sur la protection des données", "Réseau global de partage de données", "Régime général de la protection démocratique", "Registre général des personnes déclarées"], "reponse": 0, "explication": "RGPD signifie Règlement général sur la protection des données."},
        {"id": "q4", "enonce": "Depuis quand le RGPD est-il en vigueur dans l'Union européenne ?", "choix": ["Depuis 2018", "Depuis 1995", "Depuis 2005", "Depuis 2022"], "reponse": 0, "explication": "Le RGPD est en vigueur dans l'Union européenne depuis 2018."},
        {"id": "q5", "enonce": "Que doit faire une entreprise avant de collecter des données personnelles selon le RGPD ?", "choix": ["Demander le consentement", "Rien de particulier", "Payer une taxe uniquement", "Informer uniquement le gouvernement"], "reponse": 0, "explication": "Le RGPD oblige les entreprises à demander le consentement avant de collecter des données personnelles."},
        {"id": "q6", "enonce": "Qu'est-ce que le droit à l'oubli ?", "choix": ["Le droit de demander la suppression de ses données", "Le droit d'oublier ses cours", "Le droit de ne jamais utiliser internet", "Un droit qui n'existe pas"], "reponse": 0, "explication": "Le droit à l'oubli permet à chacun de demander la suppression de ses données personnelles."},
        {"id": "q7", "enonce": "Qui peut voir les traces laissées en ligne ?", "choix": ["Potentiellement un grand nombre de personnes, y compris dans le futur", "Uniquement soi-même", "Uniquement ses amis proches", "Personne ne peut jamais les voir"], "reponse": 0, "explication": "Les traces en ligne peuvent être vues par un grand nombre de personnes, y compris dans le futur."},
        {"id": "q8", "enonce": "Pourquoi faut-il réfléchir avant de publier un contenu en ligne ?", "choix": ["Car ce contenu peut avoir des conséquences durables", "Ce n'est pas nécessaire de réfléchir", "Uniquement pour des raisons esthétiques", "Cela n'a aucune importance"], "reponse": 0, "explication": "Un contenu publié peut avoir des conséquences durables (recruteurs, établissements scolaires...), d'où l'importance de réfléchir avant de publier."},
        {"id": "q9", "enonce": "A-t-on le droit d'accéder à ses propres données personnelles collectées par une entreprise ?", "choix": ["Oui, c'est un droit garanti par le RGPD", "Non, jamais", "Uniquement avec l'accord de l'entreprise", "Uniquement pour les entreprises françaises"], "reponse": 0, "explication": "Le RGPD garantit à chacun le droit d'accéder à ses données personnelles."},
        {"id": "q10", "enonce": "Un usage responsable du numérique implique-t-il uniquement des interdictions ?", "choix": ["Non, il s'agit surtout de réflexion et de vigilance", "Oui, il faut tout interdire", "Non, il n'y a aucune règle à respecter", "Cela ne concerne que les adultes"], "reponse": 0, "explication": "Un usage responsable du numérique repose sur la réflexion et la vigilance, plus que sur des interdictions strictes."},
    ],
})

L.append({
    "slug": "art-engagement-citoyen-4e", "titre": "L'art au service de l'engagement citoyen",
    "matiere": "emc", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir comment les artistes utilisent la peinture, la musique et la sculpture pour porter des messages citoyens et dénoncer des injustices.",
    "objectifs": ["Comprendre comment une œuvre d'art peut porter un message politique ou citoyen", "Connaître des exemples d'œuvres engagées", "Réfléchir au rôle de l'artiste comme témoin de son époque"],
    "contenu": [
        "De nombreux artistes utilisent leur art pour dénoncer des injustices ou défendre une cause : Guernica de Pablo Picasso (1937) dénonce les horreurs du bombardement de la ville basque de Guernica pendant la guerre civile espagnole, à travers une œuvre en noir, blanc et gris qui évoque la violence et la souffrance sans montrer directement la guerre.",
        "En musique, de nombreuses chansons ont accompagné des mouvements citoyens : elles peuvent dénoncer des injustices sociales, appeler à la paix, ou soutenir des luttes pour les droits civiques. La musique, par sa diffusion large et son pouvoir émotionnel, est un outil puissant pour sensibiliser un large public à une cause.",
        "L'art engagé pose la question du rôle de l'artiste dans la société : témoin de son époque, il peut choisir de représenter le monde tel qu'il est, de dénoncer des injustices, ou d'imaginer un monde meilleur. Analyser une œuvre engagée, c'est aussi développer son esprit critique, en comprenant le message de l'artiste et le contexte historique dans lequel il s'inscrit.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qui a peint Guernica ?", "choix": ["Pablo Picasso", "Claude Monet", "Léonard de Vinci", "Vincent Van Gogh"], "reponse": 0, "explication": "Guernica a été peint par Pablo Picasso en 1937."},
        {"id": "q2", "enonce": "Que dénonce le tableau Guernica ?", "choix": ["Le bombardement de la ville de Guernica", "Une fête populaire", "Un paysage naturel", "Un portrait de famille"], "reponse": 0, "explication": "Guernica dénonce le bombardement de la ville basque de Guernica pendant la guerre civile espagnole."},
        {"id": "q3", "enonce": "En quelle année Picasso peint-il Guernica ?", "choix": ["1937", "1900", "1945", "1960"], "reponse": 0, "explication": "Picasso peint Guernica en 1937."},
        {"id": "q4", "enonce": "Dans quelles couleurs Guernica est-il peint ?", "choix": ["Noir, blanc et gris", "Des couleurs vives et variées", "Uniquement du rouge", "Uniquement du bleu"], "reponse": 0, "explication": "Guernica est peint en noir, blanc et gris, ce qui accentue l'effet dramatique de l'œuvre."},
        {"id": "q5", "enonce": "La musique peut-elle accompagner des mouvements citoyens ?", "choix": ["Oui, de nombreuses chansons ont accompagné des luttes sociales", "Non, la musique est toujours neutre", "Uniquement la musique classique", "Cela n'a jamais existé"], "reponse": 0, "explication": "De nombreuses chansons ont accompagné des mouvements citoyens, dénonçant des injustices ou appelant à la paix."},
        {"id": "q6", "enonce": "Pourquoi la musique est-elle un outil puissant pour une cause ?", "choix": ["Grâce à sa diffusion large et son pouvoir émotionnel", "Elle n'a aucun impact", "Uniquement car elle est gratuite", "Uniquement car elle est facile à composer"], "reponse": 0, "explication": "La musique, par sa diffusion large et son pouvoir émotionnel, sensibilise efficacement un large public."},
        {"id": "q7", "enonce": "Que peut faire un artiste engagé selon le texte ?", "choix": ["Représenter le monde, dénoncer des injustices, ou imaginer un monde meilleur", "Uniquement peindre des paysages", "Uniquement suivre les modes artistiques", "Rien de particulier"], "reponse": 0, "explication": "Un artiste engagé peut représenter le monde tel qu'il est, dénoncer des injustices, ou imaginer un monde meilleur."},
        {"id": "q8", "enonce": "Que permet de développer l'analyse d'une œuvre engagée ?", "choix": ["L'esprit critique", "Uniquement des compétences techniques de dessin", "Rien de particulier", "Uniquement la mémoire"], "reponse": 0, "explication": "Analyser une œuvre engagée permet de développer son esprit critique."},
        {"id": "q9", "enonce": "Pourquoi est-il important de connaître le contexte historique d'une œuvre engagée ?", "choix": ["Pour comprendre pleinement le message de l'artiste", "Ce n'est pas important", "Uniquement pour connaître la date de création", "Uniquement pour les besoins scolaires"], "reponse": 0, "explication": "Le contexte historique permet de comprendre pleinement le message porté par l'artiste."},
        {"id": "q10", "enonce": "L'art engagé se limite-t-il à la peinture ?", "choix": ["Non, il concerne aussi la musique et d'autres formes d'art", "Oui, uniquement la peinture", "Non, uniquement la sculpture", "L'art engagé n'existe pas"], "reponse": 0, "explication": "L'art engagé concerne de nombreuses formes artistiques : peinture, musique, sculpture, littérature..."},
    ],
})

L.append({
    "slug": "patrimoine-culturel-transmission-4e", "titre": "Le patrimoine culturel et sa transmission",
    "matiere": "emc", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre l'importance du patrimoine culturel, matériel et immatériel, et les enjeux citoyens de sa préservation.",
    "objectifs": ["Distinguer patrimoine matériel et patrimoine immatériel", "Comprendre le rôle de l'UNESCO dans la protection du patrimoine mondial", "Réfléchir à la responsabilité citoyenne face à la préservation du patrimoine"],
    "contenu": [
        "Le patrimoine culturel comprend le patrimoine matériel (monuments, œuvres d'art, sites archéologiques) et le patrimoine immatériel (traditions, savoir-faire, langues, musiques, fêtes populaires), transmis de génération en génération. Ce patrimoine constitue la mémoire collective d'une société et contribue à son identité culturelle.",
        "L'UNESCO, organisation des Nations unies pour l'éducation, la science et la culture, établit des listes de sites et de pratiques culturelles considérés comme ayant une valeur universelle exceptionnelle : le patrimoine mondial (monuments, sites naturels) et le patrimoine culturel immatériel (comme la gastronomie française, inscrite en 2010).",
        "La préservation du patrimoine est une responsabilité citoyenne collective : elle implique de protéger les sites contre la dégradation, le vandalisme ou le pillage, mais aussi de transmettre activement les savoir-faire et traditions immatérielles, qui peuvent disparaître si personne ne les pratique ou ne les enseigne plus.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que le patrimoine matériel ?", "choix": ["Les monuments, œuvres d'art, sites archéologiques", "Uniquement les traditions orales", "Uniquement les langues", "Uniquement les fêtes populaires"], "reponse": 0, "explication": "Le patrimoine matériel comprend les monuments, œuvres d'art et sites archéologiques."},
        {"id": "q2", "enonce": "Qu'est-ce que le patrimoine immatériel ?", "choix": ["Les traditions, savoir-faire, langues, musiques", "Uniquement les monuments", "Uniquement les musées", "Uniquement l'argent public"], "reponse": 0, "explication": "Le patrimoine immatériel comprend les traditions, savoir-faire, langues, musiques et fêtes populaires."},
        {"id": "q3", "enonce": "Que signifie le sigle UNESCO ?", "choix": ["Organisation des Nations unies pour l'éducation, la science et la culture", "Union européenne pour la sauvegarde culturelle", "Organisation nationale pour l'éducation scolaire", "Union nationale pour l'économie et le commerce"], "reponse": 0, "explication": "UNESCO signifie Organisation des Nations unies pour l'éducation, la science et la culture."},
        {"id": "q4", "enonce": "Que fait l'UNESCO pour le patrimoine ?", "choix": ["Elle établit des listes de sites et pratiques ayant une valeur universelle exceptionnelle", "Elle détruit les monuments anciens", "Elle interdit toute visite touristique", "Elle finance uniquement des films"], "reponse": 0, "explication": "L'UNESCO établit des listes du patrimoine mondial et du patrimoine culturel immatériel."},
        {"id": "q5", "enonce": "La gastronomie française est-elle reconnue par l'UNESCO ?", "choix": ["Oui, comme patrimoine culturel immatériel depuis 2010", "Non, jamais", "Uniquement certains plats spécifiques", "Uniquement en Europe"], "reponse": 0, "explication": "La gastronomie française est inscrite au patrimoine culturel immatériel de l'UNESCO depuis 2010."},
        {"id": "q6", "enonce": "Pourquoi le patrimoine culturel est-il important pour une société ?", "choix": ["Il constitue sa mémoire collective et contribue à son identité culturelle", "Il n'a aucune importance", "Il sert uniquement au tourisme", "Il concerne uniquement les historiens"], "reponse": 0, "explication": "Le patrimoine culturel constitue la mémoire collective d'une société et contribue à son identité culturelle."},
        {"id": "q7", "enonce": "Le patrimoine immatériel peut-il disparaître ?", "choix": ["Oui, s'il n'est plus pratiqué ou enseigné", "Non, il est éternel", "Uniquement en cas de guerre", "Il ne peut jamais disparaître"], "reponse": 0, "explication": "Le patrimoine immatériel peut disparaître si personne ne le pratique ou ne le transmet plus."},
        {"id": "q8", "enonce": "Quelles menaces pèsent sur le patrimoine matériel ?", "choix": ["La dégradation, le vandalisme, le pillage", "Aucune menace n'existe", "Uniquement le changement de mode", "Uniquement les impôts"], "reponse": 0, "explication": "Le patrimoine matériel peut être menacé par la dégradation, le vandalisme ou le pillage."},
        {"id": "q9", "enonce": "La préservation du patrimoine est-elle uniquement l'affaire de l'État ?", "choix": ["Non, c'est une responsabilité citoyenne collective", "Oui, uniquement l'État", "Non, uniquement les touristes", "Cela ne concerne personne"], "reponse": 0, "explication": "La préservation du patrimoine est présentée comme une responsabilité citoyenne collective."},
        {"id": "q10", "enonce": "Comment peut-on contribuer à transmettre le patrimoine immatériel ?", "choix": ["En pratiquant et en enseignant activement les savoir-faire et traditions", "En les gardant secrets", "En les interdisant", "Cela ne se transmet jamais"], "reponse": 0, "explication": "Le patrimoine immatériel se transmet en pratiquant et en enseignant activement les savoir-faire et traditions."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "esprit-critique-information-4e", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecons EMC 4e (numerique/arts-culture) ajoutees.")
