def trier_liste(L,ordre="asc"):
    B=sorted(L)
    if ordre =="desc":
        B=B[::-1]
    return B
Liste1=[1,34,45,6,55,4,243,34]   
print(trier_liste(Liste1,ordre="desc")) 

