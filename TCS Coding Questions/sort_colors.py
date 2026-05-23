# Sort Colors
# Given an array containing only 0, 1, and 2, sort it in-place.


class Solution:
    def sortColors(self, nums) -> None:
        """
        Best approach: Dutch National Flag algorithm.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


class SolutionCounting:
    def sortColors(self, nums) -> None:
        """
        Better approach: count 0s, 1s, and 2s, then rebuild the same list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        zero_count = 0
        one_count = 0
        two_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1

        nums[:] = (
            [0] * zero_count
            + [1] * one_count
            + [2] * two_count
        )


class SolutionUsingExtraArrays:
    def sortColors(self, nums) -> None:
        """
        Brute force approach: store values in separate arrays, then combine them.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        zeros = []
        ones = []
        twos = []

        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num == 1:
                ones.append(num)
            else:
                twos.append(num)

        # Slice assignment updates the original list object in-place.
        nums[:] = zeros + ones + twos


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]

    obj = Solution()
    obj.sortColors(nums)

    print(nums)
