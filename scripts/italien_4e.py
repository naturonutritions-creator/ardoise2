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
    "slug": "dovere-consiglio-italien-4e", "titre": "Dovere, bisogna e il condizionale di consiglio",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper esprimere l'obbligo e il consiglio in italiano con dovere, bisogna e il condizionale.",
    "objectifs": ["Coniugare e usare il verbo dovere", "Usare bisogna + infinito per un obbligo generale", "Usare il condizionale di dovere (dovresti) per dare un consiglio"],
    "contenu": [
        "Il verbo dovere esprime un obbligo personale al presente indicativo : Devo finire i compiti. Io devo, tu devi, lui/lei deve, noi dobbiamo, voi dovete, loro devono. Dovere si costruisce sempre seguito da un verbo all'infinito.",
        "L'espressione impersonale bisogna, seguita da un infinito, esprime un obbligo generale, valido per tutti : Bisogna rispettare le regole. A differenza di dovere, bisogna non si coniuga secondo la persona : resta invariabile.",
        "Per dare un consiglio più leggero di un obbligo, si usa il condizionale presente di dovere : dovresti (tu), dovrebbe (lui/lei), dovreste (voi). Esempio : Dovresti studiare di più. Questa forma corrisponde al should dell'inglese o au should français « tu devrais ».",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Come si dice « je dois » in italiano ?", "choix": ["Devo", "Deve", "Dobbiamo", "Devi"], "reponse": 0, "explication": "« Io devo » corrisponde a « je dois »."},
        {"id": "q2", "enonce": "Come si coniuga dovere alla terza persona plurale ?", "choix": ["Devono", "Dovete", "Dobbiamo", "Deve"], "reponse": 0, "explication": "Loro devono è la terza persona plurale del verbo dovere."},
        {"id": "q3", "enonce": "Da cosa è sempre seguito il verbo dovere ?", "choix": ["Da un infinito", "Da un sostantivo", "Da un aggettivo", "Da un avverbio"], "reponse": 0, "explication": "Dovere si costruisce sempre seguito da un verbo all'infinito."},
        {"id": "q4", "enonce": "Cosa esprime « bisogna » ?", "choix": ["Un obbligo generale, valido per tutti", "Un consiglio leggero", "Un'ipotesi", "Un desiderio personale"], "reponse": 0, "explication": "Bisogna esprime un obbligo generale, impersonale."},
        {"id": "q5", "enonce": "Bisogna si coniuga secondo la persona ?", "choix": ["Sì, sempre", "No, resta invariabile", "Solo al plurale", "Solo al condizionale"], "reponse": 1, "explication": "Bisogna è una forma impersonale che resta sempre invariabile."},
        {"id": "q6", "enonce": "Come si dice « tu devrais » (consiglio) in italiano ?", "choix": ["Dovresti", "Devi", "Dovete", "Dovevi"], "reponse": 0, "explication": "Dovresti è il condizionale presente di dovere, usato per dare un consiglio."},
        {"id": "q7", "enonce": "Quale forma verbale esprime un consiglio più leggero di un obbligo ?", "choix": ["L'indicativo presente", "Il condizionale presente", "L'imperativo", "Il futuro"], "reponse": 1, "explication": "Il condizionale presente (dovresti, dovrebbe) esprime un consiglio più leggero."},
        {"id": "q8", "enonce": "Completa : « ___ rispettare le regole. » (obbligo generale)", "choix": ["Bisogna", "Dovresti", "Devi", "Dovremmo"], "reponse": 0, "explication": "Bisogna esprime un obbligo général, valido per tutti."},
        {"id": "q9", "enonce": "Completa : « Marco, ___ studiare di più. » (consiglio)", "choix": ["dovresti", "bisogna", "deve", "dobbiamo"], "reponse": 0, "explication": "Dovresti (condizionale) est utilisé pour donner un conseil personnalisé."},
        {"id": "q10", "enonce": "Qual è l'infinito del verbo « devo » ?", "choix": ["Dovere", "Volere", "Potere", "Sapere"], "reponse": 0, "explication": "Devo è la prima persona singolare del verbo dovere."},
    ],
})

L.append({
    "slug": "futuro-semplice-italien-4e", "titre": "Il futuro semplice",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper formare e usare il futuro semplice per parlare di progetti e previsioni.",
    "objectifs": ["Formare il futuro semplice dei verbi regolari", "Conoscere i principali futuri irregolari", "Usare il futuro per esprimere un progetto o una previsione"],
    "contenu": [
        "Il futuro semplice si forma a partire dall'infinito del verbo, togliendo la -e finale e aggiungendo le terminazioni -ò, -ai, -à, -emo, -ete, -anno. Per i verbi in -are, la a finale dell'infinito diventa e : parlare → parlerò, parlerai, parlerà...",
        "Molti verbi comuni hanno un futuro irregolare : essere → sarò, avere → avrò, andare → andrò, fare → farò, venire → verrò, potere → potrò, dovere → dovrò, vedere → vedrò. Queste forme irregolari vanno memorizzate.",
        "Il futuro semplice si usa per parlare di un progetto futuro (Domani andrò al mercato), per fare una previsione (Domani pioverà), o per esprimere una supposizione riguardo al presente (Sarà mezzogiorno, non ho l'orologio).",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Come si forma il futuro semplice dei verbi in -are ?", "choix": ["La a finale diventa e, poi si aggiungono le terminazioni", "Si aggiunge -ato all'infinito", "Non cambia mai", "Si usa sempre l'ausiliare avere"], "reponse": 0, "explication": "Per i verbi in -are, la a finale dell'infinito diventa e prima di aggiungere le terminazioni del futuro."},
        {"id": "q2", "enonce": "Qual è il futuro di « parlare » alla prima persona singolare ?", "choix": ["Parlerò", "Parlarò", "Parlavo", "Parlai"], "reponse": 0, "explication": "Parlerò è la prima persona singolare del futuro di parlare."},
        {"id": "q3", "enonce": "Qual è il futuro del verbo essere alla prima persona singolare ?", "choix": ["Sarò", "Essarò", "Sono", "Ero"], "reponse": 0, "explication": "Il futuro di essere è irregolare : sarò."},
        {"id": "q4", "enonce": "Qual è il futuro del verbo avere alla prima persona singolare ?", "choix": ["Avrò", "Averò", "Ho", "Avevo"], "reponse": 0, "explication": "Il futuro di avere è irregolare : avrò."},
        {"id": "q5", "enonce": "Qual è il futuro del verbo andare alla prima persona singolare ?", "choix": ["Andrò", "Andarò", "Vado", "Andavo"], "reponse": 0, "explication": "Il futuro di andare è irregolare : andrò."},
        {"id": "q6", "enonce": "Qual è il futuro del verbo fare alla prima persona singolare ?", "choix": ["Farò", "Facerò", "Faccio", "Facevo"], "reponse": 0, "explication": "Il futuro di fare è irregolare : farò."},
        {"id": "q7", "enonce": "Per cosa si usa il futuro semplice ?", "choix": ["Per un progetto futuro o una previsione", "Solo per il passato", "Solo per un'azione abituale", "Solo per un ordine"], "reponse": 0, "explication": "Il futuro semplice si usa per esprimere un progetto futuro o fare una previsione."},
        {"id": "q8", "enonce": "Completa : « Domani ___ (piovere). »", "choix": ["pioverà", "piovrà", "piove", "pioveva"], "reponse": 0, "explication": "Piovere è regolare al futuro : pioverà."},
        {"id": "q9", "enonce": "Il futuro può esprimere una supposizione sul presente ?", "choix": ["No, mai", "Sì, ad esempio « sarà mezzogiorno »", "Solo al passato", "Solo con l'imperativo"], "reponse": 1, "explication": "Il futuro può esprimere una supposizione riguardo al presente, come « sarà mezzogiorno »."},
        {"id": "q10", "enonce": "Qual è la terminazione del futuro alla terza persona plurale ?", "choix": ["-anno", "-erete", "-emmo", "-avano"], "reponse": 0, "explication": "La terza persona plurale del futuro ha la terminazione -anno."},
    ],
})

