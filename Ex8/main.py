f_nbr1 = float(input("Nombre 1 :"))
f_nbr2 = float(input("Nombre 2 :"))

if (f_nbr2 < 0 or f_nbr1 < 0) and not(f_nbr2 < 0 and f_nbr1 < 0):
    print('Résultat négatif')

else:
    print('Résultat positif')
