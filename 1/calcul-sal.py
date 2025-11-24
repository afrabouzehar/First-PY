nbr_heure =int(input("Nombre d'heures : "))
taux_horaire = float(input("Taux horaire : "))
montant_heure_normales = nbr_heure * taux_horaire
nombre_heure_sup = 0
if nbr_heure > 35:
    nombre_heure_sup = nbr_heure - 35
    montant_heure_sup = nombre_heure_sup * taux_horaire * 1.50
    montant_heure_normales = 35 * taux_horaire
    Montant_total = montant_heure_normales + montant_heure_sup
    print("Montant des heures normales : ", montant_heure_normales)
    print("Nombre d'heures supplémentaires : ", nombre_heure_sup)
    print("Montant heures supplémentaires : ", montant_heure_sup)
else:
    Montant_total = montant_heure_normales
    taux_horaire = nbr_heure * taux_horaire
    print("Taux horaire : ", taux_horaire)
    print("Montant des heures normales : ", montant_heure_normales)
    print("Nombre d'heures supplémentaires : 0")
    print("Montant heures supplémentaires : 0")


print("Montant total : ", Montant_total)

# Ce programme calcule le salaire total d'un employé 
# en fonction du nombre d'heures travaillées et du taux horaire.
# Il prend en compte les heures supplémentaires au-delà de 35 heures
# qui sont payées à un taux majoré de 50 %.
