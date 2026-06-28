def pal(x):
    dup = x
    last_digits = 0
    rev = 0
    while dup!=0:
        last_digits = dup%10
        rev = rev*10 + last_digits
        dup = dup//10
    return rev

x = int(input("Write the number whose last digits you wanna extract = "))
print(pal(x))