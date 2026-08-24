# -*- coding: utf-8 -*-
path = 'src/content/lessons.ts'
with open(path) as f:
    txt = f.read()

# ---- rosa (1ere declinaison) ----
old_rosa_objectifs = '''    objectifs: ["Comprendre ce qu'est une déclinaison", "Reconnaître le nominatif (sujet) et l'accusatif (COD)", "Décliner un nom de la 1ère déclinaison"],'''
new_rosa_objectifs = '''    objectifs: ["Comprendre ce qu'est une déclinaison", "Reconnaître le nominatif (sujet) et l'accusatif (COD)", "Décliner entièrement rosa, rosae à tous les cas, au singulier et au pluriel"],'''
assert txt.count(old_rosa_objectifs) == 1
txt = txt.replace(old_rosa_objectifs, new_rosa_objectifs)

old_rosa_p3 = '''"Voici quelques noms de la 1ère déclinaison à connaître : rosa (la rose), puella (la jeune fille), aqua (l'eau), terra (la terre), via (la route), vita (la vie). On retrouve d'ailleurs beaucoup de ces mots presque identiques en français : rose, aquatique, terrestre, viaduc, vital."'''
new_rosa_extra = '''"Voici la déclinaison complète de rosa, rosae (la rose) à tous les cas : au singulier, nominatif rosa, génitif rosae (de la rose), datif rosae (à/pour la rose), accusatif rosam, ablatif rosa (par/avec la rose). Au pluriel, nominatif rosae, génitif rosarum (des roses), datif rosis (aux roses), accusatif rosas, ablatif rosis (par/avec les roses).", "Voici quelques noms de la 1ère déclinaison à connaître : rosa (la rose), puella (la jeune fille), aqua (l'eau), terra (la terre), via (la route), vita (la vie). On retrouve d'ailleurs beaucoup de ces mots presque identiques en français : rose, aquatique, terrestre, viaduc, vital."'''
assert txt.count(old_rosa_p3) == 1
txt = txt.replace(old_rosa_p3, new_rosa_extra)

# ---- dominus (2e declinaison) ----
old_dom_objectifs = '''    objectifs: ["Reconnaître un nom de la 2e déclinaison", "Décliner un nom masculin en -us au nominatif et à l'accusatif", "Distinguer 1ère et 2e déclinaison"],'''
new_dom_objectifs = '''    objectifs: ["Reconnaître un nom de la 2e déclinaison", "Décliner entièrement dominus, domini à tous les cas, au singulier et au pluriel", "Distinguer 1ère et 2e déclinaison"],'''
assert txt.count(old_dom_objectifs) == 1
txt = txt.replace(old_dom_objectifs, new_dom_objectifs)

old_dom_p3 = '''"Autres noms courants de la 2e déclinaison : amicus (l'ami), populus (le peuple), equus (le cheval), liber (le livre, qui fait exception avec un « e » qui disparaît : libri au génitif). On retrouve ces racines dans des mots français : « dominer » vient de dominus, « amical » vient de amicus, « populaire » vient de populus."'''
new_dom_extra = '''"Voici la déclinaison complète de dominus, domini (le maître) à tous les cas : au singulier, nominatif dominus, génitif domini (du maître), datif domino (au/pour le maître), accusatif dominum, ablatif domino (par/avec le maître). Au pluriel, nominatif domini, génitif dominorum (des maîtres), datif dominis (aux maîtres), accusatif dominos, ablatif dominis (par/avec les maîtres).", "Autres noms courants de la 2e déclinaison : amicus (l'ami), populus (le peuple), equus (le cheval), liber (le livre, qui fait exception avec un « e » qui disparaît : libri au génitif). On retrouve ces racines dans des mots français : « dominer » vient de dominus, « amical » vient de amicus, « populaire » vient de populus."'''
assert txt.count(old_dom_p3) == 1
txt = txt.replace(old_dom_p3, new_dom_extra)

with open(path, 'w') as f:
    f.write(txt)
print("declensions expanded")
