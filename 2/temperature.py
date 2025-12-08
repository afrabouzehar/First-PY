temperature =[20,22,19,23,21,18,20]
max_temp = max(temperature)
min_temp = min(temperature)
print("Temperature la plus elevee :", max_temp)
print("Temperature la plus basse :", min_temp)
moyenne_temp = (max_temp + min_temp) / 2
print("Temperature moyenne :", moyenne_temp)
nbr_jours = 0
for temp in temperature:
    if temp < moyenne_temp:
        nbr_jours += 1
print("Nombre de jours avec temperature au-dessus de la moyenne :", nbr_jours)
temperature[2]=25
print("Nouvelle liste des temperatures :", temperature)