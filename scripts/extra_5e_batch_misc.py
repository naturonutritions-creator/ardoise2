import re

path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

def q(id_, enonce, choix, reponse, explication):
    choix_str = ", ".join(f'"{c}"' for c in choix)
    return f'''      {{
        id: "{id_}",
        enonce: "{enonce}",
        choix: [{choix_str}],
        reponse: {reponse},
        explication: "{explication}",
      }}'''

new_questions = {
    'nombres-relatifs': [
        q("q3", "Quel est l'opposé de +7 ?", ["+7", "-7", "0", "7,5"], 1, "L'opposé d'un nombre relatif a le même chiffre mais le signe contraire : l'opposé de +7 est -7."),
        q("q4", "Comment note-t-on un nombre positif en général ?", ["Avec un signe - obligatoire", "Avec un signe + (souvent omis)", "Sans aucun chiffre", "Toujours entre parenthèses"], 1, "Un nombre positif peut s'écrire avec un signe +, mais celui-ci est souvent omis (5 et +5 désignent le même nombre)."),
        q("q5", "Quel nombre est le plus grand : -10 ou -1 ?", ["-10", "-1", "Ils sont égaux", "Impossible à savoir"], 1, "Sur la droite graduée, -1 est plus à droite que -10, donc -1 est plus grand."),
        q("q6", "Où se trouve le nombre 0 sur une droite graduée par rapport aux relatifs ?", ["Toujours à gauche de tous les négatifs", "À l'origine, entre les négatifs et les positifs", "Toujours à droite de tous les positifs", "Il n'a pas de place fixe"], 1, "Le 0 est l'origine de la droite graduée, séparant les nombres négatifs (à gauche) des nombres positifs (à droite)."),
        q("q7", "Quelle est la distance à zéro (valeur absolue) de -6 ?", ["-6", "6", "0", "-1"], 1, "La distance à zéro de -6, appelée valeur absolue, est 6 (un nombre toujours positif)."),
        q("q8", "Classez du plus petit au plus grand : -3, 2, -5, 0", ["-5, -3, 0, 2", "2, 0, -3, -5", "-3, -5, 0, 2", "0, -3, -5, 2"], 0, "En ordre croissant sur la droite graduée : -5, -3, 0, 2."),
        q("q9", "Un thermomètre indique -4°C le matin puis +3°C l'après-midi. La température a-t-elle augmenté ?", ["Non, elle a baissé", "Oui, elle a augmenté", "Elle est restée stable", "Impossible à dire"], 1, "-4 est plus petit que +3, donc la température a bien augmenté entre le matin et l'après-midi."),
        q("q10", "Quel nombre relatif représente une altitude de 200 mètres sous le niveau de la mer ?", ["+200", "-200", "0", "200 uniquement sans signe"], 1, "Une altitude sous le niveau de la mer se note avec un signe négatif : -200."),
    ],
    'cycle-de-l-eau': [
        q("q3", "Comment s'appelle le phénomène par lequel la vapeur d'eau se transforme en nuages ?", ["L'évaporation", "La condensation", "La précipitation", "L'infiltration"], 1, "La condensation est le phénomène par lequel la vapeur d'eau se refroidit et forme des gouttelettes composant les nuages."),
        q("q4", "Que se passe-t-il quand les gouttelettes des nuages deviennent trop lourdes ?", ["Elles restent dans le ciel", "Elles retombent sous forme de précipitations", "Elles s'évaporent à nouveau immédiatement", "Elles se transforment en vent"], 1, "Quand les gouttelettes deviennent trop lourdes, elles retombent sous forme de pluie ou de neige : ce sont les précipitations."),
        q("q5", "Où l'eau des précipitations peut-elle aller après être tombée au sol ?", ["Elle disparaît définitivement", "Elle peut s'infiltrer dans le sol ou ruisseler vers les rivières", "Elle reste toujours en surface", "Elle remonte directement vers les nuages"], 1, "L'eau peut s'infiltrer dans le sol pour rejoindre les nappes souterraines, ou ruisseler pour rejoindre rivières et océans."),
        q("q6", "Quel est le rôle du Soleil dans le cycle de l'eau ?", ["Il refroidit l'eau des océans", "Il fournit l'énergie qui fait évaporer l'eau", "Il n'a aucun rôle", "Il crée directement la pluie"], 1, "Le Soleil chauffe l'eau et fournit l'énergie nécessaire à son évaporation, moteur du cycle de l'eau."),
        q("q7", "Le cycle de l'eau est-il un phénomène qui s'arrête un jour ?", ["Oui, une fois par an", "Non, c'est un cycle continu", "Oui, seulement en hiver", "Non, il ne fonctionne qu'en été"], 1, "Le cycle de l'eau est continu : évaporation, condensation et précipitations se répètent en permanence."),
        q("q8", "Sous quelle forme l'eau peut-elle précipiter quand il fait très froid ?", ["Uniquement sous forme de pluie", "Sous forme de neige ou de grêle", "Sous forme de vapeur", "L'eau ne précipite jamais par temps froid"], 1, "Par temps froid, l'eau peut précipiter sous forme de neige ou de grêle plutôt que de pluie."),
        q("q9", "D'où provient la majeure partie de l'eau qui s'évapore sur Terre ?", ["Des rivières uniquement", "Des océans", "Des nuages", "Des glaciers uniquement"], 1, "Les océans, qui couvrent la majorité de la surface terrestre, sont la principale source d'évaporation."),
        q("q10", "Pourquoi dit-on que l'eau suit un « cycle » ?", ["Car elle change de couleur", "Car elle repasse par les mêmes étapes de façon répétée", "Car elle ne se déplace jamais", "Car elle disparaît chaque année"], 1, "On parle de cycle car l'eau repasse continuellement par les mêmes étapes : évaporation, condensation, précipitations, infiltration/ruissellement."),
    ],
    'present-simple-anglais': [
        q("q3", "Comment forme-t-on la négation au présent simple avec « I » ?", ["I not play", "I don't play", "I doesn't play", "I no play"], 1, "À la négation, on utilise l'auxiliaire « don't » (do not) avec I, you, we, they : I don't play."),
        q("q4", "Quelle forme négative est correcte à la 3e personne du singulier ?", ["She don't play", "She doesn't play", "She not plays", "She no plays"], 1, "À la 3e personne du singulier, on utilise « doesn't » (does not) : she doesn't play."),
        q("q5", "Quel mot signale souvent une phrase au présent simple ?", ["Yesterday", "Every day", "Tomorrow", "Last week"], 1, "« Every day » (chaque jour) indique une habitude, typique du présent simple."),
        q("q6", "Quelle phrase utilise correctement le présent simple ?", ["He watch TV every evening.", "He watches TV every evening.", "He watching TV every evening.", "He is watch TV every evening."], 1, "À la 3e personne du singulier, on ajoute -s : he watches."),
        q("q7", "Comment forme-t-on une question au présent simple avec « they » ?", ["They play football?", "Do they play football?", "Does they play football?", "Are they play football?"], 1, "Avec they, on utilise l'auxiliaire « do » : Do they play football?"),
        q("q8", "Quelle terminaison prend un verbe se finissant en -ch ou -sh à la 3e personne du singulier ?", ["-s", "-es", "-ies", "Aucune terminaison"], 1, "Les verbes en -ch, -sh, -ss, -x prennent -es à la 3e personne : watch → watches."),
        q("q9", "Que signifie « I play football every Saturday » ?", ["Je jouais au football samedi dernier", "Je joue au football tous les samedis", "Je jouerai au football samedi prochain", "J'ai joué au football un samedi"], 1, "Le présent simple avec « every Saturday » exprime une habitude répétée : je joue au football tous les samedis."),
        q("q10", "Quel auxiliaire utilise-t-on pour la forme interrogative au présent simple avec « she » ?", ["Do", "Does", "Is", "Has"], 1, "Avec she (3e personne du singulier), on utilise l'auxiliaire « does » : Does she play?"),
    ],
    'pays-anglophones-5e': [
        q("q4", "Comment dit-on « appartement » en anglais britannique ?", ["Apartment", "Flat", "House", "Room"], 1, "En anglais britannique, on dit « flat » pour un appartement, contre « apartment » en anglais américain."),
        q("q5", "Citez un pays anglophone en dehors du Royaume-Uni et des États-Unis.", ["La France", "L'Australie", "L'Allemagne", "Le Portugal"], 1, "L'Australie est un pays où l'anglais est langue officielle, tout comme le Canada, l'Irlande ou la Nouvelle-Zélande."),
        q("q6", "Pourquoi l'anglais est-il parlé dans autant de pays du monde ?", ["Grâce au commerce phénicien", "En raison de la colonisation par l'Empire britannique", "Grâce à l'Union européenne", "Ce fut décidé par l'ONU"], 1, "L'expansion de l'Empire britannique du XVIIe au XXe siècle a diffusé l'anglais dans de nombreuses colonies."),
        q("q7", "Comment appelle-t-on l'anglais parlé aux États-Unis par rapport à celui du Royaume-Uni ?", ["Ils sont rigoureusement identiques", "Il existe des différences de vocabulaire et de prononciation", "Ce sont deux langues différentes", "L'anglais américain n'existe pas"], 1, "L'anglais américain et l'anglais britannique partagent la même base mais présentent des différences de vocabulaire et de prononciation."),
    ],
    'fetes-traditions-anglophones-5e': [
        q("q4", "Que représentent les jack-o'-lanterns ?", ["Des citrouilles sculptées pour Halloween", "Des dindes pour Thanksgiving", "Des sapins de Noël", "Des cadeaux de Santa Claus"], 0, "Les jack-o'-lanterns sont des citrouilles sculptées, symboles traditionnels d'Halloween."),
        q("q5", "Quel animal est traditionnellement mangé à Thanksgiving ?", ["Le poulet", "La dinde", "Le canard", "Le poisson"], 1, "La dinde (turkey) est le plat traditionnel du repas de Thanksgiving."),
        q("q6", "Comment appelle-t-on le lendemain de Noël au Royaume-Uni ?", ["New Year's Day", "Boxing Day", "Christmas Eve", "Twelfth Night"], 1, "Le 26 décembre est appelé Boxing Day au Royaume-Uni, jour férié traditionnel."),
        q("q7", "Qui apporte les cadeaux de Noël dans le monde anglophone ?", ["Le Père Fouettard", "Santa Claus", "La Befana", "Les Rois mages"], 1, "Santa Claus est le personnage traditionnel qui apporte les cadeaux de Noël dans les pays anglophones."),
    ],
    'monuments-symboles-anglophones-5e': [
        q("q5", "Quel monument préhistorique se trouve dans le sud de l'Angleterre ?", ["Le Colisée", "Stonehenge", "La tour de Pise", "L'Alhambra"], 1, "Stonehenge est un site mégalithique préhistorique situé dans le sud de l'Angleterre."),
        q("q6", "Quelle est la résidence du président des États-Unis ?", ["Buckingham Palace", "The White House", "The Tower of London", "The Capitol"], 1, "The White House (la Maison Blanche), à Washington D.C., est la résidence officielle du président américain."),
        q("q7", "Quel pont célèbre se trouve à San Francisco ?", ["Tower Bridge", "Golden Gate Bridge", "Brooklyn Bridge", "London Bridge"], 1, "Le Golden Gate Bridge, à San Francisco, est l'un des ponts les plus célèbres des États-Unis."),
        q("q8", "En quelle année la Statue de la Liberté fut-elle offerte par la France ?", ["1789", "1886", "1945", "1900"], 1, "La Statue de la Liberté fut offerte par la France aux États-Unis en 1886."),
    ],
    'paises-hispanohablantes-5e': [
        q("q4", "Citez un pays hispanophone d'Amérique latine.", ["Le Brésil", "Le Mexique", "Le Portugal", "Haïti"], 1, "Le Mexique (México) est l'un des grands pays hispanophones d'Amérique latine."),
        q("q5", "Comment appelle-t-on le phénomène de prononciation différente de la « c » et de la « z » en Amérique latine ?", ["Le seseo", "Le yeísmo", "L'acento", "La ñ"], 0, "Le « seseo » désigne la prononciation identique de la « c » (devant e/i) et de la « z » comme un « s », typique de l'espagnol d'Amérique."),
        q("q6", "Quel explorateur est associé au début de la colonisation espagnole en Amérique ?", ["Vasco de Gama", "Christophe Colomb", "Marco Polo", "Fernand de Magellan"], 1, "Les voyages de Christophe Colomb à la fin du XVe siècle marquent le début de la colonisation espagnole en Amérique."),
        q("q7", "Quelle langue parle-t-on au Brésil ?", ["L'espagnol", "Le portugais", "Le français", "L'italien"], 1, "Le Brésil, colonisé par le Portugal, a le portugais comme langue officielle, contrairement à ses voisins hispanophones."),
    ],
    'fiestas-tradiciones-hispanas-5e': [
        q("q4", "Que sont les « ofrendas » lors du Día de los Muertos ?", ["Des chants traditionnels", "Des autels décorés en l'honneur des défunts", "Des costumes de fête", "Des plats typiques uniquement"], 1, "Les ofrendas sont des autels décorés de photos, fleurs et objets en mémoire des défunts, lors du Día de los Muertos."),
        q("q5", "Quand les enfants espagnols reçoivent-ils traditionnellement leurs cadeaux de Noël ?", ["Le 25 décembre", "Le 6 janvier, jour des Rois mages", "Le 1er janvier", "Le 24 décembre"], 1, "En Espagne, les cadeaux sont traditionnellement apportés le 6 janvier, jour du Día de Reyes."),
        q("q6", "Que représentent les posadas en Amérique latine ?", ["Des processions représentant la recherche d'un logement par Marie et Joseph", "Des combats de tomates", "Des défilés de carnaval", "Des courses de chars"], 0, "Les posadas sont des processions célébrées avant Noël, représentant la recherche d'un logement par Marie et Joseph."),
        q("q7", "Où se déroule La Tomatina ?", ["À Madrid", "À Buñol", "À Séville", "À Barcelone"], 1, "La Tomatina, célèbre bataille de tomates, se déroule chaque année à Buñol, en Espagne."),
    ],
    'monumentos-simbolos-hispanos-5e': [
        q("q5", "Où se trouve le Museo del Prado ?", ["À Barcelone", "À Madrid", "À Séville", "À Grenade"], 1, "Le Museo del Prado, l'un des plus grands musées d'art du monde, se trouve à Madrid."),
        q("q6", "À quelle civilisation sont associées les pyramides de Chichén Itzá ?", ["Inca", "Maya", "Azteca", "Romaine"], 1, "Chichén Itzá est un site archéologique associé à la civilisation maya, au Mexique."),
        q("q7", "Le Machu Picchu est-il classé au patrimoine mondial de l'UNESCO ?", ["Non, il n'est pas classé", "Oui, il est classé", "Il l'a été puis déclassé", "Seulement une partie du site"], 1, "Le Machu Picchu, site archéologique inca situé dans les Andes, est classé au patrimoine mondial de l'UNESCO."),
        q("q8", "En quel siècle l'Alhambra de Grenade a-t-elle été construite ?", ["Époque musulmane médiévale", "XIXe siècle", "XXe siècle", "Antiquité romaine"], 0, "L'Alhambra est un palais-forteresse d'origine musulmane construit durant la période médiévale."),
    ],
    'italia-regioni-5e': [
        q("q6", "Quelle mer entoure l'Italie ?", ["La mer du Nord", "La mer Méditerranée", "La mer Baltique", "L'océan Atlantique"], 1, "L'Italie est entourée par la mer Méditerranée."),
        q("q7", "Dans quelle région se trouve Roma ?", ["La Toscana", "La Sicilia", "Il Lazio", "La Lombardia"], 2, "Rome, la capitale italienne, se trouve dans la région du Lazio."),
        q("q8", "Quel plat est associé à Bologna ?", ["La pizza", "Les tagliatelle al ragù", "Les arancini", "Les cannoli"], 1, "Les tagliatelle al ragù sont un plat traditionnel emblématique de Bologne."),
        q("q9", "Pourquoi de nombreux dialectes régionaux coexistent-ils avec l'italien standard ?", ["Car chaque région a sa propre histoire et culture", "Car l'italien standard n'existe pas", "Car le pays est très petit", "Ce n'est pas le cas en Italie"], 0, "Chaque région d'Italie a une identité culturelle et linguistique propre, d'où la coexistence de nombreux dialectes avec l'italien standard."),
        q("q10", "Quelle forme géographique évoque l'Italie sur une carte ?", ["Un cercle", "Une botte", "Un triangle équilatéral", "Une étoile"], 1, "L'Italie a une forme caractéristique de botte, bien visible sur une carte."),
    ],
    'feste-tradizioni-italiane-5e': [
        q("q5", "Que fait la Befana aux enfants moins sages ?", ["Elle leur apporte des jouets", "Elle leur apporte du charbon (souvent en sucre)", "Elle ne leur rend pas visite", "Elle les punit sévèrement"], 1, "La Befana apporte traditionnellement du charbon, souvent sous forme de sucre, aux enfants moins sages."),
        q("q6", "Quel gâteau mange-t-on traditionnellement à Pâques en Italie ?", ["La colomba", "Le panettone", "Le tiramisù", "Les cannoli"], 0, "La colomba, gâteau en forme de colombe, est la pâtisserie traditionnelle de Pâques en Italie."),
        q("q7", "Sur quelle place se déroule le Carnevale de Venise ?", ["Piazza Navona", "Piazza San Marco", "Piazza del Duomo", "Piazza di Spagna"], 1, "Le Carnevale de Venise se déroule notamment sur la Piazza San Marco."),
        q("q8", "Jusqu'à quelle date les fêtes de Noël se prolongent-elles traditionnellement en Italie ?", ["Le 31 décembre", "Le 6 janvier (Epifania)", "Le 1er février", "Le 25 décembre uniquement"], 1, "En Italie, Noël se prolonge traditionnellement jusqu'à l'Épiphanie, le 6 janvier."),
    ],
    'monumenti-simboli-italiani-5e': [
        q("q5", "Qu'est-ce que le Foro Romano ?", ["Un amphithéâtre pour les gladiateurs", "Le centre politique et religieux de la Rome antique", "Une basilique", "Un musée moderne"], 1, "Le Foro Romano (Forum romain) était le centre politique et religieux de la Rome antique."),
        q("q6", "Qui a conçu la coupole de la cathédrale de Florence ?", ["Michelangelo", "Brunelleschi", "Antoni Gaudí", "Léonard de Vinci"], 1, "L'architecte Brunelleschi a conçu la célèbre coupole de la cathédrale Santa Maria del Fiore à Florence."),
        q("q7", "Qu'est-ce que le Vaticano ?", ["Une région d'Italie", "Le plus petit État du monde, enclavé dans Rome", "Un musée uniquement", "Une ville portuaire"], 1, "Le Vatican est un État indépendant, le plus petit du monde, situé au cœur de Rome."),
        q("q8", "Qui a peint les fresques de la Chapelle Sixtine ?", ["Léonard de Vinci", "Michelangelo", "Raphaël uniquement", "Botticelli uniquement"], 1, "Michel-Ange (Michelangelo) est l'auteur des célèbres fresques de la Chapelle Sixtine."),
    ],
}

for slug, qs in new_questions.items():
    idx = txt.index(f'slug: "{slug}"')
    window = txt[idx:idx+9000]
    close_marker = "\n    ],\n  },\n  },"
    close_idx_rel = window.index(close_marker)
    abs_close_idx = idx + close_idx_rel
    insertion = ",\n" + ",\n".join(qs)
    txt = txt[:abs_close_idx] + insertion + txt[abs_close_idx:]

with open(path, 'w') as f:
    f.write(txt)

print("done")
