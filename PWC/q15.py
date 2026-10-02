# How can you create a program to eliminate all occurrences of a specific character within a given string? Example: Input : s = "sustainability"            c = 'i' Output : s = "sustanablty"  

def remove_chars(s,c):
    res = ""
    for i in range(len(s)):
        if s[i]!= c:
            res+=s[i]
    return res

s = "Satwik"
c = "k"
print(remove_chars(s,c))