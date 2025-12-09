votes = ["Yasmine", "Amine",
"Yasmine", "Omar", "Yasmine", "Amine", "Omar", "Amine", "Yasmine", "Sara", "Omar",
"Yasmine", "Sara"]
dictio={}
for name in votes:
    if name in dictio:
        dictio[name] += 1
    else:
        dictio[name] = 1
print("Résultat des votes :", dictio)   
MAX=max(dictio)
print("Le candidat avec le plus de votes est :", MAX,"avec", dictio[MAX], "votes" )  

    
