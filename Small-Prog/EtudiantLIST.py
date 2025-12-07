nom = ""
age = 0
notes = []
Etudiant = [{"Nom": nom, "Age": age, "Notes": notes}]

print("1.Ajouter un etudiant")
print("2.Afficher tous les etudiants")
print("3.Calculer la moyenne d'un etudiant")
print("4.Afficher l'etudiant avec la meilleure moyenne")
print("5.Quitter")

while True:
    choix = input("Votre choix: ")

    if choix == "1":
        print("Votre choix:", choix)
        nom = input("Nom de l'etudiant: ")
        age = int(input("Age de l'etudiant: "))
        notes = input("Notes de l'etudiant (separees par des espaces): ")
        notes = [float(n) for n in notes.split()]
        Etudiant.append({"Nom": nom, "Age": age, "Notes": notes})

    elif choix == "2":
        print("Votre choix:", choix)
        for etudiant in Etudiant:
            print(f"Nom: {etudiant['Nom']}, Age: {etudiant['Age']}, Notes: {etudiant['Notes']}")

    elif choix == "3":
        nom = input("Nom de l'etudiant: ")
        for etudiant in Etudiant:
            if etudiant["Nom"] == nom:
                total = 0
                nb_notes = 0
                for note in etudiant["Notes"]:
                    total += note
                    nb_notes += 1
                moyenne = total / nb_notes
                print(f"La moyenne de {nom} est {moyenne:.2f}")
                break

    elif choix == "4":
        print("Votre choix:", choix)
        meilleure_moyenne = -1
        meilleur_etudiant = None

        for etudiant in Etudiant:
            total = 0
            nb_notes = 0
            for note in etudiant["Notes"]:
                total += note
                nb_notes += 1
            moyenne = total / nb_notes
            if moyenne > meilleure_moyenne:
                meilleure_moyenne = moyenne
                meilleur_etudiant = etudiant

        if meilleur_etudiant:
            print(f"L'etudiant avec la meilleure moyenne est {meilleur_etudiant['Nom']} avec une moyenne de {meilleure_moyenne:.2f}")

    elif choix == "5":
        print("Au revoir!")
        break
