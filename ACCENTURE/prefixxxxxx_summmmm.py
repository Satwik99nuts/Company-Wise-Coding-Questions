def prefix_sum(nums):

    prefix_arr = []
    count = 0

    for i in range(len(nums)):
        count+=nums[i]
        prefix_arr.append(count)
    return prefix_arr

def ranged_sum(left, right, prefix_arr):
    if left==0:
        return prefix_arr[right]
    return prefix_arr[right] - prefix_arr[left-1]


arr = [2, 4, -1, 3, 5]
prefix = prefix_sum(arr)

print(prefix)                     # [2, 6, 5, 8, 13]
print(ranged_sum(1, 3,prefix))    # 6
print(ranged_sum(2, 4,prefix))    # 7