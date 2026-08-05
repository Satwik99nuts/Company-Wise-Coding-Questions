# def duplicate(nums):
#     seen = []
#     for i in range(len(nums)):
#         if nums[i] in seen:
#             return True
#         seen.append(nums[i])
#     return False

# cleaner version
def duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False