s_urStr = input("Entrez une chaîne de caractères : ")
s_urChar = input("Entrez un caractère : ")
print(s_urStr.find(s_urChar))
i=0
ichar = 0
while True:
    if s_urStr[i] == s_urChar:
        ichar += 1
        print("Le caractère", s_urChar, "est présent à l'index", i)
    i+=1
    if i >= len(s_urStr):
        break