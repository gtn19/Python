f_cot1, f_cot2, f_cot3 = int(input("a")),int(input("a")),int(input("a"))
array = [f_cot1,f_cot2,f_cot3]
hyp = max([])
array.remove(hyp)
if f_cot1 == f_cot2 or f_cot1 == f_cot3 or f_cot3 == f_cot2:
    if f_cot2 == f_cot3 == f_cot1:
        print("Equilateral")
    else:
        print("isocèle")
        if hyp**2 == array[0]**2 + array[1]**2:
            print("rectangle")
elif hyp**2 == array[0]**2 + array[1]**2:
    print("rectangle")