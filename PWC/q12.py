# How do you design a program to perform a series of character swaps on a given string S of length N, starting from the beginning, with each swap involving the character at position i and the character located C positions ahead (i + C)%N? Additionally, the process is repeated B times, moving one position at a time, and the goal is to determine the final string after these B swaps. Example: Input : S = "ABCDEFGH", B = 4, C = 3; Output:  DEFGBCAH Explanation:          after 1st swap: DBCAEFGH          after 2nd swap: DECABFGH          after 3rd swap: DEFABCGH          after 4th swap: DEFGBCAH 

def char_swap(s,b,c):
    s = list(s) # as strings are immutable so we just have to convert it into a list
    n = len(s)

    for i in range(b):
        j = (i+c) % n
        s[i], s[j] = s[j], s[i]
    return "".join(s)
print(char_swap("ABCDEFGH", 4, 3))