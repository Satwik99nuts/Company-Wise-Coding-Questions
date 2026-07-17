# A person stands at point O and can walk North, South, East, or West. You're given a string of characters (N/S/E/W) representing the sequence of directions walked. You may change any character in the string to any of the other three directions. Find the minimum number of changes needed so the person ends back at O. If it's impossible, return -1.
# Sample: ENNE → output 2 (convert the two N's to W's, or the two E's to S's).
# Sample: EEN → output -1 (odd length can never return to origin).

def min_changes(s):
    n = len(s)
    if n%2!=0:
        return -1
    countN = s.count('N')
    countS = s.count('S')
    countE = s.count('E')
    countW = s.count('W')
    
    return (abs(countN-countS) + abs(countE-countW))//2

s = input("Write the string, but in capital as written in the function : ")
print(min_changes(s))