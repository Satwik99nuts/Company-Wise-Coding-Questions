# How would you design a program to output the characters of a given string, which consists of lowercase characters from 'a' to 'z', in a sorted order? Example: Input : bbccdefbbaa  Output : aabbbbccdef

def sorted_chars(s):
    count = [0]*26
    for ch in s:
        count[ord(ch)-ord('a')]+=1
    res = ""
    for i in range(26):
        res+= chr(i+ord('a'))*count[i]
    return res

s = "bbccdefbbaa"
print(sorted_chars(s))
