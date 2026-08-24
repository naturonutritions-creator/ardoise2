# -*- coding: utf-8 -*-
PATH = "src/content/lessons.ts"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def lesson_block(d):
    obj = ", ".join('"' + esc(o) + '"' for o in d["objectifs"])
    cont = ", ".join('"' + esc(c) + '"' for c in d["contenu"])
    extra = ""
    if d.get("ecouteIntonation"):
        items = ", ".join('{ phrase: "' + esc(x["phrase"]) + '", type: "' + x["type"] + '" }' for x in d["ecouteIntonation"])
        extra += f'\n    ecouteIntonation: [{items}],'
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
        f'    duree: "{d["duree"]}",\n    resume: "{esc(d["resume"])}",{extra}\n'
        f'    objectifs: [{obj}],\n    contenu: [{cont}],\n    {quiz_block}\n  }},'
    )

def insert_before(txt, anchor_slug, new_dicts):
    idx = txt.index(f'  {{\n    slug: "{anchor_slug}",')
    insertion = "\n".join(lesson_block(d) for d in new_dicts) + "\n"
    return txt[:idx] + insertion + txt[idx:]

L = []

L.append({
    "slug": "modaux-obligation-conseil-anglais-4e", "titre": "Les modaux must, have to, should",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir exprimer l'obligation, l'interdiction et le conseil avec les modaux must, have to et should.",
    "ecouteIntonation": [
        {"phrase": "You must wear a seatbelt.", "type": "affirmation"},
        {"phrase": "You mustn't smoke here.", "type": "affirmation"},
        {"phrase": "Do you have to leave now?", "type": "question"},
        {"phrase": "You should ask your teacher.", "type": "affirmation"},
        {"phrase": "That's a great idea!", "type": "exclamation"},
    ],
    "objectifs": ["Distinguer must, have to et should", "Exprimer une obligation ou une interdiction", "Donner un conseil avec should"],
    "contenu": [
        "Must exprime une obligation forte, souvent décidée par celui qui parle : You must finish your homework. Sa forme négative, mustn't, exprime une interdiction : You mustn't be late.",
        "Have to exprime aussi une obligation, mais imposée par une règle extérieure (loi, règlement) : Students have to wear a uniform. Sa forme négative, don't have to, signifie qu'il n'y a pas d'obligation, contrairement à mustn't : You don't have to come if you are tired.",
        "Should exprime un conseil ou une recommandation, plus doux qu'une obligation : You should drink more water. On l'utilise pour suggérer ce qui est bon de faire, sans imposer une règle stricte.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « You must wear a seatbelt » ?", "choix": ["Une obligation forte", "Un conseil léger", "Une interdiction", "Une possibilité"], "reponse": 0, "explication": "Must exprime une obligation forte."},
        {"id": "q2", "enonce": "Que signifie « mustn't » ?", "choix": ["Une obligation", "Une interdiction", "Un conseil", "Une possibilité"], "reponse": 1, "explication": "Mustn't exprime une interdiction, contrairement à don't have to."},
        {"id": "q3", "enonce": "Que signifie « don't have to » ?", "choix": ["Une interdiction stricte", "L'absence d'obligation", "Une obligation forte", "Un conseil"], "reponse": 1, "explication": "Don't have to signifie qu'il n'y a pas d'obligation de faire quelque chose."},
        {"id": "q4", "enonce": "Quel modal exprime une obligation imposée par un règlement extérieur ?", "choix": ["Should", "Have to", "Might", "Can"], "reponse": 1, "explication": "Have to exprime une obligation imposée par une règle extérieure, comme la loi ou un règlement."},
        {"id": "q5", "enonce": "Quel modal exprime un conseil ?", "choix": ["Must", "Should", "Mustn't", "Have to"], "reponse": 1, "explication": "Should exprime un conseil ou une recommandation."},
        {"id": "q6", "enonce": "Complétez : « You ___ study for the test. » (conseil)", "choix": ["mustn't", "should", "don't have to", "having"], "reponse": 1, "explication": "Should exprime un conseil : « You should study for the test »."},
        {"id": "q7", "enonce": "Complétez : « Students ___ wear a uniform at this school. » (règle)", "choix": ["have to", "should", "mustn't", "having"], "reponse": 0, "explication": "Have to exprime une obligation imposée par le règlement de l'école."},
        {"id": "q8", "enonce": "Complétez : « You ___ smoke here. » (interdiction)", "choix": ["have to", "should", "mustn't", "don't have to"], "reponse": 2, "explication": "Mustn't exprime une interdiction : il est interdit de fumer ici."},
        {"id": "q9", "enonce": "« You don't have to come » signifie :", "choix": ["Il est interdit de venir", "Ce n'est pas obligatoire de venir", "Il faut absolument venir", "Il est conseillé de venir"], "reponse": 1, "explication": "Don't have to signifie que ce n'est pas obligatoire, la personne est libre de choisir."},
        {"id": "q10", "enonce": "Quel modal est le plus doux, un simple conseil ?", "choix": ["Must", "Mustn't", "Should", "Have to"], "reponse": 2, "explication": "Should est le modal le plus doux, utilisé pour donner un simple conseil."},
    ],
})

