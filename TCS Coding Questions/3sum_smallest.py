# Given an array of n integers nums and a target, find the number of
# index triplets i, j, k with 0 <= i < j < k < n such that:
# nums[i] + nums[j] + nums[k] < target


class Solution:
    def threeSumSmallest(self, nums, target):
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


nums = [-2, 0, 1, 3]
target = 2

obj = Solution()
print(obj.threeSumSmallest(nums, target))
