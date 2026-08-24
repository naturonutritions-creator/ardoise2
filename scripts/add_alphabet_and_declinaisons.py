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

ecoute_anglais = '''    ecouteIntonation: [
      { phrase: "Where do you live?", type: "question" },
      { phrase: "My best friend is Tom.", type: "affirmation" },
      { phrase: "That's amazing!", type: "exclamation" },
      { phrase: "Can you help me, please?", type: "question" },
      { phrase: "I go to school by bus.", type: "affirmation" },
      { phrase: "I can't believe it!", type: "exclamation" },
    ],
'''
ecoute_espagnol = '''    ecouteIntonation: [
      { phrase: "¿Dónde vives?", type: "question" },
      { phrase: "Mi mejor amigo se llama Tom.", type: "affirmation" },
      { phrase: "¡Qué increíble!", type: "exclamation" },
      { phrase: "¿Puedes ayudarme, por favor?", type: "question" },
      { phrase: "Voy al colegio en autobús.", type: "affirmation" },
      { phrase: "¡No puedo creerlo!", type: "exclamation" },
    ],
'''
ecoute_italien = '''    ecouteIntonation: [
      { phrase: "Dove abiti?", type: "question" },
      { phrase: "Il mio migliore amico si chiama Tom.", type: "affirmation" },
      { phrase: "Che incredibile!", type: "exclamation" },
      { phrase: "Puoi aiutarmi, per favore?", type: "question" },
      { phrase: "Vado a scuola in autobus.", type: "affirmation" },
      { phrase: "Non ci posso credere!", type: "exclamation" },
    ],
'''

# ---------- ENGLISH ALPHABET ----------
angl_qs = [
    q("q1", "Combien de lettres compte l'alphabet anglais ?", ["24", "26", "27", "28"], 1, "L'alphabet anglais compte 26 lettres, comme l'alphabet français."),
    q("q2", "Comment se prononce la lettre A en anglais ?", ["[a]", "[eï]", "[i:]", "[ɛ]"], 1, "La lettre A se prononce [eï] en anglais, très différemment du français."),
    q("q3", "Comment se prononce la lettre H en anglais ?", ["[aʃ]", "[eïtʃ] (« aitch »)", "[ache]", "Elle est muette"], 1, "La lettre H se dit « aitch » [eïtʃ] en anglais."),
    q("q4", "Comment appelle-t-on la lettre W en anglais ?", ["Double-u", "We", "Double-vé", "Wa"], 0, "W se dit « double-u » (double-u) en anglais, littéralement « double u »."),
    q("q5", "Que veut-on savoir si l'on demande « How do you spell your name? » ?", ["L'âge de la personne", "Comment épeler son nom", "Où elle habite", "Son numéro de téléphone"], 1, "Cette question demande d'épeler son nom lettre par lettre."),
    q("q6", "Comment se prononce la lettre G en anglais ?", ["[gé]", "[dʒi:]", "[gi]", "[je]"], 1, "La lettre G se prononce [dʒi:] en anglais."),
    q("q7", "Quelle lettre anglaise se prononce comme le mot français « oui » n'a rien à voir, mais se dit « waï » ?", ["Y", "I", "J", "U"], 0, "La lettre Y se prononce « waï » en anglais."),
    q("q8", "Comment se prononce la lettre I en anglais ?", ["[i]", "[aï]", "[ji]", "[e]"], 1, "La lettre I se prononce [aï] en anglais, comme dans le pronom « I » (je)."),
    q("q9", "Quelle expression utilise-t-on pour demander de répéter en épelant ?", ["Can you spell that, please?", "What time is it?", "How old are you?", "Where are you from?"], 0, "« Can you spell that, please? » signifie « peux-tu épeler ça, s'il te plaît ? »."),
    q("q10", "Comment se prononce la lettre J en anglais ?", ["[dʒeï]", "[ji]", "[j]", "[dʒi:]"], 0, "La lettre J se prononce [dʒeï] en anglais."),
]
angl_lesson = '''  {
    slug: "alphabet-anglais-6e",
    titre: "The English alphabet",
    matiere: "anglais",
    niveau: "6e",
    duree: "20 min",
    resume: "Apprendre à nommer et épeler les lettres de l'alphabet anglais, et distinguer leur prononciation de celle du français (niveau A1).",
    motsAEcouter: ["a", "h", "j", "w", "y"],
''' + ecoute_anglais + '''    objectifs: ["Nommer les 26 lettres de l'alphabet anglais", "Épeler un mot ou son prénom en anglais", "Distinguer la prononciation anglaise de la prononciation française de certaines lettres"],
    contenu: ["L'alphabet anglais compte 26 lettres, les mêmes que l'alphabet français, mais elles se prononcent très différemment. De A à M : A [eï], B [bi:], C [si:], D [di:], E [i:], F [ef], G [dʒi:], H [eïtʃ] (« aitch »), I [aï], J [dʒeï], K [keï], L [el], M [em].", "De N à Z : N [en], O [oʊ], P [pi:], Q [kju:], R [ɑːr], S [es], T [ti:], U [ju:], V [vi:], W [ˈdʌbəlju:] (« double-u », littéralement « double u »), X [eks], Y [waï], Z [zed] en anglais britannique ou [zi:] en anglais américain.", "Certaines lettres sont particulièrement piégeuses pour un francophone : H se dit « aitch » et non « ache », W se dit « double-u » et non « double-vé », G et J se ressemblent à l'oral ([dʒi:] et [dʒeï]) mais ne se confondent pas à l'écrit. Pour demander à quelqu'un d'épeler un mot, on dit « How do you spell that? » ou « Can you spell your name, please? », une phrase très utile en classe d'anglais."],
    quiz: {
    slug: "quiz-alphabet-anglais-6e",
    titre: "Quiz — The English alphabet",
    questions: [
''' + ",\n".join(angl_qs) + '''
    ],
  },
  },
'''