L.append({
    "slug": "futur-will-going-to-anglais-4e", "titre": "Le futur : will et going to",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir choisir entre will et going to pour parler du futur en anglais.",
    "ecouteIntonation": [
        {"phrase": "I will help you tomorrow.", "type": "affirmation"},
        {"phrase": "Are you going to travel this summer?", "type": "question"},
        {"phrase": "It's going to rain!", "type": "exclamation"},
        {"phrase": "She will call you later.", "type": "affirmation"},
    ],
    "objectifs": ["Former le futur avec will", "Former le futur avec be going to", "Choisir entre will et going to selon le contexte"],
    "contenu": [
        "Will + base verbale s'utilise pour une décision spontanée, une prédiction incertaine, ou une promesse : I will call you tonight. It will probably rain tomorrow. La forme négative est won't (will not).",
        "Be going to + base verbale s'utilise pour un projet déjà décidé avant le moment où l'on parle, ou pour une prédiction basée sur des signes visibles dans le présent : I am going to visit my grandmother next week. Look at those clouds, it's going to rain!",
        "La différence principale entre les deux formes est donc le degré de préparation : will pour une décision prise à l'instant, going to pour un projet déjà planifié. Dans la langue courante, les deux formes sont parfois interchangeables pour les prédictions générales.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quelle structure utilise-t-on pour une décision spontanée ?", "choix": ["Will", "Be going to", "Present simple", "Past simple"], "reponse": 0, "explication": "Will s'utilise pour une décision spontanée, prise au moment où l'on parle."},
        {"id": "q2", "enonce": "Quelle structure utilise-t-on pour un projet déjà décidé ?", "choix": ["Will", "Be going to", "Present perfect", "Past continuous"], "reponse": 1, "explication": "Be going to s'utilise pour un projet déjà décidé avant le moment où l'on parle."},
        {"id": "q3", "enonce": "Quelle est la forme négative de will ?", "choix": ["Willn't", "Won't", "Don't will", "Not will"], "reponse": 1, "explication": "La forme négative de will est won't (will not)."},
        {"id": "q4", "enonce": "Complétez : « I ___ help you, I promise! » (promesse spontanée)", "choix": ["am going to", "will", "was", "have"], "reponse": 1, "explication": "Will s'utilise pour exprimer une promesse spontanée."},
        {"id": "q5", "enonce": "Complétez : « Look at those clouds, it ___ rain! » (signe visible)", "choix": ["will", "is going to", "was", "has"], "reponse": 1, "explication": "Be going to s'utilise pour une prédiction basée sur un signe visible dans le présent."},
        {"id": "q6", "enonce": "Complétez : « I ___ visit my grandmother next week, I already booked the train. » (projet planifié)", "choix": ["will", "am going to", "was", "have"], "reponse": 1, "explication": "Be going to s'utilise pour un projet déjà planifié à l'avance."},
        {"id": "q7", "enonce": "Comment se forme « be going to » à la 3e personne du singulier ?", "choix": ["He going to", "He is going to", "He are going to", "He was going to"], "reponse": 1, "explication": "À la 3e personne du singulier, on utilise « is going to »."},
        {"id": "q8", "enonce": "« It will probably rain tomorrow » exprime :", "choix": ["Une prédiction incertaine", "Un projet planifié", "Une action passée", "Une habitude"], "reponse": 0, "explication": "Will exprime ici une prédiction incertaine sur le futur."},
        {"id": "q9", "enonce": "Quelle structure exprime le degré de préparation le plus élevé ?", "choix": ["Will", "Be going to", "Aucune différence", "Present simple"], "reponse": 1, "explication": "Be going to exprime un projet déjà préparé, contrairement à will qui exprime une décision spontanée."},
        {"id": "q10", "enonce": "Complétez : « Are you ___ travel this summer? »", "choix": ["will", "going to", "gone", "went"], "reponse": 1, "explication": "On utilise « going to » précédé de « be » pour parler d'un projet futur : « Are you going to travel? »."},
    ],
})

L.append({
    "slug": "voix-passive-introduction-anglais-4e", "titre": "La voix passive : introduction",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendre le principe de la voix passive et savoir la former au présent et au passé simples.",
    "objectifs": ["Comprendre la différence entre voix active et voix passive", "Former la voix passive au présent simple", "Former la voix passive au passé simple"],
    "contenu": [
        "À la voix active, le sujet fait l'action : The chef cooks the meal. À la voix passive, le sujet subit l'action, et l'accent est mis sur l'action elle-même plutôt que sur celui qui la fait : The meal is cooked (by the chef).",
        "La voix passive se forme avec l'auxiliaire be conjugué au temps voulu, suivi du participe passé du verbe : au présent simple, this bridge is built (par des ouvriers) ; au passé simple, this bridge was built in 1990. L'agent (celui qui fait l'action) est introduit par by, et peut être omis s'il n'est pas important ou inconnu.",
        "On utilise souvent la voix passive lorsque l'auteur de l'action est inconnu, évident ou sans importance : English is spoken all over the world. Cette structure est fréquente dans les textes informatifs, scientifiques ou journalistiques.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Dans « The chef cooks the meal », le sujet fait-il ou subit-il l'action ?", "choix": ["Il fait l'action (voix active)", "Il subit l'action (voix passive)", "Ni l'un ni l'autre", "Impossible à dire"], "reponse": 0, "explication": "C'est une phrase à la voix active : le sujet (the chef) fait l'action."},
        {"id": "q2", "enonce": "Comment se forme la voix passive ?", "choix": ["be + participe passé", "have + participe passé", "will + base verbale", "be + base verbale"], "reponse": 0, "explication": "La voix passive se forme avec be conjugué suivi du participe passé du verbe."},
        {"id": "q3", "enonce": "Quelle est la version passive de « The meal is cooked » ?", "choix": ["The chef cooks the meal", "The meal cooks the chef", "The meal is cooking", "The chef is cooked"], "reponse": 0, "explication": "« The chef cooks the meal » est la version active de « The meal is cooked »."},
        {"id": "q4", "enonce": "Quel mot introduit l'agent (celui qui fait l'action) à la voix passive ?", "choix": ["To", "By", "For", "With"], "reponse": 1, "explication": "L'agent est introduit par « by » à la voix passive."},
        {"id": "q5", "enonce": "Complétez : « This bridge ___ built in 1990. » (passé simple, passive)", "choix": ["is", "was", "has been", "will be"], "reponse": 1, "explication": "Au passé simple, la voix passive utilise « was/were + participe passé »."},
        {"id": "q6", "enonce": "Pourquoi utilise-t-on souvent la voix passive ?", "choix": ["Quand l'auteur de l'action est inconnu ou sans importance", "Uniquement pour les phrases négatives", "Uniquement au futur", "Jamais en anglais courant"], "reponse": 0, "explication": "La voix passive est utilisée quand l'auteur de l'action est inconnu, évident ou sans importance."},
        {"id": "q7", "enonce": "« English is spoken all over the world » est-elle à la voix active ou passive ?", "choix": ["Active", "Passive", "Ni l'une ni l'autre", "Impossible à dire"], "reponse": 1, "explication": "Cette phrase est à la voix passive : is spoken (be + participe passé)."},
        {"id": "q8", "enonce": "L'agent doit-il toujours être mentionné à la voix passive ?", "choix": ["Oui, toujours", "Non, il peut être omis", "Uniquement au présent", "Uniquement au passé"], "reponse": 1, "explication": "L'agent peut être omis s'il n'est pas important ou inconnu."},
        {"id": "q9", "enonce": "Dans quel type de texte la voix passive est-elle fréquente ?", "choix": ["Les textes informatifs et scientifiques", "Uniquement les poèmes", "Uniquement les textos", "Jamais utilisée à l'écrit"], "reponse": 0, "explication": "La voix passive est fréquente dans les textes informatifs, scientifiques ou journalistiques."},
        {"id": "q10", "enonce": "Quelle est la voix passive de « Someone stole my bike »?", "choix": ["My bike was stolen", "My bike steals someone", "Someone was stolen my bike", "My bike is stealing"], "reponse": 0, "explication": "« My bike was stolen » est la forme passive au passé simple."},
    ],
})

