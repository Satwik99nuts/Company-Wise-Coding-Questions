def lcs(a, b):
    x = len(a)
    y = len(b)

    dp = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    print(lcs(a, b))

"""
A **subsequence** means characters appear in the same order, but they do not need to be continuous.

Example:

```python
a = "abcde"
b = "ace"
```

The LCS is `"ace"`, so answer is `3`.

**Code Idea**

```python
dp[i][j]
```

means:

> LCS length between first `i` characters of `a` and first `j` characters of `b`.

So:

```python
dp[3][2]
```

means LCS of:

```text
a first 3 chars = "abc"
b first 2 chars = "ac"
```

**DP Table Size**

```python
dp = [[0] * (y + 1) for _ in range(x + 1)]
```

We create one extra row and column for empty string cases.

For:

```text
a = abcde
b = ace
```

Table size is:

```text
6 rows x 4 columns
```

Rows represent `a`:

```text
"", a, b, c, d, e
```

Columns represent `b`:

```text
"", a, c, e
```

Initial table:

```text
      ""  a  c  e
""     0  0  0  0
a      0  0  0  0
b      0  0  0  0
c      0  0  0  0
d      0  0  0  0
e      0  0  0  0
```

**Rule 1: Characters Match**

```python
if a[i-1] == b[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
```

If characters match, take diagonal value and add `1`.

Example:

```text
a[0] == b[0]
'a' == 'a'
```

So:

```python
dp[1][1] = dp[0][0] + 1 = 1
```

**Rule 2: Characters Do Not Match**

```python
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

If characters do not match, take the best answer from:

```text
top cell    -> ignoring current char of a
left cell   -> ignoring current char of b
```

**Dry Run**

Input:

```text
abcde
ace
```

Final DP table becomes:

```text
      ""  a  c  e
""     0  0  0  0
a      0  1  1  1
b      0  1  1  1
c      0  1  2  2
d      0  1  2  2
e      0  1  2  3
```

Important cells:

```text
'a' == 'a' -> dp[1][1] = 1
'c' == 'c' -> dp[3][2] = 2
'e' == 'e' -> dp[5][3] = 3
```

Finally:

```python
return dp[x][y]
```

Here:

```python
dp[5][3] = 3
```

So output is:

```text
3
```

In simple words: the code builds answers for smaller parts of the strings, then uses them to find the final LCS length.
"""
