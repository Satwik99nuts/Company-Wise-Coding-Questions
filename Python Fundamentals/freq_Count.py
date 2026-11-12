def count_freq(a):
    freq = {}

    for char in a:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 0
    return freq
print(count_freq("Hello Modi Ji"))