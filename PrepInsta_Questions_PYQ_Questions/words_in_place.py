def words_in_place(s):
    words = s.split()
    left, right = 0,len(words)-1
    
    while left<right:
        words[right],words[left] = words[left],words[right]
        left+=1
        right-=1
    return " ".join(words)

s = input("Write a Sentence : ")
print(words_in_place(s))