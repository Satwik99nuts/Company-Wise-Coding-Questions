# Given a lower and upper limit, print every palindrome number strictly
# between them.
# Example: 10, 80 -> 11, 22, 33, 44, 55, 66, 77

def pal(low, upper):
    res = []
    for i in range(low+1,upper):
        s = str(i)
        if s == s[::-1]:
            res.append(i)
    return res

print(pal(10,1000))