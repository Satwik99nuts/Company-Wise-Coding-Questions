# Given N packets of chocolates and m students, distribute one packet per
# student such that the difference between the largest and smallest packet
# given out is minimized. Return that minimum difference.
# Example: arr=[7,3,2,4,9,12,56], m=3 -> Output: 2 (pick 2,3,4)

def min_chocolates(arr,m):
    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr)-m+1):
        diff = arr[i+m-1] - arr[i]
        if diff<min_diff:
            min_diff = diff
    return min_diff

arr = [7,3,2,4,9,12,56]
m = 5
print(min_chocolates(arr,m))