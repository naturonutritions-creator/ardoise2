import { Brain, BookOpenCheck, Calculator } from "lucide-react";
import type { ProfilAdaptation } from "@/content/adaptations";

export const PROFIL_INFO: Record<
  ProfilAdaptation,
  { nom: string; description: string; icone: typeof Brain; couleur: string }
> = {
  tdah: {
    nom: "TDAH",
    description:
      "Des leçons découpées en petites étapes chronométrées, avec des pauses actives régulières, pour soutenir la concentration.",
    icone: Brain,
    couleur: "safran",
  },
  dyslexie: {
    nom: "Dyslexie",
    description:
      "Des leçons en phrases courtes et simples, avec des conseils de lecture adaptés et la lecture audio activable à tout moment.",
    icone: BookOpenCheck,
    couleur: "menthe",
  },
  dyscalculie: {
    nom: "Dyscalculie",
    description:
      "Des leçons de mathématiques avec manipulation concrète, repères visuels et étapes très détaillées pour construire le sens des nombres.",
    icone: Calculator,
    couleur: "corail",
  },
};
