// ============================================================
// TCS NQT 2026 – Top 50 Coding Questions in C++
// OPTIMAL SOLUTIONS — No Built-in STL Algorithms, Pure Logic
// Compile: g++ -O2 -o tcs50 tcs50_optimal.cpp
// ============================================================

#include <bits/stdc++.h>
using namespace std;

// ─────────────────────────────────────────────
// 1. Check Even or Odd
// Optimal: bitwise AND — faster than %2
// ─────────────────────────────────────────────
void q1_even_odd() {
    int n; cin >> n;
    cout << ((n & 1) == 0 ? "Even" : "Odd") << "\n";
}

// ─────────────────────────────────────────────
// 2. Check Prime Number
// Optimal: skip evens, trial up to sqrt — no sqrt()
// ─────────────────────────────────────────────
void q2_prime() {
    int n; cin >> n;
    if (n < 2)          { cout << "Not Prime\n"; return; }
    if (n == 2)         { cout << "Prime\n";     return; }
    if ((n & 1) == 0)   { cout << "Not Prime\n"; return; }
    for (int i = 3; i * i <= n; i += 2) {   // skip evens
        if (n % i == 0) { cout << "Not Prime\n"; return; }
    }
    cout << "Prime\n";
}

// ─────────────────────────────────────────────
// 3. Factorial
// Optimal: iterative — no recursion stack overhead
// ─────────────────────────────────────────────
void q3_factorial() {
    int n; cin >> n;
    long long result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    cout << result << "\n";
}

// ─────────────────────────────────────────────
// 4. Fibonacci Series (First N Terms)
// Optimal: single pass, constant space
// ─────────────────────────────────────────────
void q4_fibonacci() {
    int n; cin >> n;
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        long long temp = a + b;
        a = b;
        b = temp;
    }
    cout << "\n";
}

