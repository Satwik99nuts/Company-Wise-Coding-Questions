# Brute Force Approach ---> O(n**3)

class BruteForceSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        triplet_arr = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in triplet_arr:
                            triplet_arr.append(triplet)

        return triplet_arr


# Optimized Approach ---> O(n**2)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplet_arr = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet_arr.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplet_arr


n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter array elements: ").split()))

if len(nums) != n:
    print("Please enter exactly", n, "elements.")
else:
    brute_force_obj = BruteForceSolution()
    optimized_obj = Solution()

    print("Brute Force Result:", brute_force_obj.threeSum(nums[:]))
    print("Optimized Result:", optimized_obj.threeSum(nums[:]))
