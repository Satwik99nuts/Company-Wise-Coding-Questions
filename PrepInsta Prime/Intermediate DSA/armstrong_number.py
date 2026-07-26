def arms(num):
    order = len(str(num))
    total = 0
    orig = num

    while num:
        digit = num % 10
        total += digit**order
        num //= 10

    return total == orig
num = int(input())
if arms(num):
    print("Arm")
else:
    print("Not Arm")
    
    
num = int(input())        
print(arms(num))
