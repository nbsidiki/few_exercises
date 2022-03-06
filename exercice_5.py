"""
exercice_5
"""
largeur = int(input("entrez la largeur:"))
hauteur = int(input("entrez la hauteur: "))
texte = " "
cpt_h = 0
while cpt_h <= hauteur:
    cpt_l = 0
    while cpt_l <= largeur:
          texte = texte + "*"
          cpt_l = cpt_l + 1
    texte = texte + "\n"
    cpt_h = cpt_h + 1
print(texte)