L.append({
    "slug": "forma-passiva-italien-4e", "titre": "La forma passiva : introduzione",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Comprendere il principio della forma passiva e saperla formare con essere e venire.",
    "objectifs": ["Distinguere la forma attiva e la forma passiva", "Formare la forma passiva con essere + participio passato", "Conoscere l'uso di venire come alternativa a essere"],
    "contenu": [
        "Nella forma attiva, il soggetto compie l'azione : Il cuoco prepara la cena. Nella forma passiva, il soggetto subisce l'azione, e l'attenzione si sposta sull'azione stessa : La cena è preparata (dal cuoco).",
        "La forma passiva si costruisce con l'ausiliare essere, coniugato al tempo desiderato, seguito dal participio passato del verbo, che si accorda in genere e numero con il soggetto : La lettera è scritta. Le lettere sono scritte. L'agente, se menzionato, è introdotto da da : La lettera è scritta da Marco.",
        "Nei tempi semplici, si può anche usare venire al posto di essere per formare la forma passiva, con una sfumatura di enfasi sull'azione stessa : La porta viene chiusa ogni sera. Venire non si usa però nei tempi composti come il passato prossimo.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Nella forma attiva, cosa fa il soggetto ?", "choix": ["Compie l'azione", "Subisce l'azione", "Non fa nulla", "È sempre plurale"], "reponse": 0, "explication": "Nella forma attiva, il soggetto compie l'azione."},
        {"id": "q2", "enonce": "Come si forma la forma passiva ?", "choix": ["Essere + participio passato", "Avere + infinito", "Stare + gerundio", "Andare + participio"], "reponse": 0, "explication": "La forma passiva si costruisce con essere seguito dal participio passato."},
        {"id": "q3", "enonce": "Con cosa si accorda il participio passato nella forma passiva ?", "choix": ["Con il soggetto, in genere e numero", "Non si accorda mai", "Con l'agente", "Con l'ausiliare avere"], "reponse": 0, "explication": "Il participio passato si accorda con il soggetto in genere e numero nella forma passiva."},
        {"id": "q4", "enonce": "Quale preposizione introduce l'agente nella forma passiva ?", "choix": ["Da", "Di", "A", "Con"], "reponse": 0, "explication": "L'agente è introdotto dalla preposizione da : scritta da Marco."},
        {"id": "q5", "enonce": "Trasforma alla forma passiva : « Il cuoco prepara la cena. »", "choix": ["La cena è preparata dal cuoco.", "Il cuoco è preparato dalla cena.", "La cena prepara il cuoco.", "Il cuoco preparerà la cena."], "reponse": 0, "explication": "« La cena è preparata dal cuoco » è la forma passiva corretta."},
        {"id": "q6", "enonce": "Quale altro ausiliare può sostituire essere nei tempi semplici della forma passiva ?", "choix": ["Venire", "Avere", "Fare", "Stare"], "reponse": 0, "explication": "Venire può sostituire essere nei tempi semplici della forma passiva."},
        {"id": "q7", "enonce": "Venire si usa nei tempi composti come il passato prossimo ?", "choix": ["Sì, sempre", "No, non si usa nei tempi composti", "Solo al futuro", "Solo all'imperativo"], "reponse": 1, "explication": "Venire non si usa nei tempi composti come il passato prossimo per la forma passiva."},
        {"id": "q8", "enonce": "Completa : « Le lettere ___ scritte. » (plurale femminile)", "choix": ["sono", "è", "sei", "siamo"], "reponse": 0, "explication": "Con un soggetto plurale femminile, si usa sono seguito dal participio accordato : scritte."},
        {"id": "q9", "enonce": "L'agente deve sempre essere menzionato nella forma passiva ?", "choix": ["Sì, sempre obbligatorio", "No, può essere omesso", "Solo al presente", "Solo al passato"], "reponse": 1, "explication": "L'agente può essere omesso se non è importante o è sconosciuto."},
        {"id": "q10", "enonce": "Cosa mette in evidenza la forma passiva ?", "choix": ["L'azione stessa, più che chi la compie", "Sempre e solo l'agente", "Il tempo del verbo", "Il numero del soggetto"], "reponse": 0, "explication": "La forma passiva mette l'accento sull'azione, spostando l'attenzione da chi la compie."},
    ],
})

