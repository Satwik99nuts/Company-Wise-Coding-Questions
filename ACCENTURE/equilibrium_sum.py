# Given an array, find the index where the sum of elements to its left
# equals the sum of elements to its right. Return -1 if no such index exists.
# Example: [3,4,3,1,6] -> Output: 2 (3+4 = 7 on the left, 1+6 = 7 on the right)

def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        value = arr[i]
        right_sum = total_sum - left_sum - value

        if left_sum == right_sum:
            return i
        left_sum += value
    return -1 
print(equilibrium_index([3, 4, 3, 1, 6]))        