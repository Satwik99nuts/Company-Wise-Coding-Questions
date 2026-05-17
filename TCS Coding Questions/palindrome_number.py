c = int(input("Write the number to check: "))
rev = 0
temp = c
while(c!=0):
    rev = rev*10 + c%10
    c = c//10
if(temp==rev):
    print("Palindrome Number")
else:
    print("Not Palindrome")