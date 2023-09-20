def from_ten_to_n(num, n):
    num_n = ''
    while num != 0:
        num_n += str(num % n)
        num //= n
    return num_n[::-1]

def from_n_to_ten(num, n):
    num_n = 0
    for i in range(len(str(num))):
        num_n += int(str(num)[::-1][i]) * n ** i
    return num_n

def transformations(n):
    n_2 = from_ten_to_n(n, 2)

    if n % 5 == 0:
        n_2 += n_2[-3:]
    else:
        n_2 = from_ten_to_n(n % 5 * 5, 2) + n_2
    return from_n_to_ten(n_2, 2)

for i in range(1, 99):
    if transformations(i) > 512:
        print(i)
        break




