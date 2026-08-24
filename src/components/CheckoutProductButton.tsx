"use client";

import { useState } from "react";
import type { ProductId } from "@/lib/stripe";

export default function CheckoutProductButton({ product, label }: { product: ProductId; label: string }) {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  async function handleClick() {
    setLoading(true);
    setMessage(null);
    try {
      const res = await fetch("/api/checkout-produit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product }),
      });
      const data = await res.json();
      if (data.url) {
        window.location.href = data.url;
        return;
      }
      setMessage(data.message ?? "Le paiement n'est pas encore configuré sur cette démo.");
    } catch {
      setMessage("Une erreur est survenue. Réessaie plus tard.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <button
        type="button"
        onClick={handleClick}
        disabled={loading}
        className="inline-flex items-center justify-center rounded-full bg-corail-500 px-5 py-2.5 text-center text-sm font-semibold text-white transition-colors hover:bg-corail-600 disabled:opacity-60"
      >
        {loading ? "Chargement…" : label}
      </button>
      {message && <p className="mt-2 text-xs text-ardoise-700/70">{message}</p>}
    </div>
  );
}
