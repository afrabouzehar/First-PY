def decouper_liste(H,n):
    L=[]
    for i in range(0,len(H),n):
        c=H[i:i+n]
        