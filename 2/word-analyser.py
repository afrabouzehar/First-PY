word = str(input("Entrez une phrase ou un paragraphe : "))
nbr_caracteres = len(word)
print("Nombre total de caracteres :", nbr_caracteres)
nbr_mots = len(word.split())
print("Nombre total de mots :", nbr_mots)
majuscules = word.upper()
print("Texte en majuscules :", majuscules)
minuscules = word.lower()
print("Texte en minuscules :", minuscules)
caracteres_recherches = input("Entrez un caractere a rechercher : ")
nbr=0
for i in word:
    if i == caracteres_recherches:
        nbr += 1
print("Le caractere", caracteres_recherches, "apparaît", nbr, "fois dans le texte.")
palindrome = word.replace(" ", "").lower()
inverse = ""
for i in range(len(palindrome)-1, -1, -1):
    inverse += palindrome[i]
if palindrome == inverse:
    print("Le texte est un palindrome.")
else:
    print("Le texte n'est pas un palindrome.")
print("Le texte inversé est :", inverse)
   