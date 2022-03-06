"""
exo_1_en_fonction
"""
def ask_for_operator(message):
    op_list= ['+','-','*','/']
    op= ''
    while op not in op_list:
        op = input(message + ':')
    return op


def ask_for_number(message):
    number = None
    while number is None:
        value = input(message + ':')
        number = int(value)
    return number

def yes_or_no (message):
    rep_list=['yes','no']
    reponse =''
    while reponse not in rep_list:
        reponse= input(message + ':')
        return reponse == 'yes'

def calculer(operation, nombre1,nombre2):

    if operation == "+":
       resultat = nombre1 + nombre2
       return resultat
    elif operation == "-":
         resultat = nombre1 - nombre2
         return resultat
    elif operation == "*":
         resultat = nombre1 * nombre2
         return resultat
    elif operation == "/":
         if nombre2==0:
             print('operation impossible')
             return None
         else:
           resultat = nombre1 / nombre2
           return resultat


print("====calculatrice====")
continuer= True
    
while continuer :
       
        operation= ask_for_operator('entrez votre operation')
        number1 = ask_for_number('entrez votre premier nombre')
        number2 = ask_for_number('entrez votre 2ème nombre')
        resultat = calculer(operation,number1,number2)
        print('{0} {1} {2}={3}\n'.format(number1,operation,number2,resultat))
    
        continuer = yes_or_no('voulez-vous rejouer')

