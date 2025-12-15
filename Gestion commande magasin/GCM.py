commandes = {"cmd1":{"ID":"Ali","produit":[("Huile",23,27),("miel",40,10)]},"cmd2":{"ID":"Sami","produit":[("Souris",16,20),("Pomme",3,30)]},"cmd3":{"ID":"Anne","produit":[("Tomate",10,20),("Pomme",5,30)]},"cmd4":{"ID":"Sami","produit":[("Cahier",6,10),("Stylo",2,2)]}}
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
client_uniques = set()
for i in commandes.values(): # i : the whole dictionary
    client_uniques.add(i["ID"])
for i in client_uniques:
    print(i)
depense_client = {}
for i in commandes.values():
    client = i ["ID"]
    produit = i ["produit"]
    T=0
    for nom,p,Qte in produit:
        T=T+(p*Qte)
    if client in depense_client:
        depense_client ["client"] = depense_client ["client"]+T
    else:
        depense_client ["client"] = T
    print(f"Le total depense par {client} est : ",depense_client)     
quantite_client = {}
for i in commandes.values():
    client = i ["ID"]
    produit = i ["produit"]
    for nom,p,Qte in produit:
        if nom in quantite_client:
            quantite_client [nom] = quantite_client [nom]+Qte
        else:
            quantite_client[nom]=Qte
print(max(quantite_client,key=quantite_client.get))
   