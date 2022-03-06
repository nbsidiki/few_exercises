
print('===exo===')

from random import randint

questions = [
    {   
        "question": "je suis ...",
        "reponses": [ 
            "homme",
            "femme",
            "bi"
        ],
        "correct": "homme"
     },
     
{
        "question": "mon age est ...", 
        "reponses": [ 
            "20",
            "16",
            "19"
         ],
         "correct": "19"
    }
]

hasard = randint(0,len(questions)-1)
question = questions[hasard]
print("Question" +" "+ str(hasard+1) + ":" + question["question"])

cpt = 0
while cpt < len(question["reponses"]):
    print(str(cpt)+":"+ question["reponses"][cpt])
    cpt+=1

choix = int(input("Entrez le numéro :"))
if choix<0 or choix>len(question["question"]):
    print('mauvaise reponse')
    quit(-1)
if question["reponses"][choix]!= question["correct"]:
    print("mauvaise reponse,dommage")
else:
    print('bonne reponse !')             
