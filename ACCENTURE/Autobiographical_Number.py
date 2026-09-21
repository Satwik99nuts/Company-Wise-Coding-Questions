# A number N (given as a string) is "autobiographical" if, for every position i,
# the digit at position i equals the count of how many times the digit i
# appears in N. If it is autobiographical, return the count of distinct digits
# used in N; otherwise return 0. If the input is None, return 0.
# Example: n="1210" -> Output: 3
# (position 0 says "1" zero -> there's exactly one '0' in "1210": correct.
# position 1 says "2" ones -> there are two '1's in "1210": correct.
# position 2 says "1" two -> there is one '2': correct.
# position 3 says "0" threes -> there are zero '3's: correct.
# So it IS autobiographical. Distinct digits used are {1,2,0} -> 3.)

def autobiographical(n):
    if n is None:
        return 0
    count = [0] * 10  # Count of each digit from 0 to 9
    for digit in n:
        count[int(digit)] += 1
    for i in range(len(n)):
        if count[i] != int(n[i]):
            return 0
    return len(set(n))  # Return the count of distinct digits used in N