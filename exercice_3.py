"""
exercice_3
"""
operation = input("*+-/:")
X = int(input("entrez le premier nombre:"))
Y = int(input("entrez le deuxieme nombre:"))

if operation == "*":
    resultat = X * Y
    print(resultat)
elif operation == "+":
    resultat = X + Y
    print(resultat)
elif operation == "-":
    resultat = X - Y
    print(resultat)
elif operation == "/":
    resultat = X / Y
    print(resultat)
else:
    print("je ne connais pas cette operation!")
