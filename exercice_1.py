"""
exercice 1 :chaud - froid
"""

nb_to_find = int(input("entrez le nombre à trouver"))
nb_to_try = int(input("essayez de deviner le nombre:"))

ecart = abs(nb_to_find - nb_to_try)

if ecart == 0:
    print("vous avez trouvé la bonne reponse!")
elif ecart <= 5:
    print("on est bouillant")
elif ecart <=10:
    print("on est tiède!")
else:
    print("on est froid!")        