L.append({
    "slug": "discours-indirect-anglais-4e", "titre": "Le discours indirect (reported speech)",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir rapporter les paroles de quelqu'un en utilisant le discours indirect.",
    "objectifs": ["Comprendre le principe du discours indirect", "Savoir transformer une phrase du discours direct au discours indirect", "Connaître les changements de temps liés au discours indirect"],
    "contenu": [
        "Le discours direct rapporte les paroles exactes de quelqu'un entre guillemets : She said, « I am tired. » Le discours indirect (reported speech) rapporte ces mêmes paroles sans guillemets, introduites par un verbe comme said ou told : She said (that) she was tired.",
        "Lorsqu'on passe du discours direct au discours indirect, le temps du verbe recule généralement d'un cran dans le passé : le présent simple devient le prétérit (am/is/are → was/were), le présent perfect devient le past perfect, et le futur will devient would.",
        "Les pronoms et les indicateurs de temps ou de lieu changent aussi souvent : I devient he/she, my devient his/her, tomorrow devient the next day, here devient there. Par exemple : He said, « I will call you tomorrow » devient He said (that) he would call me the next day.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce que le discours direct ?", "choix": ["Rapporter les paroles exactes entre guillemets", "Rapporter des paroles sans guillemets", "Une forme de futur", "Une forme de passé"], "reponse": 0, "explication": "Le discours direct rapporte les paroles exactes de quelqu'un entre guillemets."},
        {"id": "q2", "enonce": "Qu'est-ce que le discours indirect ?", "choix": ["Rapporter des paroles entre guillemets", "Rapporter des paroles sans guillemets, introduites par said/told", "Une question directe", "Un ordre direct"], "reponse": 1, "explication": "Le discours indirect rapporte des paroles sans guillemets, introduites par un verbe comme said ou told."},
        {"id": "q3", "enonce": "Que devient le présent simple au discours indirect ?", "choix": ["Le prétérit", "Le present perfect", "Le futur", "Il ne change pas"], "reponse": 0, "explication": "Le présent simple devient généralement le prétérit au discours indirect."},
        {"id": "q4", "enonce": "Que devient « will » au discours indirect ?", "choix": ["Would", "Was", "Have", "Will (inchangé)"], "reponse": 0, "explication": "Will devient would au discours indirect."},
        {"id": "q5", "enonce": "Transformez : She said, « I am tired. » →", "choix": ["She said she is tired.", "She said she was tired.", "She says she was tired.", "She said I am tired."], "reponse": 1, "explication": "Am devient was, et I devient she au discours indirect."},
        {"id": "q6", "enonce": "Que devient « tomorrow » au discours indirect ?", "choix": ["Yesterday", "The next day", "Today", "Il ne change pas"], "reponse": 1, "explication": "Tomorrow devient généralement « the next day » au discours indirect."},
        {"id": "q7", "enonce": "Que devient « here » au discours indirect ?", "choix": ["There", "Here (inchangé)", "Now", "Then"], "reponse": 0, "explication": "Here devient there au discours indirect."},
        {"id": "q8", "enonce": "Transformez : He said, « I will call you tomorrow. » →", "choix": ["He said he will call me tomorrow.", "He said he would call me the next day.", "He said I will call you tomorrow.", "He says he would call me."], "reponse": 1, "explication": "Will devient would, I devient he, tomorrow devient the next day."},
        {"id": "q9", "enonce": "Quels verbes introducteurs sont couramment utilisés au discours indirect ?", "choix": ["Said et told", "Is et are", "Do et does", "Will et would"], "reponse": 0, "explication": "Said et told sont les verbes introducteurs les plus courants au discours indirect."},
        {"id": "q10", "enonce": "Que devient « my » quand on rapporte les paroles d'une autre personne ?", "choix": ["Cela dépend du contexte, souvent his/her", "My reste toujours inchangé", "Your", "Our"], "reponse": 0, "explication": "My devient généralement his ou her selon la personne dont on rapporte les paroles."},
    ],
})

L.append({
    "slug": "premiere-conditionnelle-anglais-4e", "titre": "La première conditionnelle (if + present, will)",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir exprimer une condition réalisable dans le futur avec la première conditionnelle.",
    "objectifs": ["Comprendre l'usage de la première conditionnelle", "Former une phrase avec if + présent simple + will", "Distinguer condition réalisable et condition irréelle"],
    "contenu": [
        "La première conditionnelle exprime une condition réalisable et sa conséquence probable dans le futur : If it rains tomorrow, we will stay home. Elle se compose de deux parties : la proposition avec if au présent simple, et la proposition principale avec will + base verbale.",
        "L'ordre des deux propositions peut être inversé sans changer le sens : If you study hard, you will pass the exam. équivaut à You will pass the exam if you study hard. Lorsque la proposition avec if est placée en premier, on la sépare de la principale par une virgule.",
        "On utilise la première conditionnelle pour parler de situations réellement possibles, contrairement à la deuxième conditionnelle (if + prétérit, would) qui exprime une situation hypothétique ou peu probable : If I won the lottery, I would travel the world.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "À quoi sert la première conditionnelle ?", "choix": ["Exprimer une condition réalisable et sa conséquence future", "Exprimer un fait passé", "Exprimer une habitude", "Exprimer un ordre"], "reponse": 0, "explication": "La première conditionnelle exprime une condition réalisable et sa conséquence probable dans le futur."},
        {"id": "q2", "enonce": "Quelle est la structure de la première conditionnelle ?", "choix": ["If + présent simple, will + base verbale", "If + prétérit, would + base verbale", "If + will, présent simple", "If + present perfect, will"], "reponse": 0, "explication": "La première conditionnelle se forme avec if + présent simple dans une proposition, will + base verbale dans l'autre."},
        {"id": "q3", "enonce": "Complétez : « If it ___ tomorrow, we will stay home. »", "choix": ["rains", "will rain", "rained", "is raining"], "reponse": 0, "explication": "Après if dans la première conditionnelle, on utilise le présent simple : rains."},
        {"id": "q4", "enonce": "Complétez : « If you study hard, you ___ pass the exam. »", "choix": ["pass", "will pass", "passed", "passing"], "reponse": 1, "explication": "Dans la proposition principale, on utilise will + base verbale : will pass."},
        {"id": "q5", "enonce": "Faut-il une virgule quand la proposition avec if est placée en premier ?", "choix": ["Oui", "Non, jamais", "Uniquement à l'oral", "Cela dépend du verbe"], "reponse": 0, "explication": "Une virgule sépare les deux propositions quand celle avec if est placée en premier."},
        {"id": "q6", "enonce": "Que signifie « if » dans cette structure ?", "choix": ["Si", "Quand", "Bien que", "Parce que"], "reponse": 0, "explication": "If signifie « si » et introduit la condition."},
        {"id": "q7", "enonce": "La première conditionnelle exprime-t-elle une situation réalisable ou hypothétique ?", "choix": ["Réalisable", "Hypothétique et peu probable", "Impossible", "Passée"], "reponse": 0, "explication": "La première conditionnelle exprime une situation réellement possible, contrairement à la deuxième conditionnelle."},
        {"id": "q8", "enonce": "Quelle structure exprime une situation hypothétique peu probable ?", "choix": ["If + présent, will", "If + prétérit, would", "If + will, présent", "If + present perfect, will"], "reponse": 1, "explication": "La deuxième conditionnelle (if + prétérit, would) exprime une situation hypothétique ou peu probable."},
        {"id": "q9", "enonce": "Peut-on inverser l'ordre des deux propositions sans changer le sens ?", "choix": ["Oui", "Non, jamais", "Uniquement au passé", "Uniquement à l'oral"], "reponse": 0, "explication": "L'ordre des deux propositions peut être inversé sans changer le sens global de la phrase."},
        {"id": "q10", "enonce": "Complétez correctement : « You will pass the exam ___ you study hard. »", "choix": ["if", "will", "would", "was"], "reponse": 0, "explication": "If introduit la condition, même en fin de phrase, sans virgule dans ce cas."},
    ],
})

