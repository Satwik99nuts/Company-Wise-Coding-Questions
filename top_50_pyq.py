# ============================================================
# TCS NQT 2026 – Top 50 Coding Questions in Python
# ============================================================
# HOW TO USE:
#   Each question is wrapped in its own function.
#   Call the function you need from the bottom of this file,
#   or copy-paste individual functions into a new file.
# ============================================================

import math

# ─────────────────────────────────────────────
# 1. Check Even or Odd
# ─────────────────────────────────────────────
def q1_even_odd():
    n = int(input())
    print("Even" if n % 2 == 0 else "Odd")

# ─────────────────────────────────────────────
# 2. Check Prime Number
# ─────────────────────────────────────────────
def q2_prime():
    n = int(input())
    if n <= 1:
        print("Not Prime"); return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Not Prime"); return
    print("Prime")

# ─────────────────────────────────────────────
# 3. Factorial of a Number
# ─────────────────────────────────────────────
def q3_factorial():
    n = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

# ─────────────────────────────────────────────
# 4. Fibonacci Series (First N Terms)
# ─────────────────────────────────────────────
def q4_fibonacci():
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# ─────────────────────────────────────────────
# 5. Reverse a Number
# ─────────────────────────────────────────────
def q5_reverse_number():
    n = int(input())
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    print(rev)

# ─────────────────────────────────────────────
# 6. Check Palindrome Number
# ─────────────────────────────────────────────
def q6_palindrome_number():
    n = int(input())
    temp, rev = n, 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    print("Palindrome" if temp == rev else "Not Palindrome")

# ─────────────────────────────────────────────
# 7. Armstrong Number
# ─────────────────────────────────────────────
def q7_armstrong():
    n = int(input())
    temp, total = n, 0
    while n != 0:
        d = n % 10
        total += d * d * d
        n //= 10
    print("Armstrong" if temp == total else "Not Armstrong")

# ─────────────────────────────────────────────
# 8. Sum of Digits
# ─────────────────────────────────────────────
def q8_sum_digits():
    n = int(input())
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    print(total)

# ─────────────────────────────────────────────
# 9. Largest of Three Numbers
# ─────────────────────────────────────────────
def q9_largest_three():
    a, b, c = map(int, input().split())
    print(max(a, b, c))

# ─────────────────────────────────────────────
# 10. GCD of Two Numbers
# ─────────────────────────────────────────────
def q10_gcd():
    a, b = map(int, input().split())
    while b:
        a, b = b, a % b
    print(a)

# ─────────────────────────────────────────────
# 11. LCM of Two Numbers
# ─────────────────────────────────────────────
def q11_lcm():
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print((a // gcd) * b)   # avoids overflow vs (a*b)//gcd

# ─────────────────────────────────────────────
# 12. Check Leap Year
# ─────────────────────────────────────────────
def q12_leap_year():
    y = int(input())
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")

# ─────────────────────────────────────────────
# 13. Count Vowels and Consonants
# ─────────────────────────────────────────────
def q13_vowels_consonants():
    s = input().lower()
    vowels = consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")

# ─────────────────────────────────────────────
# 14. Reverse a String
# ─────────────────────────────────────────────
def q14_reverse_string():
    s = input()
    print(s[::-1])

# ─────────────────────────────────────────────
# 15. Check Anagram
# ─────────────────────────────────────────────
def q15_anagram():
    s1 = input()
    s2 = input()
    print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")

# ─────────────────────────────────────────────
# 16. Remove Duplicates from String
# ─────────────────────────────────────────────
def q16_remove_duplicates():
    s = input()
    result = ""
    seen = set()
    for ch in s:
        if ch not in seen:
            result += ch
            seen.add(ch)
    print(result)

# ─────────────────────────────────────────────
# 17. Find Second Largest in Array
# ─────────────────────────────────────────────
def q17_second_largest():
    n = int(input())
    arr = list(map(int, input().split()))
    first = second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    print(second)

# ─────────────────────────────────────────────
# 18. Linear Search
# ─────────────────────────────────────────────
def q18_linear_search():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    print("Found" if key in arr else "Not Found")

# ─────────────────────────────────────────────
# 19. Binary Search (Sorted Array)
# ─────────────────────────────────────────────
def q19_binary_search():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    lo, hi = 0, n - 1
    found = False
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == key:
            found = True; break
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    print("Found" if found else "Not Found")

# ─────────────────────────────────────────────
# 20. Bubble Sort
# ─────────────────────────────────────────────
def q20_bubble_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(*arr)

# ─────────────────────────────────────────────
# 21. Selection Sort
# ─────────────────────────────────────────────
def q21_selection_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(*arr)

# ─────────────────────────────────────────────
# 22. Insertion Sort
# ─────────────────────────────────────────────
def q22_insertion_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(*arr)

# ─────────────────────────────────────────────
# 23. Matrix Addition
# ─────────────────────────────────────────────
def q23_matrix_addition():
    r, c = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(r)]
    b = [[int(x) for x in input().split()] for _ in range(r)]
    for i in range(r):
        print(*[a[i][j] + b[i][j] for j in range(c)])

# ─────────────────────────────────────────────
# 24. Transpose of Matrix
# ─────────────────────────────────────────────
def q24_transpose():
    r, c = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(r)]
    for j in range(c):
        print(*[a[i][j] for i in range(r)])

# ─────────────────────────────────────────────
# 25. Count Frequency of Element in Array
# ─────────────────────────────────────────────
def q25_frequency():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    print(arr.count(key))

# ─────────────────────────────────────────────
# 26. Check if Array is Sorted
# ─────────────────────────────────────────────
def q26_is_sorted():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Sorted" if arr == sorted(arr) else "Not Sorted")

