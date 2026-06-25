# Pair with Given Sum – 2Sum Problem
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

def two_sum(nums:list[int],target:int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target and i<j or j<i:
                return i,j
nums = list(map(int,input().split()))
target = int(input("Write the target: "))

print(two_sum(nums,target))