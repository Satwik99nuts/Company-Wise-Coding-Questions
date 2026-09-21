# Given two non-negative integers, count how many carries occur when adding
# them digit by digit from right to left.
# Example: num1=451, num2=349 -> Output: 2

def count_carry(int1,int2):
    carry = 0
    count = 0

    while int1>0 and int2>0:
        digit1 = int1%10
        digit2 = int2%10

        total = digit1+digit2+carry

        if total>=10:
            count+=1
            carry = 1
        int1 = int1//10
        int2 = int2//10
    return count