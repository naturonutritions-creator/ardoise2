"use client";

import { useRef, useState } from "react";
import { Mic, Play, Pause } from "lucide-react";
import { clsx } from "clsx";

/**
 * Joue un vrai clip audio enregistré (voix humaine) pour le son cible d'une
 * leçon de phonétique, au lieu de la synthèse vocale du navigateur. C'est le
 * seul moyen d'entendre un son isolé (comme [ch] ou [b]) exactement comme il
 * doit se dire, sans les approximations inévitables du Web Speech API sur
 * une syllabe qui n'est pas un mot réel.
 *
 * Si le fichier audio n'existe pas encore (aucun enregistrement fourni pour
 * ce son), le bouton correspondant ne s'affiche pas : `onError` le retire
 * silencieusement plutôt que de montrer un lecteur audio cassé. Chaque son
 * peut donc être ajouté progressivement, un fichier à la fois. La carte
 * entière disparaît si aucun des clips fournis n'est disponible.
 */
function UnSon({ url, label }: { url: string; label: string }) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);
  const [available, setAvailable] = useState(true);

  if (!available) return null;

  function handleClick() {
    const el = audioRef.current;
    if (!el) return;
    if (playing) {
      el.pause();
      el.currentTime = 0;
      setPlaying(false);
    } else {
      el.currentTime = 0;
      el.play().catch(() => setAvailable(false));
    }
  }

  return (
    <>
      <button
        type="button"
        onClick={handleClick}
        className={clsx(
          "inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-xs font-semibold transition-colors",
          playing
            ? "border-safran-500 bg-safran-200 text-ardoise-900"
            : "border-ardoise-900/20 bg-white text-ardoise-800 hover:border-ardoise-900/40"
        )}
      >
        {playing ? <Pause className="h-3.5 w-3.5" /> : <Play className="h-3.5 w-3.5" />}
        {playing ? "Arrêter" : label}
      </button>
      <audio
        ref={audioRef}
        src={url}
        preload="none"
        onEnded={() => setPlaying(false)}
        onPlay={() => setPlaying(true)}
        onError={() => setAvailable(false)}
      />
    </>
  );
}

export default function SonReel({ audio }: { audio?: { url: string; label: string }[] }) {
  if (!audio || audio.length === 0) return null;

  return (
    <div className="rounded-2xl border border-safran-500/30 bg-safran-100 p-6">
      <h3 className="flex items-center gap-2 font-display text-sm font-semibold text-ardoise-900">
        <Mic className="h-4 w-4 text-safran-600" />
        Écoute la vraie prononciation
      </h3>
      <p className="mt-1 text-xs text-ardoise-700/70">
        Un enregistrement d&apos;une vraie voix, pour être sûr d&apos;entendre le bon son.
      </p>
      <div className="mt-3 flex flex-wrap gap-2">
        {audio.map((a) => (
          <UnSon key={a.url} url={a.url} label={a.label} />
        ))}
      </div>
    </div>
  );
}