// ─────────────────────────────────────────────
// 5. Reverse a Number
// Optimal: digit-by-digit with %10 and /10
// ─────────────────────────────────────────────
void q5_reverse_number() {
    long long n; cin >> n;
    bool neg = (n < 0);
    if (neg) n = -n;
    long long rev = 0;
    while (n != 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    cout << (neg ? -rev : rev) << "\n";
}

// ─────────────────────────────────────────────
// 6. Check Palindrome Number
// Optimal: reverse and compare — no string conversion
// ─────────────────────────────────────────────
void q6_palindrome_number() {
    int n; cin >> n;
    if (n < 0 || (n % 10 == 0 && n != 0)) {
        cout << "Not Palindrome\n"; return;
    }
    int temp = n, rev = 0;
    while (n != 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    cout << (temp == rev ? "Palindrome" : "Not Palindrome") << "\n";
}

// ─────────────────────────────────────────────
// 7. Armstrong Number
// Optimal: count digits first, then compute digit^digits
// Manual power — no pow()
// ─────────────────────────────────────────────
void q7_armstrong() {
    int n; cin >> n;
    int temp = n;
    // count digits
    int digits = 0, t = n;
    while (t != 0) { digits++; t /= 10; }
    // sum of digit^digits
    long long total = 0;
    while (n != 0) {
        int d = n % 10;
        long long power = 1;
        for (int i = 0; i < digits; i++) power *= d;  // manual power
        total += power;
        n /= 10;
    }
    cout << (temp == total ? "Armstrong" : "Not Armstrong") << "\n";
}

// ─────────────────────────────────────────────
// 8. Sum of Digits
// Optimal: digit extraction loop
// ─────────────────────────────────────────────
void q8_sum_digits() {
    int n; cin >> n;
    if (n < 0) n = -n;
    int total = 0;
    while (n != 0) {
        total += n % 10;
        n /= 10;
    }
    cout << total << "\n";
}

// ─────────────────────────────────────────────
// 9. Largest of Three Numbers
// Optimal: two comparisons — no max()
// ─────────────────────────────────────────────
void q9_largest_three() {
    int a, b, c; cin >> a >> b >> c;
    if (a >= b && a >= c)      cout << a << "\n";
    else if (b >= a && b >= c) cout << b << "\n";
    else                       cout << c << "\n";
}

// ─────────────────────────────────────────────
// 10. GCD — Euclidean Algorithm
// Optimal: iterative — no __gcd()
// ─────────────────────────────────────────────
void q10_gcd() {
    int a, b; cin >> a >> b;
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    cout << a << "\n";
}

// ─────────────────────────────────────────────
// 11. LCM of Two Numbers
// Optimal: LCM = (a / GCD) * b — avoids overflow
// ─────────────────────────────────────────────
void q11_lcm() {
    long long a, b; cin >> a >> b;
    long long x = a, y = b;
    while (y != 0) { long long t = y; y = x % y; x = t; }
    long long gcd = x;
    cout << (a / gcd) * b << "\n";
}

// ─────────────────────────────────────────────
// 12. Check Leap Year
// Optimal: cascaded divisibility — no library
// ─────────────────────────────────────────────
void q12_leap_year() {
    int y; cin >> y;
    if      (y % 400 == 0) cout << "Leap Year\n";
    else if (y % 100 == 0) cout << "Not Leap Year\n";
    else if (y % 4   == 0) cout << "Leap Year\n";
    else                   cout << "Not Leap Year\n";
}

// ─────────────────────────────────────────────
// 13. Count Vowels and Consonants
// Optimal: single pass, manual lowercase, char comparison
// ─────────────────────────────────────────────
void q13_vowels_consonants() {
    string s; getline(cin, s);
    int vowels = 0, consonants = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        char c = s[i];
        if (c >= 'A' && c <= 'Z') c = c + 32;  // manual lowercase
        if (c >= 'a' && c <= 'z') {
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
                vowels++;
            else
                consonants++;
        }
    }
    cout << "Vowels: "     << vowels     << "\n";
    cout << "Consonants: " << consonants << "\n";
}

// ─────────────────────────────────────────────
// 14. Reverse a String
// Optimal: two-pointer swap — O(n/2), in-place
// ─────────────────────────────────────────────
void q14_reverse_string() {
    string s; getline(cin, s);
    int l = 0, r = (int)s.size() - 1;
    while (l < r) {
        char tmp = s[l]; s[l] = s[r]; s[r] = tmp;
        l++; r--;
    }
    cout << s << "\n";
}

// ─────────────────────────────────────────────
// 15. Check Anagram
// Optimal: frequency array of 26 — O(n), no sort
// ─────────────────────────────────────────────
void q15_anagram() {
    string s1, s2; cin >> s1 >> s2;
    if (s1.size() != s2.size()) { cout << "Not Anagram\n"; return; }
    int freq[26] = {};
    for (int i = 0; i < (int)s1.size(); i++) {
        freq[s1[i] - 'a']++;
        freq[s2[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++)
        if (freq[i] != 0) { cout << "Not Anagram\n"; return; }
    cout << "Anagram\n";
}

// ─────────────────────────────────────────────
// 16. Remove Duplicates from String
// Optimal: boolean seen[256] array — O(n) single pass
// ─────────────────────────────────────────────
void q16_remove_duplicates() {
    string s; cin >> s;
    bool seen[256] = {};
    string result = "";
    for (int i = 0; i < (int)s.size(); i++) {
        int idx = (unsigned char)s[i];
        if (!seen[idx]) {
            seen[idx] = true;
            result += s[i];
        }
    }
    cout << result << "\n";
}

// ─────────────────────────────────────────────
// 17. Find Second Largest in Array
// Optimal: single pass, two variables — O(n) O(1)
// ─────────────────────────────────────────────
void q17_second_largest() {
    int n; cin >> n;
    int first = INT_MIN, second = INT_MIN;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        if (x > first)                        { second = first; first = x; }
        else if (x > second && x != first)    { second = x; }
    }
    cout << second << "\n";
}

// ─────────────────────────────────────────────
// 18. Linear Search
// Optimal: early exit on first match
// ─────────────────────────────────────────────
void q18_linear_search() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int key; cin >> key;
    for (int i = 0; i < n; i++)
        if (arr[i] == key) { cout << "Found\n"; return; }
    cout << "Not Found\n";
}

// ─────────────────────────────────────────────
// 19. Binary Search (Sorted Array)
// Optimal: iterative, safe midpoint lo+(hi-lo)/2
// ─────────────────────────────────────────────
void q19_binary_search() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int key; cin >> key;
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;   // safe — avoids int overflow
        if      (arr[mid] == key) { cout << "Found\n";     return; }
        else if (arr[mid] <  key)   lo = mid + 1;
        else                        hi = mid - 1;
    }
    cout << "Not Found\n";
}

