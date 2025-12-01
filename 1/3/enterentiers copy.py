somme =0
while True:
    n=int(input("Entrez un nombre entier : "))
    if n<0:
        break
    somme+=n
print("La somme des nombres entiers saisis est :",somme)