# ─────────────────────────────────────────────
# 27. Merge Two Arrays
# ─────────────────────────────────────────────
def q27_merge_arrays():
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    print(*(a + b))

# ─────────────────────────────────────────────
# 28. Find Missing Number (1 to N)
# ─────────────────────────────────────────────
def q28_missing_number():
    n = int(input())
    arr = list(map(int, input().split()))
    print(n * (n + 1) // 2 - sum(arr))

# ─────────────────────────────────────────────
# 29. Count Words in a String
# ─────────────────────────────────────────────
def q29_count_words():
    s = input().strip()
    print(len(s.split()) if s else 0)

# ─────────────────────────────────────────────
# 30. Remove All Spaces from String
# ─────────────────────────────────────────────
def q30_remove_spaces():
    s = input()
    print(s.replace(" ", ""))

# ─────────────────────────────────────────────
# 31. Find Duplicate Elements in Array
# ─────────────────────────────────────────────
def q31_duplicates():
    n = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                print(arr[i], end=" ")
                break

# ─────────────────────────────────────────────
# 32. Move All Zeros to End
# ─────────────────────────────────────────────
def q32_move_zeros():
    n = int(input())
    arr = list(map(int, input().split()))
    non_zeros = [x for x in arr if x != 0]
    result = non_zeros + [0] * (n - len(non_zeros))
    print(*result)

# ─────────────────────────────────────────────
# 33. Rotate Array Right by 1 Position
# ─────────────────────────────────────────────
def q33_rotate_right():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [arr[-1]] + arr[:-1]
    print(*arr)

# ─────────────────────────────────────────────
# 34. Check Palindrome String
# ─────────────────────────────────────────────
def q34_palindrome_string():
    s = input()
    print("Palindrome" if s == s[::-1] else "Not Palindrome")

# ─────────────────────────────────────────────
# 35. Count Number of Digits
# ─────────────────────────────────────────────
def q35_count_digits():
    n = int(input())
    count = 0
    while n != 0:
        n //= 10
        count += 1
    print(count)

# ─────────────────────────────────────────────
# 36. Sum of Elements in Array
# ─────────────────────────────────────────────
def q36_array_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))

# ─────────────────────────────────────────────
# 37. Find Minimum Element in Array
# ─────────────────────────────────────────────
def q37_minimum():
    n = int(input())
    arr = list(map(int, input().split()))
    print(min(arr))

# ─────────────────────────────────────────────
# 38. Pattern Printing (Right Triangle)
# ─────────────────────────────────────────────
def q38_pattern():
    n = int(input())
    for i in range(1, n + 1):
        print("*" * i)

# ─────────────────────────────────────────────
# 39. Power of a Number
# ─────────────────────────────────────────────
def q39_power():
    base, exp = map(int, input().split())
    result = 1
    for _ in range(exp):
        result *= base
    print(result)

# ─────────────────────────────────────────────
# 40. Decimal to Binary
# ─────────────────────────────────────────────
def q40_dec_to_bin():
    n = int(input())
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print(binary if binary else "0")

# ─────────────────────────────────────────────
# 41. Binary to Decimal
# ─────────────────────────────────────────────
def q41_bin_to_dec():
    binary = input()
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            decimal += 2 ** i
    print(decimal)

# ─────────────────────────────────────────────
# 42. Check Perfect Number
# ─────────────────────────────────────────────
def q42_perfect_number():
    n = int(input())
    total = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    print("Perfect" if total == n else "Not Perfect")

# ─────────────────────────────────────────────
# 43. Strong Number
# ─────────────────────────────────────────────
def q43_strong_number():
    n = int(input())
    temp, total = n, 0
    while n != 0:
        d = n % 10
        total += math.factorial(d)
        n //= 10
    print("Strong" if temp == total else "Not Strong")

# ─────────────────────────────────────────────
# 44. Count Even and Odd Numbers in Array
# ─────────────────────────────────────────────
def q44_even_odd_array():
    n = int(input())
    arr = list(map(int, input().split()))
    even = sum(1 for x in arr if x % 2 == 0)
    print(f"Even: {even}")
    print(f"Odd: {n - even}")

# ─────────────────────────────────────────────
# 45. Find Intersection of Two Arrays
# ─────────────────────────────────────────────
def q45_intersection():
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    b_set = set(b)
    for x in a:
        if x in b_set:
            print(x, end=" ")

# ─────────────────────────────────────────────
# 46. Check Substring
# ─────────────────────────────────────────────
def q46_substring():
    s = input()
    sub = input()
    print("Substring Present" if sub in s else "Substring Not Present")

# ─────────────────────────────────────────────
# 47. Remove Specific Character from String
# ─────────────────────────────────────────────
def q47_remove_char():
    s = input()
    ch = input()
    print(s.replace(ch, ""))

# ─────────────────────────────────────────────
# 48. Sum of Prime Numbers up to N
# ─────────────────────────────────────────────
def q48_sum_primes():
    def is_prime(n):
        if n <= 1: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True
    n = int(input())
    print(sum(i for i in range(2, n + 1) if is_prime(i)))

# ─────────────────────────────────────────────
# 49. Reverse Words in a Sentence
# ─────────────────────────────────────────────
def q49_reverse_words():
    s = input()
    print(*s.split()[::-1])

# ─────────────────────────────────────────────
# 50. Two Sum Problem
# ─────────────────────────────────────────────
def q50_two_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                print(i, j)
                return
    print("No Pair Found")


# ─────────────────────────────────────────────
# DRIVER — change the function call below
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Example: call q1_even_odd() to run Question 1
    # Replace with whichever question you want.
    q1_even_odd()