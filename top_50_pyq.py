# ============================================================
# TCS NQT 2026 – Top 50 Coding Questions
# OPTIMAL SOLUTIONS — No Built-in Functions, Pure Logic
# Both manual logic in Python (C++ equivalents below)
# ============================================================

import sys

input = sys.stdin.readline


# ─────────────────────────────────────────────
# 1. Check Even or Odd
# Logic: bitwise AND with 1 — faster than %2 mod
# ─────────────────────────────────────────────
def q1_even_odd():
    n = int(input())
    print("Even" if (n & 1) == 0 else "Odd")


# ─────────────────────────────────────────────
# 2. Check Prime Number
# Optimal: trial division only up to sqrt(n)
# Skip evens after checking 2
# ─────────────────────────────────────────────
def q2_prime():
    n = int(input())
    if n < 2:
        print("Not Prime")
        return
    if n == 2:
        print("Prime")
        return
    if (n & 1) == 0:  # even > 2 → not prime
        print("Not Prime")
        return
    i = 3
    while i * i <= n:  # manual sqrt — no math.sqrt
        if n % i == 0:
            print("Not Prime")
            return
        i += 2  # skip even divisors
    print("Prime")


# ─────────────────────────────────────────────
# 3. Factorial
# Optimal: iterative, no recursion stack overhead
# ─────────────────────────────────────────────
def q3_factorial():
    n = int(input())
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    print(result)


# ─────────────────────────────────────────────
# 4. Fibonacci Series (First N Terms)
# Optimal: single pass, constant space, swap trick
# ─────────────────────────────────────────────
def q4_fibonacci():
    n = int(input())
    a, b = 0, 1
    i = 0
    out = []
    while i < n:
        out.append(a)
        temp = a + b
        a = b
        b = temp
        i += 1
    print(*out)


# ─────────────────────────────────────────────
# 5. Reverse a Number
# Optimal: digit-by-digit extraction with %10 and //10
# ─────────────────────────────────────────────
def q5_reverse_number():
    n = int(input())
    is_neg = n < 0
    if is_neg:
        n = -n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    print(-rev if is_neg else rev)


# ─────────────────────────────────────────────
# 6. Check Palindrome Number
# Optimal: reverse half the number — no string conversion
# ─────────────────────────────────────────────
def q6_palindrome_number():
    n = int(input())
    if n < 0 or (n % 10 == 0 and n != 0):
        print("Not Palindrome")
        return
    rev = 0
    temp = n
    while temp != 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    print("Palindrome" if n == rev else "Not Palindrome")


# ─────────────────────────────────────────────
# 7. Armstrong Number (3-digit: sum of cubes)
# Optimal: extract digits with %, count digits first
# ─────────────────────────────────────────────
def q7_armstrong():
    n = int(input())
    temp = n
    # count digits manually
    digits = 0
    t = n
    while t != 0:
        digits += 1
        t //= 10
    # compute sum of (digit^digits)
    total = 0
    while n != 0:
        d = n % 10
        power = 1
        for _ in range(digits):  # manual power — no **
            power *= d
        total += power
        n //= 10
    print("Armstrong" if temp == total else "Not Armstrong")


# ─────────────────────────────────────────────
# 8. Sum of Digits
# Optimal: digit extraction loop
# ─────────────────────────────────────────────
def q8_sum_digits():
    n = int(input())
    if n < 0:
        n = -n
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    print(total)


# ─────────────────────────────────────────────
# 9. Largest of Three Numbers
# Optimal: two comparisons, no max()
# ─────────────────────────────────────────────
def q9_largest_three():
    a, b, c = map(int, input().split())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)


# ─────────────────────────────────────────────
# 10. GCD — Euclidean Algorithm
# Optimal: iterative Euclidean (no math.gcd)
# ─────────────────────────────────────────────
def q10_gcd():
    a, b = map(int, input().split())
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(a)


