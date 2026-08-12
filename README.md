# Ardoise — soutien scolaire, du CP à la Terminale

Ardoise est un site **et** une application (Progressive Web App installable) de soutien
scolaire aligné sur le programme officiel de l'Éducation nationale : primaire, collège,
lycée. Cours, exercices, quiz auto-corrigés, suivi de progression, comptes utilisateurs et
abonnements payants.

## Identité de marque

- **Nom** : Ardoise — référence à l'ardoise magique de l'école primaire, immédiatement
  reconnaissable pour un public français, mémorable, disponible sur la plupart des
  extensions (à vérifier/déposer avant lancement : `ardoise.fr`, `ardoise.app`…).
- **Palette** : ardoise (bleu-nuit profond, `#1B2733`), craie (blanc cassé, `#F9F7F2`),
  corail (accent primaire, `#FF6B4A`), menthe (validation/succès, `#2EC4B6`), safran
  (accent secondaire, `#FFB84D`).
- **Typographies** : Fredoka (titres, chaleureuse et arrondie) + Inter (texte courant,
  très lisible). Chargées via Google Fonts dans `src/app/layout.tsx`.
- **Logo** : `src/components/Logo.tsx` (SVG) + déclinaisons PNG dans `public/icons/`.

## Stack technique

- **Next.js 16** (App Router, Turbopack) + TypeScript + Tailwind CSS v4
- **Drizzle ORM** + PostgreSQL (voir `src/lib/db/schema.ts`) — choisi plutôt que Prisma
  pour ne dépendre d'aucun binaire natif téléchargé à l'installation
- **NextAuth v4** (Credentials + JWT) pour l'authentification
- **Stripe** pour les abonnements (Checkout + webhooks)
- **PWA** maison (manifest + service worker), sans dépendance tierce

Le même code sert de **site vitrine** (accueil, programme, tarifs…) et **d'application**
(tableau de bord, leçons, quiz). Installable sur mobile/desktop comme une app grâce au
manifest PWA — pas besoin de build natif séparé pour un premier lancement. Une déclinaison
React Native pourra être envisagée dans un second temps si un besoin d'app 100% native
(notifications push natives, accès hors-ligne poussé, présence sur les stores) apparaît.

## Démarrage en local

```bash
npm install
cp .env.example .env.local   # puis complète les variables (voir plus bas)
npm run dev
```

Le site fonctionne **sans base de données ni clés Stripe configurées** : les pages
publiques (accueil, programme, leçons, quiz en mode anonyme) s'affichent normalement. Les
actions qui nécessitent une base de données (inscription, sauvegarde de progression,
paiement) renvoient un message explicite plutôt que de planter.

## Variables d'environnement

Voir `.env.example`. À configurer pour une mise en production réelle :

| Variable | Description |
|---|---|
| `DATABASE_URL` | Connexion PostgreSQL (Vercel Postgres, Neon, Supabase, Railway…) |
| `NEXTAUTH_SECRET` | `openssl rand -base64 32` |
| `NEXTAUTH_URL` | URL publique du site |
| `STRIPE_SECRET_KEY` | Clé secrète Stripe (test puis live) |
| `STRIPE_WEBHOOK_SECRET` | Secret du endpoint webhook Stripe |
| `STRIPE_PRICE_MENSUEL` / `_ANNUEL` / `_FAMILLE` | IDs des Price Stripe pour chaque offre |

## Base de données

Le schéma est défini dans `src/lib/db/schema.ts` (`users`, `subscriptions`,
`progressions`). Pour créer/mettre à jour les tables une fois `DATABASE_URL` configurée :

```bash
npm run db:generate   # génère les migrations SQL à partir du schéma
npm run db:migrate     # les applique sur la base
npm run db:studio      # interface visuelle pour explorer les données
```

## Déploiement en production (recommandé : Vercel)

1. Pousser le projet sur un dépôt GitHub/GitLab.
2. Créer une base PostgreSQL managée (Vercel Postgres, Neon ou Supabase) et récupérer
   `DATABASE_URL`.
3. Importer le projet sur [vercel.com/new](https://vercel.com/new), renseigner les
   variables d'environnement ci-dessus.
4. Lancer `npm run db:migrate` (en local, pointé vers la base de prod, ou via une action
   CI) pour créer les tables.
5. Dans le dashboard Stripe : créer les 3 produits/prix (mensuel, annuel, famille),
   configurer un endpoint webhook `https://ton-domaine.fr/api/webhooks/stripe` écoutant
   `checkout.session.completed`, copier les clés dans Vercel.
6. Associer un nom de domaine (ex. `ardoise.fr`) dans les réglages du projet Vercel.
7. Repasser les clés Stripe de test à live une fois les tests de paiement validés.

## Rendre l'app installable (PWA)

Déjà fonctionnel : `public/manifest.webmanifest`, `public/sw.js`, icônes dans
`public/icons/`. Sur mobile (Chrome/Safari) et desktop (Chrome/Edge), les utilisateurs
verront une proposition « Ajouter à l'écran d'accueil / Installer l'application ».

## Structure du contenu pédagogique

- `src/content/curriculum.ts` — cycles, niveaux, matières.
- `src/content/lessons.ts` — 52 leçons + quiz, couvrant les 12 niveaux (CP à Terminale)
  dans les matières principales (français, mathématiques, histoire-géographie, sciences,
  anglais, philosophie en Terminale).
- `src/content/exams.ts` — 2 examens blancs (Brevet en 3e, Bac en Terminale) avec sujets
  et corrigés, pages `/examens` et `/examens/[slug]`.

Cette base est une couverture large mais reste un échantillon représentatif, pas le
programme officiel exhaustif (qui compterait plusieurs centaines de leçons par matière
et par niveau sur une année scolaire complète). Pour aller plus loin : étoffer chaque
niveau avec plusieurs leçons par période, ou migrer ce contenu en base de données / CMS
headless pour permettre des mises à jour sans redéploiement du code.

## Limites de cette version à connaître avant lancement

- Le contenu pédagogique livré est un **échantillon représentatif**, pas le programme
  complet des 12 niveaux × 6 matières (volume de contenu à produire en continu).
- Pas de vérification d'email ni de réinitialisation de mot de passe à l'inscription
  (à ajouter avant un lancement public — ex. Resend + tokens signés).
- Pas d'espace parent multi-profils implémenté (prévu dans l'offre Famille, à construire).
- Mentions légales / CGV / confidentialité sont des gabarits à remplacer par de vrais
  textes juridiques (identité de l'éditeur, hébergeur, RGPD).
- `PRISMA` n'a pas été retenu à cause de restrictions réseau de l'environnement de
  build ayant servi à générer ce projet (téléchargement de binaires bloqué) ; Drizzle a
  été choisi à la place, ce qui est un choix de production tout à fait valable.

## Vérifications effectuées

- `npx eslint .` : aucune erreur.
- `npx next build` : build de production réussi (pages statiques, dynamiques et API
  routes générées sans erreur).
- Smoke tests HTTP manuels : accueil, programme, leçon, tarifs (200), tableau de bord
  protégé (redirection 307 vers `/connexion` si non authentifié), API inscription/contact/
  checkout (réponses correctes, y compris en mode démo sans base de données ni Stripe).
