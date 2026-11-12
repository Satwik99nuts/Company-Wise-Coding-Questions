def count_vowels(a):
    count = 0
    for j in a:
        if j.lower() in "aeiou":
            count+=1
    return count

print(count_vowels("aeiou"))