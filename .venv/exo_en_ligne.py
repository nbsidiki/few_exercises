from random import randint
def choix_lordi():
    jeu_list=["pierre",'feuille',"csiseaux"]
    hasard= randint(0,len(jeu_list)-1)
    return hasard

def ask_for_player():
    jeu_list=["pierre",'feuille',"csiseaux"]
    cpt=0
    while cpt<len(jeu_list):
        print(str(cpt) + ':'+ jeu_list[cpt])
        cpt+=1

    choix = int(input('Entrez votre choix :'))
    return choix

def jeu(hasard,choix):
    if choix== 0 and hasard ==1:
        print('victoire pour la machine !')
    elif choix==0 and hasard==2:
        print('victoire pour vous !')
    elif choix== 1 and hasard == 0:
        print('victoire pour vous !')
    elif choix == 1 and hasard==2:
        print('victoire pour la machine !')
    elif choix ==2 and hasard==1:
        print('victoire pour vous !')
    elif choix ==2 and hasard ==0:
        print('victoire pour la machine !')
    else:
        print('Egalité, Match Null !')

    return None


jeu_p_f_c= True
while jeu_p_f_c:
    hasard=choix_lordi()
    choix=ask_for_player()
    jeu_list=["pierre",'feuille',"csiseaux"]
    print('le choix de la machine a été'+':'+ jeu_list[hasard])
    resultat= jeu(hasard,choix)  
    break
    
