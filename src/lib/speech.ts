/**
 * Nettoyage et enrichissement du texte avant lecture à voix haute (Web Speech API).
 *
 * Dans le contenu pédagogique, les sons sont parfois notés entre crochets
 * pour l'affichage écrit, par exemple « le son [ch] comme dans "chat" ».
 * Cette notation est très utile à l'œil, et on veut qu'elle le soit aussi
 * à l'oreille : quand la voix rencontre une notation de son entre crochets,
 * elle doit prononcer ce son distinctement, plutôt que d'épeler les lettres
 * ("crochet, c, h, crochet fermé") ou de sauter silencieusement la notation.
 *
 * Comme la synthèse vocale du navigateur (Web Speech API) ne permet pas de
 * piloter la prononciation phonème par phonème (pas d'alphabet phonétique
 * international disponible de façon fiable), on utilise une astuce standard
 * en synthèse vocale : on remplace chaque code de son connu par une "graphie
 * parlée" — un petit mot ou une syllabe réelle du français que les voix
 * fr-FR prononcent presque toujours correctement et qui porte bien le son
 * visé (par exemple [ch] → « che », [eu] → « euh », [on] → « on »).
 *
 * Pour les notations qu'on ne reconnaît pas avec certitude (alphabet
 * phonétique international utilisé dans les leçons de langues étrangères,
 * par exemple), on revient au comportement précédent, plus sûr : on retire
 * la notation pour ne pas risquer une lecture incorrecte.
 */

// Graphie "parlée" pour chaque code de son rencontré entre crochets dans le
// contenu pédagogique (essentiellement les leçons de phonétique du CP/CE1).
// Choisie pour que la voix fr-FR du navigateur prononce, autant que possible,
// le son ciblé plutôt que d'épeler les lettres.
const SOUND_TO_SPEECH: Record<string, string> = {
  // Voyelles et sons complexes : ce sont déjà des syllabes françaises
  // réelles, la voix fr-FR les prononce correctement telles quelles.
  on: "on",
  oin: "oin",
  in: "in",
  ou: "ou",
  oi: "oi",
  ion: "ion",
  an: "an",
  // [ien] seul n'est pas un mot français reconnu : la voix a tendance à
  // l'épeler lettre par lettre (i, e, n) au lieu de prononcer le son en
  // une seule syllabe. On le remplace par le mot réel "bien", qui se
  // termine exactement par ce son et que toute voix fr-FR prononce bien.
  ien: "bien",
  yin: "bien",
  // [aille] seul seul n'est pas un mot très naturel à l'oral et peut être
  // prononcé trop fort ou trop dur par la voix. On le remplace par le mot
  // réel "paille", qui se termine par ce son et se prononce doucement.
  aille: "paille",
  eille: "abeille",
  euille: "feuille",
  ouille: "grenouille",
  o: "o",
  a: "a",
  i: "i",
  u: "u",
  è: "è",
  é: "é",
  aï: "aïe",
  oï: "oïe",
  wa: "oi",
  oua: "oi",
  ouin: "oin",
  // [eu] seul seul se lit "eu" (participe passé d'avoir, son [y]) : on force
  // la graphie "euh", prononcée correctement en [ø]/[œ] comme dans "feu".
  eu: "euh",
  e: "euh",
  // Notations à double graphie (deux façons d'écrire un même son) : on
  // ne garde que la partie la plus fiable à l'oral.
  "an/en": "an",
  "in/ain": "in",
  "eu/œu": "euh",
  "au/eau": "au",
  "ill/y": "fille",
  ill: "fille",
  ye: "fille",
  gn: "montagne",
  gne: "montagne",
  gi: "gi",
  ji: "ji",
  "s/ss": "s, ss",
  sse: "tasse",
  // Consonnes isolées : une syllabe inventée comme "be" ou "che" n'est pas
  // un mot réel, et certaines voix fr-FR l'interprètent mal (par exemple
  // "che" lu comme "ché", avec un é fermé, au lieu du e muet attendu). On
  // remplace donc chaque consonne isolée par un mot français réel, simple
  // et courant, qui se termine par cette consonne suivie d'un e muet — la
  // voix le prononce alors toujours correctement, comme elle le ferait
  // pour n'importe quel mot ordinaire.
  b: "robe",
  be: "robe",
  d: "aide",
  de: "aide",
  f: "girafe",
  fe: "girafe",
  g: "bague",
  gue: "bague",
  j: "je",
  je: "je",
  k: "brique",
  ke: "brique",
  que: "brique",
  l: "boule",
  le: "boule",
  m: "pomme",
  me: "pomme",
  n: "banane",
  ne: "banane",
  p: "soupe",
  pe: "soupe",
  r: "guitare",
  re: "guitare",
  s: "tasse",
  se: "tasse",
  t: "carotte",
  te: "carotte",
  v: "cave",
  ve: "cave",
  w: "oue",
  z: "ze",
  ch: "vache",
  che: "vache",
  // Graphies qui, en fin de mot, se prononcent comme le son [é] (verbes du
  // premier groupe à l'infinitif, mots en -ez) : chanter, nez... On force
  // la prononciation [é] plutôt que d'épeler les lettres "e" et "r"/"z".
  er: "é",
  ez: "é",
};