L.append({
    "slug": "discorso-indiretto-italien-4e", "titre": "Il discorso indiretto",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper riportare le parole di qualcuno usando il discorso indiretto in italiano.",
    "objectifs": ["Comprendere il principio del discorso indiretto", "Trasformare una frase dal discorso diretto al discorso indiretto", "Conoscere i principali cambiamenti di tempo verbale"],
    "contenu": [
        "Il discorso diretto riporta le parole esatte di qualcuno tra virgolette : Maria dice: « Sono stanca. » Il discorso indiretto riporta le stesse parole senza virgolette, introdotte da un verbo come dire seguito da che : Maria dice che è stanca.",
        "Quando il verbo introduttivo è al presente (dice che), il tempo della frase riportata generalmente non cambia. Ma quando il verbo introduttivo è al passato (ha detto che), il tempo arretra spesso : il presente diventa imperfetto, il passato prossimo diventa trapassato prossimo, il futuro diventa condizionale passato.",
        "Anche i pronomi e gli indicatori di tempo o luogo cambiano spesso : io diventa lui/lei, qui diventa lì, domani diventa il giorno dopo. Esempio : Marco ha detto: « Verrò domani » diventa Marco ha detto che sarebbe venuto il giorno dopo.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Cos'è il discorso diretto ?", "choix": ["Riportare le parole esatte tra virgolette", "Riportare parole senza virgolette", "Una forma del futuro", "Un tipo di domanda"], "reponse": 0, "explication": "Il discorso diretto riporta le parole esatte di qualcuno tra virgolette."},
        {"id": "q2", "enonce": "Cos'è il discorso indiretto ?", "choix": ["Riportare parole tra virgolette", "Riportare parole senza virgolette, introdotte da che", "Un ordine diretto", "Una domanda diretta"], "reponse": 1, "explication": "Il discorso indiretto riporta parole senza virgolette, introdotte da un verbo seguito da che."},
        {"id": "q3", "enonce": "Se il verbo introduttivo è al presente, il tempo della frase riportata cambia generalmente ?", "choix": ["Sì, sempre", "No, generalmente non cambia", "Sempre al futuro", "Sempre al passato"], "reponse": 1, "explication": "Se il verbo introduttivo è al presente, il tempo della frase riportata generalmente non cambia."},
        {"id": "q4", "enonce": "Cosa diventa il presente quando il verbo introduttivo è al passato ?", "choix": ["L'imperfetto", "Il futuro", "Il condizionale presente", "Rimane invariato"], "reponse": 0, "explication": "Quando il verbo introduttivo è al passato, il presente diventa generalmente imperfetto."},
        {"id": "q5", "enonce": "Cosa diventa il futuro semplice al discorso indiretto con un verbo introduttivo al passato ?", "choix": ["Il condizionale passato", "Il presente", "L'imperfetto", "Rimane invariato"], "reponse": 0, "explication": "Il futuro diventa generalmente condizionale passato quando il verbo introduttivo è al passato."},
        {"id": "q6", "enonce": "Trasforma : Maria dice: « Sono stanca. » →", "choix": ["Maria dice che è stanca.", "Maria dice che ero stanca.", "Maria dirà che è stanca.", "Maria ha detto sono stanca."], "reponse": 0, "explication": "Con un verbo introduttivo al presente, il tempo non cambia : Maria dice che è stanca."},
        {"id": "q7", "enonce": "Cosa diventa « domani » al discorso indiretto passato ?", "choix": ["Il giorno dopo", "Ieri", "Oggi", "Rimane domani"], "reponse": 0, "explication": "Domani diventa generalmente « il giorno dopo » al discorso indiretto passato."},
        {"id": "q8", "enonce": "Cosa diventa « qui » al discorso indiretto ?", "choix": ["Lì", "Qui (invariato)", "Ora", "Allora"], "reponse": 0, "explication": "Qui diventa generalmente lì al discorso indiretto."},
        {"id": "q9", "enonce": "Trasforma : Marco ha detto: « Verrò domani. » →", "choix": ["Marco ha detto che sarebbe venuto il giorno dopo.", "Marco ha detto che viene domani.", "Marco dice che verrà domani.", "Marco ha detto che è venuto domani."], "reponse": 0, "explication": "Il futuro diventa condizionale passato, e domani diventa il giorno dopo."},
        {"id": "q10", "enonce": "Quale congiunzione introduce generalmente il discorso indiretto in italiano ?", "choix": ["Che", "Se", "Perché", "Quando"], "reponse": 0, "explication": "La congiunzione che introduce generalmente il discorso indiretto dopo un verbo come dire."},
    ],
})

L.append({
    "slug": "periodo-ipotetico-primo-tipo-italien-4e", "titre": "Il periodo ipotetico di primo tipo",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper esprimere una condizione realizzabile con il periodo ipotetico di primo tipo.",
    "objectifs": ["Comprendere l'uso del periodo ipotetico di primo tipo", "Formare una frase con se + presente + futuro", "Distinguere una condizione reale da una condizione irreale"],
    "contenu": [
        "Il periodo ipotetico di primo tipo (o « della realtà ») esprime una condizione realizzabile e la sua conseguenza probabile : Se piove domani, resteremo a casa. Si compone di due parti : la proposizione con se al presente indicativo, e la proposizione principale al futuro semplice (o al presente).",
        "L'ordine delle due proposizioni può essere invertito senza cambiare il senso : Se studi, supererai l'esame. equivale a Supererai l'esame se studi. Quando la proposizione con se è posta per prima, si separa dalla principale con una virgola.",
        "Il periodo ipotetico di primo tipo si usa per situazioni realmente possibili, a differenza del periodo ipotetico di secondo tipo (se + congiuntivo imperfetto + condizionale) che esprime una situazione ipotetica o poco probabile : Se vincessi alla lotteria, viaggerei per il mondo.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "A cosa serve il periodo ipotetico di primo tipo ?", "choix": ["Esprimere una condizione realizzabile e la sua conseguenza", "Esprimere un fatto passato", "Esprimere un'abitudine", "Esprimere un ordine"], "reponse": 0, "explication": "Il periodo ipotetico di primo tipo esprime una condizione realizzabile e la sua conseguenza probabile."},
        {"id": "q2", "enonce": "Qual è la struttura del periodo ipotetico di primo tipo ?", "choix": ["Se + presente, futuro", "Se + congiuntivo imperfetto, condizionale", "Se + futuro, presente", "Se + condizionale, presente"], "reponse": 0, "explication": "La struttura è se + presente indicativo, futuro semplice nella proposizione principale."},
        {"id": "q3", "enonce": "Completa : « Se ___ domani, resteremo a casa. »", "choix": ["piove", "pioverà", "piovesse", "pioveva"], "reponse": 0, "explication": "Dopo se nel periodo ipotetico di primo tipo, si usa il presente indicativo : piove."},
        {"id": "q4", "enonce": "Completa : « Se studi, ___ l'esame. »", "choix": ["superi", "supererai", "superassi", "superavi"], "reponse": 1, "explication": "Nella proposizione principale si usa il futuro semplice : supererai."},
        {"id": "q5", "enonce": "Il periodo ipotetico di primo tipo esprime una situazione realizzabile o ipotetica ?", "choix": ["Realizzabile", "Ipotetica e poco probabile", "Impossibile", "Passata"], "reponse": 0, "explication": "Il periodo ipotetico di primo tipo esprime una situazione realmente possibile."},
        {"id": "q6", "enonce": "Quale struttura esprime una situazione ipotetica poco probabile ?", "choix": ["Se + presente, futuro", "Se + congiuntivo imperfetto, condizionale", "Se + indicativo passato, presente", "Se + gerundio, futuro"], "reponse": 1, "explication": "Il periodo ipotetico di secondo tipo (se + congiuntivo imperfetto, condizionale) esprime una situazione ipotetica poco probabile."},
        {"id": "q7", "enonce": "Serve una virgola quando la proposizione con se è posta per prima ?", "choix": ["Sì", "No, mai", "Solo all'orale", "Dipende dal verbo"], "reponse": 0, "explication": "Una virgola separa le due proposizioni quando quella con se è posta per prima."},
        {"id": "q8", "enonce": "Cosa significa « se » in questa struttura ?", "choix": ["Si", "Quando", "Sebbene", "Perché"], "reponse": 0, "explication": "Se significa « si » in francese, e introduce la condizione."},
        {"id": "q9", "enonce": "Si può invertire l'ordine delle due proposizioni senza cambiare il senso ?", "choix": ["Sì", "No, mai", "Solo al passato", "Solo con il congiuntivo"], "reponse": 0, "explication": "L'ordine delle due proposizioni può essere invertito senza cambiare il senso generale."},
        {"id": "q10", "enonce": "Completa correttamente : « Vincerò la gara se mi ___ molto. » (allenarsi, presente)", "choix": ["alleno", "allenerò", "allenassi", "allenavo"], "reponse": 0, "explication": "Dopo se, si usa il presente indicativo : mi alleno."},
    ],
})

