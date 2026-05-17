a = int(input("Write the number: "))
if(a<1):
    print("Invalid")
else:
    is_Prime = True
for i in range(2,a):
    if(a%i == 0):
        is_Prime = False
        break
    else:
        is_Prime = True

if is_Prime:
    print(a,"is a primr number")
else:
    print(a,"is not a prime number")