
#Entrée des données
i_nbr = int(input('Combien de livre désirer vous :'))
f_prix = float(input("Prix d'un livre :"))
f_reduc = float(input("Montant de la réduction :"))

#Calcul
f_coeff_reduc = float((100-f_reduc)/100)
f_m = i_nbr * f_prix * f_coeff_reduc

#Affichage dans la console
print('Le montant de la commande est de :',f_m)