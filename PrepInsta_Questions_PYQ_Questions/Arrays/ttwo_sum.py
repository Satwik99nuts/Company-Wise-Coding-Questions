def two_sum(nums:list[int],target:int)->list[int]:
    # brute force
    # n = len(nums)
    # for i in range(n+1):
    #     for j in range(i+1,n+1):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]


    # optimal -> using hashmap
    mil_gaya = {}
    for i, num in enumerate(nums):
        bacha_hua = target - nums[i]
        if bacha_hua in mil_gaya:
            return [mil_gaya[bacha_hua],i]
        mil_gaya[num] = i
    
nums = [2,7,11,15]
target = 26
print(two_sum(nums,target))