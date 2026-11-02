f_a1 = 2
f_b1 = 1

area_rectangle_2 = 16

f_a2 = (f_a1 + f_b1) /2
f_b2 = area_rectangle_2 / f_a2
print(f_a2, f_b2)
area_rectangle_2 = f_a1 * f_b1

f_a3 = (f_a2 + f_b2) /2
f_b3 = area_rectangle_2 / f_a3
area_rectangle_3 = f_a3 * f_b3
print(f_a3, f_b3)
while f_a3 - f_b3 < 1*10**-5 :
    f_a2 = (f_a3 + f_b3) /2
    f_b2 = area_rectangle_3 / f_a3
    area_rectangle_2 = f_a3 * f_b3

    f_a3 = (f_a2 + f_b2) /2
    f_b3 = area_rectangle_2 / f_a3
    area_rectangle_3 = f_a3 * f_b3

