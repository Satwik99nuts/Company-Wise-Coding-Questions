def para(sentence):
    words = sentence.split()
    result = []
    for i, word in enumerate(words):
        if i < len(word):
            result.append(word[i])
    return "".join(result)


sentence = "Satwik is a Great Guy"
print(para(sentence))  # Imd