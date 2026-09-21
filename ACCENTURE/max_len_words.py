def max_len_of_word(s):
    longest = s[0]

    for i in s:
        if len(i)>len(longest):
            longest = i
    return longest
print(max_len_of_word(["yes", "no", "number"]))