L.append({
    "slug": "pronomi-relativi-italien-4e", "titre": "I pronomi relativi che, cui, il quale",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper usare i pronomi relativi che, cui e il quale per collegare due idee in una frase.",
    "objectifs": ["Usare che come soggetto o complemento oggetto", "Usare cui dopo una preposizione", "Conoscere l'uso del quale come alternativa più formale"],
    "contenu": [
        "Il pronome relativo che è il più usato in italiano : è invariabile e può essere soggetto (La donna che abita qui è medico) o complemento oggetto (Il libro che ho letto era bellissimo) della proposizione relativa. Che non si usa mai dopo una preposizione.",
        "Dopo una preposizione (a, di, con, per, in...), si usa cui invece di che : La persona a cui ho scritto è mia zia. Il paese in cui vivo è la Francia. Cui è anch'esso invariabile, ma richiede sempre una preposizione davanti.",
        "Il quale (la quale, i quali, le quali) può sostituire che o cui, soprattutto in uno stile più formale o scritto, e si accorda in genere e numero con il nome a cui si riferisce : L'uomo, il quale abita qui, è medico. Con una preposizione : la persona alla quale ho scritto.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Qual è il pronome relativo più usato in italiano ?", "choix": ["Che", "Cui", "Il quale", "Chi"], "reponse": 0, "explication": "Che è il pronome relativo più usato in italiano, invariabile."},
        {"id": "q2", "enonce": "Che può essere usato dopo una preposizione ?", "choix": ["Sì, sempre", "No, mai", "Solo con di", "Solo con a"], "reponse": 1, "explication": "Che non si usa mai dopo una preposizione ; si usa cui in questo caso."},
        {"id": "q3", "enonce": "Quale pronome relativo si usa dopo una preposizione ?", "choix": ["Cui", "Che", "Chi", "Quello"], "reponse": 0, "explication": "Cui si usa dopo una preposizione, come a, di, con, in."},
        {"id": "q4", "enonce": "Completa : « Il libro ___ ho letto era bellissimo. » (complemento oggetto)", "choix": ["che", "cui", "il quale", "chi"], "reponse": 0, "explication": "Che s'utilise ici comme complément d'objet, sans préposition."},
        {"id": "q5", "enonce": "Completa : « La persona a ___ ho scritto è mia zia. »", "choix": ["che", "cui", "chi", "quale"], "reponse": 1, "explication": "Après une préposition (a), on utilise cui."},
        {"id": "q6", "enonce": "Il quale s'accorde-t-il en genre et en nombre ?", "choix": ["Sì", "No, è invariabile", "Solo al plurale", "Solo al femminile"], "reponse": 0, "explication": "Il quale (la quale, i quali, le quali) s'accorde en genre et en nombre avec le nom auquel il se réfère."},
        {"id": "q7", "enonce": "In quale registro il quale è particolarmente usato ?", "choix": ["Uno stile più formale e scritto", "Solo all'orale informale", "Solo con i bambini", "Mai usato in italiano"], "reponse": 0, "explication": "Il quale è particolarmente usato in uno stile più formale o scritto."},
        {"id": "q8", "enonce": "Completa : « Il paese in ___ vivo è la Francia. »", "choix": ["cui", "che", "chi", "quanto"], "reponse": 0, "explication": "Après une préposition (in), on utilise cui."},
        {"id": "q9", "enonce": "Che peut-il être sujet d'une proposition relative ?", "choix": ["Sì", "No, mai", "Solo al passato", "Solo con cui"], "reponse": 0, "explication": "Che peut être sujet de la proposition relative, comme dans « La donna che abita qui »."},
        {"id": "q10", "enonce": "Quale pronome relativo est invariable ?", "choix": ["Che et cui", "Il quale uniquement", "Aucun n'est invariable", "Seulement che"], "reponse": 0, "explication": "Che et cui sont tous deux invariables, contrairement à il quale qui s'accorde."},
    ],
})