L.append({
    "slug": "pronoms-relatifs-anglais-4e", "titre": "Les pronoms relatifs who, which, that",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir utiliser les pronoms relatifs who, which et that pour relier deux idées dans une phrase.",
    "objectifs": ["Utiliser who pour parler d'une personne", "Utiliser which pour parler d'une chose", "Comprendre l'usage général de that"],
    "contenu": [
        "Un pronom relatif permet de relier deux phrases en évitant une répétition, en donnant plus d'informations sur un nom déjà mentionné. Who s'utilise pour désigner une personne : The woman who lives next door is a doctor. (au lieu de : The woman is a doctor. She lives next door.)",
        "Which s'utilise pour désigner une chose, un animal ou une idée : The book which I read last week was amazing. That peut remplacer who ou which dans de nombreux cas, en particulier à l'oral et dans un style informel : The book that I read last week was amazing.",
        "Dans certains cas, le pronom relatif peut être totalement omis lorsqu'il n'est pas sujet de la proposition relative : The book (that/which) I read was amazing. En revanche, lorsqu'il est sujet, il ne peut jamais être omis : The man who called you is my uncle.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quel pronom relatif utilise-t-on pour une personne ?", "choix": ["Who", "Which", "What", "Whose seulement"], "reponse": 0, "explication": "Who s'utilise pour désigner une personne."},
        {"id": "q2", "enonce": "Quel pronom relatif utilise-t-on pour une chose ?", "choix": ["Who", "Which", "Whom", "Aucun"], "reponse": 1, "explication": "Which s'utilise pour désigner une chose, un animal ou une idée."},
        {"id": "q3", "enonce": "Que peut remplacer « that » dans de nombreux cas ?", "choix": ["Who ou which", "Uniquement who", "Uniquement which", "Aucun des deux"], "reponse": 0, "explication": "That peut souvent remplacer who ou which, notamment à l'oral."},
        {"id": "q4", "enonce": "Complétez : « The woman ___ lives next door is a doctor. »", "choix": ["who", "which", "what", "whom"], "reponse": 0, "explication": "Who s'utilise pour désigner une personne, ici « the woman »."},
        {"id": "q5", "enonce": "Complétez : « The book ___ I read last week was amazing. »", "choix": ["who", "which", "whose", "whom"], "reponse": 1, "explication": "Which s'utilise pour désigner une chose, ici « the book »."},
        {"id": "q6", "enonce": "Peut-on omettre le pronom relatif quand il est sujet de la relative ?", "choix": ["Oui, toujours", "Non, jamais", "Uniquement à l'écrit", "Uniquement au passé"], "reponse": 1, "explication": "Le pronom relatif ne peut jamais être omis lorsqu'il est sujet de la proposition relative."},
        {"id": "q7", "enonce": "Dans « The man who called you is my uncle », peut-on omettre « who » ?", "choix": ["Oui", "Non, car who est sujet de la relative", "Cela dépend du contexte", "Uniquement à l'oral"], "reponse": 1, "explication": "Who est ici sujet de la proposition relative (who called you), il ne peut donc pas être omis."},
        {"id": "q8", "enonce": "À quoi sert un pronom relatif ?", "choix": ["À relier deux phrases en évitant une répétition", "À former le futur", "À former une question", "À exprimer une négation"], "reponse": 0, "explication": "Un pronom relatif permet de relier deux phrases en évitant une répétition."},
        {"id": "q9", "enonce": "Dans quel registre « that » est-il particulièrement fréquent ?", "choix": ["À l'oral et dans un style informel", "Uniquement dans les textes juridiques", "Uniquement au passé", "Jamais utilisé"], "reponse": 0, "explication": "That est particulièrement fréquent à l'oral et dans un style informel."},
        {"id": "q10", "enonce": "Complétez : « The book (___) I read was amazing » (pronom non sujet, peut être omis)", "choix": ["that/which", "who", "whose", "whom"], "reponse": 0, "explication": "That ou which peuvent être omis ici car ils ne sont pas sujets de la proposition relative."},
    ],
})

