s_sexe = str(input("H/F :"))
f_Weight = float(input("Poids :"))
f_Heigth = float(input("Taille :"))

i_MasseCorp = int(f_Weight/(f_Heigth*f_Heigth))

if (i_MasseCorp >= 25 and s_sexe == "H") or (i_MasseCorp >= 23 and s_sexe == "F"):
    print("Vous devriez surveillez votre alimentation.")
if (i_MasseCorp <= 19 and s_sexe == "H") or (i_MasseCorp <= 18 and s_sexe == "F"):
    print("Vous devriez prendre des forces")
else:
    print("Tout va bien.")