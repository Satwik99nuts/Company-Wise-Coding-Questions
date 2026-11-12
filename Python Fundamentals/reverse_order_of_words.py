sentence = "I am Satwik"
words = sentence.split()
result = []
i = len(words) - 1
while i>=0:
    result.append(words[i])
    i-=1
print(" ".join(result))
