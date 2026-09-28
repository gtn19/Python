s_word = str(input("Entrez un mot :"))
f_wordSize = int(len(s_word)-1)

print(s_word[f_wordSize] + s_word[1:f_wordSize] + s_word[0])