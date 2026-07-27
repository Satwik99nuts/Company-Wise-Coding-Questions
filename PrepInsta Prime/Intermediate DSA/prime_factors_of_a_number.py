def prime_fac_of_num(num):
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num = num // i
        i += 2

    if num > 2:
        factors.append(num)

    return factors


num = int(input("Enter number: ").lstrip("\ufeff"))
print(prime_fac_of_num(num))
