"use client";

import { useEffect, useRef, useState } from "react";
import { Volume2, Square } from "lucide-react";
import { clsx } from "clsx";
import { cleanForSpeech } from "@/lib/speech";
import { segmentByLanguage } from "@/lib/langSegments";

/**
 * Bouton "Écouter". Deux sources possibles :
 *  1. `audioUrl` — un vrai fichier audio enregistré (la voix de l'utilisateur).
 *     C'est la priorité : si le fichier existe, c'est lui qui est joué.
 *  2. À défaut (pas de `audioUrl`, ou fichier introuvable), on retombe sur la
 *     synthèse vocale du navigateur (Web Speech API), comme avant.
 *
 * Ce mécanisme de repli est important : tant qu'un fichier audio n'a pas
 * encore été fourni pour une leçon donnée, le bouton continue de fonctionner
 * normalement grâce à la synthèse vocale.
 */
export default function ReadAloud({
  text,
  label = "Écouter",
  className,
  lang = "fr-FR",
  mixedLang = false,
  secondText,
  secondLang,
  audioUrl,
}: {
  text: string;
  label?: string;
  className?: string;
  lang?: string;
  mixedLang?: boolean;
  /** Texte optionnel lu juste après `text` (ex. la lettre en français après son nom en langue étrangère). */
  secondText?: string;
  secondLang?: string;
  /** Fichier audio d'une vraie voix enregistrée, prioritaire sur la synthèse vocale. */
  audioUrl?: string;
}) {
  const [speaking, setSpeaking] = useState(false);
  const audioElRef = useRef<HTMLAudioElement | null>(null);
  const realAudioFailedRef = useRef(false);

  // Coupe la lecture en cours si le composant est démonté (changement de page).
  useEffect(() => {
    return () => {
      if (typeof window !== "undefined" && "speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
      audioElRef.current?.pause();
    };
  }, []);

  function speakWithSynthesis() {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;

    window.speechSynthesis.cancel();

    const segments = mixedLang
      ? segmentByLanguage(cleanForSpeech(text), lang)
      : [{ text: cleanForSpeech(text), lang }];

    if (secondText) {
      segments.push({ text: cleanForSpeech(secondText), lang: secondLang ?? "fr-FR" });
    }

    let remaining = segments.length;
    segments.forEach((seg) => {
      const utterance = new SpeechSynthesisUtterance(seg.text);
      utterance.lang = seg.lang;
      // Débit proche du naturel pour une diction fluide, tout en gardant une
      // articulation nette (un débit trop lent hache la voix et nuit à la
      // fluidité, un débit par défaut à 1 a tendance à avaler les liaisons).
      utterance.rate = 0.95;
      utterance.pitch = 1;
      utterance.onend = () => {
        remaining -= 1;
        if (remaining <= 0) setSpeaking(false);
      };
      utterance.onerror = () => {
        remaining -= 1;
        if (remaining <= 0) setSpeaking(false);
      };
      window.speechSynthesis.speak(utterance);
    });
    setSpeaking(true);
  }

  function handleClick() {
    if (speaking) {
      window.speechSynthesis?.cancel();
      audioElRef.current?.pause();
      setSpeaking(false);
      return;
    }

    if (audioUrl && !realAudioFailedRef.current) {
      if (!audioElRef.current) {
        audioElRef.current = new Audio(audioUrl);
        audioElRef.current.onended = () => setSpeaking(false);
      }
      const el = audioElRef.current;
      el.currentTime = 0;
      el
        .play()
        .then(() => setSpeaking(true))
        .catch(() => {
          // Fichier absent ou illisible : on retombe sur la synthèse vocale.
          realAudioFailedRef.current = true;
          speakWithSynthesis();
        });
      return;
    }

    speakWithSynthesis();
  }

  return (
    <button
      type="button"
      onClick={handleClick}
      className={clsx(
        "inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-xs font-semibold transition-colors",
        speaking
          ? "border-corail-500 bg-corail-100 text-corail-600"
          : "border-ardoise-900/20 bg-white text-ardoise-800 hover:border-ardoise-900/40",
        className
      )}
      aria-label={speaking ? "Arrêter la lecture" : label}
    >
      {speaking ? <Square className="h-3.5 w-3.5" /> : <Volume2 className="h-3.5 w-3.5" />}
      {speaking ? "Arrêter" : label}
    </button>
  );
}