L.append({
    "slug": "quantifieurs-much-many-anglais-4e", "titre": "Exprimer la quantité : much, many, few, little, a lot of",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir utiliser les quantifieurs adaptés aux noms dénombrables et indénombrables.",
    "objectifs": ["Distinguer noms dénombrables et indénombrables", "Utiliser many et few avec les dénombrables", "Utiliser much et little avec les indénombrables"],
    "contenu": [
        "Les noms dénombrables (countable nouns) peuvent se compter et avoir un pluriel : one apple, two apples. Les noms indénombrables (uncountable nouns) ne peuvent pas se compter directement et n'ont pas de pluriel : water, information, money, time.",
        "Avec les noms dénombrables au pluriel, on utilise many (beaucoup) et few (peu) : There aren't many apples left. There are few students in this class. Avec les noms indénombrables, on utilise much (beaucoup) et little (peu) : There isn't much water left. There is little information available.",
        "A lot of (ou lots of) s'utilise avec les deux types de noms, aussi bien dans les phrases affirmatives que négatives ou interrogatives : There is a lot of traffic today. There are a lot of tourists in this city. Much et many s'utilisent surtout dans les phrases négatives et interrogatives, plus rarement dans les phrases affirmatives.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qu'est-ce qu'un nom dénombrable ?", "choix": ["Un nom qui peut se compter et avoir un pluriel", "Un nom qui ne peut jamais se compter", "Un nom toujours au singulier", "Un nom sans article"], "reponse": 0, "explication": "Un nom dénombrable peut se compter et avoir un pluriel, comme apple/apples."},
        {"id": "q2", "enonce": "Citez un nom indénombrable.", "choix": ["Apple", "Water", "Book", "Student"], "reponse": 1, "explication": "Water est un nom indénombrable : on ne dit pas « two waters » dans ce sens."},
        {"id": "q3", "enonce": "Quel quantifieur utilise-t-on avec les dénombrables pluriels pour « beaucoup » ?", "choix": ["Much", "Many", "Little", "Aucun"], "reponse": 1, "explication": "Many s'utilise avec les noms dénombrables au pluriel pour exprimer « beaucoup »."},
        {"id": "q4", "enonce": "Quel quantifieur utilise-t-on avec les indénombrables pour « beaucoup » ?", "choix": ["Many", "Much", "Few", "A few"], "reponse": 1, "explication": "Much s'utilise avec les noms indénombrables pour exprimer « beaucoup »."},
        {"id": "q5", "enonce": "Quel quantifieur exprime « peu » avec un nom dénombrable pluriel ?", "choix": ["Little", "Few", "Much", "A lot of"], "reponse": 1, "explication": "Few exprime « peu » avec les noms dénombrables au pluriel."},
        {"id": "q6", "enonce": "Quel quantifieur exprime « peu » avec un nom indénombrable ?", "choix": ["Few", "Little", "Many", "A lot of"], "reponse": 1, "explication": "Little exprime « peu » avec les noms indénombrables."},
        {"id": "q7", "enonce": "Complétez : « There aren't ___ apples left. »", "choix": ["much", "many", "little", "a little"], "reponse": 1, "explication": "Many s'utilise avec le nom dénombrable pluriel « apples »."},
        {"id": "q8", "enonce": "Complétez : « There isn't ___ water left. »", "choix": ["many", "much", "few", "a few"], "reponse": 1, "explication": "Much s'utilise avec le nom indénombrable « water »."},
        {"id": "q9", "enonce": "Quel quantifieur peut s'utiliser avec les deux types de noms ?", "choix": ["A lot of", "Many uniquement", "Much uniquement", "Few uniquement"], "reponse": 0, "explication": "A lot of (ou lots of) s'utilise aussi bien avec les dénombrables qu'avec les indénombrables."},
        {"id": "q10", "enonce": "Dans quel type de phrases much et many sont-ils surtout utilisés ?", "choix": ["Uniquement les phrases affirmatives", "Les phrases négatives et interrogatives", "Uniquement au passé", "Uniquement à l'impératif"], "reponse": 1, "explication": "Much et many s'utilisent surtout dans les phrases négatives et interrogatives."},
    ],
})

L.append({
    "slug": "environnement-vocabulaire-anglais-4e", "titre": "Parler de l'environnement en anglais",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Acquérir le vocabulaire de l'environnement et du développement durable pour en discuter en anglais.",
    "objectifs": ["Acquérir le vocabulaire de l'environnement", "Savoir exprimer une opinion sur un enjeu écologique", "Comprendre un court texte sur le développement durable"],
    "contenu": [
        "Le vocabulaire de l'environnement inclut des mots essentiels : climate change (le changement climatique), global warming (le réchauffement climatique), pollution (la pollution), renewable energy (l'énergie renouvelable), recycling (le recyclage), endangered species (les espèces menacées), et sustainable development (le développement durable).",
        "Pour exprimer une opinion sur un sujet écologique, on peut utiliser des structures comme : In my opinion, we should reduce plastic waste. I think that renewable energy is the future. I strongly believe that everyone should recycle. It is essential to protect endangered species.",
        "De nombreux pays anglophones mènent des actions pour l'environnement : au Royaume-Uni et en Australie, des campagnes encouragent le recyclage et la réduction des déchets plastiques ; au Canada, de vastes programmes protègent les forêts et la faune sauvage face au changement climatique.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « climate change » ?", "choix": ["Le changement climatique", "Le recyclage", "L'énergie solaire", "La pollution de l'eau"], "reponse": 0, "explication": "Climate change signifie « le changement climatique »."},
        {"id": "q2", "enonce": "Que signifie « renewable energy » ?", "choix": ["L'énergie renouvelable", "L'énergie nucléaire", "Le pétrole", "Le charbon"], "reponse": 0, "explication": "Renewable energy signifie « l'énergie renouvelable »."},
        {"id": "q3", "enonce": "Que signifie « endangered species » ?", "choix": ["Les espèces menacées", "Les espèces domestiques", "Les espèces invasives", "Les plantes uniquement"], "reponse": 0, "explication": "Endangered species signifie « les espèces menacées »."},
        {"id": "q4", "enonce": "Comment dit-on « le développement durable » en anglais ?", "choix": ["Sustainable development", "Global warming", "Plastic waste", "Recycling"], "reponse": 0, "explication": "Le développement durable se dit sustainable development en anglais."},
        {"id": "q5", "enonce": "Quelle structure permet d'exprimer une opinion ?", "choix": ["In my opinion...", "Once upon a time...", "How are you?", "Thank you very much"], "reponse": 0, "explication": "« In my opinion » est une structure classique pour exprimer une opinion."},
        {"id": "q6", "enonce": "Que signifie « recycling » ?", "choix": ["Le recyclage", "Le réchauffement", "La déforestation", "La pollution"], "reponse": 0, "explication": "Recycling signifie « le recyclage »."},
        {"id": "q7", "enonce": "Que signifie « pollution » en anglais ?", "choix": ["Le même mot qu'en français, la pollution", "Le recyclage", "L'énergie propre", "La forêt"], "reponse": 0, "explication": "Pollution se traduit directement par « la pollution »."},
        {"id": "q8", "enonce": "Quel pays anglophone mène de vastes programmes pour protéger ses forêts ?", "choix": ["Le Canada", "Aucun pays anglophone", "Uniquement les États-Unis", "Uniquement l'Inde"], "reponse": 0, "explication": "Le Canada mène de vastes programmes pour protéger ses forêts et sa faune sauvage."},
        {"id": "q9", "enonce": "Comment exprimer fortement une conviction en anglais ?", "choix": ["I strongly believe that...", "Maybe...", "I don't know...", "Perhaps..."], "reponse": 0, "explication": "« I strongly believe that » permet d'exprimer fortement une conviction."},
        {"id": "q10", "enonce": "Que signifie « global warming » ?", "choix": ["Le réchauffement climatique", "Le recyclage", "L'énergie solaire", "La biodiversité"], "reponse": 0, "explication": "Global warming signifie « le réchauffement climatique »."},
    ],
})

