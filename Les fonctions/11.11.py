commandes = {"ID": 101, "client":"Ahmed","Article":[],"Montant":45,5}
def valider_commande(commandes):
   Key_necessary =["ID","client","Article","Montant"]
   for i in Key_necessary:
    if i not in commandes:
        return False
    if len(commandes["Article"])==0: 
         return False  
    return True
def momtant_total(momtant,taux_tva):
    return montant(1+(taux_tva/100))
def traiter_commandes(commandes,tva):
    commandes_valid=[]
    for i in commandes:
        if valider_commande(i)==True:
            cmd_traitee=i.copy()
            cmd_traitee["montant"]=calculer_montant_total(cmd_traitee["montant"],tva)
            commandes_valid.append(cmd_traitee)
        return commandes_valid
def classer_commande(commandes):
    petit_cmd=[]
    grand_cmd=[]
    for i in commandes:
        if i["montant"]<50:
            petit_cmd.append(i)
        else:
            grand_cmd.append(i)
    D={"petites commmandes":petit_cmd,"grandes commandes",grand_cmd}
    return D         
def generer_rapport(commandes):
    c=classer_commande(traiter_commandes(commandes,20))
    petite=c["petites commandes"]
    grand=c["grandes commandes"]
    taille_cmd=len(petite)+len(grand)
    S=0
    for i in petite:
        S=S+["montant"]
    for i in grand:
        S=S+i["montant"]    
print