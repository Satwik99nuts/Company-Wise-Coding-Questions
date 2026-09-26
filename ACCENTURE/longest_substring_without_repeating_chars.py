def longest_sub(s):
    l = 0
    unique_chars = set()
    window_len = 0
    longest_str = 0

    for r in range(len(s)):
        while s[r] in unique_chars:
            if r in unique_chars:
                unique_chars.remove(s[r])
            lp+=1
        unique_chars.add(s[r])
        window_len = len(s)-l+1
        longest_str = max(window_len,longest_str)
        