positifs = 0
negatifs = 0
nuls = 0
for i in range(5):
    n = int(input("Entrez un nombre : "))
    if n>0:
       positifs += 1
    elif n<0:
        negatifs += 1
    else:
        nuls += 1
print("Nombres positifs :", positifs)
print("Nombres négatifs :", negatifs)
print("Nombres nuls :", nuls)
