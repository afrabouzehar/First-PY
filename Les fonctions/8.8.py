def somme_chiffres(n):
    T=0
    str_n=str(n)
    for i in str_n:
        T=T+int(i)
    return T
nombre=input("Entrez un nombre : ")
print("La somme de ces nombres est: " ,somme_chiffres(nombre))            