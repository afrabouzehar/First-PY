temperatures = [20, 22, 19, 23, 21, 18, 20]
moyenne = sum([20, 22, 19, 23, 21, 18, 20]) /len([20, 22, 19, 23, 21, 18, 20])
print("La température moyenne est de :", moyenne)
max_temp = max([20, 22, 19, 23, 21, 18, 20])  
print("La température maximale est de :", max_temp)
min_temp = min([20, 22, 19, 23, 21, 18, 20])
print("La température minimale est de :", min_temp)
nbr_jours_au_dessus_moyenne = 0
for i in [20, 22, 19, 23, 21, 18, 20]:
    if i > moyenne:
        nbr_jours_au_dessus_moyenne += 1
print("Nombre de jours avec température au-dessus de la moyenne :", nbr_jours_au_dessus_moyenne)
print("Température au-dessus de la moyenne :", i)
temperatures[2] = 25
print("Nouvelle liste des températures :", temperatures)