L.append({
    "slug": "esprimere-quantita-italien-4e", "titre": "Esprimere la quantità : molto, poco, troppo",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper usare gli indicatori di quantità molto, poco, troppo e abbastanza in italiano.",
    "objectifs": ["Usare molto, poco, troppo come aggettivi e avverbi", "Accordare correttamente questi indicatori quando sono aggettivi", "Conoscere abbastanza e la sua invariabilità"],
    "contenu": [
        "Molto, poco e troppo possono essere usati come aggettivi, e in questo caso si accordano in genere e numero con il sostantivo : Ho molti amici. Ho poca pazienza. Mangio troppi dolci. Come aggettivi, questi indicatori variano quindi secondo il nome che accompagnano.",
        "Molto, poco e troppo possono anche essere usati come avverbi, per modificare un verbo o un aggettivo : in questo caso, restano invariabili. Sono molto stanco. Ho dormito poco. Sei troppo veloce. Notare la differenza con la forma aggettivale, che varia.",
        "Abbastanza (assez) è invece sempre invariabile, sia come aggettivo che come avverbio : Ho abbastanza soldi. Sono abbastanza stanco. La distinzione tra la funzione aggettivale (accordo) e la funzione avverbiale (invariabile) è essenziale per usare correttamente molto, poco e troppo.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Molto si accorda quando è usato come aggettivo ?", "choix": ["Sì", "No, mai", "Solo al plurale", "Solo al femminile"], "reponse": 0, "explication": "Come aggettivo, molto si accorda in genere e numero con il sostantivo."},
        {"id": "q2", "enonce": "Completa : « Ho molt___ amici. » (accordo)", "choix": ["i", "o", "a", "e"], "reponse": 0, "explication": "Molti amici : l'aggettivo si accorda al maschile plurale."},
        {"id": "q3", "enonce": "Completa : « Ho poc___ pazienza. » (accordo)", "choix": ["a", "o", "i", "e"], "reponse": 0, "explication": "Poca pazienza : l'aggettivo si accorda al femminile singolare."},
        {"id": "q4", "enonce": "Molto varia quando è usato come avverbio ?", "choix": ["No, resta invariabile", "Sì, sempre", "Solo al presente", "Solo al plurale"], "reponse": 0, "explication": "Come avverbio, molto resta invariabile : « Sono molto stanco »."},
        {"id": "q5", "enonce": "Nella frase « Sono molto stanco », molto è aggettivo o avverbio ?", "choix": ["Aggettivo", "Avverbio", "Sostantivo", "Preposizione"], "reponse": 1, "explication": "Qui, molto modifica l'aggettivo stanco, è quindi un avverbio invariabile."},
        {"id": "q6", "enonce": "Nella frase « Ho molti amici », molti è aggettivo o avverbio ?", "choix": ["Aggettivo", "Avverbio", "Pronome", "Preposizione"], "reponse": 0, "explication": "Qui, molti accompagna e si accorda con il sostantivo amici, è quindi un aggettivo."},
        {"id": "q7", "enonce": "Abbastanza si accorda mai ?", "choix": ["No, è sempre invariabile", "Sì, sempre", "Solo al plurale", "Solo come aggettivo"], "reponse": 0, "explication": "Abbastanza è sempre invariabile, sia come aggettivo che come avverbio."},
        {"id": "q8", "enonce": "Completa : « Mangio tropp___ dolci. » (accordo)", "choix": ["i", "o", "a", "e"], "reponse": 0, "explication": "Troppi dolci : l'aggettivo si accorda al maschile plurale."},
        {"id": "q9", "enonce": "Completa : « Sei tropp___ veloce. » (avverbio)", "choix": ["o", "a", "i", "e"], "reponse": 0, "explication": "Come avverbio, troppo resta invariabile : « Sei troppo veloce »."},
        {"id": "q10", "enonce": "Cosa significa abbastanza ?", "choix": ["Assez", "Beaucoup", "Peu", "Trop"], "reponse": 0, "explication": "Abbastanza signifie « assez » en français."},
    ],
})

L.append({
    "slug": "ambiente-sviluppo-sostenibile-italien-4e", "titre": "L'ambiente e lo sviluppo sostenibile",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Acquisire il vocabolario dell'ambiente e dello sviluppo sostenibile in italiano.",
    "objectifs": ["Acquisire il vocabolario dell'ambiente", "Saper esprimere un'opinione su un tema ecologico", "Comprendere un breve testo sullo sviluppo sostenibile"],
    "contenu": [
        "Il vocabolario dell'ambiente comprende parole essenziali : il cambiamento climatico, il riscaldamento globale, l'inquinamento, le energie rinnovabili, il riciclaggio, le specie in via di estinzione, lo sviluppo sostenibile.",
        "Per esprimere un'opinione su un tema ecologico, si possono usare strutture come : Secondo me, dovremmo ridurre i rifiuti di plastica. Penso che le energie rinnovabili siano il futuro. Credo fermamente che tutti dovrebbero riciclare.",
        "L'Italia porta avanti diverse iniziative per l'ambiente : la raccolta differenziata è obbligatoria in molte città, e numerosi parchi naturali proteggono la biodiversità del paese, come il Parco Nazionale del Gran Paradiso, il primo parco nazionale istituito in Italia.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Come si dice « le changement climatique » en italien ?", "choix": ["Il cambiamento climatico", "Il riciclaggio", "L'energia solare", "L'inquinamento dell'acqua"], "reponse": 0, "explication": "Il cambiamento climatico signifie « le changement climatique »."},
        {"id": "q2", "enonce": "Come si dice « les énergies renouvelables » ?", "choix": ["Le energie rinnovabili", "L'energia nucleare", "Il petrolio", "Il carbone"], "reponse": 0, "explication": "Le energie rinnovabili signifie « les énergies renouvelables »."},
        {"id": "q3", "enonce": "Come si dice « les espèces en voie de disparition » ?", "choix": ["Le specie in via di estinzione", "Le specie domestiche", "Le specie invasive", "Solo le piante"], "reponse": 0, "explication": "Le specie in via di estinzione signifie « les espèces menacées »."},
        {"id": "q4", "enonce": "Come si dice « le développement durable » ?", "choix": ["Lo sviluppo sostenibile", "Il riscaldamento globale", "I rifiuti di plastica", "Il riciclaggio"], "reponse": 0, "explication": "Lo sviluppo sostenibile signifie « le développement durable »."},
        {"id": "q5", "enonce": "Quale struttura permette di esprimere un'opinione ?", "choix": ["Secondo me...", "C'era una volta...", "Come stai?", "Grazie mille"], "reponse": 0, "explication": "« Secondo me » est une structure classique pour exprimer une opinion."},
        {"id": "q6", "enonce": "Come si dice « le riciclage » ?", "choix": ["Il riciclaggio", "Il riscaldamento", "La deforestazione", "L'inquinamento"], "reponse": 0, "explication": "Il riciclaggio signifie « le recyclage »."},
        {"id": "q7", "enonce": "Qual è il primo parco nazionale istituito in Italia ?", "choix": ["Il Parco Nazionale del Gran Paradiso", "Nessun parco nazionale in Italia", "Il Parco di Yellowstone", "Il Parco della Vanoise"], "reponse": 0, "explication": "Le Parc National du Gran Paradiso est le premier parc national institué en Italie."},
        {"id": "q8", "enonce": "La raccolta differenziata è obbligatoria in molte città italiane ?", "choix": ["Sì", "No, mai", "Solo a Roma", "Solo in campagna"], "reponse": 0, "explication": "La collecte sélective (raccolta differenziata) est obligatoire dans de nombreuses villes italiennes."},
        {"id": "q9", "enonce": "Come esprimere fortemente una convinzione in italiano ?", "choix": ["Credo fermamente che...", "Forse...", "Non lo so...", "Magari..."], "reponse": 0, "explication": "« Credo fermamente che » permet d'exprimer fortement une conviction."},
        {"id": "q10", "enonce": "Come si dice « le réchauffement climatique » ?", "choix": ["Il riscaldamento globale", "Il riciclaggio", "L'energia solare", "La biodiversità"], "reponse": 0, "explication": "Il riscaldamento globale signifie « le réchauffement climatique »."},
    ],
})

