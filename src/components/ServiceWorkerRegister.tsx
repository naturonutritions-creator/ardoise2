"use client";

import { useEffect } from "react";

export default function ServiceWorkerRegister() {
  useEffect(() => {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("/sw.js").catch(() => {
        // L'enregistrement du service worker échoue silencieusement (ex. en dev)
      });
    }
  }, []);

  return null;
}