// ─────────────────────────────────────────────
// 20. Bubble Sort
// Optimal: early exit swapped flag — O(n) best case
// ─────────────────────────────────────────────
void q20_bubble_sort() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = tmp;
                swapped = true;
            }
        }
        if (!swapped) break;   // already sorted
    }
    for (int i = 0; i < n; i++) cout << arr[i] << " \n"[i==n-1];
}

// ─────────────────────────────────────────────
// 21. Selection Sort
// Optimal: only swap when min_idx changed — fewer swaps
// ─────────────────────────────────────────────
void q21_selection_sort() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx]) min_idx = j;
        if (min_idx != i) {
            int tmp = arr[i]; arr[i] = arr[min_idx]; arr[min_idx] = tmp;
        }
    }
    for (int i = 0; i < n; i++) cout << arr[i] << " \n"[i==n-1];
}

// ─────────────────────────────────────────────
// 22. Insertion Sort
// Optimal: shift (not swap) — fewer writes per iteration
// ─────────────────────────────────────────────
void q22_insertion_sort() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 1; i < n; i++) {
        int key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];   // shift right — no swap
            j--;
        }
        arr[j + 1] = key;
    }
    for (int i = 0; i < n; i++) cout << arr[i] << " \n"[i==n-1];
}

// ─────────────────────────────────────────────
// 23. Matrix Addition
// Optimal: single nested loop, element-wise
// ─────────────────────────────────────────────
void q23_matrix_addition() {
    int r, c; cin >> r >> c;
    int a[r][c], b[r][c];
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) cin >> a[i][j];
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) cin >> b[i][j];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            cout << a[i][j] + b[i][j] << " \n"[j==c-1];
    }
}

// ─────────────────────────────────────────────
// 24. Transpose of Matrix
// Optimal: swap indices to transpose
// ─────────────────────────────────────────────
void q24_transpose() {
    int r, c; cin >> r >> c;
    int a[r][c];
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) cin >> a[i][j];
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++)
            cout << a[i][j] << " \n"[i==r-1];
    }
}

// ─────────────────────────────────────────────
// 25. Count Frequency of Element
// Optimal: single pass — no count()
// ─────────────────────────────────────────────
void q25_frequency() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int key; cin >> key;
    int count = 0;
    for (int i = 0; i < n; i++) if (arr[i] == key) count++;
    cout << count << "\n";
}

// ─────────────────────────────────────────────
// 26. Check if Array is Sorted
// Optimal: single pass, stop at first violation
// ─────────────────────────────────────────────
void q26_is_sorted() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) { cout << "Not Sorted\n"; return; }
    }
    cout << "Sorted\n";
}

// ─────────────────────────────────────────────
// 27. Merge Two Arrays
// Optimal: direct copy loop
// ─────────────────────────────────────────────
void q27_merge_arrays() {
    int n1; cin >> n1;
    int a[n1]; for (int i = 0; i < n1; i++) cin >> a[i];
    int n2; cin >> n2;
    int b[n2]; for (int i = 0; i < n2; i++) cin >> b[i];
    for (int i = 0; i < n1; i++) cout << a[i] << " ";
    for (int i = 0; i < n2; i++) cout << b[i] << " \n"[i==n2-1];
}

// ─────────────────────────────────────────────
// 28. Find Missing Number (1 to N)
// Optimal: Gauss formula — O(n) O(1), no sum()
// ─────────────────────────────────────────────
void q28_missing_number() {
    int n; cin >> n;
    long long expected = (long long)n * (n + 1) / 2;
    long long actual = 0;
    for (int i = 0; i < n - 1; i++) { int x; cin >> x; actual += x; }
    cout << expected - actual << "\n";
}

