def sec_large_el(arr):
    n = len(arr)
    largest = float('-inf')
    sec_largest = float('-inf')
    
    for i in range(len(arr)):
        if arr[i]>largest:
            sec_largest = largest
            largest = arr[i]
    return sec_largest

arr = [1,2,3,4,5,6]
print(sec_large_el(arr))