L.append({
    "slug": "svizzera-italiana-san-marino-italien-4e", "titre": "La Svizzera italiana e San Marino",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Scoprire il Ticino, regione italofona della Svizzera, e la Repubblica di San Marino.",
    "objectifs": ["Situare il Ticino e conoscere le sue caratteristiche", "Situare San Marino e conoscere la sua storia", "Arricchire il vocabolario sul mondo italofono al di fuori dell'Italia"],
    "contenu": [
        "L'italiano non si parla solo in Italia : è anche una delle quattro lingue ufficiali della Svizzera, insieme al tedesco, al francese e al romancio. Il Canton Ticino, nel sud della Svizzera, è la principale regione italofona del paese, con la sua città più grande, Lugano, situata sulle rive di un lago omonimo.",
        "San Marino è uno dei paesi più piccoli del mondo, interamente circondato dal territorio italiano, nell'Italia centrale. È considerata una delle repubbliche più antiche del mondo ancora esistenti, fondata secondo la tradizione nel 301 dopo Cristo. La sua capitale porta lo stesso nome, San Marino.",
        "Questi territori italofoni, pur non facendo parte dell'Italia, condividono una lingua e una cultura vicine a quelle italiane, con anche delle particolarità locali proprie : espressioni dialettali, tradizioni culinarie specifiche, e una storia politica indipendente da quella dell'Italia.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "L'italiano è una lingua ufficiale della Svizzera ?", "choix": ["Sì", "No, mai", "Solo a livello locale", "Solo nel passato"], "reponse": 0, "explication": "L'italiano è una delle quattro lingue ufficiali della Svizzera."},
        {"id": "q2", "enonce": "Quali sono le quattro lingue ufficiali della Svizzera ?", "choix": ["Tedesco, francese, italiano e romancio", "Solo tedesco e francese", "Solo italiano", "Inglese, francese, tedesco e spagnolo"], "reponse": 0, "explication": "La Svizzera ha quattro lingue ufficiali : tedesco, francese, italiano e romancio."},
        {"id": "q3", "enonce": "Qual è il principale cantone italofono della Svizzera ?", "choix": ["Il Canton Ticino", "Il Canton Vaud", "Il Canton Zurigo", "Il Canton Berna"], "reponse": 0, "explication": "Il Canton Ticino è la principale regione italofona della Svizzera."},
        {"id": "q4", "enonce": "Qual è la città più grande del Canton Ticino ?", "choix": ["Lugano", "Ginevra", "Berna", "Zurigo"], "reponse": 0, "explication": "Lugano è la città più grande del Canton Ticino."},
        {"id": "q5", "enonce": "San Marino è circondato dal territorio di quale paese ?", "choix": ["L'Italia", "La Francia", "La Svizzera", "L'Austria"], "reponse": 0, "explication": "San Marino è interamente circondato dal territorio italiano."},
        {"id": "q6", "enonce": "San Marino fa parte dell'Italia ?", "choix": ["No, è un paese indipendente", "Sì, è una regione italiana", "Solo parzialmente", "Non esiste più"], "reponse": 0, "explication": "San Marino è un paese indipendente, benché circondato dall'Italia."},
        {"id": "q7", "enonce": "San Marino è considerata una delle repubbliche più antiche del mondo ?", "choix": ["Sì", "No, è molto recente", "Fondata nel ventesimo secolo", "Non è una repubblica"], "reponse": 0, "explication": "San Marino è considerata una delle repubbliche più antiche del mondo ancora esistenti."},
        {"id": "q8", "enonce": "Secondo la tradizione, in che anno fu fondata San Marino ?", "choix": ["301 dopo Cristo", "1900 dopo Cristo", "50 avanti Cristo", "1500 dopo Cristo"], "reponse": 0, "explication": "Secondo la tradizione, San Marino fu fondata nel 301 dopo Cristo."},
        {"id": "q9", "enonce": "Come si chiama la capitale di San Marino ?", "choix": ["San Marino, come il paese", "Roma", "Lugano", "Rimini"], "reponse": 0, "explication": "La capitale di San Marino porta lo stesso nome del paese : San Marino."},
        {"id": "q10", "enonce": "Questi territori italofoni condividono una cultura vicina a quella italiana ?", "choix": ["Sì, con anche particolarità locali", "No, cultura completamente diversa", "Solo la lingua, nessuna cultura comune", "Non esistono legami culturali"], "reponse": 0, "explication": "Questi territori condividono lingua e cultura vicine all'Italia, con particolarità locali proprie."},
    ],
})

