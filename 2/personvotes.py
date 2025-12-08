Liste_Noms=["Yasmine", "Amine","Yasmine", "Omar", "Yasmine", "Amine", "Omar", "Amine", "Yasmine", "Sara", "Omar","Yasmine", "Sara"]
Nbr_Votes = {}
for nom in Liste_Noms:
    if nom in Nbr_Votes:
        Nbr_Votes[nom] += 1 
    else:
        Nbr_Votes[nom] = 1
print("Resultas des votes :",Nbr_Votes)
max_votes = max(Nbr_Votes)
print("Candidat avec le plus de votes :", max_votes,"avec", Nbr_Votes[max_votes], "votes")



    
    
