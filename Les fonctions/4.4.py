def compter_voyelles(chaine):
    voyelles="aiueoyAIUEOY"
    compter=0
    for i in chaine:
        if i in voyelles:
            compter+=1
    return(compter)
mot= str(input("Entrez un mot : "))
print("Le nombre des voyelles dans ce mot : ",compter_voyelles(mot))        