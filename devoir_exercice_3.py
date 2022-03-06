"""
exercice_3
"""
nombre = int(input("Entrez l'annee pour voir si elle est bissextile:"))

if (nombre % 400 == 0 or nombre % 4 == 0 and nombre % 100 != 0) :
    print("bravo! Vous avez trouvez une annee bissextile")
else :
    print(" vous avez menti forrtt")