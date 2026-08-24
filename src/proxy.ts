import { NextResponse, type NextRequest } from "next/server";
import { getToken } from "next-auth/jwt";

// Robots/outils connus pour l'aspiration ou l'entraînement d'IA sur le contenu du site.
// Les moteurs de recherche légitimes (Googlebot, Bingbot, DuckDuckBot...) ne sont pas
// bloqués afin de préserver le référencement naturel du site.
const BLOCKED_USER_AGENT = new RegExp(
  [
    "GPTBot",
    "ChatGPT-User",
    "CCBot",
    "anthropic-ai",
    "ClaudeBot",
    "Claude-Web",
    "Bytespider",
    "PetalBot",
    "Amazonbot",
    "Applebot-Extended",
    "meta-externalagent",
    "FacebookBot",
    "Diffbot",
    "omgili",
    "AhrefsBot",
    "SemrushBot",
    "MJ12bot",
    "DotBot",
    "dataforseo",
    "magpie-crawler",
    "Scrapy",
    "python-requests",
    "python-urllib",
    "HTTrack",
    "SiteSucker",
    "Wget",
    "libwww-perl",
    "Go-http-client",
  ].join("|"),
  "i"
);

export default async function proxy(req: NextRequest) {
  const userAgent = req.headers.get("user-agent") || "";

  if (BLOCKED_USER_AGENT.test(userAgent)) {
    return new NextResponse("Accès refusé : l'extraction automatisée du contenu est interdite.", {
      status: 403,
    });
  }

  if (req.nextUrl.pathname.startsWith("/tableau-de-bord")) {
    const token = await getToken({ req });
    if (!token) {
      const signInUrl = new URL("/connexion", req.url);
      signInUrl.searchParams.set("callbackUrl", req.url);
      return NextResponse.redirect(signInUrl);
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|manifest.webmanifest|icon.png|apple-icon.png|sw.js).*)",
  ],
};
