y = int(input("Write the number:"))
def fibronacci(y):
    a = 0
    b = 1
    for i in range(1, y):
        c = a + b
        a = b
        b = c
    return a 
print(fibronacci(y))