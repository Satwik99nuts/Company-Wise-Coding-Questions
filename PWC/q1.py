# Given an array of random numbers, Push all the zeros of a given array to the end of the array. For example, if the given array is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be the same. Expected time complexity is O(n) and extra space is O(1). Example: Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0}; Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0}; Input : arr[]  = {1, 2, 0, 0, 0, 3, 6}; Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

def push_zeroes(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[k] = arr[i]
            k+=1
            
    while k<len(arr):
        arr[k] = 0
        k+=1
    return arr
arr = [1,0,0,4,6,0,9,0]
print(push_zeroes(arr))