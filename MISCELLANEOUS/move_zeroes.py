def move_zeroes(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
