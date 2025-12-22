def decouper_liste(H,n):
    L=[]
    for i in range(0,len(H),n):
        c=H[i:i+n]
        L.append(c)
    return L
Liste=[1,2,3,4,5,6,7,8,9]
print(decouper_liste(Liste,2))