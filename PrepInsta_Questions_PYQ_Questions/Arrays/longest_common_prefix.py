def longest(s:list[str]):
    s.sort()
    first = s[0]
    last = s[-1]
    ans = ""
    min_len = min(len(first),len(last))

    for i in range(min_len):
        if first[i]!=last[i]:
            return ans
        ans+=last[i]
    return ans

s = ["flower", "flow", "flight"]
print(longest(s))