# Program for checking if two strings are Anagram of each other – Is Anagram?
# anagram means that the two strings contain the same set of letters
from collections import Counter
def valid_anagram(char1,char2)->bool:
    dchar1 = Counter(char1)
    dchar2 = Counter(char2)
    return dchar1 == dchar2

char1 = input("Write the first character: ")
char2 = input("Write the second character: ")
print(valid_anagram)