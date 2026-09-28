i_age = int(input("Quelle age :"))
f_prix = input("Prix du billet :")

def calculer_Prix():
    if i_age < 2:
        f_prix = 0
    if i_age <10 and i_age > 2:
        f_prix = f_prix / 2
    if i_age < 27 or i_age > 70:
        f_prix = f_prix*0.9
    return f_prix


print("Le prix du billet est de : ",calculer_Prix())