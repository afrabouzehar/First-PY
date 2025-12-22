def est_palindrome(chaine):
    chaine=chaine.lower()
    word_reverse = ""
    for i in range(len(chaine)-1,-1,-1):
        word_reverse+=chaine[i]
    return (chaine == word_reverse)
word= str(input("Entrez un mot : "))
print(est_palindrome(word))