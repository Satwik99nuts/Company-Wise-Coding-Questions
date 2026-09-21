# Given a string and an integer k, return the first k words of the string.
# Example: "Hello I am a passionate developer", k=4 -> "Hello I am a"

def first_k_words(text,k):
    words = text.split()
    return " ".join(words[:k])
print(first_k_words("Hello I am a passionate developer", 4))