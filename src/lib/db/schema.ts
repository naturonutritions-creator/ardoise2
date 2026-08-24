import {
  pgTable,
  serial,
  text,
  varchar,
  timestamp,
  integer,
  boolean,
  uniqueIndex,
} from "drizzle-orm/pg-core";

export const users = pgTable(
  "users",
  {
    id: serial("id").primaryKey(),
    name: varchar("name", { length: 120 }).notNull(),
    email: varchar("email", { length: 255 }).notNull(),
    passwordHash: text("password_hash").notNull(),
    role: varchar("role", { length: 20 }).notNull().default("eleve"), // eleve | parent | admin
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [uniqueIndex("users_email_idx").on(table.email)]
);

export const subscriptions = pgTable("subscriptions", {
  id: serial("id").primaryKey(),
  userId: integer("user_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
  stripeCustomerId: varchar("stripe_customer_id", { length: 255 }),
  stripeSubscriptionId: varchar("stripe_subscription_id", { length: 255 }),
  plan: varchar("plan", { length: 40 }).notNull().default("gratuit"), // gratuit | mensuel | annuel | famille
  status: varchar("status", { length: 30 }).notNull().default("inactive"), // active | inactive | past_due | canceled
  currentPeriodEnd: timestamp("current_period_end"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const progressions = pgTable(
  "progressions",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    lessonSlug: varchar("lesson_slug", { length: 160 }).notNull(),
    lessonDone: boolean("lesson_done").notNull().default(false),
    quizScore: integer("quiz_score"), // sur 100
    quizAttempts: integer("quiz_attempts").notNull().default(0),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
  },
  (table) => [uniqueIndex("progressions_user_lesson_idx").on(table.userId, table.lessonSlug)]
);

export const passwordResetTokens = pgTable(
  "password_reset_tokens",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    tokenHash: varchar("token_hash", { length: 64 }).notNull(), // sha256 du token envoyé par email (le token en clair n'est jamais stocké)
    expiresAt: timestamp("expires_at").notNull(),
    usedAt: timestamp("used_at"), // renseigné une fois le token consommé, pour empêcher toute réutilisation
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [uniqueIndex("password_reset_tokens_hash_idx").on(table.tokenHash)]
);

export const purchases = pgTable("purchases", {
  id: serial("id").primaryKey(),
  userId: integer("user_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
  product: varchar("product", { length: 40 }).notNull(), // brevet-pack | bac-pack
  stripeCustomerId: varchar("stripe_customer_id", { length: 255 }),
  stripeSessionId: varchar("stripe_session_id", { length: 255 }),
  status: varchar("status", { length: 30 }).notNull().default("active"), // active | refunded
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export type User = typeof users.$inferSelect;
export type NewUser = typeof users.$inferInsert;
export type Subscription = typeof subscriptions.$inferSelect;
export type Progression = typeof progressions.$inferSelect;
export type Purchase = typeof purchases.$inferSelect;
export type PasswordResetToken = typeof passwordResetTokens.$inferSelect;