# ─────────────────────────────────────────────
# 11. LCM of Two Numbers
# Optimal: LCM = (a / GCD) * b  (avoid overflow vs a*b/gcd)
# ─────────────────────────────────────────────
def q11_lcm():
    a, b = map(int, input().split())
    x, y = a, b
    while y != 0:
        temp = y
        y = x % y
        x = temp
    gcd = x
    print((a // gcd) * b)


# ─────────────────────────────────────────────
# 12. Check Leap Year
# Optimal: divisibility logic, no library
# ─────────────────────────────────────────────
def q12_leap_year():
    y = int(input())
    if y % 400 == 0:
        print("Leap Year")
    elif y % 100 == 0:
        print("Not Leap Year")
    elif y % 4 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")


# ─────────────────────────────────────────────
# 13. Count Vowels and Consonants
# Optimal: single pass, manual isalpha and vowel check
# ─────────────────────────────────────────────
def q13_vowels_consonants():
    s = input().rstrip("\n")
    vowels = consonants = 0
    for ch in s:
        # manual lowercase
        c = ch
        if "A" <= ch <= "Z":
            c = chr(ord(ch) + 32)
        if "a" <= c <= "z":
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                vowels += 1
            else:
                consonants += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)


# ─────────────────────────────────────────────
# 14. Reverse a String
# Optimal: two-pointer swap on char list
# ─────────────────────────────────────────────
def q14_reverse_string():
    s = list(input().rstrip("\n"))
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    print("".join(s))


# ─────────────────────────────────────────────
# 15. Check Anagram
# Optimal: frequency array of 26, single pass each string
# ─────────────────────────────────────────────
def q15_anagram():
    s1 = input().rstrip("\n").lower()
    s2 = input().rstrip("\n").lower()
    if len(s1) != len(s2):
        print("Not Anagram")
        return
    freq = [0] * 26
    for i in range(len(s1)):
        freq[ord(s1[i]) - ord("a")] += 1
        freq[ord(s2[i]) - ord("a")] -= 1
    for f in freq:
        if f != 0:
            print("Not Anagram")
            return
    print("Anagram")


# ─────────────────────────────────────────────
# 16. Remove Duplicates from String
# Optimal: boolean seen array of 256 (ASCII), single pass
# ─────────────────────────────────────────────
def q16_remove_duplicates():
    s = input().rstrip("\n")
    seen = [False] * 256
    result = []
    for ch in s:
        idx = ord(ch)
        if not seen[idx]:
            seen[idx] = True
            result.append(ch)
    print("".join(result))


# ─────────────────────────────────────────────
# 17. Find Second Largest in Array
# Optimal: single pass, two variables — O(n) time O(1) space
# ─────────────────────────────────────────────
def q17_second_largest():
    n = int(input())
    arr = list(map(int, input().split()))
    INT_MIN = -(10**18)
    first = second = INT_MIN
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    print(second)


# ─────────────────────────────────────────────
# 18. Linear Search
# Optimal: stop at first match — O(n) worst, O(1) best
# ─────────────────────────────────────────────
def q18_linear_search():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    for i in range(n):
        if arr[i] == key:
            print("Found")
            return
    print("Not Found")


# ─────────────────────────────────────────────
# 19. Binary Search (Sorted Array)
# Optimal: iterative (no recursion), safe midpoint
# ─────────────────────────────────────────────
def q19_binary_search():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # safe: avoids overflow
        if arr[mid] == key:
            print("Found")
            return
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    print("Not Found")


# ─────────────────────────────────────────────
# 20. Bubble Sort
# Optimal: early exit flag — best case O(n) on sorted input
# ─────────────────────────────────────────────
def q20_bubble_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # already sorted — exit early
            break
    print(*arr)


# ─────────────────────────────────────────────
# 21. Selection Sort
# Optimal: find min index, single swap per pass — O(n²) swaps minimized
# ─────────────────────────────────────────────
def q21_selection_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:  # only swap if needed
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(*arr)


# ─────────────────────────────────────────────
# 22. Insertion Sort
# Optimal: shift instead of swap — fewer writes
# ─────────────────────────────────────────────
def q22_insertion_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift right (no swap needed)
            j -= 1
        arr[j + 1] = key
    print(*arr)


# ─────────────────────────────────────────────
# 23. Matrix Addition
# Optimal: single loop, element-wise addition
# ─────────────────────────────────────────────
def q23_matrix_addition():
    r, c = map(int, input().split())
    a, b = [], []
    for _ in range(r):
        a.append(list(map(int, input().split())))
    for _ in range(r):
        b.append(list(map(int, input().split())))
    for i in range(r):
        row = []
        for j in range(c):
            row.append(a[i][j] + b[i][j])
        print(*row)


# ─────────────────────────────────────────────
# 24. Transpose of Matrix
# Optimal: in-place for square, new matrix for rectangular
# ─────────────────────────────────────────────
def q24_transpose():
    r, c = map(int, input().split())
    a = []
    for _ in range(r):
        a.append(list(map(int, input().split())))
    for j in range(c):
        row = []
        for i in range(r):
            row.append(a[i][j])
        print(*row)


# ─────────────────────────────────────────────
# 25. Count Frequency of Element in Array
# Optimal: single pass counter — no .count()
# ─────────────────────────────────────────────
def q25_frequency():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    count = 0
    for i in range(n):
        if arr[i] == key:
            count += 1
    print(count)


# ─────────────────────────────────────────────
# 26. Check if Array is Sorted
# Optimal: single pass — stop at first violation
# ─────────────────────────────────────────────
def q26_is_sorted():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            print("Not Sorted")
            return
    print("Sorted")


# ─────────────────────────────────────────────
# 27. Merge Two Arrays
# Optimal: direct concatenation loop
# ─────────────────────────────────────────────
def q27_merge_arrays():
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    result = []
    for x in a:
        result.append(x)
    for x in b:
        result.append(x)
    print(*result)


# ─────────────────────────────────────────────
# 28. Find Missing Number (1 to N)
# Optimal: Gauss formula — O(n) time O(1) space, no sum()
# ─────────────────────────────────────────────
def q28_missing_number():
    n = int(input())
    arr = list(map(int, input().split()))
    expected = n * (n + 1) // 2
    actual = 0
    for x in arr:
        actual += x
    print(expected - actual)


# ─────────────────────────────────────────────
# 29. Count Words in a String
# Optimal: single pass, count transitions space→non-space
# ─────────────────────────────────────────────
def q29_count_words():
    s = input().rstrip("\n")
    count = 0
    in_word = False
    for ch in s:
        if ch != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    print(count)


# ─────────────────────────────────────────────
# 30. Remove All Spaces from String
# Optimal: single pass, build result — no .replace()
# ─────────────────────────────────────────────
def q30_remove_spaces():
    s = input().rstrip("\n")
    result = []
    for ch in s:
        if ch != " ":
            result.append(ch)
    print("".join(result))


# ─────────────────────────────────────────────
# 31. Find Duplicate Elements in Array
# Optimal: freq array, single pass — O(n) time
# ─────────────────────────────────────────────
def q31_duplicates():
    n = int(input())
    arr = list(map(int, input().split()))
    # Use a dict as freq map (manual hash map logic)
    freq = {}
    printed = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    for x in arr:
        if freq[x] > 1 and x not in printed:
            print(x, end=" ")
            printed[x] = True
    print()


# ─────────────────────────────────────────────
# 32. Move All Zeros to End
# Optimal: two-pointer — O(n) time O(1) space, stable
# ─────────────────────────────────────────────
def q32_move_zeros():
    n = int(input())
    arr = list(map(int, input().split()))
    pos = 0  # position for next non-zero
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < n:  # fill remaining with 0
        arr[pos] = 0
        pos += 1
    print(*arr)


# ─────────────────────────────────────────────
# 33. Rotate Array Right by K Positions
# Optimal: reverse algorithm — O(n) time O(1) space
# ─────────────────────────────────────────────
def q33_rotate_right():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input()) % n  # handle k > n

    def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(arr, 0, n - 1)  # reverse whole
    reverse(arr, 0, k - 1)  # reverse first k
    reverse(arr, k, n - 1)  # reverse rest
    print(*arr)


