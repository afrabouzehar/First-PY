a = int(input("Entrez la longeur du cote a  : "))
b = int(input("Entrez la longeur du cote b : "))
c = int(input("Entrez la longeur du cote c : "))
if a + b > c and a + c > b and b + c > a:
    print("Triangle valide.")
else:
    print("Triangle invalide.")


# Ce programme vérifie si trois longueurs entrées par l'utilisateur
# peuvent former un triangle valide selon l'inégalité triangulaire.