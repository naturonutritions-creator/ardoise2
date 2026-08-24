/**
 * Découpe un texte en segments alternant français et langue étrangère, pour
 * les leçons d'anglais/espagnol/italien : le texte explicatif reste lu en
 * français, seuls les mots/phrases explicitement dans la langue étrangère
 * (entre « guillemets », ou juste avant une traduction entre parenthèses)
 * sont prononcés dans cette langue.
 */
export interface LangSegment {
  text: string;
  lang: string;
}

const FRENCH = "fr-FR";

export function segmentByLanguage(text: string, foreignLang: string): LangSegment[] {
  if (!text || foreignLang === FRENCH) return [{ text, lang: FRENCH }];

  const segments: LangSegment[] = [];
  // 1) « phrase étrangère » entre guillemets français
  // 2) mot(s) étranger(s) juste avant (traduction française)
  // Le groupe 2 (mot(s) étranger(s) juste avant une parenthèse) est volontairement
  // limité à 2 mots maximum : au-delà, on capturait parfois des mots de liaison
  // français qui précédaient le vrai mot étranger (ex. « on utilise many » au lieu
  // de « many » seul), ce qui fragmentait et hachait la lecture audio.
  const pattern = /«\s*([^»]+?)\s*»|(?:^|[^A-Za-zÀ-ÖØ-öø-ÿ'’])((?:[A-Za-zÀ-ÖØ-öø-ÿ'’]+[- ]){0,1}[A-Za-zÀ-ÖØ-öø-ÿ'’]+)\s*\(([^()]+)\)/g;
  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = pattern.exec(text)) !== null) {
    if (match.index > lastIndex) {
      const before = text.slice(lastIndex, match.index);
      if (before.trim()) segments.push({ text: before, lang: FRENCH });
    }
    if (match[1] !== undefined) {
      segments.push({ text: match[1], lang: foreignLang });
    } else {
      segments.push({ text: match[2].trim(), lang: foreignLang });
      segments.push({ text: `(${match[3]})`, lang: FRENCH });
    }
    lastIndex = pattern.lastIndex;
  }

  if (lastIndex < text.length) {
    const rest = text.slice(lastIndex);
    if (rest.trim()) segments.push({ text: rest, lang: FRENCH });
  }

  return segments.length > 0 ? segments : [{ text, lang: FRENCH }];
}
