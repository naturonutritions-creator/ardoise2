"use client";

import { useState, type FormEvent } from "react";

export default function ContactForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "done" | "error">("idle");

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setStatus("loading");
    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message }),
      });
      setStatus(res.ok ? "done" : "error");
    } catch {
      setStatus("error");
    }
  }

  if (status === "done") {
    return (
      <p className="rounded-lg bg-menthe-100 px-4 py-3 text-sm text-menthe-600">
        Merci ! Ton message a bien été envoyé, on te répond très vite.
      </p>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Nom</label>
        <input
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Email</label>
        <input
          type="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Message</label>
        <textarea
          required
          minLength={10}
          rows={5}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
      </div>
      {status === "error" && (
        <p className="text-sm text-corail-600">Une erreur est survenue, réessaie plus tard.</p>
      )}
      <button
        type="submit"
        disabled={status === "loading"}
        className="rounded-full bg-corail-500 px-5 py-2.5 text-sm font-semibold text-white hover:bg-corail-600 disabled:opacity-60"
      >
        {status === "loading" ? "Envoi…" : "Envoyer"}
      </button>
    </form>
  );
}
