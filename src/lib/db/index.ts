import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

// La connexion est paresseuse : aucune requête n'est envoyée tant qu'on n'utilise
// pas `db`. Cela permet au projet de compiler et de démarrer même sans
// DATABASE_URL configurée (ex. en aperçu local sans base de données).
// `connect_timeout` court pour échouer vite plutôt que de faire attendre
// l'utilisateur si la base n'est pas joignable.
const connectionString =
  process.env.DATABASE_URL ?? "postgres://placeholder:placeholder@localhost:5432/placeholder";

const client = postgres(connectionString, {
  max: 1,
  connect_timeout: 5,
  idle_timeout: 20,
  onnotice: () => {},
});

export const db = drizzle(client, { schema });
export { schema };
