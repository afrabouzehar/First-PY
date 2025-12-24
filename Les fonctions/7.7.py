def test_premiers(z):
    if z<2:
        return False
    for i in range (2,z):
        if z%i==0:
            return False
    return True
def nombres_premiers(a,b):
    L=[]
    for i in range(a,b+1):
        if test_premiers(i)==True:
            L.append(i)
    return L                
nbr_1= int(input("Entrez le premier nbr : "))
nbr_2= int(input("Entrez un autre nbr : ")) 
print(nombres_premiers(nbr_1,nbr_2))