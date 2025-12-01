liste = []
while True:
    prenom = input("Entrez un prénom (ou tapez 'stop' pour terminer) : ")
    if prenom.upper() == 'STOP':
        break
    else:
        liste.append(prenom)
for i in liste:
    print(i)