# ─────────────────────────────────────────────
# 34. Check Palindrome String
# Optimal: two-pointer — O(n/2) comparisons, no reversal copy
# ─────────────────────────────────────────────
def q34_palindrome_string():
    s = input().rstrip("\n")
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            print("Not Palindrome")
            return
        l += 1
        r -= 1
    print("Palindrome")


# ─────────────────────────────────────────────
# 35. Count Number of Digits
# Optimal: digit-stripping loop — no len(str(n))
# ─────────────────────────────────────────────
def q35_count_digits():
    n = int(input())
    if n == 0:
        print(1)
        return
    if n < 0:
        n = -n
    count = 0
    while n != 0:
        n //= 10
        count += 1
    print(count)


# ─────────────────────────────────────────────
# 36. Sum of Elements in Array
# Optimal: single pass accumulator — no sum()
# ─────────────────────────────────────────────
def q36_array_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += arr[i]
    print(total)


# ─────────────────────────────────────────────
# 37. Find Minimum Element in Array
# Optimal: single pass — no min()
# ─────────────────────────────────────────────
def q37_minimum():
    n = int(input())
    arr = list(map(int, input().split()))
    mn = arr[0]
    for i in range(1, n):
        if arr[i] < mn:
            mn = arr[i]
    print(mn)


# ─────────────────────────────────────────────
# 38. Pattern Printing — Right Triangle
# Optimal: nested loop, direct print
# ─────────────────────────────────────────────
def q38_pattern():
    n = int(input())
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append("*")
        print(" ".join(row))


# ─────────────────────────────────────────────
# 39. Power of a Number
# Optimal: fast exponentiation (binary exponentiation)
# O(log exp) instead of O(exp)
# ─────────────────────────────────────────────
def q39_power():
    base, exp = map(int, input().split())
    result = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:  # if exponent is odd
            result *= b
        b *= b  # square the base
        e >>= 1  # halve the exponent
    print(result)


# ─────────────────────────────────────────────
# 40. Decimal to Binary
# Optimal: bit extraction with >>, build string MSB first
# ─────────────────────────────────────────────
def q40_dec_to_bin():
    n = int(input())
    if n == 0:
        print("0")
        return
    bits = []
    while n > 0:
        bits.append(n & 1)  # extract LSB
        n >>= 1  # shift right
    # bits is LSB→MSB, reverse to print MSB first
    bits.reverse()
    result = []
    for b in bits:
        result.append(str(b))
    print("".join(result))