idx = txt.index('slug: "se-presenter-anglais"')
marker = "\n  {\n    "
_pos = txt.rindex(marker, 0, idx)
insert_pos = _pos + 1
assert txt[insert_pos:insert_pos+4] == '  {\n'
txt = txt[:insert_pos] + angl_lesson + txt[insert_pos:]

# ---------- SPANISH ALPHABET ----------
esp_qs = [
    q("q1", "Combien de lettres compte l'alphabet espagnol ?", ["26", "27", "28", "25"], 1, "L'alphabet espagnol compte 27 lettres : les 26 lettres du français plus la « ñ »."),
    q("q2", "Quelle lettre est propre à l'espagnol et n'existe pas en français ?", ["La ç", "La ñ", "La ü", "La ê"], 1, "La « ñ » (eñe) est une lettre propre à l'espagnol, utilisée dans des mots comme « año » ou « niño »."),
    q("q3", "Comment se prononce la lettre H en espagnol ?", ["Comme en français", "Elle est toujours muette", "Comme un [k]", "Comme un [j]"], 1, "La lettre H (hache) est toujours muette en espagnol, comme dans « hola »."),
    q("q4", "Comment se prononce la lettre J en espagnol ?", ["Comme le J français", "Un son guttural, proche du R du fond de la gorge", "Elle est muette", "Comme un [j] anglais"], 1, "La lettre J (jota) se prononce avec un son guttural, différent du J français."),
    q("q5", "Que signifie un accent (tilde) sur une voyelle comme dans « café » ?", ["Rien de particulier", "Il marque la syllabe accentuée (tonique)", "Il change la lettre en consonne", "Il indique le pluriel"], 1, "L'accent écrit (tilde) marque la syllabe sur laquelle porte l'accent tonique du mot."),
    q("q6", "Comment s'appelle la lettre « ñ » en espagnol ?", ["Ene", "Eñe", "Ce", "Efe"], 1, "La lettre « ñ » s'appelle « eñe » en espagnol."),
    q("q7", "Comment se prononce généralement « ll » en espagnol (par exemple dans « llamo ») ?", ["Comme un l double", "Proche d'un son « y »", "Comme un « j » français", "Elle est muette"], 1, "« ll » se prononce le plus souvent comme un son proche du « y », par exemple dans « me llamo »."),
    q("q8", "La lettre « ñ » est-elle une simple variante de la lettre « n » ?", ["Oui, c'est juste un n avec un accent", "Non, c'est une lettre à part entière de l'alphabet espagnol", "Non, elle n'existe plus aujourd'hui", "Oui, elles se prononcent pareil"], 1, "La « ñ » est considérée comme une lettre à part entière de l'alphabet espagnol, pas une simple variante du n."),
    q("q9", "Comment se prononce le « rr » en espagnol (par exemple dans « perro ») ?", ["Comme un r français normal", "Un r fortement roulé", "Il est muet", "Comme un l"], 1, "Le « rr » se prononce avec un r fortement roulé, plus marqué qu'un simple « r »."),
    q("q10", "Comment s'appelle la lettre W en espagnol ?", ["Uve", "Doble uve", "Ve doble solamente en inglés", "Equis"], 1, "La lettre W s'appelle « doble uve » (ou « uve doble ») en espagnol."),
]
esp_lesson = '''  {
    slug: "alfabeto-espagnol-6e",
    titre: "El alfabeto español",
    matiere: "espagnol",
    niveau: "6e",
    duree: "20 min",
    resume: "Découvrir les lettres de l'alphabet espagnol, dont la fameuse « ñ », et leur prononciation particulière (niveau A1).",
    motsAEcouter: ["eñe", "erre", "hache", "jota", "doble uve"],
''' + ecoute_espagnol + '''    objectifs: ["Nommer les lettres de l'alphabet espagnol", "Reconnaître la lettre ñ, propre à l'espagnol", "Distinguer la prononciation espagnole de certaines lettres (h, j, ll, rr)"],
    contenu: ["L'alphabet espagnol compte 27 lettres : les 26 lettres du français, plus la « ñ » (eñe), une lettre à part entière propre à l'espagnol que l'on trouve dans des mots comme « año » (année) ou « niño » (enfant). Les noms des lettres : a, be, ce, de, e, efe, ge, hache, i, jota, ka, ele, eme, ene, eñe, o, pe, cu, erre, ese, te, u, uve, doble uve, equis, ye (ou i griega), zeta.", "Certaines lettres se prononcent très différemment du français : la « h » (hache) est toujours muette (« hola » se prononce « ola »), la « j » (jota) a un son guttural, rauque, prononcé au fond de la gorge, très différent du J français. Les doubles lettres « ll » et « rr » ont aussi des sons particuliers : « ll » se prononce le plus souvent comme un « y » (« me llamo » = « je m'appelle »), et « rr » est un r fortement roulé, plus intense qu'un simple r.", "Les voyelles peuvent porter un accent écrit, appelé « tilde » (á, é, í, ó, ú), qui indique sur quelle syllabe porte l'accent tonique du mot : ce n'est pas une lettre différente, juste une marque de prononciation. La « ñ », en revanche, est bien une lettre séparée du « n » dans l'alphabet espagnol, avec son propre son [ɲ], proche du « gn » français dans « montagne »."],
    quiz: {
    slug: "quiz-alfabeto-espagnol-6e",
    titre: "Quiz — El alfabeto español",
    questions: [
''' + ",\n".join(esp_qs) + '''
    ],
  },
  },
'''

