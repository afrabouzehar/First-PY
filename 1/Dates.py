annee = int (input("Entrez une année : "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(annee, "est une année bissextile.")
else:
    print(annee, "n'est pas une année bissextile.")

# Ce programme détermine si une année entrée par l'utilisateur est bissextile ou non,
# et affiche le résultat.