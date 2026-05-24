# # Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.
# Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: 39
# Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 400
# Explanation: arr3 = 400, which is maximum.

class Solution:
    def max_size_subarr(self, window_size, nums):
        n = len(nums)

        if window_size > n or window_size <= 0:
            return None

        window_sum = sum(nums[:window_size])
        max_sum = window_sum

        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            max_sum = max(max_sum, window_sum)

        return max_sum


n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter array elements: ").split()))
window_size = int(input("Enter window size: "))

if len(nums) != n:
    print("Please enter exactly", n, "elements.")
else:
    obj = Solution()
    result = obj.max_size_subarr(window_size, nums)

    if result is None:
        print("Invalid window size.")
    else:
        print("Maximum sum of subarray of size", window_size, "is:", result)
