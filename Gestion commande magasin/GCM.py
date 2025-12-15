commandes = {"cmd1":{"ID":"Ali","produit":[("Huile",23,27),("miel",40,10)]},"cmd2":{"ID":"Sami","produit":[("Souris",10,20),("Pomme",5,30)]},"cmd3":{"ID":"Anne","produit":[("Tomate",10,20),("Pomme",5,30)]}}
for i,j in commandes.items():
    print("==== commandes",i,"====")
    print("client",{j["ID"]})
    for nom,p,Qte in j["produit"]:
        print(f"Nom {nom}| Prix_unitaire {p}| Quantite {Qte}")
for i,j in commandes.items():
    client = j["ID"]
    produit = j["produit"]        
    T = 0
    for nom,p,Qte in produit:
        T = T+(Qte*p)
    print("==== commandes",i,"====")
    print(f"client {client}| Somme total {T}")    
T=0
for i,j in commandes.items():
    client = j["ID"]
    produit = j["produit"]        
    for nom,p,Qte in produit:
        T = T+(Qte*p)
print(f"----chiffre d'affaire {T}----")       