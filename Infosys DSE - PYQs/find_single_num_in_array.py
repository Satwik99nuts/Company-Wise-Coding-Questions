def single_num(nums):
    res = 0
    for n in nums:
        res = res^n
    return res

nums = list(map(int,input().split())) # nums = [4,1,2,1,2] or nums = [7,3,5,3,7]
print(single_num(nums))