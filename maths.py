
import math
def aireexpo():
   a= int(input("Entrez la borne inferieur :"))
   b= int(input("la borne superieur :"))
   if(a>b):
      print("l'intervalle n'est pas bon")
   else:
     resultat= float(math.exp(b)-math.exp(a))
     print(resultat)

   return 0

def aireinverse():
    a= int(input("Entrez la borne inferieur :"))
    b= int(input("la borne superieur :"))
    if(a>b):
      print("l'intervalle n'est pas bon !")
    elif(a<0 and b>0):
        print("l'intervalle pose problème(il contient 0)")
    elif( a==0 or b==0):
        print("a et b ne peuvent pas etre egale à 0 !")
    else:
        if(a>0 and b>0):
           resultat=float(math.log(b)-math.log(a))
           print(resultat)
        elif(a<0 and b<0):
           resultat=float(-(math.log(-b)-math.log(-a)))
           print(resultat)
    return 0


print(aireinverse())