def sumofdigits(n):
    ld = 0
    summ = 0
    while(n!=0):
        ld = n%10
        summ+=ld
        n = n//10
    return summ

n = int(input("Write the number: "))
print(sumofdigits(n))        