def est_palindrome(chaine):
    word_reverse = ""
    for i in range(len(chaine)-1,-1,-1):
        word_reverse+=chaine[i]
    return (chaine == word_reverse)
word=  

