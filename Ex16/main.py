
import random
s_char = ',;:!§%µ*$£}=+-@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
s_result = ''
while len(s_result) < 10:
    i_randT = random.randint(0,len(s_char)-1)
    s_result += s_char[i_randT]
print(s_result)