// Certaines leçons de phonétique isolent une graphie entre guillemets
// français dans une phrase, plutôt qu'entre crochets, par exemple :
// « Quel mot se termine par le son [é] écrit « er » ? ». Sans traitement,
// la voix a tendance à épeler ces lettres isolées ("e", "r") au lieu de
// prononcer le son qu'elles représentent. On applique donc la même table
// de correspondance à ces graphies entre guillemets, uniquement pour les
// graphies courtes et connues (pour ne jamais toucher un mot ordinaire
// entre guillemets, comme une citation).
function speakQuotedGraphemes(text: string): string {
  return text.replace(/«\s*([a-zA-Zàâéèêëîïôùûüÿœæ]{1,4})\s*»/g, (match, grapheme: string) => {
    const key = grapheme.trim().toLowerCase();
    const spoken = SOUND_TO_SPEECH[key];
    return spoken ? `, ${spoken}, ` : match;
  });
}

/**
 * Remplace chaque notation de son entre crochets par sa graphie "parlée",
 * en insérant de courtes pauses (virgules) pour bien détacher le son du
 * reste de la phrase à l'oral. Les notations inconnues (alphabet
 * phonétique international, par exemple) sont simplement retirées, comme
 * avant, pour éviter une lecture incorrecte.
 */
function speakSounds(text: string): string {
  return text.replace(/\[([^[\]]{1,12})\]/g, (_match, code: string) => {
    const key = code.trim();
    const spoken = SOUND_TO_SPEECH[key];
    if (spoken) {
      return `, ${spoken}, `;
    }
    // Notation non reconnue (ex. alphabet phonétique international) :
    // on retire pour ne pas risquer une lecture erronée lettre par lettre.
    return "";
  });
}