L.append({
    "slug": "culture-australie-canada-anglais-4e", "titre": "La culture de l'Australie et du Canada",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Découvrir des éléments culturels et géographiques de l'Australie et du Canada, deux pays anglophones.",
    "objectifs": ["Situer l'Australie et le Canada et connaître leurs capitales", "Découvrir des éléments culturels de ces deux pays", "Enrichir son vocabulaire sur le monde anglophone"],
    "contenu": [
        "L'Australie est à la fois un pays et un continent, situé dans l'hémisphère sud. Sa capitale est Canberra (et non Sydney, la ville la plus peuplée). L'Australie est connue pour sa faune unique (kangaroos, koalas), pour l'Uluru (Ayers Rock), un immense monolithe sacré pour les Aborigènes, peuples autochtones du pays, et pour la Grande Barrière de corail (the Great Barrier Reef), le plus grand récif corallien du monde.",
        "Le Canada, deuxième plus grand pays du monde par sa superficie, a pour capitale Ottawa. C'est un pays bilingue, où l'anglais et le français sont tous deux langues officielles, notamment au Québec, majoritairement francophone. Le Canada est réputé pour ses grands espaces naturels, ses forêts, ses lacs, et pour le hockey sur glace, sport national très populaire.",
        "Ces deux pays font partie du Commonwealth, une organisation regroupant d'anciennes colonies britanniques. Ils partagent aussi une riche diversité culturelle, liée à une immigration importante venue du monde entier, qui a façonné une identité multiculturelle propre à chacun de ces deux pays anglophones.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quelle est la capitale de l'Australie ?", "choix": ["Sydney", "Canberra", "Melbourne", "Perth"], "reponse": 1, "explication": "La capitale de l'Australie est Canberra, et non Sydney qui est la ville la plus peuplée."},
        {"id": "q2", "enonce": "Quelle est la capitale du Canada ?", "choix": ["Toronto", "Montréal", "Ottawa", "Vancouver"], "reponse": 2, "explication": "La capitale du Canada est Ottawa."},
        {"id": "q3", "enonce": "Comment appelle-t-on les peuples autochtones d'Australie ?", "choix": ["Les Aborigènes", "Les Maoris", "Les Inuits", "Les Vikings"], "reponse": 0, "explication": "Les Aborigènes sont les peuples autochtones d'Australie."},
        {"id": "q4", "enonce": "Qu'est-ce que l'Uluru ?", "choix": ["Un immense monolithe sacré en Australie", "Une ville canadienne", "Un animal australien", "Un lac canadien"], "reponse": 0, "explication": "L'Uluru (Ayers Rock) est un immense monolithe sacré pour les Aborigènes en Australie."},
        {"id": "q5", "enonce": "Comment appelle-t-on le plus grand récif corallien du monde, en Australie ?", "choix": ["The Great Barrier Reef", "The Grand Canyon", "The Great Lakes", "The Rocky Mountains"], "reponse": 0, "explication": "The Great Barrier Reef (la Grande Barrière de corail) est le plus grand récif corallien du monde."},
        {"id": "q6", "enonce": "Quelles sont les langues officielles du Canada ?", "choix": ["Anglais uniquement", "Français uniquement", "Anglais et français", "Espagnol et anglais"], "reponse": 2, "explication": "Le Canada est un pays bilingue, où l'anglais et le français sont tous deux langues officielles."},
        {"id": "q7", "enonce": "Quelle province canadienne est majoritairement francophone ?", "choix": ["L'Ontario", "Le Québec", "L'Alberta", "La Colombie-Britannique"], "reponse": 1, "explication": "Le Québec est la province canadienne majoritairement francophone."},
        {"id": "q8", "enonce": "Quel sport est particulièrement populaire au Canada ?", "choix": ["Le hockey sur glace", "Le cricket", "Le rugby", "Le baseball uniquement"], "reponse": 0, "explication": "Le hockey sur glace est le sport national très populaire au Canada."},
        {"id": "q9", "enonce": "L'Australie et le Canada font-ils partie du Commonwealth ?", "choix": ["Non, aucun des deux", "Oui, tous les deux", "Uniquement l'Australie", "Uniquement le Canada"], "reponse": 1, "explication": "L'Australie et le Canada font tous deux partie du Commonwealth."},
        {"id": "q10", "enonce": "Quel animal est emblématique de l'Australie ?", "choix": ["Le kangourou", "L'ours polaire", "Le castor", "Le renne"], "reponse": 0, "explication": "Le kangourou est un animal emblématique de la faune australienne."},
    ],
})

