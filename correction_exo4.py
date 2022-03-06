"""
correction
"""

print('==exercice 4==')
anne = int(input("entrez une annee : "))

trouver = 0
while trouver < 10:
    if ((anne % 4 == 0) and(anne % 100 != 0)) or anne % 400 == 0:
        print(anne)
        trouver += 1

    anne += 1      