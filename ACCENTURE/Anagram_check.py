# Given two strings s and t, determine whether t can be formed by rearranging
# the characters of s (i.e. whether they are anagrams of each other).
# # Example: s="listen", t="silent" -> Output: True

from collections import Counter
def anagram(s,t):
    if Counter(s) == Counter(t):
        return True
    else:
        return False