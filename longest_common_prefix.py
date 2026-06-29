def longest_prefix(x: list[str]) -> str:
    if not x:
        return ""

    x = sorted(x)
    ans = ""
    first = x[0]
    last = x[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]

    return ans


x = ["flower", "flow", "flight"]
print(longest_prefix(x))
