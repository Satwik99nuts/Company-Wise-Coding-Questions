# Given a string of words and spaces, return the length of the last word.
# Example: " I am a passionate Developer " -> Output: 9 ("Developer")


def last_word(s):
    words = s.split()
    if len(words)<0:
        return 0
    return len(words[-1])

s = input("Write your sentence : ")
print(last_word(s))