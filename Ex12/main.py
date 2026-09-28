f_cot1, f_cot2, f_cot3 = float(input("a")),float(input("a")),float(input("a"))
array = [f_cot1,f_cot2,f_cot3]
hyp = max(array)
array.remove(hyp)
if ( not (f_cot1 - f_cot2) < 0 and not (f_cot1 - f_cot2) > 0 or not (f_cot3 - f_cot2) < 0 and not (f_cot3 - f_cot2) > 0 or not (f_cot1 - f_cot3) < 0 and not (f_cot1 - f_cot3) > 0):
    if not (f_cot1 - f_cot2 + f_cot3) < 0 + f_cot1 and not (f_cot1 - f_cot2 + f_cot3) > 0 + f_cot2:
        print("Equilateral")
    else:
        print("Isocèle")
if not(hyp**2 - (array[0]**2 + array[1]**2)) < 0 and not(hyp**2 - (array[0]**2 + array[1]**2)) > 0:
    print(" rectangle")