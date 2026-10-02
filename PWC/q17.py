# How can you create a program to generate bit patterns ranging from 0 to 2^N-1, ensuring that each successive pattern differs from the previous one by only one bit? Example: Input: N = 2 Output: 00 01 11 10 Input: N = 3 Output: 000 001 011 010 110 111 101 100

def succ_bits(n):
    res = [""]
    for _ in range(n):
        new = []
        for i in res:
            new.append("0" + i)
        for i in reversed(res):
            new.append("1" + i)
        res = new
    return res

print(succ_bits(5))