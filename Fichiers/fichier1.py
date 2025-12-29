try:
    path = "C:/Users/HP/Desktop/bn/fexercice1.txt"
    with open (path,'r',encoding="utf-8")as f:
        lignes=f.readlines()
        for i in lignes:
            print(i.strip()) 
        print(f"Le nombre de lignes est {len(lignes)}")
        

except FileNotFoundError:
    print("pas trouve")            