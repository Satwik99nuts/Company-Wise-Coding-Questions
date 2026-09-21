# Given an array (length > 3, all elements unique), treat index 0 as even.
# Return the sum of the second-largest element among even-indexed elements
# and the second-smallest element among odd-indexed elements. Return 0 if the
# array is empty or has length <= 3.
# Example: [3,2,1,7,5,4] -> even positions (0,2,4): [3,1,5], odd positions
# (1,3,5): [2,7,4]. Second-largest of [3,1,5] is 3. Second-smallest of
# [2,7,4] is 4. Output: 3+4 = 7

def sec_lar(arr):
    if len(arr)<=3 or len(arr)==0:
        return 0

    even = []
    odd = []

    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    sec_largest = even[-2]
    sec_smallest = odd[1]

    return sec_largest+sec_smallest

print(sec_lar([3, 2, 1, 7, 5, 4]))