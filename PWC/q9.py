# Given a string of size n, write functions to perform the following operations on a string- Left (Or anticlockwise) rotate the given string by d elements (where d <= n) Right (Or clockwise) rotate the given string by d elements (where d <= n) Example: Input : s = "qwertyu"             
# d = 2 Output : Left rotation : "ertyuqw"               
#                Right rotation : "yuqwert"

def rotate(s,d):
    n = len(s)
    if n==0:
        return s
    d = d % n #edge case, when d > n
    left = s[d:] + s[:d]
    right = s[n-d:] + s[:n-d]
    return left, right

s = "Satwik"
d = 5
print(rotate(s,d))