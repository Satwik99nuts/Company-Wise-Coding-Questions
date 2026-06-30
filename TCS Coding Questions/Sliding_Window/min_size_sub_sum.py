# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def min_size_sub_arr_sum(nums,target):
    low = 0
    min_len = float("inf")
    window_sum = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        
        while window_sum>=target:
            min_len = min(min_len,i-low+1)
            window_sum -= nums[low]
            low+=1
    return 0 if min_len == float("inf") else min_len
nums = [1,2,3,4,5]        
target = 6
print(min_size_sub_arr_sum(nums,target))