// ─────────────────────────────────────────────
// 29. Count Words in a String
// Optimal: track space→non-space transitions
// ─────────────────────────────────────────────
void q29_count_words() {
    string s; getline(cin, s);
    int count = 0;
    bool in_word = false;
    for (int i = 0; i < (int)s.size(); i++) {
        if (s[i] != ' ') {
            if (!in_word) { count++; in_word = true; }
        } else {
            in_word = false;
        }
    }
    cout << count << "\n";
}

// ─────────────────────────────────────────────
// 30. Remove All Spaces from String
// Optimal: single pass, write non-spaces — no replace()
// ─────────────────────────────────────────────
void q30_remove_spaces() {
    string s; getline(cin, s);
    string result = "";
    for (int i = 0; i < (int)s.size(); i++)
        if (s[i] != ' ') result += s[i];
    cout << result << "\n";
}

// ─────────────────────────────────────────────
// 31. Find Duplicate Elements in Array
// Optimal: freq array — O(n) time, single pass
// ─────────────────────────────────────────────
void q31_duplicates() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    // For general integers, use a map manually
    // Assuming values 1..n for TCS context
    int freq[n + 1];
    for (int i = 0; i <= n; i++) freq[i] = 0;
    for (int i = 0; i < n; i++) freq[arr[i]]++;
    bool found = false;
    for (int i = 1; i <= n; i++)
        if (freq[i] > 1) { cout << i << " "; found = true; }
    if (!found) cout << "No duplicates";
    cout << "\n";
}

// ─────────────────────────────────────────────
// 32. Move All Zeros to End
// Optimal: two-pointer — O(n) O(1), stable order
// ─────────────────────────────────────────────
void q32_move_zeros() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int pos = 0;
    for (int i = 0; i < n; i++)
        if (arr[i] != 0) arr[pos++] = arr[i];
    while (pos < n) arr[pos++] = 0;
    for (int i = 0; i < n; i++) cout << arr[i] << " \n"[i==n-1];
}

// ─────────────────────────────────────────────
// 33. Rotate Array Right by K
// Optimal: reverse algorithm — O(n) O(1)
// ─────────────────────────────────────────────
void q33_rotate_right() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int k; cin >> k;
    k %= n;

    auto rev = [&](int l, int r) {
        while (l < r) { int t = arr[l]; arr[l] = arr[r]; arr[r] = t; l++; r--; }
    };
    rev(0, n - 1);   // reverse whole array
    rev(0, k - 1);   // reverse first k
    rev(k, n - 1);   // reverse rest
    for (int i = 0; i < n; i++) cout << arr[i] << " \n"[i==n-1];
}

// ─────────────────────────────────────────────
// 34. Check Palindrome String
// Optimal: two-pointer — O(n/2), no copy
// ─────────────────────────────────────────────
void q34_palindrome_string() {
    string s; cin >> s;
    int l = 0, r = (int)s.size() - 1;
    while (l < r) {
        if (s[l] != s[r]) { cout << "Not Palindrome\n"; return; }
        l++; r--;
    }
    cout << "Palindrome\n";
}

// ─────────────────────────────────────────────
// 35. Count Number of Digits
// Optimal: digit-stripping loop — no to_string / log10
// ─────────────────────────────────────────────
void q35_count_digits() {
    int n; cin >> n;
    if (n == 0) { cout << 1 << "\n"; return; }
    if (n < 0) n = -n;
    int count = 0;
    while (n != 0) { n /= 10; count++; }
    cout << count << "\n";
}

// ─────────────────────────────────────────────
// 36. Sum of Elements in Array
// Optimal: single pass accumulator — no accumulate()
// ─────────────────────────────────────────────
void q36_array_sum() {
    int n; cin >> n;
    long long total = 0;
    for (int i = 0; i < n; i++) { int x; cin >> x; total += x; }
    cout << total << "\n";
}

