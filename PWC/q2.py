# Given a sorted array of positive integers, rearrange the array alternately i.e first element should be a maximum value, at second position minimum value, at third position second max, at fourth position second min, and so on.  Example: Input: arr[] = {1, 2, 3, 4, 5, 6, 7}  Output: arr[] = {7, 1, 6, 2, 5, 3, 4} Input: arr[] = {1, 2, 3, 4, 5, 6}  Output: arr[] = {6, 1, 5, 2, 4, 3} 

def alt_max_min(arr):
    left = 0 
    right = len(arr) - 1
    arr.sort()
    result = []
    while left<=right:
        if left<=right:
            result.append(right)
            right-=1
        elif left<=right:
            result.append(left)
            left+=1
    return result

arr = [1,2,3,6,6,7,8,9,4]
print(alt_max_min(arr))