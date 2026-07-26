def reve(n):
    rev = 0
    ld = 0
    
    while(n!=0):
        ld = n%10
        rev = rev*10+ld
        n = n//10
    return rev

n = int(input("Write it: "))
print(reve(n))