"""
exercice_6
"""
maliste = ["d", 1 , 4]
taile = len(maliste)
cpt = 0
min_index = 0
while cpt < taile:
    if len(maliste[cpt]) < len(maliste[min_index]):
       maliste[min_index] = maliste[cpt]
       
    cpt = cpt + 1
    print(maliste[min_index])
    