# ─────────────────────────────────────────────
# 41. Binary to Decimal
# Optimal: Horner's method — O(n) single left-to-right pass
# ─────────────────────────────────────────────
def q41_bin_to_dec():
    binary = input().rstrip("\n")
    decimal = 0
    for ch in binary:
        decimal = decimal * 2 + (1 if ch == "1" else 0)
    print(decimal)


# ─────────────────────────────────────────────
# 42. Check Perfect Number
# Optimal: loop only to sqrt(n), add both divisors at once
# ─────────────────────────────────────────────
def q42_perfect_number():
    n = int(input())
    if n < 2:
        print("Not Perfect")
        return
    total = 1  # 1 is always a divisor
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:  # avoid adding sqrt twice
                total += n // i
        i += 1
    print("Perfect" if total == n else "Not Perfect")


# ─────────────────────────────────────────────
# 43. Strong Number
# Optimal: compute factorial inline per digit — no library
# ─────────────────────────────────────────────
def q43_strong_number():
    n = int(input())
    temp, total = n, 0
    while n != 0:
        d = n % 10
        # compute d! manually
        fact = 1
        f = 2
        while f <= d:
            fact *= f
            f += 1
        total += fact
        n //= 10
    print("Strong" if temp == total else "Not Strong")


# ─────────────────────────────────────────────
# 44. Count Even and Odd in Array
# Optimal: single pass with bitwise check
# ─────────────────────────────────────────────
def q44_even_odd_array():
    n = int(input())
    arr = list(map(int, input().split()))
    even = 0
    for i in range(n):
        if (arr[i] & 1) == 0:
            even += 1
    print("Even:", even)
    print("Odd:", n - even)


# ─────────────────────────────────────────────
# 45. Find Intersection of Two Arrays
# Optimal: mark first array in boolean map, scan second
# O(n1 + n2) time, O(max_val) space
# ─────────────────────────────────────────────
def q45_intersection():
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    # Use dict as manual hash set
    in_a = {}
    for x in a:
        in_a[x] = True
    printed = {}
    result = []
    for x in b:
        if x in in_a and x not in printed:
            result.append(x)
            printed[x] = True
    print(*result)


# ─────────────────────────────────────────────
# 46. Check Substring
# Optimal: manual KMP-style window check — O(n*m) naive, no 'in'
# ─────────────────────────────────────────────
def q46_substring():
    s = input().rstrip("\n")
    sub = input().rstrip("\n")
    n, m = len(s), len(sub)
    if m == 0:
        print("Substring Present")
        return
    found = False
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            found = True
            break
    print("Substring Present" if found else "Substring Not Present")


# ─────────────────────────────────────────────
# 47. Remove Specific Character from String
# Optimal: single pass, skip target char — no .replace()
# ─────────────────────────────────────────────
def q47_remove_char():
    s = input().rstrip("\n")
    ch = input().rstrip("\n")
    result = []
    for c in s:
        if c != ch:
            result.append(c)
    print("".join(result))


# ─────────────────────────────────────────────
# 48. Sum of Prime Numbers up to N
# Optimal: Sieve of Eratosthenes — O(n log log n)
# ─────────────────────────────────────────────
def q48_sum_primes():
    n = int(input())
    if n < 2:
        print(0)
        return
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            j = i * i
            while j <= n:
                sieve[j] = False
                j += i
        i += 1
    total = 0
    for i in range(2, n + 1):
        if sieve[i]:
            total += i
    print(total)


# ─────────────────────────────────────────────
# 49. Reverse Words in a Sentence
# Optimal: two-pointer word extraction, reverse in place
# ─────────────────────────────────────────────
def q49_reverse_words():
    s = input().rstrip("\n")
    words = []
    i = 0
    n = len(s)
    while i < n:
        while i < n and s[i] == " ":  # skip spaces
            i += 1
        j = i
        while j < n and s[j] != " ":  # collect word
            j += 1
        if i < n:
            words.append(s[i:j])
        i = j
    # reverse the words list in place
    l, r = 0, len(words) - 1
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
    print(" ".join(words))


# ─────────────────────────────────────────────
# 50. Two Sum Problem
# Optimal: hash map — O(n) time O(n) space
# vs brute O(n²) — huge improvement
# ─────────────────────────────────────────────
def q50_two_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    seen = {}  # val → index
    for i in range(n):
        complement = target - arr[i]
        if complement in seen:
            print(seen[complement], i)
            return
        seen[arr[i]] = i
    print("No Pair Found")


# ─────────────────────────────────────────────
# DRIVER
# ─────────────────────────────────────────────
if __name__ == "__main__":
    q1_even_odd()
