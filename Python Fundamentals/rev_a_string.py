def rev_str(a):
    # res = ""
    # for char in a:
    #     res = char + res
    # return res

    result = ""
    i = len(a) - 1
    while i>=0:
        result += a[i]
        i-=1
    return result
print(rev_str("String"))