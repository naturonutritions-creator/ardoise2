import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async headers() {
    return [
      {
        // S'applique à toutes les pages du site.
        source: "/:path*",
        headers: [
          {
            // Empêche le site d'être affiché dans une <iframe> sur un autre site
            // (protège contre le "clonage" par framing).
            key: "X-Frame-Options",
            value: "SAMEORIGIN",
          },
          {
            key: "Content-Security-Policy",
            value: "frame-ancestors 'self'",
          },
          {
            key: "X-Content-Type-Options",
            value: "nosniff",
          },
          {
            key: "Referrer-Policy",
            value: "strict-origin-when-cross-origin",
          },
          {
            key: "Permissions-Policy",
            value: "browsing-topics=()",
          },
          {
            // Signale explicitement aux robots d'IA de ne pas utiliser le contenu
            // pour l'entraînement de modèles (en complément du blocage dans robots.txt).
            key: "X-Robots-Tag",
            value: "noai, noimageai",
          },
        ],
      },
    ];
  },
};

export default nextConfig;
