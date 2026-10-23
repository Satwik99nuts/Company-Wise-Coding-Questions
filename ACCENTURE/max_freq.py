# For every word in a string:
# 1. Ignore extra spaces between words.
# 2. Extract the first and last character of each word.
# 3. Count how frequently each combination appears.
# 4. Return only the combination(s) with the highest frequency, preserving their original order of appearance.
# Example
# Input:
# apple ant banana axe apple


# Step 1: Extract first + last character.
# Word	Combination
# apple	ae
# ant	at
# banana	ba
# axe	ae
# apple	ae
# Step 2: Count frequencies.
# Combination	Frequency
# ae	3
# at	1
# ba	1
# Output:
# ae


# Here, ae appears three times, more frequently than the other combinations.

def max_freq_word(s):
    words = s.split()

    req_words = []
    for word in words:
        req_word = word[0] + word[-1]
        req_words.append(req_word)

    freq = {}
    for req_word in req_words:
        freq[req_word] = freq.get(req_word,0)+1
    max_freq = max(freq.values())


    res = []
    for req_word in req_words:
        if req_word not in res and freq[req_word] == max_freq:
            res.append(req_word)
    return res

s = "apple ant banana axe apple"
print(max_freq_word(s))
