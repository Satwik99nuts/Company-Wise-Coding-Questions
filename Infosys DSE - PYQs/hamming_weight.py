# So hamming weight is essential for the error detection and correction, cryptography and process level  algorithms

def hamming(x):
    count = 0
    while(x>0):
        x = x&(x-1)
        count+=1
    return count

x = 10
print(hamming(x))
    