def information_personnel():
    nom = input("entrez votre nom")
    from datetime import datetime
    annee_courante = datetime.now().year
    annee_de_naissance = int(input("entrez le votre annee de naissance"))
    age = annee_courante - annee_de_naissance

    print (f"bonjour {nom} tu as {age}")

information_personnel() 