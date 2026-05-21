class Solution:
    def three_sum_closest(self, nums: list[int], target: int):
        n = len(nums)
        nums.sort()

        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum
        return closest_sum


n = int(input("Enter number of elements: ").strip().lstrip("\ufeff"))
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

if len(nums) != n:
    print("Please enter exactly", n, "elements.")
else:
    obj = Solution()
    print("Closest Sum:", obj.three_sum_closest(nums, target))
