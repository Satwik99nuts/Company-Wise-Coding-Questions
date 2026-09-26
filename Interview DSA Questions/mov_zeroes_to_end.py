def move_zeroes(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
    return arr
arr = [0,0,0,1,2,0,3]
print(move_zeroes(arr))