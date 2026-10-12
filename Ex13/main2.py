s_word = str(input("Entrez un mot :"))
i_wordSize = int(len(s_word)-1)

print(s_word[i_wordSize] + s_word[1:i_wordSize] + s_word[0])