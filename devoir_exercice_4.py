"""
exercice_3
"""
annee = int(input("Entrez l'annee pour voir si elle est bissextile:"))
if annee % 400 == 0:
   annee1 = annee
   while annee1 <= annee + 36 :
      print(annee1)
      annee1 = annee1 + 4
   print("vous avez les 10 annees bissextiles avenir") 

else:
    print('vous avez menti fortttt')