// ─────────────────────────────────────────────
// 37. Find Minimum Element in Array
// Optimal: single pass — no min() or sort
// ─────────────────────────────────────────────
void q37_minimum() {
    int n; cin >> n;
    int mn; cin >> mn;
    for (int i = 1; i < n; i++) {
        int x; cin >> x;
        if (x < mn) mn = x;
    }
    cout << mn << "\n";
}

// ─────────────────────────────────────────────
// 38. Pattern Printing — Right Triangle
// Optimal: nested loop, direct output
// ─────────────────────────────────────────────
void q38_pattern() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++)
            cout << "* ";
        cout << "\n";
    }
}

// ─────────────────────────────────────────────
// 39. Power of a Number
// Optimal: Binary Exponentiation — O(log exp) vs O(exp)
// ─────────────────────────────────────────────
void q39_power() {
    long long base, exp; cin >> base >> exp;
    long long result = 1;
    long long b = base;
    while (exp > 0) {
        if (exp & 1) result *= b;  // odd exponent: multiply
        b *= b;                    // square the base
        exp >>= 1;                 // halve the exponent
    }
    cout << result << "\n";
}

// ─────────────────────────────────────────────
// 40. Decimal to Binary
// Optimal: bit extraction with >> operator
// ─────────────────────────────────────────────
void q40_dec_to_bin() {
    int n; cin >> n;
    if (n == 0) { cout << "0\n"; return; }
    int bits[32], cnt = 0;
    while (n > 0) {
        bits[cnt++] = n & 1;   // extract LSB
        n >>= 1;               // shift right
    }
    for (int i = cnt - 1; i >= 0; i--)  // print MSB first
        cout << bits[i];
    cout << "\n";
}

// ─────────────────────────────────────────────
// 41. Binary to Decimal
// Optimal: Horner's method — O(n) single left-to-right pass
// avoids computing 2^i separately
// ─────────────────────────────────────────────
void q41_bin_to_dec() {
    string binary; cin >> binary;
    long long decimal = 0;
    for (int i = 0; i < (int)binary.size(); i++)
        decimal = decimal * 2 + (binary[i] == '1' ? 1 : 0);
    cout << decimal << "\n";
}

// ─────────────────────────────────────────────
// 42. Check Perfect Number
// Optimal: loop to sqrt(n), add both divisors at once
// Halves iterations vs naive loop to n/2
// ─────────────────────────────────────────────
void q42_perfect_number() {
    int n; cin >> n;
    if (n < 2) { cout << "Not Perfect\n"; return; }
    long long total = 1;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            total += i;
            if (i != n / i) total += n / i;  // avoid counting sqrt twice
        }
    }
    cout << (total == n ? "Perfect" : "Not Perfect") << "\n";
}

// ─────────────────────────────────────────────
// 43. Strong Number
// Optimal: inline factorial per digit — no precomputed array needed
// ─────────────────────────────────────────────
void q43_strong_number() {
    int n; cin >> n;
    int temp = n;
    long long total = 0;
    while (n != 0) {
        int d = n % 10;
        long long fact = 1;
        for (int f = 2; f <= d; f++) fact *= f;  // d! inline
        total += fact;
        n /= 10;
    }
    cout << (temp == total ? "Strong" : "Not Strong") << "\n";
}

// ─────────────────────────────────────────────
// 44. Count Even and Odd in Array
// Optimal: single pass, bitwise check
// ─────────────────────────────────────────────
void q44_even_odd_array() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int even = 0;
    for (int i = 0; i < n; i++)
        if ((arr[i] & 1) == 0) even++;
    cout << "Even: " << even     << "\n";
    cout << "Odd: "  << n - even << "\n";
}

// ─────────────────────────────────────────────
// 45. Find Intersection of Two Arrays
// Optimal: mark first array, scan second — O(n1+n2)
// Manual boolean array (assumes values 0..10000)
// ─────────────────────────────────────────────
void q45_intersection() {
    int n1; cin >> n1;
    int a[n1]; for (int i = 0; i < n1; i++) cin >> a[i];
    int n2; cin >> n2;
    int b[n2]; for (int i = 0; i < n2; i++) cin >> b[i];

    bool in_a[10001] = {};
    bool printed[10001] = {};
    for (int i = 0; i < n1; i++) in_a[a[i]] = true;
    for (int i = 0; i < n2; i++) {
        if (in_a[b[i]] && !printed[b[i]]) {
            cout << b[i] << " ";
            printed[b[i]] = true;
        }
    }
    cout << "\n";
}

