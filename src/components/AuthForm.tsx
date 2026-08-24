"use client";

import { useState, type FormEvent } from "react";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";
import Link from "next/link";

export function ConnexionForm() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const res = await signIn("credentials", { email, password, redirect: false });

    setLoading(false);
    if (res?.error) {
      setError("Email ou mot de passe incorrect.");
      return;
    }
    router.push("/tableau-de-bord");
    router.refresh();
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
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
        <label className="block text-sm font-medium text-ardoise-800">Mot de passe</label>
        <input
          type="password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
        <div className="mt-1 text-right">
          <Link href="/mot-de-passe-oublie" className="text-xs text-ardoise-700/60 hover:text-corail-600">
            Mot de passe oublié ?
          </Link>
        </div>
      </div>
      {error && <p className="text-sm text-corail-600">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-full bg-ardoise-900 px-4 py-2.5 text-sm font-semibold text-craie hover:bg-ardoise-800 disabled:opacity-60"
      >
        {loading ? "Connexion…" : "Se connecter"}
      </button>
      <p className="text-center text-sm text-ardoise-700/70">
        Pas encore de compte ?{" "}
        <Link href="/inscription" className="font-semibold text-corail-600">
          Créer un compte
        </Link>
      </p>
    </form>
  );
}

export function InscriptionForm() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const res = await fetch("/api/inscription", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, password }),
    });
    const data = await res.json();

    if (!res.ok) {
      setError(data.message ?? "Une erreur est survenue.");
      setLoading(false);
      return;
    }

    const signInRes = await signIn("credentials", { email, password, redirect: false });
    setLoading(false);

    if (signInRes?.error) {
      router.push("/connexion");
      return;
    }
    router.push("/tableau-de-bord");
    router.refresh();
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Nom</label>
        <input
          type="text"
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
        <label className="block text-sm font-medium text-ardoise-800">Mot de passe</label>
        <input
          type="password"
          required
          minLength={8}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
        <p className="mt-1 text-xs text-ardoise-700/60">8 caractères minimum.</p>
      </div>
      {error && <p className="text-sm text-corail-600">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-full bg-corail-500 px-4 py-2.5 text-sm font-semibold text-white hover:bg-corail-600 disabled:opacity-60"
      >
        {loading ? "Création…" : "Créer mon compte gratuit"}
      </button>
      <p className="text-center text-sm text-ardoise-700/70">
        Déjà un compte ?{" "}
        <Link href="/connexion" className="font-semibold text-corail-600">
          Se connecter
        </Link>
      </p>
    </form>
  );
}


export function MotDePasseOublieForm() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setMessage(null);

    const res = await fetch("/api/mot-de-passe-oublie", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    });
    const data = await res.json();
    setLoading(false);

    if (!res.ok) {
      setError(data.message ?? "Une erreur est survenue.");
      return;
    }
    setMessage(data.message ?? "Si un compte existe avec cet email, un lien de réinitialisation vient d'être envoyé.");
  }

  if (message) {
    return (
      <div className="space-y-4 text-center">
        <p className="text-sm text-ardoise-800">{message}</p>
        <p className="text-sm text-ardoise-700/70">
          Pense à vérifier tes spams si tu ne vois rien arriver d&apos;ici quelques minutes.
        </p>
        <Link href="/connexion" className="inline-block text-sm font-semibold text-corail-600">
          Retour à la connexion
        </Link>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <p className="text-sm text-ardoise-700/70">
        Indique l&apos;email de ton compte : on t&apos;envoie un lien pour choisir un nouveau mot de passe.
      </p>
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
      {error && <p className="text-sm text-corail-600">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-full bg-ardoise-900 px-4 py-2.5 text-sm font-semibold text-craie hover:bg-ardoise-800 disabled:opacity-60"
      >
        {loading ? "Envoi…" : "Envoyer le lien de réinitialisation"}
      </button>
      <p className="text-center text-sm text-ardoise-700/70">
        <Link href="/connexion" className="font-semibold text-corail-600">
          Retour à la connexion
        </Link>
      </p>
    </form>
  );
}

export function ReinitialiserMotDePasseForm({ token }: { token: string }) {
  const router = useRouter();
  const [password, setPassword] = useState("");
  const [confirmation, setConfirmation] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);

    if (password !== confirmation) {
      setError("Les deux mots de passe ne correspondent pas.");
      return;
    }

    setLoading(true);
    const res = await fetch("/api/reinitialiser-mot-de-passe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token, password }),
    });
    const data = await res.json();
    setLoading(false);

    if (!res.ok) {
      setError(data.message ?? "Une erreur est survenue.");
      return;
    }

    setSuccess(true);
    setTimeout(() => router.push("/connexion"), 2000);
  }

  if (success) {
    return (
      <div className="space-y-2 text-center">
        <p className="text-sm font-medium text-ardoise-800">Mot de passe mis à jour avec succès !</p>
        <p className="text-sm text-ardoise-700/70">Redirection vers la connexion…</p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Nouveau mot de passe</label>
        <input
          type="password"
          required
          minLength={8}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
        <p className="mt-1 text-xs text-ardoise-700/60">8 caractères minimum.</p>
      </div>
      <div>
        <label className="block text-sm font-medium text-ardoise-800">Confirme le mot de passe</label>
        <input
          type="password"
          required
          minLength={8}
          value={confirmation}
          onChange={(e) => setConfirmation(e.target.value)}
          className="mt-1 w-full rounded-lg border border-ardoise-900/20 px-3 py-2 text-sm focus:border-corail-500 focus:outline-none"
        />
      </div>
      {error && <p className="text-sm text-corail-600">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-full bg-corail-500 px-4 py-2.5 text-sm font-semibold text-white hover:bg-corail-600 disabled:opacity-60"
      >
        {loading ? "Mise à jour…" : "Choisir ce mot de passe"}
      </button>
    </form>
  );
}
