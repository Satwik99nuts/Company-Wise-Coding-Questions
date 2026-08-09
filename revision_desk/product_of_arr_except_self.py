# def proarr(nums):
#     n = len(nums)
#     left_arr = [0]*n
#     right_arr = [0]*n
#     left_mul = 1
#     right_mul = 1

#     for i in range(n):
#         j = -i-1 #basically ye n-2 ko represent kar raha hai
#         left_arr[i] = left_mul
#         right_arr[i] = right_mul

#         left_mul = left_mul*nums[i]
#         right_mul = right_mul*nums[j]

#     return [left_arr[i] * right_arr[n - i - 1] for i in range(n)]


def proarr(nums):
    n = len(nums)
    ans = [1] * n

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans
