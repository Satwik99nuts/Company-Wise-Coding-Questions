# How can you write a program to identify and print the leaders in an array, considering an element as a leader if it surpasses all the elements to its right, with the rightmost element always being classified as a leader? Example: Input: arr[] = {16, 17, 4, 3, 5, 2},  Output: 17, 5, 2   Input: arr[] = {1, 2, 3, 4, 5, 2},  Output: 5, 2

def leader_arr(nums):
    res = []
    max_right = float('-inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>max_right:
            res.append(nums[i])
            max_right = nums[i]
    return res[::-1]

nums = [16,17,4,3,5,2]
print(leader_arr(nums))