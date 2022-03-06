"""
exercice_2
"""
from datetime import datetime
annee_courante = datetime.now().year
annee_de_naissance = int(input("entrez le nombre à trouver"))
age = annee_courante - annee_de_naissance
print(age)
