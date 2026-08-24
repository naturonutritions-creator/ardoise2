import nodemailer from "nodemailer";

/**
 * Envoi d'emails transactionnels (réinitialisation de mot de passe, etc.).
 *
 * Configuration via variables d'environnement SMTP_HOST / SMTP_PORT / SMTP_USER /
 * SMTP_PASSWORD / SMTP_FROM (voir .env.example). Si le SMTP n'est pas configuré
 * (environnement de démo/développement), l'email n'est pas réellement envoyé :
 * son contenu est simplement affiché dans la console du serveur, pour que le
 * flux reste testable sans service d'envoi d'email configuré.
 */
export async function sendEmail(to: string, subject: string, html: string, text: string) {
  const host = process.env.SMTP_HOST;
  const port = process.env.SMTP_PORT ? Number(process.env.SMTP_PORT) : undefined;
  const user = process.env.SMTP_USER;
  const pass = process.env.SMTP_PASSWORD;
  const from = process.env.SMTP_FROM || "Cap Réussite <no-reply@cap-reussite.fr>";

  if (!host || !port || !user || !pass) {
    // Démo/développement sans SMTP configuré : on n'échoue pas, on trace l'email dans les logs serveur.
    console.log(
      `[mailer] SMTP non configuré — email non envoyé.\nÀ : ${to}\nSujet : ${subject}\n\n${text}`
    );
    return { sent: false as const };
  }

  const transporter = nodemailer.createTransport({
    host,
    port,
    secure: port === 465,
    auth: { user, pass },
  });

  await transporter.sendMail({ from, to, subject, html, text });
  return { sent: true as const };
}
