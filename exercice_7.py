"""
exercice_7
"""
maliste = [
    [1, 2, 3],
    ['a','b','c']
]
ligne = len(maliste)
cpt_l = 0
while cpt_l < ligne:
      cpt_c = 0
      colonne = len(maliste[cpt_l])
      while cpt_c < colonne:
            print(maliste[cpt_l][cpt_c])
            cpt_c +=1
 
      cpt_l +=1    