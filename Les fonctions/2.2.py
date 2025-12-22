def trouver_max(Liste):
    max=Liste[0]    
    for i in Liste:
        if i>max:
            max=i
    return(max)
Liste_nbr=[98,45,34,34,54,32,76,75,43]
print("Le plus grand nombre est :", trouver_max(Liste_nbr))