export interface EvaluationQuestion {
  enonce: string;
  choix: string[];
  reponse: number;
  explication: string;
}

export interface EvaluationMatiere {
  matiere: string;
  questions: EvaluationQuestion[];
}

export interface EvaluationTrimestrielle {
  slug: string;
  niveau: string;
  trimestre: 1 | 2 | 3;
  titre: string;
  description: string;
  matieres: EvaluationMatiere[];
}

export const EVALUATIONS: EvaluationTrimestrielle[] = [
  {
    slug: "cp-trimestre-1",
    niveau: "cp",
    trimestre: 1,
    titre: "Évaluation trimestrielle — CP — Trimestre 1",
    description: "Bilan du premier trimestre : premiers sons, nombres jusqu'à 20, repères dans le temps.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel mot contient le son [ch] ?",
          choix: ["Chat", "Robot", "Ami", "Lune"],
          reponse: 0,
          explication: "« Chat » contient le son [ch].",
        },
        {
          enonce: "Quel mot contient le son [ou] ?",
          choix: ["Loup", "Chat", "Robot", "Ami"],
          reponse: 0,
          explication: "« Loup » contient le son [ou].",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Quel nombre vient après 14 ?",
          choix: ["13", "15", "20", "10"],
          reponse: 1,
          explication: "Après 14 vient 15.",
        },
        {
          enonce: "Quel est le plus grand : 9 ou 17 ?",
          choix: ["9", "17", "Égaux", "Impossible"],
          reponse: 1,
          explication: "17 est plus grand que 9.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Combien y a-t-il de jours dans une semaine ?",
          choix: ["5", "6", "7", "8"],
          reponse: 2,
          explication: "Il y a 7 jours dans une semaine.",
        },
        {
          enonce: "Quel jour vient après lundi ?",
          choix: ["Dimanche", "Mardi", "Mercredi", "Samedi"],
          reponse: 1,
          explication: "Après lundi vient mardi.",
        }
        ],
      }
    ],
  },
  {
    slug: "cp-trimestre-2",
    niveau: "cp",
    trimestre: 2,
    titre: "Évaluation trimestrielle — CP — Trimestre 2",
    description: "Bilan du deuxième trimestre : nouveaux sons, nombres jusqu'à 100, les cinq sens.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel mot contient le son [on] ?",
          choix: ["Maison", "Chat", "Ami", "Robot"],
          reponse: 0,
          explication: "« Maison » contient le son [on].",
        },
        {
          enonce: "Quel mot contient le son [oi] ?",
          choix: ["Roi", "Chat", "Ami", "Lune"],
          reponse: 0,
          explication: "« Roi » contient le son [oi].",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien de dizaines y a-t-il dans 60 ?",
          choix: ["5", "6", "7", "60"],
          reponse: 1,
          explication: "60 est composé de 6 dizaines.",
        },
        {
          enonce: "Quel nombre vient juste avant 50 ?",
          choix: ["48", "49", "51", "45"],
          reponse: 1,
          explication: "Avant 50 vient 49.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Quel organe utilise-t-on pour voir ?",
          choix: ["Le nez", "Les yeux", "Les oreilles", "La langue"],
          reponse: 1,
          explication: "Les yeux permettent de voir.",
        },
        {
          enonce: "Quel organe utilise-t-on pour entendre ?",
          choix: ["Les yeux", "Les oreilles", "Le nez", "La langue"],
          reponse: 1,
          explication: "Les oreilles permettent d'entendre.",
        }
        ],
      }
    ],
  },
  {
    slug: "cp-trimestre-3",
    niveau: "cp",
    trimestre: 3,
    titre: "Évaluation trimestrielle — CP — Trimestre 3",
    description: "Bilan de fin d'année : sons complexes, addition simple, bilan général.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel mot contient le son [gn] ?",
          choix: ["Montagne", "Chat", "Ami", "Robot"],
          reponse: 0,
          explication: "« Montagne » contient le son [gn].",
        },
        {
          enonce: "Quel mot contient le son [j] ?",
          choix: ["Jardin", "Chat", "Robot", "Ami"],
          reponse: 0,
          explication: "« Jardin » commence par le son [j].",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 4 + 3 ?",
          choix: ["6", "7", "8", "5"],
          reponse: 1,
          explication: "4 + 3 = 7.",
        },
        {
          enonce: "Combien font 5 + 5 ?",
          choix: ["9", "10", "11", "8"],
          reponse: 1,
          explication: "5 + 5 = 10.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Combien y a-t-il de sens principaux ?",
          choix: ["3", "4", "5", "6"],
          reponse: 2,
          explication: "Il y a cinq sens principaux.",
        },
        {
          enonce: "Quel organe permet de sentir les odeurs ?",
          choix: ["Les yeux", "Le nez", "Les oreilles", "La langue"],
          reponse: 1,
          explication: "Le nez est l'organe de l'odorat.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce1-trimestre-1",
    niveau: "ce1",
    trimestre: 1,
    titre: "Évaluation trimestrielle — CE1 — Trimestre 1",
    description: "Bilan du premier trimestre : le pluriel des noms, l'addition posée, les saisons.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel est le pluriel de « un chat » ?",
          choix: ["Un chats", "Des chat", "Des chats", "Les chate"],
          reponse: 2,
          explication: "On ajoute -s : des chats.",
        },
        {
          enonce: "Quel mot ne change pas au pluriel ?",
          choix: ["Table", "Nez", "Ballon", "Fleur"],
          reponse: 1,
          explication: "« Nez » se termine déjà par -z, il reste identique.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 15 + 12 ?",
          choix: ["25", "26", "27", "28"],
          reponse: 2,
          explication: "15 + 12 = 27.",
        },
        {
          enonce: "Dans une addition posée, par quelle colonne commence-t-on ?",
          choix: ["Les dizaines", "Les unités", "Les centaines", "Peu importe"],
          reponse: 1,
          explication: "On commence toujours par les unités.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Combien y a-t-il de saisons dans une année ?",
          choix: ["2", "3", "4", "5"],
          reponse: 2,
          explication: "Il y a 4 saisons dans une année.",
        },
        {
          enonce: "Quelle saison vient après l'hiver ?",
          choix: ["L'été", "Le printemps", "L'automne", "Aucune"],
          reponse: 1,
          explication: "Après l'hiver vient le printemps.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce1-trimestre-2",
    niveau: "ce1",
    trimestre: 2,
    titre: "Évaluation trimestrielle — CE1 — Trimestre 2",
    description: "Bilan du deuxième trimestre : approfondissement du pluriel, additions, saisons.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel est le pluriel de « un bateau » ?",
          choix: ["Des bateaus", "Des bateaux", "Un bateaux", "Les bateau"],
          reponse: 1,
          explication: "Les mots en -eau prennent un -x au pluriel.",
        },
        {
          enonce: "Quel est le pluriel de « une souris » ?",
          choix: ["Des souris", "Des sourisse", "Un souris", "Des souriss"],
          reponse: 0,
          explication: "« Souris » se termine déjà par -s, il ne change pas.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 28 + 15 ?",
          choix: ["41", "42", "43", "44"],
          reponse: 2,
          explication: "28 + 15 = 43.",
        },
        {
          enonce: "Combien font 36 + 9 ?",
          choix: ["44", "45", "46", "43"],
          reponse: 1,
          explication: "36 + 9 = 45.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "En quelle saison fait-il le plus froid ?",
          choix: ["L'été", "L'automne", "L'hiver", "Le printemps"],
          reponse: 2,
          explication: "L'hiver est généralement la saison la plus froide.",
        },
        {
          enonce: "Quelle saison précède l'automne ?",
          choix: ["L'hiver", "Le printemps", "L'été", "Aucune"],
          reponse: 2,
          explication: "L'été précède l'automne.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce1-trimestre-3",
    niveau: "ce1",
    trimestre: 3,
    titre: "Évaluation trimestrielle — CE1 — Trimestre 3",
    description: "Bilan de fin d'année : bilan général grammaire, calcul et repères temporels.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quel est le pluriel de « un cheval » ? (cas particulier)",
          choix: ["Des chevals", "Des chevaux", "Un chevaux", "Les cheval"],
          reponse: 1,
          explication: "« Cheval » a un pluriel particulier : chevaux.",
        },
        {
          enonce: "Quel mot est déjà au pluriel ?",
          choix: ["Ballon", "Ballons", "Ballonne", "Ballonnet"],
          reponse: 1,
          explication: "« Ballons » est au pluriel, avec le -s final.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 45 + 27 ?",
          choix: ["70", "71", "72", "73"],
          reponse: 2,
          explication: "45 + 27 = 72.",
        },
        {
          enonce: "Combien font 19 + 19 ?",
          choix: ["36", "37", "38", "39"],
          reponse: 2,
          explication: "19 + 19 = 38.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Combien de saisons connaît-on en une année complète ?",
          choix: ["2", "3", "4", "5"],
          reponse: 2,
          explication: "Une année compte 4 saisons.",
        },
        {
          enonce: "Quelle saison voit pousser le plus de fleurs ?",
          choix: ["L'hiver", "Le printemps", "L'automne", "Aucune"],
          reponse: 1,
          explication: "Le printemps est la saison où les fleurs poussent le plus.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce2-trimestre-1",
    niveau: "ce2",
    trimestre: 1,
    titre: "Évaluation trimestrielle — CE2 — Trimestre 1",
    description: "Bilan du premier trimestre : verbe et sujet, la multiplication, états de la matière.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Dans « Le chien court vite », quel est le verbe ?",
          choix: ["Le", "Chien", "Court", "Vite"],
          reponse: 2,
          explication: "« Court » est le verbe conjugué.",
        },
        {
          enonce: "Comment trouve-t-on le sujet d'un verbe ?",
          choix: ["En devinant", "En posant « qui est-ce qui fait l'action ? »", "Impossible", "En regardant la fin"],
          reponse: 1,
          explication: "On pose la question « qui est-ce qui fait l'action ? ».",
        },
        {
          enonce: "Dans « Les enfants jouent dans le jardin », quel est le sujet ?",
          choix: ["Jouent", "Les enfants", "Dans", "Le jardin"],
          reponse: 1,
          explication: "« Les enfants » est celui qui fait l'action de jouer.",
        },
        {
          enonce: "Un nom peut-il être sujet d'un verbe ?",
          choix: ["Oui", "Non", "Jamais", "Seulement les noms propres"],
          reponse: 0,
          explication: "Un nom (commun ou propre) peut tout à fait être sujet d'un verbe.",
        },
        {
          enonce: "Dans « Le vent souffle fort », quel est le verbe ?",
          choix: ["Le", "Vent", "Souffle", "Fort"],
          reponse: 2,
          explication: "« Souffle » est le verbe conjugué de la phrase.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 3 × 6 ?",
          choix: ["16", "17", "18", "19"],
          reponse: 2,
          explication: "3 × 6 = 18.",
        },
        {
          enonce: "Que signifie 4 × 2 ?",
          choix: ["4 + 2", "4 + 4", "2 + 2", "4 - 2"],
          reponse: 1,
          explication: "4 × 2 signifie qu'on additionne 4 deux fois : 4 + 4.",
        },
        {
          enonce: "Combien font 5 × 4 ?",
          choix: ["16", "18", "20", "24"],
          reponse: 2,
          explication: "5 × 4 = 20.",
        },
        {
          enonce: "Combien font 2 × 9 ?",
          choix: ["16", "18", "20", "22"],
          reponse: 1,
          explication: "2 × 9 = 18.",
        },
        {
          enonce: "La multiplication est-elle une addition répétée ?",
          choix: ["Oui", "Non", "Jamais", "Seulement parfois"],
          reponse: 0,
          explication: "La multiplication correspond bien à une addition répétée du même nombre.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Quel est l'état de la glace ?",
          choix: ["Liquide", "Solide", "Gazeux", "Aucun"],
          reponse: 1,
          explication: "La glace est de l'eau à l'état solide.",
        },
        {
          enonce: "Quel est l'état de l'eau à température ambiante ?",
          choix: ["Solide", "Liquide", "Gazeux", "Aucun"],
          reponse: 1,
          explication: "À température ambiante, l'eau est liquide.",
        },
        {
          enonce: "Quel est l'état de la vapeur d'eau ?",
          choix: ["Solide", "Liquide", "Gazeux", "Aucun"],
          reponse: 2,
          explication: "La vapeur d'eau est à l'état gazeux, invisible à l'œil nu.",
        },
        {
          enonce: "Peut-on voir l'eau à l'état gazeux à l'œil nu ?",
          choix: ["Oui, toujours", "Non, la vapeur d'eau est invisible", "Seulement la nuit", "Jamais dans l'air"],
          reponse: 1,
          explication: "La vapeur d'eau, sous forme de gaz, est invisible à l'œil nu.",
        },
        {
          enonce: "Quel est l'état de l'eau dans une rivière ?",
          choix: ["Solide", "Liquide", "Gazeux", "Aucun"],
          reponse: 1,
          explication: "L'eau d'une rivière est à l'état liquide.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce2-trimestre-2",
    niveau: "ce2",
    trimestre: 2,
    titre: "Évaluation trimestrielle — CE2 — Trimestre 2",
    description: "Bilan du deuxième trimestre : accord sujet-verbe, tables de multiplication, changements d'état.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quelle phrase est correctement accordée ?",
          choix: ["Les chats dort.", "Les chats dorment.", "Le chats dorment.", "Les chat dort."],
          reponse: 1,
          explication: "« Les chats dorment » : le sujet pluriel impose un verbe au pluriel.",
        },
        {
          enonce: "Dans « Nous jouons dehors », quel est le sujet ?",
          choix: ["Nous", "Jouons", "Dehors", "Aucun"],
          reponse: 0,
          explication: "« Nous » est le sujet du verbe « jouons ».",
        },
        {
          enonce: "Dans « Les oiseaux chantent », le sujet est-il singulier ou pluriel ?",
          choix: ["Singulier", "Pluriel"],
          reponse: 1,
          explication: "« Les oiseaux » est un sujet pluriel.",
        },
        {
          enonce: "Un verbe pluriel se termine souvent par...",
          choix: ["-e", "-ent", "-s uniquement", "-ai"],
          reponse: 1,
          explication: "Beaucoup de verbes au pluriel se terminent par -ent à la 3e personne.",
        },
        {
          enonce: "Dans « Tu chantes bien », quel est le sujet ?",
          choix: ["Chantes", "Tu", "Bien", "Aucun"],
          reponse: 1,
          explication: "« Tu » est le sujet du verbe « chantes ».",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 5 × 6 ?",
          choix: ["25", "30", "35", "20"],
          reponse: 1,
          explication: "5 × 6 = 30.",
        },
        {
          enonce: "Combien font 7 × 3 ?",
          choix: ["18", "21", "24", "27"],
          reponse: 1,
          explication: "7 × 3 = 21.",
        },
        {
          enonce: "Combien font 6 × 5 ?",
          choix: ["25", "30", "35", "20"],
          reponse: 1,
          explication: "6 × 5 = 30.",
        },
        {
          enonce: "Combien font 8 × 2 ?",
          choix: ["14", "16", "18", "20"],
          reponse: 1,
          explication: "8 × 2 = 16.",
        },
        {
          enonce: "Combien font 9 × 3 ?",
          choix: ["18", "21", "24", "27"],
          reponse: 2,
          explication: "9 × 3 = 27.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Comment s'appelle le passage de l'eau liquide à l'eau solide ?",
          choix: ["La fusion", "La solidification", "L'évaporation", "La condensation"],
          reponse: 1,
          explication: "Ce passage s'appelle la solidification.",
        },
        {
          enonce: "À quelle température l'eau se transforme-t-elle en vapeur ?",
          choix: ["0°C", "50°C", "100°C", "10°C"],
          reponse: 2,
          explication: "L'eau se transforme en vapeur à partir de 100°C.",
        },
        {
          enonce: "Comment s'appelle le passage de l'eau liquide à la vapeur ?",
          choix: ["La fusion", "L'évaporation", "La solidification", "La condensation"],
          reponse: 1,
          explication: "Ce passage s'appelle l'évaporation (ou l'ébullition à 100°C).",
        },
        {
          enonce: "Comment s'appelle le passage de la glace à l'eau liquide ?",
          choix: ["La fusion", "La solidification", "L'évaporation", "La condensation"],
          reponse: 0,
          explication: "Ce passage s'appelle la fusion.",
        },
        {
          enonce: "À quelle température la glace fond-elle ?",
          choix: ["-10°C", "0°C", "50°C", "100°C"],
          reponse: 1,
          explication: "La glace fond à partir de 0°C.",
        }
        ],
      }
    ],
  },
  {
    slug: "ce2-trimestre-3",
    niveau: "ce2",
    trimestre: 3,
    titre: "Évaluation trimestrielle — CE2 — Trimestre 3",
    description: "Bilan de fin d'année : grammaire, multiplication et états de la matière (bilan complet).",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Dans « Les enfants chantent une chanson », quel est le sujet ?",
          choix: ["Une chanson", "Chantent", "Les enfants", "Chanson"],
          reponse: 2,
          explication: "« Les enfants » est celui qui fait l'action.",
        },
        {
          enonce: "Le verbe s'accorde toujours avec...",
          choix: ["Le COD", "Le sujet", "L'adjectif", "Rien"],
          reponse: 1,
          explication: "Le verbe s'accorde toujours avec son sujet.",
        },
        {
          enonce: "Dans « Le chat dort », quel est le sujet ?",
          choix: ["Le chat", "Dort", "Le", "Aucun"],
          reponse: 0,
          explication: "« Le chat » est celui qui fait l'action de dormir.",
        },
        {
          enonce: "Si le sujet est au pluriel, le verbe doit être...",
          choix: ["Au singulier", "Au pluriel", "À l'infinitif", "Cela n'a pas d'importance"],
          reponse: 1,
          explication: "Le verbe s'accorde en nombre avec son sujet : sujet pluriel, verbe pluriel.",
        },
        {
          enonce: "Dans « Les élèves écoutent la maîtresse », quel est le verbe ?",
          choix: ["Les élèves", "Écoutent", "La", "Maîtresse"],
          reponse: 1,
          explication: "« Écoutent » est le verbe conjugué de la phrase.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Combien font 8 × 4 ?",
          choix: ["28", "30", "32", "34"],
          reponse: 2,
          explication: "8 × 4 = 32.",
        },
        {
          enonce: "Combien font 9 × 2 ?",
          choix: ["16", "18", "20", "22"],
          reponse: 1,
          explication: "9 × 2 = 18.",
        },
        {
          enonce: "Combien font 7 × 4 ?",
          choix: ["24", "26", "28", "30"],
          reponse: 2,
          explication: "7 × 4 = 28.",
        },
        {
          enonce: "Combien font 6 × 6 ?",
          choix: ["30", "32", "34", "36"],
          reponse: 3,
          explication: "6 × 6 = 36.",
        },
        {
          enonce: "Combien font 10 × 5 ?",
          choix: ["40", "45", "50", "55"],
          reponse: 2,
          explication: "10 × 5 = 50.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Les changements d'état de l'eau sont-ils réversibles ?",
          choix: ["Oui", "Non", "Cela dépend", "Jamais"],
          reponse: 0,
          explication: "L'eau peut passer d'un état à l'autre et revenir en arrière.",
        },
        {
          enonce: "Quel est l'état de la vapeur d'eau ?",
          choix: ["Solide", "Liquide", "Gazeux", "Aucun"],
          reponse: 2,
          explication: "La vapeur d'eau est à l'état gazeux.",
        },
        {
          enonce: "L'eau peut-elle exister sous trois états différents ?",
          choix: ["Non, un seul état", "Oui : solide, liquide, gazeux", "Non, deux états seulement", "L'eau n'a pas d'état"],
          reponse: 1,
          explication: "L'eau existe sous trois états : solide, liquide et gazeux.",
        },
        {
          enonce: "Quel est le nom scientifique de la glace fondue ?",
          choix: ["De l'eau liquide", "De la vapeur", "Un solide", "Un gaz"],
          reponse: 0,
          explication: "La glace fondue devient de l'eau liquide.",
        },
        {
          enonce: "Le passage de l'état gazeux à l'état liquide s'appelle :",
          choix: ["La fusion", "La condensation", "L'évaporation", "La solidification"],
          reponse: 1,
          explication: "Ce passage s'appelle la condensation.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm1-trimestre-1",
    niveau: "cm1",
    trimestre: 1,
    titre: "Évaluation trimestrielle — CM1 — Trimestre 1",
    description: "Bilan du premier trimestre : homophones a/à et/est, grands nombres, Préhistoire.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Complète : « Il ___ un vélo. »",
          choix: ["a", "à"],
          reponse: 0,
          explication: "On peut dire « il avait un vélo », donc c'est « a ».",
        },
        {
          enonce: "Complète : « Paul ___ Marie jouent. »",
          choix: ["et", "est"],
          reponse: 0,
          explication: "« Et » relie deux noms.",
        },
        {
          enonce: "Complète : « Le chien ___ dans le jardin. »",
          choix: ["a couru", "à couru"],
          reponse: 0,
          explication: "On peut dire « il avait couru », donc c'est « a ».",
        },
        {
          enonce: "« À » avec accent introduit souvent...",
          choix: ["Un lieu ou une direction", "Une addition", "Un verbe conjugué", "Rien de particulier"],
          reponse: 0,
          explication: "« À » avec accent introduit souvent un lieu, une direction ou un complément.",
        },
        {
          enonce: "Quelle astuce permet de choisir entre « a » et « à » ?",
          choix: ["Remplacer par « avait »", "Compter les lettres", "Regarder la couleur du mot", "Aucune astuce n'existe"],
          reponse: 0,
          explication: "Si on peut remplacer par « avait », c'est « a » (le verbe avoir).",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Comment se lit 10 000 ?",
          choix: ["Mille", "Dix mille", "Cent mille", "Cent"],
          reponse: 1,
          explication: "10 000 se lit « dix mille ».",
        },
        {
          enonce: "Quel nombre est le plus grand : 4 500 ou 4 050 ?",
          choix: ["4 500", "4 050", "Égaux", "Impossible"],
          reponse: 0,
          explication: "4 500 est plus grand que 4 050.",
        },
        {
          enonce: "Comment s'écrit en chiffres « sept mille deux cents » ?",
          choix: ["720", "7200", "7020", "70200"],
          reponse: 1,
          explication: "« Sept mille deux cents » s'écrit 7200.",
        },
        {
          enonce: "Combien de centaines y a-t-il dans 3 400 ?",
          choix: ["3", "4", "34", "340"],
          reponse: 2,
          explication: "3 400 contient 34 centaines.",
        },
        {
          enonce: "Quel est le plus petit nombre : 6 090 ou 6 900 ?",
          choix: ["6 090", "6 900", "Égaux", "Impossible à dire"],
          reponse: 0,
          explication: "6 090 est plus petit que 6 900.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Comment vivaient les hommes du Paléolithique ?",
          choix: ["Sédentaires", "Nomades, chasseurs-cueilleurs", "Dans des villes", "Ils n'existaient pas"],
          reponse: 1,
          explication: "Ils étaient nomades, chasseurs-cueilleurs.",
        },
        {
          enonce: "Quels outils utilisaient-ils ?",
          choix: ["Des outils en métal", "Des outils en pierre taillée", "Des outils en plastique", "Aucun outil"],
          reponse: 1,
          explication: "Ils utilisaient des outils en pierre taillée.",
        },
        {
          enonce: "Comment les hommes préhistoriques se procuraient-ils leur nourriture ?",
          choix: ["En cultivant la terre", "En chassant et en cueillant", "Au supermarché", "Ils ne mangeaient pas"],
          reponse: 1,
          explication: "Au Paléolithique, les hommes chassaient et cueillaient leur nourriture.",
        },
        {
          enonce: "Le Paléolithique est-il une période très ancienne ?",
          choix: ["Non, très récente", "Oui, la plus ancienne période de la Préhistoire", "Elle n'a jamais existé", "Elle date d'hier"],
          reponse: 1,
          explication: "Le Paléolithique est la plus longue et plus ancienne période de la Préhistoire.",
        },
        {
          enonce: "Où vivaient souvent les hommes du Paléolithique ?",
          choix: ["Dans des immeubles", "Dans des grottes ou des campements", "Dans des châteaux", "Sous l'eau"],
          reponse: 1,
          explication: "Ils vivaient souvent dans des grottes ou des campements temporaires.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm1-trimestre-2",
    niveau: "cm1",
    trimestre: 2,
    titre: "Évaluation trimestrielle — CM1 — Trimestre 2",
    description: "Bilan du deuxième trimestre : homophones approfondis, décomposition des nombres, Néolithique.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Complète : « Le ciel ___ bleu. »",
          choix: ["et", "est"],
          reponse: 1,
          explication: "On peut dire « le ciel était bleu », donc c'est « est ».",
        },
        {
          enonce: "Quel mot peut être remplacé par « avait » ?",
          choix: ["à", "a", "et", "est"],
          reponse: 1,
          explication: "« a » peut être remplacé par « avait ».",
        },
        {
          enonce: "Complète : « Elle ___ contente de son cadeau. »",
          choix: ["et", "est"],
          reponse: 1,
          explication: "On peut dire « elle était contente », donc c'est « est ».",
        },
        {
          enonce: "Quelle astuce permet de choisir entre « et » et « est » ?",
          choix: ["Remplacer par « était »", "Compter les syllabes", "Regarder la ponctuation", "Aucune astuce"],
          reponse: 0,
          explication: "Si on peut remplacer par « était », c'est « est » (le verbe être).",
        },
        {
          enonce: "« Et » est-il un verbe ou une conjonction ?",
          choix: ["Un verbe", "Une conjonction de coordination", "Un adjectif", "Un adverbe"],
          reponse: 1,
          explication: "« Et » est une conjonction de coordination qui relie des mots ou groupes de mots.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Comment décompose-t-on 2 345 ?",
          choix: ["2000+300+40+5", "200+300+40+5", "2000+30+4+5", "2+3+4+5"],
          reponse: 0,
          explication: "2 345 = 2000 + 300 + 40 + 5.",
        },
        {
          enonce: "Combien de milliers y a-t-il dans 15 800 ?",
          choix: ["1", "15", "158", "5"],
          reponse: 1,
          explication: "15 800 contient 15 milliers.",
        },
        {
          enonce: "Comment décompose-t-on 5 672 ?",
          choix: ["5000+600+70+2", "500+600+70+2", "5000+60+7+2", "5+6+7+2"],
          reponse: 0,
          explication: "5 672 = 5000 + 600 + 70 + 2.",
        },
        {
          enonce: "Combien de dizaines y a-t-il dans 480 ?",
          choix: ["4", "8", "48", "480"],
          reponse: 2,
          explication: "480 contient 48 dizaines.",
        },
        {
          enonce: "Quel nombre correspond à 3000 + 200 + 50 + 4 ?",
          choix: ["3254", "3524", "3245", "3452"],
          reponse: 0,
          explication: "3000 + 200 + 50 + 4 = 3254.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Quelle activité apparaît au Néolithique ?",
          choix: ["L'agriculture", "L'écriture", "L'automobile", "L'électricité"],
          reponse: 0,
          explication: "L'agriculture apparaît au Néolithique.",
        },
        {
          enonce: "Que signifie « se sédentariser » ?",
          choix: ["Se déplacer sans arrêt", "S'installer durablement", "Chasser", "Peindre"],
          reponse: 1,
          explication: "Se sédentariser signifie s'installer durablement quelque part.",
        },
        {
          enonce: "Quelle invention permet de conserver la nourriture au Néolithique ?",
          choix: ["La poterie", "Le téléphone", "L'ordinateur", "La voiture"],
          reponse: 0,
          explication: "La poterie permettait de conserver et transporter la nourriture.",
        },
        {
          enonce: "Quels animaux les hommes du Néolithique commencent-ils à élever ?",
          choix: ["Des dinosaures", "Des animaux domestiques comme les moutons", "Aucun animal", "Uniquement des poissons"],
          reponse: 1,
          explication: "L'élevage d'animaux domestiques se développe au Néolithique.",
        },
        {
          enonce: "Le Néolithique est-il associé au début de l'agriculture ?",
          choix: ["Non", "Oui", "Cela concerne le Moyen Âge", "Cela concerne l'Antiquité"],
          reponse: 1,
          explication: "Le Néolithique est marqué par le développement de l'agriculture et de l'élevage.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm1-trimestre-3",
    niveau: "cm1",
    trimestre: 3,
    titre: "Évaluation trimestrielle — CM1 — Trimestre 3",
    description: "Bilan de fin d'année : bilan complet grammaire, numération et Préhistoire.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Quelle phrase est correcte ?",
          choix: ["Il va a la piscine.", "Il va à la piscine.", "Il a à la piscine.", "Il a a la piscine."],
          reponse: 1,
          explication: "« Il va à la piscine » est la phrase correcte.",
        },
        {
          enonce: "Complète : « Mon frère ___ ma sœur sont grands. »",
          choix: ["et", "est"],
          reponse: 0,
          explication: "« Et » relie « mon frère » et « ma sœur ».",
        },
        {
          enonce: "Complète : « Elle va ___ l'école. »",
          choix: ["a", "à"],
          reponse: 1,
          explication: "« À » introduit ici le lieu où elle va.",
        },
        {
          enonce: "Complète : « Mon chat ___ trois ans. »",
          choix: ["a", "à"],
          reponse: 0,
          explication: "On peut dire « avait trois ans », donc c'est « a ».",
        },
        {
          enonce: "Quelle phrase utilise correctement « et »/« est » ?",
          choix: ["Il et grand.", "Il est grand.", "Il a grand.", "Il à grand."],
          reponse: 1,
          explication: "« Il est grand » utilise correctement le verbe être « est ».",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Quel nombre vient juste après 9 999 ?",
          choix: ["9 998", "10 000", "10 001", "9 990"],
          reponse: 1,
          explication: "Après 9 999 vient 10 000.",
        },
        {
          enonce: "Range du plus grand au plus petit : lequel est le plus grand ?",
          choix: ["3 450", "3 045", "3 540", "3 405"],
          reponse: 2,
          explication: "3 540 est le plus grand des quatre nombres.",
        },
        {
          enonce: "Range du plus petit au plus grand : lequel est le plus petit ?",
          choix: ["7 200", "7 020", "7 002", "7 220"],
          reponse: 2,
          explication: "7 002 est le plus petit des quatre nombres.",
        },
        {
          enonce: "Combien font 10 000 + 500 ?",
          choix: ["1050", "10500", "10050", "100500"],
          reponse: 1,
          explication: "10 000 + 500 = 10 500.",
        },
        {
          enonce: "Quel nombre est juste avant 5 000 ?",
          choix: ["4 999", "5 001", "4 990", "5 100"],
          reponse: 0,
          explication: "Le nombre juste avant 5 000 est 4 999.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Qu'est-ce qui marque la fin de la Préhistoire ?",
          choix: ["L'agriculture", "L'écriture", "Le feu", "Les dinosaures"],
          reponse: 1,
          explication: "L'invention de l'écriture marque la fin de la Préhistoire.",
        },
        {
          enonce: "Le Néolithique vient après quelle période ?",
          choix: ["Le Moyen Âge", "Le Paléolithique", "L'Antiquité", "La Révolution"],
          reponse: 1,
          explication: "Le Néolithique succède au Paléolithique.",
        },
        {
          enonce: "Dans quel ordre se succèdent ces deux périodes ?",
          choix: ["Néolithique puis Paléolithique", "Paléolithique puis Néolithique", "En même temps", "Aucun ordre particulier"],
          reponse: 1,
          explication: "Le Paléolithique précède le Néolithique dans la Préhistoire.",
        },
        {
          enonce: "Quelle période précède immédiatement l'Antiquité ?",
          choix: ["Le Moyen Âge", "Le Néolithique", "La Renaissance", "La Révolution"],
          reponse: 1,
          explication: "Le Néolithique, avec l'invention de l'écriture, précède l'Antiquité.",
        },
        {
          enonce: "La Préhistoire se termine-t-elle avec un événement précis ?",
          choix: ["Non, aucun événement précis", "Oui, l'invention de l'écriture", "Oui, la Révolution française", "Oui, la chute de Rome"],
          reponse: 1,
          explication: "L'invention de l'écriture marque conventionnellement la fin de la Préhistoire.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm2-trimestre-1",
    niveau: "cm2",
    trimestre: 1,
    titre: "Évaluation trimestrielle — CM2 — Trimestre 1",
    description: "Bilan du premier trimestre : compléments du verbe, fractions simples, Révolution française.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Dans « Elle mange une pomme », quel est le COD ?",
          choix: ["Elle", "Mange", "Une pomme", "Aucun"],
          reponse: 2,
          explication: "« Une pomme » répond à « elle mange quoi ? ».",
        },
        {
          enonce: "Le COI est-il introduit par une préposition ?",
          choix: ["Oui, toujours", "Non, jamais", "Parfois", "Cela dépend"],
          reponse: 0,
          explication: "Le COI est toujours introduit par une préposition.",
        },
        {
          enonce: "Dans « Elle offre un cadeau à sa mère », quel est le COI ?",
          choix: ["Elle", "Un cadeau", "À sa mère", "Offre"],
          reponse: 2,
          explication: "« À sa mère » est le COI, introduit par la préposition « à ».",
        },
        {
          enonce: "Le COD répond à quelle question ?",
          choix: ["Où ?", "Quoi ? ou Qui ?", "Quand ?", "Pourquoi ?"],
          reponse: 1,
          explication: "Le COD répond à la question « quoi ? » ou « qui ? » posée après le verbe.",
        },
        {
          enonce: "Dans « Elle parle à son frère », quel complément est « à son frère » ?",
          choix: ["COD", "COI", "Sujet", "Attribut"],
          reponse: 1,
          explication: "« À son frère » est un COI, introduit par « à ».",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Dans la fraction 3/4, que représente le 4 ?",
          choix: ["Le nombre de parts prises", "Le nombre total de parts", "Rien", "Le résultat"],
          reponse: 1,
          explication: "4 est le dénominateur, le nombre total de parts.",
        },
        {
          enonce: "Quelle fraction est la plus grande : 2/5 ou 3/5 ?",
          choix: ["2/5", "3/5", "Égales", "Impossible"],
          reponse: 1,
          explication: "Avec le même dénominateur, 3/5 est plus grand.",
        },
        {
          enonce: "Dans la fraction 3/4, que représente le 3 ?",
          choix: ["Le dénominateur", "Le numérateur", "Rien", "Le résultat"],
          reponse: 1,
          explication: "3 est le numérateur, le nombre de parts prises.",
        },
        {
          enonce: "Quelle fraction représente la moitié d'un tout ?",
          choix: ["1/2", "1/4", "2/2", "1/3"],
          reponse: 0,
          explication: "1/2 représente la moitié d'un tout.",
        },
        {
          enonce: "2/4 et 1/2 représentent-elles la même quantité ?",
          choix: ["Non", "Oui, ce sont des fractions équivalentes", "Cela dépend", "2/4 est plus grand"],
          reponse: 1,
          explication: "2/4 et 1/2 sont des fractions équivalentes, représentant la même quantité.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Que se passe-t-il le 14 juillet 1789 ?",
          choix: ["Le sacre du roi", "La prise de la Bastille", "La fin de la Révolution", "Rien"],
          reponse: 1,
          explication: "Le peuple parisien prend la Bastille.",
        },
        {
          enonce: "Quels groupes ne payaient pas d'impôts avant la Révolution ?",
          choix: ["Le peuple", "La noblesse et le clergé", "Les paysans", "Tout le monde"],
          reponse: 1,
          explication: "La noblesse et le clergé étaient exemptés d'impôts.",
        },
        {
          enonce: "Comment appelle-t-on les trois groupes de la société avant 1789 ?",
          choix: ["Les trois ordres", "Les trois royaumes", "Les trois provinces", "Les trois rois"],
          reponse: 0,
          explication: "La société d'Ancien Régime est divisée en trois ordres : clergé, noblesse, tiers état.",
        },
        {
          enonce: "Qui forme le tiers état ?",
          choix: ["Uniquement les nobles", "La grande majorité de la population (paysans, bourgeois...)", "Uniquement le clergé", "Uniquement le roi"],
          reponse: 1,
          explication: "Le tiers état regroupe la grande majorité de la population, hors noblesse et clergé.",
        },
        {
          enonce: "Qui est roi de France en 1789 ?",
          choix: ["Louis XIV", "Louis XVI", "Napoléon", "Henri IV"],
          reponse: 1,
          explication: "Louis XVI est roi de France au début de la Révolution en 1789.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm2-trimestre-2",
    niveau: "cm2",
    trimestre: 2,
    titre: "Évaluation trimestrielle — CM2 — Trimestre 2",
    description: "Bilan du deuxième trimestre : COD/COI approfondis, comparaison de fractions, la République.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Dans « Il pense à ses vacances », quel complément est-ce ?",
          choix: ["COD", "COI", "Sujet", "Attribut"],
          reponse: 1,
          explication: "« à ses vacances » est un COI.",
        },
        {
          enonce: "Dans « Le chat mange la souris », quel est le COD ?",
          choix: ["Le chat", "Mange", "La souris", "Aucun"],
          reponse: 2,
          explication: "« La souris » répond à « le chat mange quoi ? ».",
        },
        {
          enonce: "Dans « Je téléphone à ma cousine », quel complément est « à ma cousine » ?",
          choix: ["COD", "COI", "Sujet", "Attribut"],
          reponse: 1,
          explication: "« À ma cousine » est un COI, introduit par la préposition « à ».",
        },
        {
          enonce: "Un verbe peut-il avoir à la fois un COD et un COI ?",
          choix: ["Non, jamais", "Oui, c'est possible", "Seulement au passé", "Seulement à l'oral"],
          reponse: 1,
          explication: "Un verbe peut avoir à la fois un COD et un COI dans la même phrase.",
        },
        {
          enonce: "Dans « Il donne un livre à son ami », quel est le COD ?",
          choix: ["Il", "Un livre", "À son ami", "Donne"],
          reponse: 1,
          explication: "« Un livre » répond à « il donne quoi ? » : c'est le COD.",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Quelle fraction représente le tout entier ?",
          choix: ["1/2", "3/3", "1/4", "2/5"],
          reponse: 1,
          explication: "3/3 représente le tout entier.",
        },
        {
          enonce: "Comment appelle-t-on le nombre du haut d'une fraction ?",
          choix: ["Le numérateur", "Le dénominateur", "Le diviseur", "Le total"],
          reponse: 0,
          explication: "Le nombre du haut s'appelle le numérateur.",
        },
        {
          enonce: "Comment appelle-t-on le nombre du bas d'une fraction ?",
          choix: ["Le numérateur", "Le dénominateur", "Le diviseur uniquement", "Le total"],
          reponse: 1,
          explication: "Le nombre du bas s'appelle le dénominateur.",
        },
        {
          enonce: "Quelle fraction est plus grande que 1 (un tout) ?",
          choix: ["3/4", "5/5", "7/4", "2/3"],
          reponse: 2,
          explication: "7/4 est supérieur à 1 car le numérateur dépasse le dénominateur.",
        },
        {
          enonce: "Comment appelle-t-on une fraction dont le numérateur est plus grand que le dénominateur ?",
          choix: ["Une fraction décimale", "Une fraction supérieure à 1", "Une fraction nulle", "Un nombre entier uniquement"],
          reponse: 1,
          explication: "Une fraction dont le numérateur dépasse le dénominateur est supérieure à 1.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Que proclame la Révolution française ?",
          choix: ["Le retour du roi absolu", "Les droits de l'Homme et du citoyen", "Rien", "La fin de la France"],
          reponse: 1,
          explication: "Elle proclame la Déclaration des droits de l'Homme et du citoyen.",
        },
        {
          enonce: "Quel régime remplace la monarchie absolue ?",
          choix: ["La République", "Une autre monarchie", "Aucun changement", "Une dictature"],
          reponse: 0,
          explication: "La Révolution instaure la République.",
        },
        {
          enonce: "En quelle année la Première République est-elle proclamée ?",
          choix: ["1789", "1792", "1804", "1815"],
          reponse: 1,
          explication: "La Première République est proclamée en 1792.",
        },
        {
          enonce: "Que signifie « République » par opposition à « monarchie » ?",
          choix: ["Le pouvoir appartient à un roi seul", "Le pouvoir n'appartient pas à un roi héréditaire", "Il n'y a aucune différence", "La République est une région de France"],
          reponse: 1,
          explication: "Dans une République, le pouvoir n'appartient pas à un roi héréditaire.",
        },
        {
          enonce: "La Déclaration des droits de l'Homme affirme-t-elle l'égalité des citoyens ?",
          choix: ["Non", "Oui", "Seulement pour les nobles", "Seulement pour les hommes riches"],
          reponse: 1,
          explication: "La Déclaration affirme l'égalité des citoyens devant la loi.",
        }
        ],
      }
    ],
  },
  {
    slug: "cm2-trimestre-3",
    niveau: "cm2",
    trimestre: 3,
    titre: "Évaluation trimestrielle — CM2 — Trimestre 3",
    description: "Bilan de fin d'année (préparation à la 6e) : grammaire, fractions et Révolution française.",
    matieres: [
      {
        matiere: "francais",
        questions: [
        {
          enonce: "Vrai ou faux : tous les verbes ont un complément d'objet.",
          choix: ["Vrai", "Faux"],
          reponse: 1,
          explication: "Certains verbes n'ont pas besoin de complément d'objet.",
        },
        {
          enonce: "Le COD répond à quelle question ?",
          choix: ["Où ?", "Quoi ? ou Qui ?", "Quand ?", "Comment ?"],
          reponse: 1,
          explication: "Le COD répond à la question « quoi ? » ou « qui ? ».",
        },
        {
          enonce: "Certains verbes n'ont-ils vraiment besoin d'aucun complément d'objet ?",
          choix: ["Non, tous en ont besoin", "Oui, comme « dormir » ou « partir »", "Cela n'existe pas", "Uniquement au futur"],
          reponse: 1,
          explication: "Des verbes comme « dormir » ou « partir » n'ont pas besoin de complément d'objet.",
        },
        {
          enonce: "Quelle est la fonction de « rapidement » dans « Il court rapidement » ?",
          choix: ["COD", "COI", "Complément circonstanciel de manière", "Sujet"],
          reponse: 2,
          explication: "« Rapidement » est un complément circonstanciel de manière, pas un complément d'objet.",
        },
        {
          enonce: "Le COD peut-il être remplacé par un pronom comme « le », « la », « les » ?",
          choix: ["Non, jamais", "Oui, c'est possible", "Seulement au pluriel", "Seulement à l'oral"],
          reponse: 1,
          explication: "Le COD peut être remplacé par les pronoms « le », « la », « les ».",
        }
        ],
      },
      {
        matiere: "mathematiques",
        questions: [
        {
          enonce: "Si je mange 3 parts sur une pizza coupée en 8, quelle fraction ai-je mangée ?",
          choix: ["3/8", "8/3", "5/8", "3/5"],
          reponse: 0,
          explication: "J'ai mangé 3 parts sur 8, soit 3/8.",
        },
        {
          enonce: "Quelle fraction est équivalente au tout ?",
          choix: ["4/4", "1/4", "4/1", "0/4"],
          reponse: 0,
          explication: "4/4 représente le tout entier.",
        },
        {
          enonce: "Quelle fraction est égale à 1/2 ?",
          choix: ["2/4", "1/4", "3/4", "1/3"],
          reponse: 0,
          explication: "2/4 est une fraction équivalente à 1/2.",
        },
        {
          enonce: "Si je mange la moitié d'un gâteau coupé en 6 parts égales, combien de parts ai-je mangées ?",
          choix: ["1", "2", "3", "4"],
          reponse: 2,
          explication: "La moitié de 6 parts correspond à 3 parts.",
        },
        {
          enonce: "Peut-on simplifier la fraction 4/8 ?",
          choix: ["Non", "Oui, elle est équivalente à 1/2", "Elle est déjà la plus simple", "Cela n'a aucun sens"],
          reponse: 1,
          explication: "4/8 peut être simplifiée en 1/2, en divisant le numérateur et le dénominateur par 4.",
        }
        ],
      },
      {
        matiere: "decouverte-du-monde",
        questions: [
        {
          enonce: "Le 14 juillet est aujourd'hui...",
          choix: ["Un jour ordinaire", "La fête nationale française", "Férié au Royaume-Uni", "Aucune de ces réponses"],
          reponse: 1,
          explication: "Le 14 juillet est la fête nationale française.",
        },
        {
          enonce: "Pourquoi le peuple se révolte-t-il en 1789 ?",
          choix: ["Sans raison", "À cause des inégalités et de la pauvreté", "Pour changer de roi", "Pour agrandir le pays"],
          reponse: 1,
          explication: "Les inégalités sociales et la pauvreté sont des causes majeures.",
        },
        {
          enonce: "Quel document important la Révolution française produit-elle en 1789 ?",
          choix: ["Le Code civil", "La Déclaration des droits de l'Homme et du citoyen", "La Constitution de 1958", "Le traité de Versailles"],
          reponse: 1,
          explication: "La Déclaration des droits de l'Homme et du citoyen est adoptée en 1789.",
        },
        {
          enonce: "La Révolution française a-t-elle eu une influence au-delà de la France ?",
          choix: ["Non, aucune", "Oui, ses idées ont influencé d'autres pays", "Elle n'a jamais existé", "Uniquement en Amérique"],
          reponse: 1,
          explication: "Les idées de la Révolution française ont influencé de nombreux autres pays.",
        },
        {
          enonce: "Que symbolise la prise de la Bastille pour les Français ?",
          choix: ["Le début de la Révolution et la fin de l'arbitraire royal", "Une simple fête populaire", "La victoire d'une guerre étrangère", "Rien de particulier"],
          reponse: 0,
          explication: "La prise de la Bastille symbolise le début de la Révolution contre l'arbitraire royal.",
        }
        ],
      }
    ],
  }
];

export function evaluationsByNiveau(niveau: string) {
  return EVALUATIONS.filter((e) => e.niveau === niveau).sort((a, b) => a.trimestre - b.trimestre);
}

export function evaluationBySlug(slug: string) {
  return EVALUATIONS.find((e) => e.slug === slug);
}
