import type { Metadata, Viewport } from "next";
import "./globals.css";
import ServiceWorkerRegister from "@/components/ServiceWorkerRegister";

export const metadata: Metadata = {
  title: "Ardoise — Soutien scolaire du CP à la Terminale",
  description:
    "Ardoise est la plateforme de soutien scolaire alignée sur le programme officiel de l'Éducation nationale, du primaire à la Terminale : cours, exercices et quiz.",
  manifest: "/manifest.webmanifest",
  applicationName: "Ardoise",
  appleWebApp: {
    capable: true,
    statusBarStyle: "default",
    title: "Ardoise",
  },
};

export const viewport: Viewport = {
  themeColor: "#1b2733",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className="h-full antialiased">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fredoka:wght@500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-full flex flex-col bg-craie text-ardoise-900 font-sans">
        {children}
        <ServiceWorkerRegister />
      </body>
    </html>
  );
}
