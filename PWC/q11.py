# How can you create a program to display the frequency of each character in a given string, organizing the results in alphabetical order? Example: Input: str = “aabccccddd”  Output: a2b1c4d3 

def count_freq(s):
    freq = {}
    res = ""

    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch] = 1
    for ch in sorted(freq):
        res += ch + str(freq[ch])
    return res

s = "aabccccddd"
print(count_freq(s))