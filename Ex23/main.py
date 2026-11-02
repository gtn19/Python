i_urInt = str(input("Entrez un nombre : "))
i_urBase = int(input("Entrez une base : "))
s_nbrltr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_result = ""
while i_urInt != "0":
    print(int(i_urInt) % i_urBase)
    if int(i_urInt) % i_urBase != 0:
        s_result += s_nbrltr[int(i_urInt) % i_urBase]
    else:
        s_result += "0"

    i_urInt = str(int(i_urInt) // i_urBase)

print("Le nombre en base", i_urBase, "est :", s_result[::-1])