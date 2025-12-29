commande = {"ID": 101, "client":"Ahmed","Article":[...],"Montant":45,5}
def valider_commande(commande):
   Key_necessary =["ID","client","Article","Montant"]
   for i in Key_necessary:
    if i not in commande:
        return False
g            