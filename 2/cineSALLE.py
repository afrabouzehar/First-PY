cinema = [[0 for i in range(4)] for j in range(5)]
print("Salle apres la reservation de la rangee 2, siege 3 :")
for i in cinema:
    print(i)
    cinema[1][2] = 1
if cinema[3][2] == 0:
    libre = 0
    print("La place a la rangee 4,siege 1 est disponible.",libre)
nbr_places_libres = 0
for i in cinema:
    for j in i:
        if j == 0:
            nbr_places_libres += 1
print("Nombre total de place libres  :",nbr_places_libres)
print("Salle apres la reservation de 3 places cote a cote de la rangee 5 :")
cinema[4][0] = 1
cinema[4][1] = 1        
cinema[4][2] = 1
for i in cinema:
    print(i)