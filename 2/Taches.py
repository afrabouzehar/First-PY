taches=[]
taches.append("Faire les courses")
taches.append("Envoyer un email")
taches.append("Etudier")
taches.append("Nettoyer la maison")
print("Liste des taches :", taches)
taches_recherchees = input("Entrez la tache a rechercher : ")
if taches_recherchees in taches:
    print("La tache", taches_recherchees, "est dans la position :",taches.index(taches_recherchees))
else:
    print("La tache", taches_recherchees, "n'est pas dans la liste.")
taches_recherchees2 = input("Entrez la tache a ajouter : ")
position= int(input("À quelle position souhaitez-vous ajouter la tâche (entre 0 et 4) ? :"))
taches.insert(position,taches_recherchees2)
print("Liste mise a jour des taches :", taches)
