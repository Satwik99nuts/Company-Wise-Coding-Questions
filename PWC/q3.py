# Given an array arr[] of integers, segregate even and odd numbers in the array such that all the even numbers should be present first, and then the odd numbers. Example: Input: arr[] = {7, 2, 9, 4, 6, 1, 3, 8, 5} Output: 2 4 6 8 7 9 1 3 5 Input: arr[] = {1, 3, 2, 4, 7, 6, 9, 10} Output:  2 4 6 10 7 1 9 3


def segregate_even_odd(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        if arr[left]%2==0:
            left+=1
        elif arr[right]%2!=0:
            right-=1
        else:
            arr[left],arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return arr
arr = [1, 3, 2, 4, 7, 6, 9, 10]
print(segregate_even_odd(arr))