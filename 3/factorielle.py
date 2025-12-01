n = int(input("Entrez un nombre : "))
fact = 1
if n>=0:
    if n==0 or n==1:
        print(1)
    else: 
         for i in range(1, n + 1):
             fact *= i

print("La factorielle de", n, "est :", fact)         
