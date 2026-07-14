def power_of_two(x):
    if x <=0:
        return False
    return (x&(x-1)) == 0

x = int(input("Write the number you wanna check : "))
print(power_of_two(x))