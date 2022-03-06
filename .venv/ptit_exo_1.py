choix = True
 
while choix:
    print('===exercice_1_fiche_1===')
    operation = input("Entrez votre operation +-/* :")
    nombre1 = int(input("entrez le premier nombre :"))
    nombre2 = int(input("entrez le deuxième nombre :"))
    
    if operation == "+":
       resultat = nombre1 + nombre2
       print (resultat)
    elif operation == "-":
         resultat = nombre1 - nombre2
         print (resultat)
    elif operation == "*":
         resultat = nombre1 * nombre2
         print(resultat)
    elif operation == "/":
         if nombre2==0:
             print('operation impossible')
             break
         else:
           resultat = nombre1 / nombre2
           print (resultat)
    else:
        print('je ne connais pas ce resultat') 
    choix=''
    while choix != 'yes' or choix!= 'no' :  
          choix= input("voulez_vous continuer? yes ou no :") 
          break
    if choix == 'yes':
     print('vous recommencez le jeu')
    
    else:
        print('le jeu est terminer')
        break
    