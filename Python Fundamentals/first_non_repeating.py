def non_repeating(a):

    freq = {}
    count = 0

    for i in a:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    for char in a:
        if freq[char] == 1:
            return char
    return None
print(non_repeating("Satwik"))