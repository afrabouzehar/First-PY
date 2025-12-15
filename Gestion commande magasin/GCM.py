commandes = {"cmd1":{"ID":"Ali","produit":[("Huile",23,27),("miel",40,10)]},"cmd2":{"ID":"Ali","produit":[("Souris",10,20),("Pomme",5,30)]}}
for i,j in commandes.items():
    print("==== commandes",i,"====")
    print("client",{j["ID"]})
    for nom,p,Qte in j["produit"]:
        print(f"Nom {nom}| Prix_unitaire {p}| Quantite {Qte}")
   