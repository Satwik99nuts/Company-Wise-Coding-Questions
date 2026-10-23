def sum_of_digits(num):
    sum_nums=0
    while(num>0):
        ld = num%10
        sum_nums+=ld
        num=num//10
    return sum_nums

num = int(input("Write the number : "))
print(sum_of_digits(num))