L.append({
    "slug": "used-to-habitudes-passees-anglais-4e", "titre": "Used to : parler d'habitudes passées",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Savoir utiliser used to pour décrire une habitude ou un état du passé qui n'existe plus aujourd'hui.",
    "objectifs": ["Comprendre le sens de used to", "Former des phrases affirmatives, négatives et interrogatives avec used to", "Distinguer used to du prétérit simple"],
    "contenu": [
        "Used to + base verbale s'utilise pour parler d'une habitude répétée ou d'un état qui existait dans le passé, mais qui n'est plus vrai aujourd'hui : I used to live in London (mais je n'y vis plus maintenant). She used to play the piano every day (mais elle ne joue plus, ou plus aussi souvent).",
        "La forme négative se construit avec didn't use to : I didn't use to like vegetables (attention, pas de -d à use dans cette forme). La forme interrogative se construit avec did... use to : Did you use to live here?",
        "Il ne faut pas confondre used to avec le prétérit simple : le prétérit simple décrit une action ponctuelle passée (I lived in Paris in 2015), tandis que used to insiste sur le caractère habituel ou durable de l'état ou de l'action passée, et sur le contraste avec le présent.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "À quoi sert « used to » ?", "choix": ["Parler d'une habitude passée qui n'existe plus", "Parler du futur", "Donner un ordre", "Poser une question au présent"], "reponse": 0, "explication": "Used to s'utilise pour parler d'une habitude ou d'un état passé qui n'est plus vrai aujourd'hui."},
        {"id": "q2", "enonce": "Complétez : « I ___ live in London, but now I live in Paris. »", "choix": ["use to", "used to", "am using to", "will use to"], "reponse": 1, "explication": "Used to exprime une habitude passée révolue."},
        {"id": "q3", "enonce": "Quelle est la forme négative de used to ?", "choix": ["Didn't used to", "Didn't use to", "Doesn't use to", "Not used to"], "reponse": 1, "explication": "La forme négative est didn't use to (sans -d à use)."},
        {"id": "q4", "enonce": "Quelle est la forme interrogative de used to ?", "choix": ["Use to you...?", "Did you use to...?", "Do you used to...?", "Are you used to...?"], "reponse": 1, "explication": "La forme interrogative se construit avec did + sujet + use to."},
        {"id": "q5", "enonce": "Complétez : « ___ you use to play football when you were young? »", "choix": ["Did", "Do", "Were", "Have"], "reponse": 0, "explication": "Did s'utilise pour former la question avec used to."},
        {"id": "q6", "enonce": "Que suggère « She used to play the piano every day » ?", "choix": ["Elle joue encore tous les jours", "Elle jouait autrefois, mais plus maintenant (ou plus autant)", "Elle ne joue jamais", "Elle va commencer à jouer"], "reponse": 1, "explication": "Used to indique que cette habitude appartient au passé et ne se vérifie plus aujourd'hui."},
        {"id": "q7", "enonce": "Quelle est la différence principale entre used to et le prétérit simple ?", "choix": ["Used to insiste sur une habitude passée révolue", "Il n'y a aucune différence", "Used to parle du futur", "Le prétérit ne peut jamais s'utiliser avec des habitudes"], "reponse": 0, "explication": "Used to insiste sur le caractère habituel ou durable de l'état passé, contrairement au prétérit simple qui décrit une action ponctuelle."},
        {"id": "q8", "enonce": "Complétez correctement : « I didn't ___ like vegetables when I was a child. »", "choix": ["used to", "use to", "using to", "uses to"], "reponse": 1, "explication": "Après didn't, on utilise « use to » sans -d."},
        {"id": "q9", "enonce": "« I lived in Paris in 2015 » décrit-il une habitude ou une action ponctuelle ?", "choix": ["Une habitude", "Une action ponctuelle datée", "Ni l'un ni l'autre", "Une action future"], "reponse": 1, "explication": "Le prétérit simple ici décrit une action ponctuelle, datée précisément (in 2015)."},
        {"id": "q10", "enonce": "Used to peut-il s'utiliser pour un état passé (pas seulement une action) ?", "choix": ["Non, jamais", "Oui, par exemple pour un lieu de résidence passé", "Uniquement pour les sports", "Uniquement pour la nourriture"], "reponse": 1, "explication": "Used to peut aussi décrire un état passé, comme un lieu de résidence (I used to live in London)."},
    ],
})

L.append({
    "slug": "voyages-vacances-vocabulaire-anglais-4e", "titre": "Le vocabulaire des voyages et des vacances",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Acquérir le vocabulaire nécessaire pour parler de voyages, de vacances et d'expériences touristiques.",
    "ecouteIntonation": [
        {"phrase": "Where did you go on holiday?", "type": "question"},
        {"phrase": "We stayed in a lovely hotel.", "type": "affirmation"},
        {"phrase": "What an amazing trip!", "type": "exclamation"},
        {"phrase": "Did you enjoy your flight?", "type": "question"},
    ],
    "objectifs": ["Acquérir le vocabulaire des voyages", "Savoir raconter une expérience de vacances", "Comprendre un court récit de voyage"],
    "contenu": [
        "Le vocabulaire des voyages inclut des mots essentiels : a flight (un vol), luggage/baggage (les bagages), a passport (un passeport), a journey/a trip (un voyage), accommodation (l'hébergement), a youth hostel (une auberge de jeunesse), sightseeing (visiter les sites touristiques), a souvenir (un souvenir).",
        "Pour raconter des vacances passées, on utilise souvent le prétérit simple : Last summer, we travelled to Scotland. We visited many castles and we stayed in a small guesthouse near the coast. On peut aussi utiliser le present perfect pour parler d'une expérience de vie sans préciser quand : I have visited Ireland twice.",
        "Décrire une expérience touristique implique souvent d'exprimer une impression : It was breathtaking! The scenery was absolutely stunning. I really enjoyed the local food. Ces expressions permettent d'enrichir un récit de voyage et de le rendre plus vivant et personnel.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Que signifie « a flight » ?", "choix": ["Un vol", "Un train", "Un bus", "Un bateau"], "reponse": 0, "explication": "A flight signifie « un vol » en avion."},
        {"id": "q2", "enonce": "Que signifie « luggage » ?", "choix": ["Les bagages", "Le passeport", "Le billet", "L'hôtel"], "reponse": 0, "explication": "Luggage (ou baggage) signifie « les bagages »."},
        {"id": "q3", "enonce": "Que signifie « accommodation » ?", "choix": ["L'hébergement", "Le transport", "La nourriture", "Le climat"], "reponse": 0, "explication": "Accommodation signifie « l'hébergement »."},
        {"id": "q4", "enonce": "Que signifie « a youth hostel » ?", "choix": ["Une auberge de jeunesse", "Un hôtel de luxe", "Un camping", "Un aéroport"], "reponse": 0, "explication": "A youth hostel signifie « une auberge de jeunesse »."},
        {"id": "q5", "enonce": "Que signifie « sightseeing » ?", "choix": ["Visiter les sites touristiques", "Faire ses valises", "Prendre l'avion", "Réserver un hôtel"], "reponse": 0, "explication": "Sightseeing signifie « visiter les sites touristiques »."},
        {"id": "q6", "enonce": "Quel temps utilise-t-on souvent pour raconter des vacances passées et datées ?", "choix": ["Le prétérit simple", "Le futur simple", "Le present continuous", "L'impératif"], "reponse": 0, "explication": "Le prétérit simple s'utilise pour raconter des événements passés datés, comme des vacances."},
        {"id": "q7", "enonce": "Quel temps utilise-t-on pour une expérience de vie sans préciser quand ?", "choix": ["Le present perfect", "Le prétérit simple uniquement", "Le futur", "L'impératif"], "reponse": 0, "explication": "Le present perfect s'utilise pour une expérience de vie sans préciser le moment exact."},
        {"id": "q8", "enonce": "Que signifie « It was breathtaking! » ?", "choix": ["C'était à couper le souffle !", "C'était ennuyeux", "C'était fatigant", "C'était bon marché"], "reponse": 0, "explication": "Breathtaking signifie « à couper le souffle », une impression très positive."},
        {"id": "q9", "enonce": "Que signifie « a souvenir » ?", "choix": ["Un objet-souvenir rapporté d'un voyage", "Un passeport", "Un vol", "Une valise"], "reponse": 0, "explication": "A souvenir désigne un objet rapporté en souvenir d'un voyage."},
        {"id": "q10", "enonce": "Comment demande-t-on où quelqu'un est parti en vacances ?", "choix": ["Where did you go on holiday?", "What is your name?", "How old are you?", "What time is it?"], "reponse": 0, "explication": "« Where did you go on holiday? » permet de demander la destination de vacances de quelqu'un."},
    ],
})

