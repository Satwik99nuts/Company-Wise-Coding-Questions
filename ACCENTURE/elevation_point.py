# A bitonic array first rises and then falls, like a mountain.
# The elevation point is the largest value (the top of that mountain).
# Examples: [1, 2, 3, 4, 3, 2, 1] -> 4; [5, 3] -> 5.


def elevation_point(numbers):
    """Return the peak in a bitonic array using binary search."""
    if not numbers:
        return None

    left = 0
    right = len(numbers) - 1

    # If middle is lower than its right neighbour, the slope still rises.
    # Therefore, the peak must be to the right. Otherwise it is to the left
    # or is middle itself.
    while left < right:
        middle = (left + right) // 2
        if numbers[middle] < numbers[middle + 1]:
            left = middle + 1
        else:
            right = middle

    return numbers[left]


print(elevation_point([1, 2, 3, 4, 3, 2, 1]))  # 4
print(elevation_point([5, 3]))  # 5


# Simpler alternative: check each item one by one. It takes O(n) time,
# while the binary-search solution above takes O(log n).
#
# def elevation_point_by_scanning(numbers):
#     for index, value in enumerate(numbers):
#         bigger_than_left = index == 0 or value > numbers[index - 1]
#         bigger_than_right = index == len(numbers) - 1 or value > numbers[index + 1]
#         if bigger_than_left and bigger_than_right:
#             return value
#     return None