// Corrections ponctuelles de prononciation pour des mots précis que la
// synthèse vocale du navigateur lit parfois de façon incorrecte, malgré une
// orthographe standard. On respelle ces mots uniquement pour la lecture à
// voix haute (le texte affiché à l'écran, lui, n'est jamais modifié).
const WORD_PRONUNCIATION_FIXES: [RegExp, string][] = [
  // La terminaison "-er" citée seule (par exemple comme réponse à un quiz
  // de conjugaison : "-er", "-ir", "-re", "-oir") est souvent épelée
  // lettre par lettre ("e", "r") par la voix, au lieu d'être prononcée
  // comme le son [é] qu'elle représente réellement en fin d'infinitif.
  // On ne cible que le suffixe isolé (entouré d'espaces ou de bornes de
  // texte), jamais un mot entier qui se terminerait par "er" (comme
  // "chanter", laissé intact car déjà bien prononcé par la voix fr-FR).
  [/(^|\s)-er(\s|$)/gi, "$1é$2"],
  // "bijou" est parfois lu avec un son nasalisé en [on] au lieu du son
  // [ou] attendu en fin de mot. La coupe avec un tiret ("bi-jou") pouvait
  // être lue comme un mot composé avec un accent mal placé sur la
  // première syllabe : on sépare plutôt par un espace, ce qui pousse la
  // voix à articuler nettement les deux syllabes et à bien prononcer le
  // [ou] final, comme dans "chou" ou "genou".
  [/\bbijoux?\b/gi, "bi jou"],
  [/\bgenoux?\b/gi, "ge nou"],
  [/\bhiboux?\b/gi, "i bou"],
  // "sœur" (et "cœur", même graphie en "œu") est parfois lu avec un son
  // mal articulé. La respelling précédente ("seureu") ajoutait une syllabe
  // qui n'existe pas dans le mot (sœur n'a qu'une seule syllabe) et
  // dénaturait la prononciation. On respelle plutôt sur le modèle du mot
  // "heure" — dont la terminaison "-eure" est presque toujours bien
  // prononcée [œʁ] par les voix fr-FR — pour rester au plus près du mot
  // réel tout en garantissant le bon son.
  [/\bsœur\b/gi, "seur"],
  [/\bcœur\b/gi, "keur"],
  [/\bsœurs\b/gi, "seurs"],
  [/\bcœurs\b/gi, "keurs"],
  // Le son [z] est parfois mal articulé par la voix, surtout en début de
  // mot ou de syllabe accentuée (ex. "zèbre", "zoo"), où il peut être
  // prononcé trop faiblement ou confondu avec [s]. On appuie le son en
  // doublant légèrement la consonne à l'oral, sans changer l'orthographe
  // affichée à l'écran.
  [/\bzèbre(s)?\b/gi, "zzèbre$1"],
  [/\bzoo(s)?\b/gi, "zzoo$1"],
  [/\bzigzag(s)?\b/gi, "zzigzag$1"],
  [/\bzéro(s)?\b/gi, "zzéro$1"],
];

function fixKnownPronunciations(text: string): string {
  let result = text;
  for (const [pattern, replacement] of WORD_PRONUNCIATION_FIXES) {
    result = result.replace(pattern, replacement);
  }
  return result;
}

// Dans les phrases de lecture du CP (phrasesLectureCp), les lettres muettes
// finales sont marquées entre tildes pour être affichées dans une couleur
// différente à l'écran (ex. "Le cha~t~ dor~t~."). Pour la lecture à voix
// haute, ces lettres restent muettes : on retire seulement les tildes en
// gardant les lettres, la voix les lira normalement (donc les lettres
// muettes françaises usuelles ne seront de toute façon pas prononcées par
// une voix fr-FR correcte, ex. le "t" final de "chat").
function stripSilentLetterMarkup(text: string): string {
  return text.replace(/~([^~]*)~/g, "$1");
}

export function cleanForSpeech(text: string): string {
  if (!text) return text;

  let cleaned = stripSilentLetterMarkup(text);
  cleaned = speakSounds(cleaned);
  cleaned = speakQuotedGraphemes(cleaned);
  cleaned = fixKnownPronunciations(cleaned);

  cleaned = cleaned
    // Recolle les espaces multiples laissés par les remplacements.
    .replace(/\s{2,}/g, " ")
    // Nettoie les virgules dupliquées ou mal placées introduites par
    // speakSounds (ex. "mot, on,  , se retrouve" → "mot, on, se retrouve").
    .replace(/,\s*,/g, ",")
    // Évite les espaces juste avant une ponctuation.
    .replace(/\s+([.,;:!?»])/g, "$1")
    // Évite les doublons de ponctuation type ".." ou ". ."
    .replace(/\.\s*\./g, ".")
    .trim();

  return cleaned;
}
