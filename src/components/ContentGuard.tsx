"use client";

import { useEffect } from "react";

/**
 * Décourage la copie automatisée du contenu pédagogique : bloque le clic droit
 * (menu contextuel) et désactive la sélection de texte à la souris sur les
 * pages où ce composant est monté (leçons, textes de compréhension, textes à
 * traduire). Reste sans effet sur les robots d'aspiration, qui sont bloqués en
 * amont via robots.txt et le middleware (voir src/proxy.ts) ; ce composant vise
 * la copie manuelle occasionnelle du contenu affiché à l'écran.
 */
export default function ContentGuard() {
  useEffect(() => {
    const blockContextMenu = (e: MouseEvent) => e.preventDefault();
    document.addEventListener("contextmenu", blockContextMenu);
    document.body.classList.add("content-protected");
    return () => {
      document.removeEventListener("contextmenu", blockContextMenu);
      document.body.classList.remove("content-protected");
    };
  }, []);

  return null;
}
