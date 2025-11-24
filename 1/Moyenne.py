Anglais = float(input("Note en Anglais (coeff.2) : "))
Maths = float(input("Note en Mathematiques (coeff.5) : "))
Info = float(input("Note en Informatique (coeff.2) : "))
c_ang = 2
c_maths = 5
c_info = 3
moy = (Anglais*c_ang+ Maths*c_maths+Info*c_info)/(c_ang+c_maths+c_info)
print("Moyenne obtenue : " , moy)

#Calcul de la moyenne pondérée de trois matières : Anglais, Mathématiques et Informatique, avec des coefficients respectifs de 2, 5 et 3.