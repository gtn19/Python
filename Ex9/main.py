i_age = input("Quelle age :")
f_prix = input("Prix du billet :")

def calculer_Prix():
    if i_age < 2:
        f_prix = 0
    elif i_age <10:
        f_prix = f_prix / 2
    elif i_age < 27 or i_age > 70:
        f_prix = f_prix*0.9