// ─────────────────────────────────────────────
// 46. Check Substring
// Optimal: manual sliding window O(n*m) — no find()
// ─────────────────────────────────────────────
void q46_substring() {
    string s, sub;
    getline(cin, s);
    getline(cin, sub);
    int n = s.size(), m = sub.size();
    if (m == 0) { cout << "Substring Present\n"; return; }
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && s[i + j] == sub[j]) j++;
        if (j == m) { cout << "Substring Present\n"; return; }
    }
    cout << "Substring Not Present\n";
}

// ─────────────────────────────────────────────
// 47. Remove Specific Character from String
// Optimal: single pass, skip target — no replace()
// ─────────────────────────────────────────────
void q47_remove_char() {
    string s; getline(cin, s);
    char ch; cin >> ch;
    string result = "";
    for (int i = 0; i < (int)s.size(); i++)
        if (s[i] != ch) result += s[i];
    cout << result << "\n";
}

// ─────────────────────────────────────────────
// 48. Sum of Prime Numbers up to N
// Optimal: Sieve of Eratosthenes — O(n log log n)
// ─────────────────────────────────────────────
void q48_sum_primes() {
    int n; cin >> n;
    if (n < 2) { cout << 0 << "\n"; return; }
    bool sieve[n + 1];
    for (int i = 0; i <= n; i++) sieve[i] = true;
    sieve[0] = sieve[1] = false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= n; j += i)
                sieve[j] = false;
        }
    }
    long long total = 0;
    for (int i = 2; i <= n; i++) if (sieve[i]) total += i;
    cout << total << "\n";
}

// ─────────────────────────────────────────────
// 49. Reverse Words in a Sentence
// Optimal: collect words, reverse array — O(n) O(n)
// ─────────────────────────────────────────────
void q49_reverse_words() {
    string s; getline(cin, s);
    string words[100];
    int wc = 0, i = 0, n = s.size();
    while (i < n) {
        while (i < n && s[i] == ' ') i++;      // skip spaces
        int j = i;
        while (j < n && s[j] != ' ') j++;      // collect word
        if (i < n) words[wc++] = s.substr(i, j - i);
        i = j;
    }
    for (int k = wc - 1; k >= 0; k--)          // reverse order
        cout << words[k] << (k == 0 ? "\n" : " ");
}

// ─────────────────────────────────────────────
// 50. Two Sum Problem
// Optimal: hash map O(n) — vs brute force O(n²)
// Manual open-addressing hash map
// ─────────────────────────────────────────────
void q50_two_sum() {
    int n; cin >> n;
    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];
    int target; cin >> target;

    // Manual hash map: key=value, value=index
    // Use array of pairs, linear probing
    const int SZ = 20011;  // prime size
    int ht_key[SZ], ht_val[SZ];
    bool ht_used[SZ];
    for (int i = 0; i < SZ; i++) ht_used[i] = false;

    auto hfind = [&](int key) -> int {
        int h = ((key % SZ) + SZ) % SZ;
        while (ht_used[h] && ht_key[h] != key) h = (h + 1) % SZ;
        return h;
    };

    for (int i = 0; i < n; i++) {
        int complement = target - arr[i];
        int h = hfind(complement);
        if (ht_used[h] && ht_key[h] == complement) {
            cout << ht_val[h] << " " << i << "\n"; return;
        }
        // insert arr[i] -> i
        int ih = hfind(arr[i]);
        ht_key[ih] = arr[i]; ht_val[ih] = i; ht_used[ih] = true;
    }
    cout << "No Pair Found\n";
}

// ─────────────────────────────────────────────
// DRIVER — change function call below
// ─────────────────────────────────────────────
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Replace with whichever question you want to run:
    q1_even_odd();
    return 0;
}