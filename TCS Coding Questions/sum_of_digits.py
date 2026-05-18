digit = int(input("Write the number : "))
sum = 0

i = 0
while(digit!=0):
    sum += digit%10
    digit=digit//10

print(sum)