L.append({
    "slug": "imperfetto-abitudini-passate-italien-4e", "titre": "L'imperfetto per le abitudini passate",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Saper usare l'imperfetto per descrivere un'abitudine o uno stato del passato.",
    "objectifs": ["Formare l'imperfetto dei verbi regolari", "Usare l'imperfetto per un'abitudine passata", "Distinguere l'imperfetto dal passato prossimo"],
    "contenu": [
        "L'imperfetto si forma togliendo la terminazione dell'infinito (-are, -ere, -ire) e aggiungendo le terminazioni -avo/-evo/-ivo, -avi/-evi/-ivi, -ava/-eva/-iva, -avamo/-evamo/-ivamo, -avate/-evate/-ivate, -avano/-evano/-ivano : parlare → parlavo, parlavi, parlava...",
        "L'imperfetto si usa in particolare per descrivere un'abitudine o un'azione ripetuta nel passato, senza precisare quando essa è iniziata o finita : Da bambino, andavo sempre al mare in estate. Ogni giorno, mangiavo la pasta a pranzo.",
        "A differenza del passato prossimo, che descrive un'azione ponctuale e conclusa nel passato (Ieri sono andato al mare), l'imperfetto insiste sulla ripetizione o sulla durata dell'abitudine, senza indicare un momento preciso di inizio o fine.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Come si forma l'imperfetto dei verbi in -are ?", "choix": ["Con le terminazioni -avo, -avi, -ava...", "Con le terminazioni -evo, -evi, -eva...", "Con le terminazioni -ivo, -ivi, -iva...", "Non esiste per i verbi in -are"], "reponse": 0, "explication": "I verbi in -are formano l'imperfetto con le terminazioni -avo, -avi, -ava, -avamo, -avate, -avano."},
        {"id": "q2", "enonce": "Qual è l'imperfetto di « parlare » alla prima persona singolare ?", "choix": ["Parlavo", "Parlerò", "Ho parlato", "Parlai"], "reponse": 0, "explication": "Parlavo è la prima persona singolare dell'imperfetto di parlare."},
        {"id": "q3", "enonce": "Per cosa si usa in particolare l'imperfetto ?", "choix": ["Per un'abitudine o un'azione ripetuta nel passato", "Per un'azione unica e conclusa", "Per il futuro", "Per un ordine"], "reponse": 0, "explication": "L'imperfetto si usa per descrivere un'abitudine o un'azione ripetuta nel passato."},
        {"id": "q4", "enonce": "Completa : « Da bambino, ___ (andare) sempre al mare. »", "choix": ["andavo", "andrò", "sono andato", "vado"], "reponse": 0, "explication": "Andavo (imperfetto) exprime une habitude passée, sans précision de début ou fin."},
        {"id": "q5", "enonce": "Qual è la differenza principale tra imperfetto e passato prossimo ?", "choix": ["L'imperfetto insiste sulla ripetizione o la durata, il passato prossimo su un'azione conclusa", "Non c'è alcuna differenza", "L'imperfetto è solo per il futuro", "Il passato prossimo è solo per le abitudini"], "reponse": 0, "explication": "L'imperfetto insiste sulla ripetizione o la durata di un'abitudine, mentre il passato prossimo descrive un'azione ponctuelle et conclue."},
        {"id": "q6", "enonce": "Quale frase esprime un'abitudine passata ?", "choix": ["Ogni giorno, mangiavo la pasta a pranzo.", "Ieri sono andato al mare.", "Domani andrò al mercato.", "Ho appena finito i compiti."], "reponse": 0, "explication": "« Ogni giorno, mangiavo » exprime une habitude répétée dans le passé, à l'imperfetto."},
        {"id": "q7", "enonce": "Quale frase descrive un'azione puntuale e conclusa ?", "choix": ["Ieri sono andato al mare.", "Andavo spesso al mare.", "Vado sempre al mare.", "Andrò al mare domani."], "reponse": 0, "explication": "« Ieri sono andato » (passato prossimo) descrive une action ponctuelle datée et conclue."},
        {"id": "q8", "enonce": "Qual è l'imperfetto del verbo essere alla prima persona singolare ?", "choix": ["Ero", "Sono", "Sarò", "Sia"], "reponse": 0, "explication": "L'imperfetto del verbo essere è irregolare : ero, eri, era..."},
        {"id": "q9", "enonce": "L'imperfetto precisa sempre il momento esatto di inizio o fine di un'azione ?", "choix": ["No, mai", "Sì, sempre", "Solo al plurale", "Solo con avere"], "reponse": 0, "explication": "L'imperfetto non precisa il momento esatto di inizio o fine, contrariamente al passato prossimo."},
        {"id": "q10", "enonce": "Qual è la terminazione dell'imperfetto per i verbi in -ere alla terza persona singolare ?", "choix": ["-eva", "-ava", "-iva", "-erà"], "reponse": 0, "explication": "I verbi in -ere hanno la terminazione -eva alla terza persona singolare dell'imperfetto."},
    ],
})

L.append({
    "slug": "viaggi-vacanze-vocabolario-italien-4e", "titre": "Il vocabolario dei viaggi e delle vacanze",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Acquisire il vocabolario necessario per parlare di viaggi, vacanze ed esperienze turistiche.",
    "objectifs": ["Acquisire il vocabolario dei viaggi", "Saper raccontare un'esperienza di vacanza", "Comprendere un breve racconto di viaggio"],
    "contenu": [
        "Il vocabolario dei viaggi comprende parole essenziali : un volo, i bagagli, un passaporto, un viaggio, un alloggio, un ostello della gioventù, fare turismo, visitare i monumenti, un souvenir, una guida turistica.",
        "Per raccontare vacanze passate, si usa spesso il passato prossimo o l'imperfetto : L'estate scorsa, abbiamo viaggiato in Toscana. Abbiamo visitato molti castelli e siamo rimasti in un piccolo agriturismo vicino al mare.",
        "Descrivere un'esperienza turistica implica spesso esprimere un'impressione : È stato mozzafiato! Il paesaggio era assolutamente stupendo. Mi è piaciuto molto il cibo locale. Queste espressioni arricchiscono un racconto di viaggio e lo rendono più vivo e personale.",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Come si dice « un vol » in italiano ?", "choix": ["Un volo", "Un treno", "Un autobus", "Una nave"], "reponse": 0, "explication": "Un volo signifie « un vol » en avion."},
        {"id": "q2", "enonce": "Come si dice « les bagages » ?", "choix": ["I bagagli", "Il passaporto", "Il biglietto", "L'hotel"], "reponse": 0, "explication": "I bagagli signifie « les bagages »."},
        {"id": "q3", "enonce": "Come si dice « l'hébergement » ?", "choix": ["L'alloggio", "Il trasporto", "Il cibo", "Il clima"], "reponse": 0, "explication": "L'alloggio signifie « l'hébergement »."},
        {"id": "q4", "enonce": "Come si dice « une auberge de jeunesse » ?", "choix": ["Un ostello della gioventù", "Un hotel di lusso", "Un campeggio", "Un aeroporto"], "reponse": 0, "explication": "Un ostello della gioventù signifie « une auberge de jeunesse »."},
        {"id": "q5", "enonce": "Come si dice « faire du tourisme » ?", "choix": ["Fare turismo", "Fare le valigie", "Prendere l'aereo", "Prenotare un hotel"], "reponse": 0, "explication": "Fare turismo signifie « faire du tourisme »."},
        {"id": "q6", "enonce": "Quali tempi si usano spesso per raccontare vacanze passate ?", "choix": ["Il passato prossimo e l'imperfetto", "Solo il futuro", "Solo il presente", "Solo l'imperativo"], "reponse": 0, "explication": "Le passato prossimo et l'imperfetto sont fréquemment utilisés pour raconter des vacances passées."},
        {"id": "q7", "enonce": "Come si dice « C'était à couper le souffle! » ?", "choix": ["È stato mozzafiato!", "Era noioso!", "Era stancante!", "Era economico!"], "reponse": 0, "explication": "Mozzafiato signifie « à couper le souffle », une impression très positive."},
        {"id": "q8", "enonce": "Come si dice « un souvenir » (oggetto) ?", "choix": ["Un souvenir", "Un passaporto", "Un volo", "Una valigia"], "reponse": 0, "explication": "Un souvenir désigne également en italien un objet rapporté d'un voyage."},
        {"id": "q9", "enonce": "Come si dice « une guide touristique » ?", "choix": ["Una guida turistica", "Un ostello", "Un bagaglio", "Un passaporto"], "reponse": 0, "explication": "Una guida turistica signifie « un guide touristique »."},
        {"id": "q10", "enonce": "Come si dice « L'estate scorsa, abbiamo viaggiato in Toscana » ?", "choix": ["L'été dernier, nous avons voyagé en Toscane.", "L'été prochain, nous voyagerons en Toscane.", "Chaque été, nous voyageons en Toscane.", "En ce moment, nous voyageons en Toscane."], "reponse": 0, "explication": "Cette phrase au passato prossimo raconte un voyage passé daté : « l'été dernier »."},
    ],
})

