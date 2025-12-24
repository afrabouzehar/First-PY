def somme_div(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
nbr=int(input("Entre un nbr : "))    
print("la somme des diviseurs propres de ce nombre : ",somme_div(nbr))