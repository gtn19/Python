i_N = int(input("Entrez un nombre : "))
i = 0
i_result = 0
while i < i_N:
    i_result += i
    i += 1
print(i_result)


_Vmax = int(input("Entrez un nombre : "))
i = 0
i_result = 0
while i < _Vmax:
    i_result += i
    if i_result >= _Vmax:
        break
    i += 1
print("Iterations : ", i, "Somme : ", i_result)