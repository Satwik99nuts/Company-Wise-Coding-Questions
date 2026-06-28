def move_zeroes(nums:list[int])->None:
    left = 0
    n = len(nums)
    for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1

nums = [1,2,0,5,7,0]
print("Before Swapping",nums)
move_zeroes(nums)
print("After Swapping",nums)