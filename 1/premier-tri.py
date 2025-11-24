v1 = int (input(" Entrez un nombre : "))
v2 = int (input(" Entrez un autre nombre : "))
v3 = int (input(" Entrez un troisième nombre : "))
if v3<v2:
    v2,v3 = v3,v2
if v3<v1:
    v1,v3 = v3,v1
if v2<v1:
    v1,v2 = v2,v1
print("Le tri des nombres est : ",v1,v2,v3)

# Ce programme trie trois nombres entiers entrés par l'utilisateur
# et affiche les nombres dans l'ordre décroissant.