L.append({
    "slug": "essai-argumentatif-anglais-4e", "titre": "Rédiger un court essai argumentatif en anglais",
    "matiere": "anglais", "niveau": "4e", "duree": "20 min",
    "resume": "Apprendre la structure d'un court essai argumentatif en anglais pour défendre une opinion.",
    "objectifs": ["Connaître la structure d'un essai argumentatif simple", "Utiliser des connecteurs logiques pour organiser ses idées", "Savoir défendre une opinion à l'écrit en anglais"],
    "contenu": [
        "Un essai argumentatif simple en anglais comprend généralement trois parties : une introduction qui présente le sujet et annonce l'opinion défendue (Nowadays, many people think that... In this essay, I will argue that...), un développement qui présente des arguments avec des exemples, et une conclusion qui résume la position défendue.",
        "Pour organiser ses idées, on utilise des connecteurs logiques : firstly / secondly / finally (premièrement / deuxièmement / enfin) pour lister des arguments ; however / on the other hand (cependant / d'un autre côté) pour nuancer ou présenter un contre-argument ; for example / for instance (par exemple) pour illustrer une idée ; therefore / as a result (par conséquent) pour exprimer une conséquence.",
        "Pour défendre une opinion, on peut utiliser des expressions comme : I believe that... / In my opinion... / I am convinced that... Il est aussi recommandé, dans un essai équilibré, d'évoquer brièvement un point de vue opposé avant de conclure fermement sur sa propre position : Although some people disagree, I still believe that...",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Combien de parties comprend généralement un essai argumentatif simple ?", "choix": ["Deux", "Trois : introduction, développement, conclusion", "Cinq", "Une seule"], "reponse": 1, "explication": "Un essai argumentatif simple comprend une introduction, un développement et une conclusion."},
        {"id": "q2", "enonce": "Que signifie « firstly » ?", "choix": ["Premièrement", "Enfin", "Cependant", "Par exemple"], "reponse": 0, "explication": "Firstly signifie « premièrement », utilisé pour introduire un premier argument."},
        {"id": "q3", "enonce": "Quel connecteur permet d'introduire un contre-argument ?", "choix": ["Firstly", "However", "For example", "Therefore"], "reponse": 1, "explication": "However (cependant) permet d'introduire une nuance ou un contre-argument."},
        {"id": "q4", "enonce": "Quel connecteur permet de donner un exemple ?", "choix": ["For example", "Finally", "However", "Therefore"], "reponse": 0, "explication": "For example (par exemple) permet d'illustrer une idée par un exemple."},
        {"id": "q5", "enonce": "Quel connecteur exprime une conséquence ?", "choix": ["Therefore", "Firstly", "However", "For instance"], "reponse": 0, "explication": "Therefore (par conséquent) exprime une conséquence logique."},
        {"id": "q6", "enonce": "Quelle expression permet d'introduire son opinion ?", "choix": ["In my opinion...", "Once upon a time...", "The end.", "How are you?"], "reponse": 0, "explication": "« In my opinion » est une expression classique pour introduire une opinion personnelle."},
        {"id": "q7", "enonce": "Pourquoi est-il conseillé d'évoquer un point de vue opposé dans un essai équilibré ?", "choix": ["Ce n'est jamais conseillé", "Pour montrer qu'on a considéré différents angles avant de conclure", "Pour changer d'avis à la fin", "Pour remplir de l'espace"], "reponse": 1, "explication": "Évoquer un point de vue opposé montre une réflexion équilibrée avant de conclure fermement sur sa position."},
        {"id": "q8", "enonce": "Que fait la conclusion d'un essai argumentatif ?", "choix": ["Elle résume la position défendue", "Elle introduit un nouveau sujet", "Elle pose une question sans réponse", "Elle liste uniquement des exemples"], "reponse": 0, "explication": "La conclusion résume et confirme la position défendue tout au long de l'essai."},
        {"id": "q9", "enonce": "Quelle structure introduit typiquement un essai argumentatif ?", "choix": ["In this essay, I will argue that...", "The End.", "Once upon a time...", "Chapter One"], "reponse": 0, "explication": "« In this essay, I will argue that » est une formule d'introduction typique d'un essai argumentatif."},
        {"id": "q10", "enonce": "Que signifie « on the other hand » ?", "choix": ["D'un autre côté", "Par conséquent", "Premièrement", "Enfin"], "reponse": 0, "explication": "On the other hand signifie « d'un autre côté », utilisé pour nuancer ou opposer une idée."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_before(txt, "italien" if False else "preterit-anglais" , [])  # placeholder guard, not used

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

# insert after preterit-anglais (append following the sole existing 4e anglais lesson)
start = txt.index('  {\n    slug: "preterit-anglais",')
nxt = txt.index('\n  {\n    slug:', start + 10)
insertion = "\n" + "\n".join(lesson_block(d) for d in L)
txt = txt[:nxt] + insertion + txt[nxt:]

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lecons Anglais 4e ajoutees.")
