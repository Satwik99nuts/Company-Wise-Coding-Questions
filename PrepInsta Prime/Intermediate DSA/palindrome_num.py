def pal(n):
    rev = 0
    orig = n
    ispal = False
    while(n!=0):
        rev = (rev*10) + (n%10)
        n = n//10
        
        if orig == rev:
            ispal=True
    return ispal

n = int(input("Write the number = "))
print(pal(n))