L.append({
    "slug": "testo-argomentativo-breve-italien-4e", "titre": "Scrivere un breve testo argomentativo",
    "matiere": "italien", "niveau": "4e", "duree": "20 min",
    "resume": "Imparare la struttura di un breve testo argomentativo in italiano per difendere un'opinione.",
    "objectifs": ["Conoscere la struttura di un semplice testo argomentativo", "Usare connettori logici per organizzare le proprie idee", "Saper difendere un'opinione per iscritto in italiano"],
    "contenu": [
        "Un semplice testo argomentativo in italiano comprende generalmente tre parti : un'introduzione che presenta il tema e annuncia l'opinione difesa (Oggigiorno, molte persone pensano che... In questo testo, sosterrò che...), uno sviluppo con argomenti ed esempi, e una conclusione che riassume la posizione difesa.",
        "Per organizzare le proprie idee, si usano connettori logici : innanzitutto / inoltre / infine per elencare argomenti ; tuttavia / d'altra parte per sfumare o presentare un controargomento ; per esempio / ad esempio per illustrare un'idea ; quindi / di conseguenza per esprimere una conseguenza.",
        "Per difendere un'opinione, si possono usare espressioni come : Credo che... / Secondo me... / Sono convinto che... È anche consigliabile, in un testo equilibrato, evocare brevemente un punto di vista opposto prima di concludere fermamente sulla propria posizione : Anche se alcuni non sono d'accordo, credo comunque che...",
    ],
    "quiz": [
        {"id": "q1", "enonce": "Quante parti comprende generalmente un semplice testo argomentativo ?", "choix": ["Due", "Tre : introduzione, sviluppo, conclusione", "Cinque", "Una sola"], "reponse": 1, "explication": "Un testo argomentativo semplice comprende un'introduzione, uno sviluppo e una conclusione."},
        {"id": "q2", "enonce": "Cosa significa « innanzitutto » ?", "choix": ["Prima di tutto", "Infine", "Tuttavia", "Per esempio"], "reponse": 0, "explication": "Innanzitutto signifie « premièrement », utilisé pour introduire un premier argument."},
        {"id": "q3", "enonce": "Quale connettore permette di introdurre un controargomento ?", "choix": ["Innanzitutto", "Tuttavia", "Per esempio", "Quindi"], "reponse": 1, "explication": "Tuttavia (cependant) permet d'introduire une nuance ou un contre-argument."},
        {"id": "q4", "enonce": "Quale connettore permette di dare un esempio ?", "choix": ["Per esempio", "Infine", "Tuttavia", "Quindi"], "reponse": 0, "explication": "Per esempio (par exemple) permet d'illustrer une idée par un exemple."},
        {"id": "q5", "enonce": "Quale connettore esprime una conseguenza ?", "choix": ["Quindi", "Innanzitutto", "Tuttavia", "Per esempio"], "reponse": 0, "explication": "Quindi (par conséquent) exprime une conséquence logique."},
        {"id": "q6", "enonce": "Quale espressione permette di introdurre la propria opinione ?", "choix": ["Secondo me...", "C'era una volta...", "Fine.", "Come stai?"], "reponse": 0, "explication": "« Secondo me » est une expression classique pour introduire une opinion personnelle."},
        {"id": "q7", "enonce": "Perché è consigliabile evocare un punto di vista opposto in un testo equilibrato ?", "choix": ["Non è mai consigliabile", "Per mostrare di aver considerato diversi punti di vista prima di concludere", "Per cambiare idea alla fine", "Per riempire spazio"], "reponse": 1, "explication": "Evocare un punto di vista opposto mostra una riflessione equilibrata prima di concludere fermamente sulla propria posizione."},
        {"id": "q8", "enonce": "Cosa fa la conclusione di un testo argomentativo ?", "choix": ["Riassume la posizione difesa", "Introduce un nuovo argomento", "Pone una domanda senza risposta", "Elenca solo esempi"], "reponse": 0, "explication": "La conclusione riassume e conferma la posizione difesa lungo tutto il testo."},
        {"id": "q9", "enonce": "Quale struttura introduce tipicamente un testo argomentativo ?", "choix": ["In questo testo, sosterrò che...", "Fine.", "C'era una volta...", "Capitolo Primo"], "reponse": 0, "explication": "« In questo testo, sosterrò che » est une formule d'introduction typique d'un texte argumentatif."},
        {"id": "q10", "enonce": "Cosa significa « d'altra parte » ?", "choix": ["D'un autre côté", "Par conséquent", "Premièrement", "Enfin"], "reponse": 0, "explication": "D'altra parte signifie « d'un autre côté », utilisé pour nuancer ou opposer une idée."},
    ],
})

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

txt = insert_after(txt, "monumenti-simboli-italiani-5e", L)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"{len(L)} lezioni Italiano 4e aggiunte.")
