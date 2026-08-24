export interface ExamEpreuve {
  matiere: string;
  duree: string;
  bareme: string;
  sujet: string[];
  corrige: string[];
}

export interface Exam {
  slug: string;
  titre: string;
  niveau: string;
  description: string;
  dureeTotale: string;
  epreuves: ExamEpreuve[];
  pack: "brevet" | "bac"; // regroupement pour le pack payant de 6 examens
  numero: number; // 1 à 6, position dans le pack
}

export const EXAMS: Exam[] = [
  {
    slug: "brevet-blanc-1",
    titre: "Brevet blanc n°1",
    niveau: "3e",
    description:
      "Une épreuve d'entraînement type, inspirée du Diplôme national du brevet, pour s'exercer dans les conditions du jour J en français, mathématiques et histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 1,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Après avoir lu un texte narratif de ton choix (extrait de roman étudié en classe), identifie le narrateur et précise s'il est extérieur à l'histoire ou s'il en est un personnage.",
          "Question 2 (grammaire, 10 points) : Dans une phrase de ton choix contenant un dialogue, relève un verbe conjugué et donne son sujet, son temps et son mode.",
          "Question 3 (interprétation, 10 points) : Explique en quelques lignes quel sentiment domine dans le passage choisi, en t'appuyant sur au moins une citation précise.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention particulière aux accords sujet-verbe et aux homophones grammaticaux.",
          "Rédaction au choix (50 points) : soit un texte d'imagination qui prolonge ou transforme un texte étudié en classe, soit un texte de réflexion argumentée sur une question de société abordée en cours (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : on distingue un narrateur externe (« il/elle », absent de l'histoire) d'un narrateur interne (« je », personnage de l'histoire) — le point clé est de justifier avec un indice du texte (pronoms, informations connues du narrateur).",
          "Question 2 : la réponse attendue précise les trois éléments demandés (sujet, temps, mode) et non seulement l'infinitif du verbe.",
          "Question 3 : une bonne réponse cite précisément le texte entre guillemets et relie la citation au sentiment identifié, plutôt que de rester dans l'impression générale.",
          "Dictée : les erreurs les plus fréquentes portent sur les accords sujet-verbe avec un sujet éloigné, et sur les homophones a/à, et/est, ou/où.",
          "Rédaction : le correcteur valorise une structure claire (introduction, plusieurs paragraphes, conclusion), la richesse du vocabulaire et le respect de la consigne (type de texte demandé).",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Calcul (20 points) : Calculer A = (5/3) + (2/9) et donner le résultat sous forme de fraction irréductible.",
          "Exercice 2 — Géométrie (30 points) : ABC est un triangle rectangle en A tel que AB = 6 cm et AC = 8 cm. Calculer la longueur BC en utilisant le théorème adapté.",
          "Exercice 3 — Proportionnalité (25 points) : Une recette pour 4 personnes nécessite 250 g de farine. Quelle quantité de farine faut-il pour 10 personnes ?",
          "Exercice 4 — Problème (25 points) : Un magasin propose une réduction de 20 % sur un article à 45 €. Calculer le prix après réduction, puis exprimer cette réduction sous forme de coefficient multiplicateur.",
        ],
        corrige: [
          "Exercice 1 : on met au même dénominateur (9) : 15/9 + 2/9 = 17/9, déjà irréductible.",
          "Exercice 2 : ABC est rectangle en A, donc BC est l'hypoténuse. D'après Pythagore : BC² = AB² + AC² = 36 + 64 = 100, donc BC = 10 cm.",
          "Exercice 3 : le rapport de proportionnalité est 10/4 = 2,5 ; il faut donc 250 × 2,5 = 625 g de farine.",
          "Exercice 4 : une réduction de 20 % correspond à un coefficient multiplicateur de 0,8. Prix final = 45 × 0,8 = 36 €.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique en quelques lignes ce qu'est la Seconde Guerre mondiale et cite au moins deux conséquences majeures du conflit.",
          "Question de connaissances (10 points) : Qu'est-ce que la décolonisation ? Donne un exemple de territoire qui a obtenu son indépendance après 1945.",
          "Étude de document (15 points) : à partir d'une carte ou d'un texte fourni par l'enseignant sur les inégalités de développement dans le monde, identifie deux informations que le document apporte.",
          "EMC (10 points) : Explique ce qu'est le droit de vote et pourquoi il est considéré comme un pilier de la démocratie.",
        ],
        corrige: [
          "Réponse attendue : dater le conflit (1939-1945), citer des belligérants et au moins deux conséquences (bilan humain très lourd, création de l'ONU, redéfinition des frontières...).",
          "Réponse attendue : définir la décolonisation comme le processus d'indépendance des anciennes colonies après 1945, et citer un exemple précis avec une date approximative.",
          "Réponse attendue : identifier des informations explicites du document (chiffres, légende de carte) sans faire de hors-sujet.",
          "Réponse attendue : relier le droit de vote à la participation des citoyens aux décisions collectives et au principe de légitimité démocratique.",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-1",
    titre: "Bac blanc n°1",
    niveau: "terminale",
    description:
      "Une épreuve d'entraînement type pour le Baccalauréat général, couvrant le tronc commun (philosophie, histoire-géographie) et un exemple d'épreuve de spécialité (mathématiques). À adapter selon tes spécialités réellement choisies.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 1,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Peut-on désirer sans souffrir ? »",
          "Sujet 2 : « La liberté consiste-t-elle à faire ce que l'on veut ? »",
          "Consignes : le devoir doit comporter une introduction avec problématisation du sujet, un développement structuré en plusieurs parties argumentées et illustrées d'exemples ou de références philosophiques, et une conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : distinguer le désir comme manque (source de souffrance selon certaines lectures platoniciennes) et le désir comme puissance d'exister (Spinoza), pour nuancer une réponse univoque.",
          "Pour le sujet 2, une piste possible : interroger la liberté comme absence de contrainte (faire ce que l'on veut) puis la confronter à l'idée d'une liberté éclairée par la raison, qui peut impliquer de renoncer à certains désirs immédiats.",
          "Dans les deux cas, le correcteur valorise la clarté de la problématique, la progression logique du raisonnement, et l'usage précis (non plaqué) de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Soit la suite (u_n) définie par u_0 = 2 et u_(n+1) = 0,5 × u_n + 3. Montrer que la suite (v_n) définie par v_n = u_n − 6 est géométrique de raison 0,5, puis exprimer u_n en fonction de n.",
          "Exercice 2 (7 points) : Soit f la fonction définie sur ℝ par f(x) = e^x − x − 1. Étudier le sens de variation de f, puis en déduire le signe de f(x) selon les valeurs de x.",
          "Exercice 3 (5 points) : Une urne contient 3 boules rouges et 5 boules bleues. On tire successivement deux boules sans remise. Calculer la probabilité de tirer deux boules rouges.",
        ],
        corrige: [
          "Exercice 1 : v_(n+1) = u_(n+1) − 6 = 0,5u_n + 3 − 6 = 0,5u_n − 3 = 0,5(u_n − 6) = 0,5 v_n, donc (v_n) est bien géométrique de raison 0,5 et v_0 = u_0 − 6 = −4. On obtient v_n = −4 × 0,5^n, donc u_n = 6 − 4 × 0,5^n.",
          "Exercice 2 : f'(x) = e^x − 1, qui s'annule en x = 0. f est décroissante sur ]−∞ ; 0] et croissante sur [0 ; +∞[. Le minimum est f(0) = 1 − 0 − 1 = 0, donc f(x) ≥ 0 pour tout x réel.",
          "Exercice 3 : P = (3/8) × (2/7) = 6/56 = 3/28.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « Dans quelle mesure la décolonisation a-t-elle transformé les relations internationales depuis 1945 ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir d'un ou deux documents fournis par l'enseignant sur un enjeu géopolitique contemporain, identifier les idées principales, confronter les points de vue si plusieurs documents, et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie structure la réponse en plusieurs axes (contexte de l'après-guerre, formes variées de la décolonisation, conséquences sur l'équilibre mondial et l'émergence de nouveaux acteurs) avec des exemples précis et datés.",
          "Partie 2 : le correcteur attend une analyse qui va au-delà de la paraphrase du document — il faut expliciter le point de vue de l'auteur ou de la source, et, si pertinent, souligner ses limites ou son contexte de production.",
        ],
      },
    ],
  },
  {
    slug: "brevet-blanc-2",
    titre: "Brevet blanc n°2",
    niveau: "3e",
    description:
      "Deuxième sujet d'entraînement type Brevet, avec des questions différentes en français, mathématiques et histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 2,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Dans un texte poétique de ton choix étudié en classe, relève une image (comparaison ou métaphore) et explique ce qu'elle évoque.",
          "Question 2 (grammaire, 10 points) : Identifie une proposition subordonnée dans une phrase du texte et précise sa fonction.",
          "Question 3 (interprétation, 10 points) : En t'appuyant sur le texte, explique ce que le poète cherche à faire ressentir au lecteur.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention aux accords dans le groupe nominal et aux terminaisons verbales homophones.",
          "Rédaction au choix (50 points) : soit la suite d'un texte narratif étudié en classe, soit un texte argumentatif sur l'importance de la lecture (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : une bonne réponse nomme la figure de style, cite le passage précis, et explique l'effet produit (sensation, sentiment, idée suggérée).",
          "Question 2 : il faut nommer le type de subordonnée (relative, conjonctive...) et sa fonction (complément, épithète, etc.), pas seulement la repérer.",
          "Question 3 : le correcteur valorise une réponse qui relie une intention de l'auteur à des procédés d'écriture précis relevés dans le texte.",
          "Dictée : erreurs fréquentes sur les accords des participes passés et les terminaisons -é/-er/-ez.",
          "Rédaction : cohérence narrative pour la suite de texte, ou argumentation structurée avec exemples pour le texte argumentatif.",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Calcul (20 points) : Calculer B = 3 × (4 − 7) + 5² et détailler les étapes en respectant les priorités opératoires.",
          "Exercice 2 — Géométrie (30 points) : Un rectangle a une longueur de 12 cm et une largeur de 7 cm. Calculer son périmètre puis son aire.",
          "Exercice 3 — Statistiques (25 points) : Voici une série de notes : 12, 15, 9, 18, 14, 11. Calculer la moyenne de la série.",
          "Exercice 4 — Problème (25 points) : Un article coûte 80 € et son prix augmente de 15 %. Calculer le nouveau prix.",
        ],
        corrige: [
          "Exercice 1 : B = 3 × (−3) + 25 = −9 + 25 = 16.",
          "Exercice 2 : Périmètre = 2 × (12 + 7) = 38 cm ; Aire = 12 × 7 = 84 cm².",
          "Exercice 3 : Moyenne = (12+15+9+18+14+11)/6 = 79/6 ≈ 13,17.",
          "Exercice 4 : une hausse de 15 % correspond à un coefficient multiplicateur de 1,15. Nouveau prix = 80 × 1,15 = 92 €.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique en quelques lignes ce qu'est la Première Guerre mondiale et cite au moins deux de ses conséquences.",
          "Question de connaissances (10 points) : Qu'est-ce que la mondialisation ? Donne un exemple concret de flux mondialisé.",
          "Étude de document (15 points) : à partir d'un document sur les espaces urbains dans le monde, identifie deux informations qu'il apporte.",
          "EMC (10 points) : Explique ce qu'est la laïcité et pourquoi ce principe est important dans la société française.",
        ],
        corrige: [
          "Réponse attendue : dater le conflit (1914-1918), citer des conséquences (bilan humain, redécoupage des frontières en Europe, tensions menant à la Seconde Guerre mondiale).",
          "Réponse attendue : définir la mondialisation comme l'intensification des échanges à l'échelle mondiale, et citer un exemple précis (marchandise, information, migration).",
          "Réponse attendue : identifier des informations explicites du document sans hors-sujet.",
          "Réponse attendue : définir la laïcité comme la séparation des Églises et de l'État garantissant la liberté de conscience et l'égalité de tous les citoyens.",
        ],
      },
    ],
  },
  {
    slug: "brevet-blanc-3",
    titre: "Brevet blanc n°3",
    niveau: "3e",
    description:
      "Troisième sujet d'entraînement type Brevet : théâtre en français, équations et géométrie en mathématiques, colonisation et valeurs de la République en histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 3,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Dans un extrait de pièce de théâtre étudié en classe, identifie le conflit entre deux personnages et explique son enjeu.",
          "Question 2 (grammaire, 10 points) : Relève une didascalie dans l'extrait et explique ce qu'elle apporte à la mise en scène.",
          "Question 3 (interprétation, 10 points) : Explique comment le dialogue permet de faire progresser l'action dans la scène choisie.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention aux accords du participe passé avec avoir et être.",
          "Rédaction au choix (50 points) : soit l'écriture d'un dialogue théâtral entre deux personnages en conflit, soit un texte argumentatif sur l'utilité du théâtre (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : il faut nommer les deux personnages, préciser l'objet du désaccord et son importance dans l'intrigue.",
          "Question 2 : une bonne réponse explique la fonction précise de la didascalie (indication de jeu, de ton, de déplacement...).",
          "Question 3 : le correcteur valorise une réponse qui montre comment les répliques créent une progression dramatique (tension, retournement...).",
          "Dictée : attention à l'accord du participe passé avec avoir (COD placé avant) et avec être (accord avec le sujet).",
          "Rédaction : pour le dialogue, respect des codes du théâtre (didascalies, réplique par personnage) ; pour l'argumentation, structure claire avec exemples.",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Équations (20 points) : Résoudre l'équation 3x + 5 = 20.",
          "Exercice 2 — Géométrie repérée (30 points) : Dans un repère, placer les points A(1;2) et B(4;6), puis calculer la longueur AB.",
          "Exercice 3 — Pourcentages (25 points) : Dans une classe de 25 élèves, 60 % pratiquent un sport. Combien d'élèves cela représente-t-il ?",
          "Exercice 4 — Problème (25 points) : Deux forfaits de téléphone : Forfait A = 10 € + 0,05 €/minute ; Forfait B = 20 € fixe. À partir de combien de minutes le forfait B devient-il plus avantageux ?",
        ],
        corrige: [
          "Exercice 1 : 3x = 20 − 5 = 15, donc x = 5.",
          "Exercice 2 : AB = √((4−1)² + (6−2)²) = √(9+16) = √25 = 5.",
          "Exercice 3 : 60 % de 25 = 0,6 × 25 = 15 élèves.",
          "Exercice 4 : on cherche x tel que 10 + 0,05x > 20, soit 0,05x > 10, donc x > 200 minutes : à partir de 201 minutes, le forfait B est plus avantageux.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique ce qu'est la colonisation et cite un exemple de colonie française.",
          "Question de connaissances (10 points) : Qu'est-ce que le développement durable ? Cite ses trois piliers.",
          "Étude de document (15 points) : à partir d'un document sur les inégalités face au développement dans le monde, identifie deux informations qu'il apporte.",
          "EMC (10 points) : Cite trois valeurs de la République française et explique brièvement l'une d'entre elles.",
        ],
        corrige: [
          "Réponse attendue : définir la colonisation comme la domination d'un territoire par une puissance étrangère, avec un exemple précis (Algérie, Indochine...).",
          "Réponse attendue : citer les piliers économique, social et environnemental, avec une brève explication de leur articulation.",
          "Réponse attendue : identifier des informations explicites du document sans hors-sujet.",
          "Réponse attendue : Liberté, Égalité, Fraternité (ou laïcité) avec une explication correcte d'au moins une valeur.",
        ],
      },
    ],
  },
  {
    slug: "brevet-blanc-4",
    titre: "Brevet blanc n°4",
    niveau: "3e",
    description:
      "Quatrième sujet d'entraînement type Brevet : texte autobiographique en français, calcul littéral et volumes en mathématiques, mémoire de la Révolution et mondialisation en histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 4,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Dans un extrait autobiographique étudié en classe, identifie un souvenir marquant raconté par le narrateur.",
          "Question 2 (grammaire, 10 points) : Relève une phrase à la première personne et explique l'effet produit par ce choix d'énonciation.",
          "Question 3 (interprétation, 10 points) : Explique ce que ce souvenir révèle de la personnalité ou de l'évolution du narrateur.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention aux temps du récit (imparfait/passé simple).",
          "Rédaction au choix (50 points) : soit le récit d'un souvenir personnel marquant, soit un texte de réflexion sur l'importance de la mémoire (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : une bonne réponse résume précisément l'épisode raconté, avec des détails du texte.",
          "Question 2 : il faut expliquer que la première personne crée une proximité avec le lecteur et engage la subjectivité du narrateur.",
          "Question 3 : le correcteur valorise une réponse qui relie le souvenir à une évolution ou une prise de conscience du narrateur.",
          "Dictée : attention à l'alternance imparfait (description, habitude) / passé simple (action ponctuelle) dans le récit.",
          "Rédaction : pour le récit personnel, respect de la cohérence temporelle ; pour la réflexion, structure argumentée avec exemples précis.",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Calcul littéral (20 points) : Développer et réduire l'expression E = 3(x + 2) − 2(x − 1).",
          "Exercice 2 — Volumes (30 points) : Calculer le volume d'un cube d'arête 5 cm.",
          "Exercice 3 — Proportionnalité (25 points) : Un robinet remplit 40 L en 8 minutes. Combien de litres remplit-il en 20 minutes, à débit constant ?",
          "Exercice 4 — Problème (25 points) : Un vélo coûte 250 € avec une remise de 12 %. Calculer le prix payé.",
        ],
        corrige: [
          "Exercice 1 : E = 3x + 6 − 2x + 2 = x + 8.",
          "Exercice 2 : Volume = 5³ = 125 cm³.",
          "Exercice 3 : le débit est 40/8 = 5 L/min, donc en 20 minutes : 5 × 20 = 100 L.",
          "Exercice 4 : une remise de 12 % correspond à un coefficient de 0,88. Prix payé = 250 × 0,88 = 220 €.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique en quelques lignes ce qu'est la Révolution française et cite un événement clé.",
          "Question de connaissances (10 points) : Qu'est-ce qu'une firme transnationale ? Donne un exemple.",
          "Étude de document (15 points) : à partir d'un document sur les flux migratoires dans le monde, identifie deux informations qu'il apporte.",
          "EMC (10 points) : Explique ce qu'est la justice et le rôle d'un tribunal dans une démocratie.",
        ],
        corrige: [
          "Réponse attendue : dater la Révolution (1789), citer un événement (prise de la Bastille, Déclaration des droits de l'homme...).",
          "Réponse attendue : définir la firme transnationale comme une entreprise implantée dans plusieurs pays, avec un exemple concret.",
          "Réponse attendue : identifier des informations explicites du document sans hors-sujet.",
          "Réponse attendue : expliquer que la justice tranche les conflits selon la loi et garantit les droits des citoyens, indépendamment du pouvoir politique.",
        ],
      },
    ],
  },
  {
    slug: "brevet-blanc-5",
    titre: "Brevet blanc n°5",
    niveau: "3e",
    description:
      "Cinquième sujet d'entraînement type Brevet : compréhension d'un roman en français, nombres relatifs et Thalès en mathématiques, guerre froide et aires urbaines en histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 5,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Dans un roman étudié en classe, décris la situation initiale d'un personnage principal.",
          "Question 2 (grammaire, 10 points) : Dans une phrase du texte, identifie un complément circonstanciel et précise ce qu'il exprime (temps, lieu, manière...).",
          "Question 3 (interprétation, 10 points) : Explique un obstacle rencontré par le personnage principal et comment il tente de le surmonter.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention aux homophones grammaticaux (ce/se, ces/ses, on/ont).",
          "Rédaction au choix (50 points) : soit l'écriture de la suite du roman étudié, soit un texte de réflexion sur le courage (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : une bonne réponse mentionne le contexte, le lieu et la situation du personnage en début d'histoire.",
          "Question 2 : il faut nommer le complément et préciser précisément ce qu'il exprime.",
          "Question 3 : le correcteur valorise une réponse précise sur la nature de l'obstacle et la stratégie du personnage.",
          "Dictée : les homophones grammaticaux sont une source d'erreur fréquente ; il faut vérifier par substitution (ce/cela, se/lui-même...).",
          "Rédaction : cohérence avec l'univers du roman pour la suite ; structure argumentée avec exemples pour la réflexion.",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Nombres relatifs (20 points) : Calculer C = −7 + 12 − 4 − (−3).",
          "Exercice 2 — Théorème de Thalès (30 points) : Dans un triangle ABC, une droite parallèle à (BC) coupe (AB) en D et (AC) en E, avec AD = 3, AB = 6, AC = 8. Calculer AE.",
          "Exercice 3 — Statistiques (25 points) : Une série de tailles (en cm) : 150, 155, 148, 160, 152. Calculer l'étendue de cette série.",
          "Exercice 4 — Problème (25 points) : Un trajet en train coûte 45 € plein tarif, avec une réduction de 25 % pour les moins de 26 ans. Calculer le prix réduit.",
        ],
        corrige: [
          "Exercice 1 : C = −7 + 12 − 4 + 3 = 4.",
          "Exercice 2 : d'après Thalès, AD/AB = AE/AC, donc 3/6 = AE/8, donc AE = 8 × 3/6 = 4.",
          "Exercice 3 : étendue = valeur max − valeur min = 160 − 148 = 12 cm.",
          "Exercice 4 : une réduction de 25 % correspond à un coefficient de 0,75. Prix réduit = 45 × 0,75 = 33,75 €.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique ce qu'est la guerre froide et cite les deux blocs qui s'opposent.",
          "Question de connaissances (10 points) : Qu'est-ce qu'une aire urbaine ? Donne un exemple français.",
          "Étude de document (15 points) : à partir d'un document sur l'étalement urbain, identifie deux informations qu'il apporte.",
          "EMC (10 points) : Explique ce qu'est la liberté de la presse et pourquoi elle est essentielle en démocratie.",
        ],
        corrige: [
          "Réponse attendue : définir la guerre froide comme l'opposition entre le bloc de l'Ouest (États-Unis) et le bloc de l'Est (URSS) après 1945, sans conflit armé direct entre les deux.",
          "Réponse attendue : définir l'aire urbaine comme une ville-centre et sa périphérie liées par les déplacements domicile-travail, avec un exemple (Paris, Lyon...).",
          "Réponse attendue : identifier des informations explicites du document sans hors-sujet.",
          "Réponse attendue : expliquer que la liberté de la presse permet d'informer les citoyens et de contrôler le pouvoir, condition essentielle du débat démocratique.",
        ],
      },
    ],
  },
  {
    slug: "brevet-blanc-6",
    titre: "Brevet blanc n°6",
    niveau: "3e",
    description:
      "Sixième sujet d'entraînement type Brevet : texte de science-fiction en français, fonctions linéaires et trigonométrie en mathématiques, Ve République et laïcité en histoire-géographie-EMC.",
    dureeTotale: "Environ 5h30 au total (à répartir sur plusieurs séances)",
    pack: "brevet",
    numero: 6,
    epreuves: [
      {
        matiere: "Français",
        duree: "3h",
        bareme: "100 points",
        sujet: [
          "Question 1 (compréhension, 10 points) : Dans un texte de science-fiction ou d'anticipation étudié en classe, décris le monde imaginé par l'auteur.",
          "Question 2 (grammaire, 10 points) : Relève une phrase au futur ou au conditionnel et explique sa valeur (hypothèse, prévision...).",
          "Question 3 (interprétation, 10 points) : Explique quel message ou quelle mise en garde l'auteur adresse au lecteur à travers ce monde imaginaire.",
          "Dictée (20 points) : Un texte d'une quinzaine de lignes est dicté ; attention aux accords dans les groupes nominaux complexes.",
          "Rédaction au choix (50 points) : soit l'écriture d'un texte d'anticipation imaginant le monde dans 50 ans, soit un texte de réflexion sur le progrès technique (250 mots minimum).",
        ],
        corrige: [
          "Question 1 : une bonne réponse décrit précisément les éléments qui rendent ce monde différent du nôtre (technologie, société, règles...).",
          "Question 2 : il faut identifier le temps/mode employé et expliquer sa valeur précise dans la phrase.",
          "Question 3 : le correcteur valorise une réponse qui relie les éléments du récit à une critique ou un questionnement de l'auteur sur notre société actuelle.",
          "Dictée : attention aux accords en genre et en nombre dans les groupes nominaux avec plusieurs adjectifs.",
          "Rédaction : cohérence et originalité pour le texte d'anticipation ; structure argumentée et nuancée pour la réflexion.",
        ],
      },
      {
        matiere: "Mathématiques",
        duree: "2h",
        bareme: "100 points",
        sujet: [
          "Exercice 1 — Fonctions linéaires (20 points) : Soit f(x) = 4x. Calculer f(3) et déterminer le nombre x tel que f(x) = 20.",
          "Exercice 2 — Trigonométrie (30 points) : Dans un triangle rectangle en A, AB = 5 cm et l'angle en B mesure 40°. Calculer la longueur AC (arrondie au dixième).",
          "Exercice 3 — Statistiques (25 points) : Un jeu de dé à 6 faces est lancé. Quelle est la probabilité d'obtenir un nombre pair ?",
          "Exercice 4 — Problème (25 points) : Une location de vélo coûte 5 € de forfait + 2 € par heure. Écrire l'expression du prix p(x) en fonction du nombre d'heures x, puis calculer p(4).",
        ],
        corrige: [
          "Exercice 1 : f(3) = 4 × 3 = 12. Pour f(x) = 20 : 4x = 20, donc x = 5.",
          "Exercice 2 : dans le triangle rectangle en A, tan(B) = AC/AB, donc AC = AB × tan(40°) ≈ 5 × 0,839 ≈ 4,2 cm.",
          "Exercice 3 : les issues paires sont 2, 4, 6 sur 6 possibles, donc la probabilité est 3/6 = 1/2.",
          "Exercice 4 : p(x) = 5 + 2x. Pour x = 4 : p(4) = 5 + 2×4 = 13 €.",
        ],
      },
      {
        matiere: "Histoire-Géographie-EMC",
        duree: "2h",
        bareme: "50 points",
        sujet: [
          "Question de connaissances (15 points) : Explique ce qu'est la Ve République et cite l'année de sa fondation.",
          "Question de connaissances (10 points) : Qu'est-ce qu'une mer ou un océan stratégique ? Donne un exemple d'enjeu maritime.",
          "Étude de document (15 points) : à partir d'un document sur les espaces maritimes mondiaux, identifie deux informations qu'il apporte.",
          "EMC (10 points) : Explique ce qu'est une discrimination et donne un exemple de moyen de la combattre.",
        ],
        corrige: [
          "Réponse attendue : dater la Ve République (1958), fondée par le général de Gaulle, avec un régime présidentiel renforcé.",
          "Réponse attendue : expliquer qu'un espace maritime peut être stratégique pour le commerce, les ressources ou la sécurité, avec un exemple précis (détroit, zone économique exclusive...).",
          "Réponse attendue : identifier des informations explicites du document sans hors-sujet.",
          "Réponse attendue : définir la discrimination comme un traitement inégal fondé sur un critère illégitime (origine, sexe, handicap...), et citer un moyen de lutte (loi, association, éducation...).",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-2",
    titre: "Bac blanc n°2",
    niveau: "terminale",
    description:
      "Deuxième sujet d'entraînement type Bac, avec des sujets différents en philosophie, mathématiques (spécialité, exemple) et histoire-géographie.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 2,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Le bonheur dépend-il de nous ? »",
          "Sujet 2 : « L'art nous éloigne-t-il du réel ? »",
          "Consignes : introduction avec problématisation, développement structuré et argumenté avec exemples ou références philosophiques, conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : opposer une conception stoïcienne (le bonheur dépend de notre jugement sur les choses) à une conception qui souligne le poids des circonstances extérieures (fortune, santé, relations).",
          "Pour le sujet 2, une piste possible : distinguer l'art comme évasion du réel (mimésis critiquée par Platon) et l'art comme révélation d'une vérité sur le réel (une œuvre peut nous faire voir le monde autrement).",
          "Le correcteur valorise la clarté de la problématique, la progression logique, et l'usage précis de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Soit f(x) = e^(2x) − 3. Étudier les variations de f sur ℝ et déterminer l'équation de la tangente à la courbe au point d'abscisse 0.",
          "Exercice 2 (7 points) : Une urne contient 4 boules blanches et 6 boules noires. On tire une boule, on note sa couleur, on la remet, puis on tire à nouveau. Calculer la probabilité d'obtenir deux boules de couleurs différentes.",
          "Exercice 3 (5 points) : Soit (u_n) une suite arithmétique de premier terme u_0 = 5 et de raison r = 3. Calculer u_10 et la somme S = u_0 + u_1 + ... + u_10.",
        ],
        corrige: [
          "Exercice 1 : f'(x) = 2e^(2x) > 0 pour tout x, donc f est strictement croissante sur ℝ. f(0) = 1 − 3 = −2 et f'(0) = 2, donc la tangente a pour équation y = 2x − 2.",
          "Exercice 2 : P(différentes) = P(blanche puis noire) + P(noire puis blanche) = (4/10 × 6/10) + (6/10 × 4/10) = 24/100 + 24/100 = 48/100 = 0,48.",
          "Exercice 3 : u_10 = u_0 + 10r = 5 + 30 = 35. S = 11 × (u_0 + u_10)/2 = 11 × 40/2 = 220.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « Dans quelle mesure les États-Unis exercent-ils une puissance mondiale depuis 1945 ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir de documents sur la construction européenne, identifier les idées principales et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie distingue plusieurs formes de puissance (militaire, économique, culturelle, diplomatique) et nuance avec les limites actuelles de cette puissance (concurrence chinoise, contestations internes).",
          "Partie 2 : le correcteur attend une analyse qui explicite le point de vue de la source et souligne, si pertinent, ses limites ou son contexte de production.",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-3",
    titre: "Bac blanc n°3",
    niveau: "terminale",
    description:
      "Troisième sujet d'entraînement type Bac : le travail et la technique en philosophie, fonctions logarithme et géométrie dans l'espace en mathématiques, l'Afrique et la France dans le monde en histoire-géographie.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 3,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Le travail nous libère-t-il ? »",
          "Sujet 2 : « La technique peut-elle tout résoudre ? »",
          "Consignes : introduction avec problématisation, développement structuré et argumenté avec exemples ou références philosophiques, conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : opposer le travail comme aliénation (Marx) au travail comme moyen d'émancipation et de reconnaissance sociale.",
          "Pour le sujet 2, une piste possible : interroger la puissance de la technique moderne tout en montrant ses limites face aux problèmes proprement politiques ou moraux qu'elle ne peut trancher seule.",
          "Le correcteur valorise la clarté de la problématique, la progression logique, et l'usage précis de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Résoudre dans ℝ l'équation ln(x + 1) = 2, en précisant les conditions d'existence.",
          "Exercice 2 (7 points) : ABCDEFGH est un cube d'arête 4 cm. Calculer la longueur de la diagonale [AG] du cube.",
          "Exercice 3 (5 points) : Soit (u_n) géométrique de premier terme u_0 = 3 et de raison q = 2. Calculer u_5.",
        ],
        corrige: [
          "Exercice 1 : condition x + 1 > 0, soit x > −1. ln(x+1) = 2 ⟺ x + 1 = e², donc x = e² − 1.",
          "Exercice 2 : la diagonale d'un cube d'arête a mesure a√3, donc AG = 4√3 ≈ 6,9 cm.",
          "Exercice 3 : u_5 = u_0 × q^5 = 3 × 32 = 96.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « Quels sont les défis du développement en Afrique aujourd'hui ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir de documents sur la place de la France dans le monde, identifier les idées principales et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie distingue les dynamiques positives (croissance, démographie, urbanisation) des défis persistants (inégalités, gouvernance, dépendance économique), avec des exemples précis.",
          "Partie 2 : le correcteur attend une analyse qui va au-delà de la paraphrase, en expliquant le point de vue de la source et ses limites éventuelles.",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-4",
    titre: "Bac blanc n°4",
    niveau: "terminale",
    description:
      "Quatrième sujet d'entraînement type Bac : la conscience et l'inconscient en philosophie, nombres complexes et suites en mathématiques, la Russie et les mers/océans en histoire-géographie.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 4,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Puis-je me connaître moi-même ? »",
          "Sujet 2 : « L'inconscient est-il une excuse ? »",
          "Consignes : introduction avec problématisation, développement structuré et argumenté avec exemples ou références philosophiques, conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : interroger les limites de l'introspection (illusion de transparence à soi) à la lumière de l'hypothèse freudienne de l'inconscient.",
          "Pour le sujet 2, une piste possible : distinguer expliquer un acte par l'inconscient et l'excuser moralement — la responsabilité peut subsister même si les causes sont en partie inconscientes.",
          "Le correcteur valorise la clarté de la problématique, la progression logique, et l'usage précis de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Soit z = 3 + 4i. Calculer le module de z et donner sa forme trigonométrique (valeur approchée de l'argument acceptée).",
          "Exercice 2 (7 points) : Soit (u_n) définie par u_0 = 1 et u_(n+1) = u_n + 2n + 1. Calculer u_1, u_2 et u_3, et conjecturer une formule explicite de u_n.",
          "Exercice 3 (5 points) : Résoudre dans ℂ l'équation z² + 4 = 0.",
        ],
        corrige: [
          "Exercice 1 : |z| = √(3² + 4²) = √25 = 5. L'argument θ vérifie cos θ = 3/5, sin θ = 4/5, donc θ ≈ 0,93 rad.",
          "Exercice 2 : u_1 = 1 + 1 = 2, u_2 = 2 + 3 = 5, u_3 = 5 + 5 = 10. On conjecture u_n = n² + 1 (à vérifier par récurrence).",
          "Exercice 3 : z² = −4, donc z = 2i ou z = −2i.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « La Russie est-elle encore une grande puissance aujourd'hui ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir de documents sur les mers et océans comme enjeu stratégique, identifier les idées principales et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie distingue les atouts de la puissance russe (ressources, arme nucléaire, siège à l'ONU) et ses fragilités (économie moins diversifiée, isolement diplomatique croissant).",
          "Partie 2 : le correcteur attend une analyse qui explicite les enjeux (ressources, routes maritimes, zones économiques exclusives) et le point de vue de la source.",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-5",
    titre: "Bac blanc n°5",
    niveau: "terminale",
    description:
      "Cinquième sujet d'entraînement type Bac : la justice et l'État en philosophie, intégrales et probabilités en mathématiques, le Moyen-Orient et la Chine en histoire-géographie.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 5,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Faut-il obéir aux lois injustes ? »",
          "Sujet 2 : « L'État est-il l'ennemi de la liberté individuelle ? »",
          "Consignes : introduction avec problématisation, développement structuré et argumenté avec exemples ou références philosophiques, conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : opposer le devoir d'obéissance nécessaire à l'ordre social et le droit (voire le devoir) de désobéissance civile face à une loi manifestement injuste.",
          "Pour le sujet 2, une piste possible : distinguer une conception de l'État comme contrainte (Hobbes, nécessaire pour sortir de l'état de nature) et une conception où l'État est la condition d'exercice d'une liberté effective (Rousseau).",
          "Le correcteur valorise la clarté de la problématique, la progression logique, et l'usage précis de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Calculer l'intégrale I = ∫ de 0 à 2 de (3x² + 1) dx.",
          "Exercice 2 (7 points) : Une variable aléatoire X suit une loi binomiale de paramètres n = 10 et p = 0,3. Calculer l'espérance E(X).",
          "Exercice 3 (5 points) : Deux événements A et B vérifient P(A) = 0,4, P(B) = 0,5 et P(A∩B) = 0,2. Calculer P(A∪B).",
        ],
        corrige: [
          "Exercice 1 : une primitive de 3x²+1 est x³+x. I = [x³+x] de 0 à 2 = (8+2) − 0 = 10.",
          "Exercice 2 : E(X) = n × p = 10 × 0,3 = 3.",
          "Exercice 3 : P(A∪B) = P(A) + P(B) − P(A∩B) = 0,4 + 0,5 − 0,2 = 0,7.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « Pourquoi le Moyen-Orient est-il une zone de tensions récurrentes depuis 1945 ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir de documents sur la puissance chinoise, identifier les idées principales et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie mobilise plusieurs facteurs (ressources pétrolières, rivalités religieuses et politiques, ingérences extérieures, question israélo-palestinienne) avec des exemples datés.",
          "Partie 2 : le correcteur attend une analyse des différentes dimensions de la puissance chinoise (économique, militaire, technologique, diplomatique) et un regard critique sur la source.",
        ],
      },
    ],
  },
  {
    slug: "bac-blanc-6",
    titre: "Bac blanc n°6",
    niveau: "terminale",
    description:
      "Sixième sujet d'entraînement type Bac : le langage et la vérité en philosophie, dérivation et dénombrement en mathématiques, mondialisation et développement durable en histoire-géographie.",
    dureeTotale: "Environ 8h au total (à répartir sur plusieurs séances)",
    pack: "bac",
    numero: 6,
    epreuves: [
      {
        matiere: "Philosophie",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Sujet de dissertation au choix (l'élève ne traite qu'un seul sujet) :",
          "Sujet 1 : « Le langage trahit-il toujours la pensée ? »",
          "Sujet 2 : « Peut-on être certain de détenir la vérité ? »",
          "Consignes : introduction avec problématisation, développement structuré et argumenté avec exemples ou références philosophiques, conclusion qui répond à la problématique.",
        ],
        corrige: [
          "Pour le sujet 1, une piste possible : interroger l'écart entre pensée et mots (l'inexprimable, l'approximation du langage) tout en reconnaissant que le langage est aussi ce qui rend la pensée communicable et structurée.",
          "Pour le sujet 2, une piste possible : distinguer certitude subjective et vérité objective, en s'appuyant sur le doute méthodique cartésien comme méthode de recherche de la vérité.",
          "Le correcteur valorise la clarté de la problématique, la progression logique, et l'usage précis de références philosophiques.",
        ],
      },
      {
        matiere: "Mathématiques (exemple spécialité)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Exercice 1 (8 points) : Soit f(x) = x³ − 3x. Calculer f'(x) et étudier le signe de f'(x) pour déterminer les variations de f.",
          "Exercice 2 (7 points) : Un code PIN est composé de 4 chiffres (de 0 à 9), avec répétition possible. Combien de codes différents peut-on former ?",
          "Exercice 3 (5 points) : Une classe de 30 élèves doit élire 2 délégués parmi 5 candidats. Combien de binômes de délégués sont possibles (sans distinction de rôle) ?",
        ],
        corrige: [
          "Exercice 1 : f'(x) = 3x² − 3 = 3(x²−1) = 3(x−1)(x+1). f' est négative sur ]−1;1[ et positive ailleurs : f est donc décroissante sur [−1;1] et croissante sur ]−∞;−1] et [1;+∞[.",
          "Exercice 2 : chaque chiffre a 10 possibilités indépendantes, donc 10⁴ = 10 000 codes possibles.",
          "Exercice 3 : il s'agit d'une combinaison de 2 parmi 5 : C(5,2) = 10 binômes possibles.",
        ],
      },
      {
        matiere: "Histoire-Géographie (tronc commun)",
        duree: "4h",
        bareme: "20 points",
        sujet: [
          "Partie 1 — Question problématisée (10 points) : « Quels acteurs portent la mondialisation aujourd'hui ? »",
          "Partie 2 — Étude critique d'un ou deux documents (10 points) : à partir de documents sur le développement durable, identifier les idées principales et discuter leurs limites.",
        ],
        corrige: [
          "Partie 1 : une bonne copie distingue plusieurs types d'acteurs (firmes transnationales, États, organisations internationales, ONG, sociétés civiles) et leurs rôles respectifs dans la mondialisation.",
          "Partie 2 : le correcteur attend une analyse qui articule les trois piliers du développement durable et interroge les limites ou tensions présentées dans le document (par exemple entre croissance économique et préservation environnementale).",
        ],
      },
    ],
  },
];

export function examBySlug(slug: string) {
  return EXAMS.find((e) => e.slug === slug);
}
