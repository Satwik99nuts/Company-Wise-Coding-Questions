x = int(input("Write the number you want factorial of: "))
def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)

print("The factorial of", x, "is", fact(x))