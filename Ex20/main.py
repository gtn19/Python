i_nbr = int(input("Entrez un nombre : "))
i = 0
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

while i_nbr != 1:
    if is_prime(i) and i_nbr % i == 0:
        i_nbr -= i_nbr / i
        print(i)
    else:
        i+=1