idx = txt.index('slug: "saludos-presentaciones-espagnol-6e"')
_pos = txt.rindex(marker, 0, idx)
insert_pos = _pos + 1
assert txt[insert_pos:insert_pos+4] == '  {\n'
txt = txt[:insert_pos] + esp_lesson + txt[insert_pos:]

# ---------- ITALIAN ALPHABET ----------
ita_qs = [
    q("q1", "Combien de lettres compte l'alphabet italien standard ?", ["26", "24", "21", "27"], 2, "L'alphabet italien standard ne compte que 21 lettres : il manque j, k, w, x, y (sauf dans des mots étrangers)."),
    q("q2", "Quelles lettres sont absentes de l'alphabet italien standard ?", ["A, e, i, o, u", "J, k, w, x, y", "B, c, d, f, g", "Toutes les consonnes doubles"], 1, "J, k, w, x et y ne font pas partie de l'alphabet italien standard, sauf dans des mots d'origine étrangère."),
    q("q3", "Comment se prononce le « c » italien devant un « a », un « o » ou un « u » ?", ["[tʃ] comme « tch »", "[k] dur, comme dans « casa »", "Il est muet", "[s] comme en français"], 1, "Devant a, o, u, le « c » italien se prononce [k], un son dur, comme dans « casa »."),
    q("q4", "Comment se prononce le « c » italien devant un « e » ou un « i » ?", ["[k] dur", "[tʃ] comme « tch », par exemple dans « cena »", "Il est muet", "Comme un « s »"], 1, "Devant e et i, le « c » italien se prononce [tʃ], comme « tch » dans « cena » (dîner)."),
    q("q5", "Comment garder le son [k] dur devant un « e » ou un « i » en italien ?", ["En ajoutant un h : che, chi", "En doublant le c", "C'est impossible", "En ajoutant un i"], 0, "On ajoute un « h » pour garder le son dur devant e/i : « che », « chi » (comme dans « chitarra »)."),
    q("q6", "Que change une consonne double (doppia) en italien, par exemple entre « pena » et « penna » ?", ["Rien, cela s'entend pareil à l'oral", "Le sens du mot et la prononciation (son plus long)", "Seulement l'orthographe", "La consonne double n'existe pas en italien"], 1, "Les doubles consonnes se prononcent de façon plus longue et peuvent changer le sens du mot : « pena » (peine) / « penna » (stylo)."),
    q("q7", "Comment se prononce « gli » en italien ?", ["Comme « gli » en français", "Un son proche de [ʎ], comme dans « famiglia »", "[gi] dur", "Il est muet"], 1, "« gli » se prononce avec un son mouillé proche de [ʎ], comme dans « famiglia »."),
    q("q8", "Comment se prononce « gn » en italien, comme dans « gnocchi » ?", ["[gn] séparé", "Un son proche du « gn » français dans « montagne »", "[g] seul", "[n] seul"], 1, "« gn » se prononce comme le « gn » français dans « montagne », un son mouillé unique."),
    q("q9", "Dans quel cas les lettres j, k, w, x, y apparaissent-elles en italien ?", ["Jamais, sous aucun prétexte", "Uniquement dans des mots d'origine étrangère", "Uniquement en début de phrase", "Uniquement au pluriel"], 1, "Ces lettres n'apparaissent en italien que dans des mots empruntés à d'autres langues (comme « jeans » ou « weekend »)."),
    q("q10", "Comment se prononce le « g » italien devant un « e » ou un « i », comme dans « giorno » ?", ["[g] dur", "[dʒ] comme « dj »", "Il est muet", "[j] français"], 1, "Devant e et i, le « g » italien se prononce [dʒ], comme dans « giorno » (jour)."),
]
ita_lesson = '''  {
    slug: "alfabeto-italien-6e",
    titre: "L'alfabeto italiano",
    matiere: "italien",
    niveau: "6e",
    duree: "20 min",
    resume: "Découvrir les 21 lettres de l'alphabet italien et les règles de prononciation du c, du g et des doubles consonnes (niveau A1).",
    motsAEcouter: ["ci", "gi", "gli", "gn", "doppia"],
''' + ecoute_italien + '''    objectifs: ["Connaître les 21 lettres de l'alphabet italien", "Prononcer correctement c et g selon la voyelle qui suit", "Reconnaître l'effet des doubles consonnes à l'oral"],
    contenu: ["L'italien standard n'utilise que 21 lettres, contrairement au français qui en compte 26 : il n'y a pas de j, k, w, x, y (sauf dans des mots empruntés à d'autres langues, comme « jeans » ou « weekend »). Les noms des lettres : a, bi, ci, di, e, effe, gi, acca, i, elle, emme, enne, o, pi, cu, erre, esse, ti, u, vu (ou vi), zeta.", "Les lettres « c » et « g » ont chacune deux prononciations selon la voyelle qui suit : devant a, o, u, elles sont dures, [k] et [g] (« casa », « gatto ») ; devant e, i, elles sont douces, [tʃ] et [dʒ] (« cena », « giorno »). Pour garder le son dur devant e/i, on ajoute un « h » : « che », « chi », « ghe », « ghi » (comme dans « chitarra », guitare).", "Les consonnes doubles (consonanti doppie) se prononcent de façon plus longue et intense à l'oral, et peuvent changer complètement le sens d'un mot : « pena » (peine) devient « penna » (stylo) avec deux n, « sono » (je suis) devient « sonno » (sommeil) avec deux n. Les groupes « gli » [ʎ] et « gn » [ɲ] ont aussi des sons mouillés particuliers, comme dans « famiglia » (famille) et « gnocchi »."],
    quiz: {
    slug: "quiz-alfabeto-italien-6e",
    titre: "Quiz — L'alfabeto italiano",
    questions: [
''' + ",\n".join(ita_qs) + '''
    ],
  },
  },
'''

idx = txt.index('slug: "saluti-presentazioni-italien-6e"')
_pos = txt.rindex(marker, 0, idx)
insert_pos = _pos + 1
assert txt[insert_pos:insert_pos+4] == '  {\n'
txt = txt[:insert_pos] + ita_lesson + txt[insert_pos:]

with open(path, 'w') as f:
    f.write(txt)

print("alphabet lessons inserted")
