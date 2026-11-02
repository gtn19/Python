s_urStr = input("Entrez une chaîne de caractères : ")
i = 0
s_result = ""
while i < len(s_urStr):
    s_result += s_urStr[len(s_urStr) - 1 - i]
    i += 1
print(s_result)
i=0
while i < int(len(s_urStr )/2):
    if s_urStr[i] == s_urStr[len(s_urStr) - 1 - i]:
        print("Le caractère", s_urStr[i], "est le même que le caractère", s_urStr[len(s_urStr) - 1 - i])
        print("La chaîne est un palindrome pour le moment.")
        i+=1
    else:
        print("Le caractère", s_urStr[i], "n'est pas le même que le caractère", s_urStr[len(s_urStr) - 1 - i])
        print("La chaîne n'est pas un palindrome.")
        break


# if s_urStr == s_result:
#     print("La chaîne est un palindrome.")