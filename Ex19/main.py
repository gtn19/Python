import random
i_RandNum = random.randint(0, 100)
i_turn = 0

while i_turn < 10:
    i_UserNum = int(input("Entrez un nombre entre 0 et 100 : "))
    if i_UserNum == i_RandNum:
        print("Bravo ! Vous avez trouvé le nombre mystère en", i_turn, "tours.")
        break
    else:
        if i_UserNum < i_RandNum:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")
    i_turn += 1