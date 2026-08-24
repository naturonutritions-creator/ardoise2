"use client";

import { useEffect, useRef, useState } from "react";
import { Volume2, Square } from "lucide-react";
import { clsx } from "clsx";
import { cleanForSpeech } from "@/lib/speech";

interface Token {
  text: string;
  isWord: boolean;
}

function tokenize(text: string): Token[] {
  const regex = /[\p{L}\p{N}'’-]+|[^\p{L}\p{N}'’-]+/gu;
  const tokens: Token[] = [];
  let m: RegExpExecArray | null;
  while ((m = regex.exec(text))) {
    tokens.push({ text: m[0], isWord: /[\p{L}\p{N}]/u.test(m[0]) });
  }
  return tokens;
}

/**
 * Lit un texte à voix haute et surligne en même temps le mot en cours de
 * lecture (effet "karaoké"), pour aider les élèves dyslexiques à suivre la
 * lecture des yeux en même temps qu'ils l'entendent.
 *
 * S'appuie sur l'événement `boundary` de la Web Speech API, qui indique la
 * position (en caractères) du mot en train d'être prononcé dans le texte
 * envoyé à la synthèse vocale. Comme ce texte "parlé" (nettoyé par
 * `cleanForSpeech`, ex. [ch] -> "che") peut légèrement différer du texte
 * affiché, on fait correspondre les mots par leur position dans l'ordre
 * (le Ne mot prononcé surligne le Ne mot affiché) plutôt que par index de
 * caractère brut, ce qui reste fiable même après ce nettoyage.
 */
export default function SyncedReadAloud({
  text,
  lang = "fr-FR",
  className,
  textClassName,
}: {
  text: string;
  lang?: string;
  className?: string;
  textClassName?: string;
}) {
  const [speaking, setSpeaking] = useState(false);
  const [activeWord, setActiveWord] = useState(-1);
  const displayTokens = useRef<Token[]>(tokenize(text));
  const wordIndices = useRef<number[]>([]);

  useEffect(() => {
    displayTokens.current = tokenize(text);
    wordIndices.current = displayTokens.current
      .map((t, i) => (t.isWord ? i : -1))
      .filter((i) => i >= 0);
  }, [text]);

  useEffect(() => {
    return () => {
      if (typeof window !== "undefined" && "speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  function handleClick() {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;

    if (speaking) {
      window.speechSynthesis.cancel();
      setSpeaking(false);
      setActiveWord(-1);
      return;
    }

    window.speechSynthesis.cancel();

    const spoken = cleanForSpeech(text);
    const spokenWordCount = (spoken.match(/[\p{L}\p{N}'’-]+/gu) ?? []).length;
    let wordsSeen = 0;

    const utterance = new SpeechSynthesisUtterance(spoken);
    utterance.lang = lang;
    utterance.rate = 0.75;
    utterance.pitch = 1;

    utterance.onboundary = (event) => {
      if (event.name && event.name !== "word") return;
      const ordinal = Math.min(wordsSeen, spokenWordCount - 1);
      const targetTokenIndex = wordIndices.current[ordinal];
      if (targetTokenIndex !== undefined) setActiveWord(targetTokenIndex);
      wordsSeen += 1;
    };
    utterance.onend = () => {
      setSpeaking(false);
      setActiveWord(-1);
    };
    utterance.onerror = () => {
      setSpeaking(false);
      setActiveWord(-1);
    };

    window.speechSynthesis.speak(utterance);
    setSpeaking(true);
  }

  return (
    <div className={className}>
      <p className={clsx("leading-relaxed text-ardoise-800", textClassName)}>
        {displayTokens.current.map((token, i) => (
          <span
            key={i}
            className={clsx(
              token.isWord && i === activeWord && "rounded bg-safran-300/70 px-0.5 text-ardoise-900"
            )}
          >
            {token.text}
          </span>
        ))}
      </p>
      <button
        type="button"
        onClick={handleClick}
        className={clsx(
          "mt-2 inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-xs font-semibold transition-colors",
          speaking
            ? "border-corail-500 bg-corail-100 text-corail-600"
            : "border-ardoise-900/20 bg-white text-ardoise-800 hover:border-ardoise-900/40"
        )}
        aria-label={speaking ? "Arrêter la lecture" : "Écouter"}
      >
        {speaking ? <Square className="h-3.5 w-3.5" /> : <Volume2 className="h-3.5 w-3.5" />}
        {speaking ? "Arrêter" : "Écouter"}
      </button>
    </div>
  );
}
