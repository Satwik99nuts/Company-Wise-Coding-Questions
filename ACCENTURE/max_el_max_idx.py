def max_el_idx(arr):
    max_el = arr[0]
    max_idx = 0

    for i in range(len(arr)):
        if arr[i]>max_el:
            max_el = arr[i]
            max_idx = i
    return max_el, max_idx
arr = [23, 45, 82, 27, 66, 12, 78, 13, 71, 86]
print(max_el_idx(arr))
value, idx = max_el_idx([23, 45, 82, 27, 66, 12, 78, 13, 71, 86])
print(value)
print(idx)