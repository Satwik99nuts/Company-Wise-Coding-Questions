# How do you print all unique elements from an unsorted integer array that may contain duplicates, ensuring each element is displayed only once in the output? Example: Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45} Output: 12, 10, 9, 45, 2 Input: arr[] = {1, 2, 3, 4, 5} Output: 1, 2, 3, 4, 5

def unique_elements(nums):
    unique = {}
    res = []
    for num in nums:
        if num not in unique:
            res.append(num)
            unique[num]=1
    return res
nums = [12, 10, 9, 45, 2, 10, 10, 45]
print(unique_elements(nums))