for i in range(1,5):
    for j in range(i):
        print('*', end="") 
    print()
for i in range(4,1,-1):
    for j in range(1,i):
        print('*', end="")
    print()  

#or like this

lign=0
for lign in range(1,7):
    if lign<=4:
        etoiles=lign
    else:
        etoiles=8-lign
    for j in range(etoiles):
        print('*', end="")
    print()
    
    
       
       