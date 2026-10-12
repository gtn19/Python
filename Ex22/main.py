s_urStr = input("Entrez une chaîne de caractères : ")
while True:
    s_urStr = s_urStr[::-1]
    break
print(s_urStr)
if s_urStr == s_urStr[::-1]:
    print("La chaîne est un palindrome.")