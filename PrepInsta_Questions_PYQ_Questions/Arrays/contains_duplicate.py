# Program for checking duplicate in an array – Duplicate Integer Problem
# return true or false

# brute force --> O(n)
# def check_dup(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# hash-method-->O(n)
def check_dup(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print("Write the values down below : ")
a = list(map(int,input().split()))
print(check_dup(a))