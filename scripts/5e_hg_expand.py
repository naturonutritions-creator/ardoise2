# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

extra = {
    "debuts-islam": "La Mecque, ville sainte de l'islam, abrite la Kaaba, un édifice cubique vénéré que les pèlerins musulmans continuent aujourd'hui de visiter lors du pèlerinage annuel du hajj, l'un des cinq piliers de leur religion.",
    "byzance-heritiere-empire-romain-5e": "La basilique Sainte-Sophie, chef-d'œuvre architectural voulu par Justinien, a connu une histoire mouvementée : église chrétienne pendant près de mille ans, elle devient une mosquée après la conquête ottomane de 1453, puis un musée au XXe siècle, avant de redevenir une mosquée en 2020.",
    "empire-carolingien-charlemagne-5e": "Le traité de Verdun, qui partage l'empire en 843, est précédé par les Serments de Strasbourg en 842, un texte dans lequel les petits-fils de Charlemagne s'engagent l'un envers l'autre : il s'agit du plus ancien texte connu écrit en langue romane, ancêtre du français.",
    "naissance-diffusion-islam-5e": "Les savants du monde musulman, notamment à Bagdad où fut fondée la Maison de la Sagesse, traduisent et prolongent les connaissances grecques, indiennes et perses : on leur doit par exemple la diffusion des chiffres arabes (empruntés à l'Inde) et d'importants progrès en médecine, en astronomie et en algèbre.",
    "seigneurie-societe-feodale-5e": "Le château fort est le symbole du pouvoir seigneurial : d'abord simple bâtisse en bois sur une motte de terre (motte castrale), il devient à partir du XIe-XIIe siècle une puissante forteresse de pierre, avec donjon, remparts et douves, qui protège le seigneur tout en affirmant son autorité sur la région.",
    "eglise-moyen-age-5e": "L'Église prélève aussi un impôt appelé la dîme, correspondant à un dixième des récoltes des paysans, qui contribue à sa puissance économique. Les chemins de pèlerinage, comme celui de Saint-Jacques-de-Compostelle en Espagne, attirent chaque année des milliers de fidèles à travers toute l'Europe.",
    "affirmation-etat-monarchique-5e": "En 1302, le roi Philippe le Bel réunit pour la première fois les états généraux, une assemblée rassemblant des représentants du clergé, de la noblesse et du tiers état, afin d'obtenir leur soutien face au pape : cette assemblée, réunie de façon exceptionnelle, deviendra plus tard un enjeu majeur au moment de la Révolution française.",
    "renaissance-humanisme-decouvertes-5e": "Grâce à l'imprimerie, le nombre de livres produits en Europe explose : on estime qu'environ 20 millions de livres sont imprimés durant la seconde moitié du XVe siècle, contre seulement quelques milliers copiés à la main chaque année auparavant, ce qui démocratise considérablement l'accès au savoir.",
    "reforme-monarchie-absolue-5e": "Un autre réformateur, le Français Jean Calvin, développe à Genève à partir des années 1530 une autre branche du protestantisme, le calvinisme, qui se répand notamment en France, en Suisse et aux Pays-Bas, et qui insiste particulièrement sur l'idée de prédestination.",
    "demographie-developpement-inegal-5e": "Certains pays, comme le Niger, ont encore aujourd'hui une natalité très élevée et une population très jeune, tandis que d'autres, comme le Japon, connaissent au contraire un vieillissement marqué de leur population et une natalité très faible, ce qui pose des défis économiques et sociaux très différents selon les pays.",
    "ressources-limitees-gerer-renouveler-5e": "L'accès à l'eau potable reste très inégal dans le monde : plusieurs centaines de millions de personnes n'y ont toujours pas facilement accès, notamment en Afrique subsaharienne, alors que la demande en eau ne cesse d'augmenter avec la croissance démographique et les besoins de l'agriculture et de l'industrie.",
    "risques-changement-global-5e": "Le tsunami de décembre 2004 dans l'océan Indien, qui a fait environ 230 000 morts dans plusieurs pays, illustre à quel point la vulnérabilité des populations (habitations proches des côtes, absence de système d'alerte à l'époque) peut transformer un aléa naturel en catastrophe humaine dramatique.",
    "respecter-autrui-5e": "Sur internet, l'apparent anonymat peut donner l'impression que les propos postés n'ont pas de conséquences réelles : c'est faux, le cyberharcèlement laisse des traces identifiables et est puni par la loi au même titre que le harcèlement en personne, avec des peines pouvant aller jusqu'à plusieurs années de prison dans les cas les plus graves.",
    "valeurs-republique-ue-5e": "Le principe de laïcité trouve son origine dans la loi de séparation des Églises et de l'État, votée en 1905 : elle met fin au statut privilégié dont bénéficiait l'Église catholique en France et garantit depuis la neutralité religieuse de l'État envers toutes les convictions, religieuses ou non.",
    "culture-civique-5e": "Dans de nombreux pays démocratiques, dont la France, le taux d'abstention (le nombre de citoyens qui ne votent pas) est un sujet de préoccupation : il interroge sur l'intérêt des citoyens pour la vie politique et alimente régulièrement le débat public sur la meilleure façon de renforcer la participation citoyenne.",
}

count = 0
for slug, paragraph in extra.items():
    marker_start = f'slug: "{slug}"'
    idx = txt.index(marker_start)
    quiz_idx = txt.index("quiz: {", idx)
    close_pattern_a = '"],\n    quiz: {'
    close_pattern_b = '",\n    ],\n    '
    try:
        close_idx = txt.rindex(close_pattern_a, idx, quiz_idx + len('quiz: {'))
        esc = paragraph.replace('"', '\\"')
        insertion = f', "{esc}"'
        txt = txt[:close_idx+1] + insertion + txt[close_idx+1:]
        count += 1
        continue
    except ValueError:
        pass
    # fallback for older multi-line formatted contenu arrays (debuts-islam style)
    close_idx = txt.rindex('",\n    ],\n', idx, quiz_idx + len('quiz: {'))
    esc = paragraph.replace('"', '\\"')
    insertion = f',\n      "{esc}",'
    insert_pos = close_idx + 1
    txt = txt[:insert_pos] + insertion + txt[insert_pos:]
    count += 1

with open(path, 'w') as f:
    f.write(txt)
print("5e paragraphs added:", count)
