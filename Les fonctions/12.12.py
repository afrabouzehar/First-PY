def decaler_caractere(c, decalage):
    if c is alpha ==False:
        raise ValueError(f"{c}n'est pas alphabet ")
    if c.upper()==True:
        position=ord(c)-ord('A')
        nouvelle_pas=(position+pas)%26
        return chr(ord('A')+position+pas)
    else:
        position=ord(c)-ord('a')
        nouvelle_pas=(position+pas)%26
        return chr(ord('a')+position+pas)    
def decrypter_message(message,decalage):
    message_cryptee=""
    for i in message:
        try:
            message_cryptee+=decaler_caractere(i,decalage)
        except:
            message_cryptee+=i
    return message_cryptee
