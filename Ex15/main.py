import random
s_maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s_specChar = ',;:!§%µ*$£}=+-@'
s_result = ''
for i in range(10):
    i_randT = random.randint(0,4)
    if i_randT == 0 :
        i_randT = random.randint(0,len(s_maj)-1)
        s_result += s_maj[i_randT]
    elif i_randT == 1:
        i_randT = random.randint(0,len(s_maj)-1)
        s_result += s_maj[i_randT].lower()
    elif i_randT == 2:
        i_randT = random.randint(0,len(s_specChar)-1)
        s_result += s_specChar[i_randT]
    else:
        i_randT = random.randint(0,9)
        s_result += str(i_randT)
print(s_result)


s_char = ',;:!§%µ*$£}=+-@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
s_result = ''
for i in range(10):
    i_randT = random.randint(0,len(s_char)-1)
    s_result += s_char[i_randT]
print(s_result)