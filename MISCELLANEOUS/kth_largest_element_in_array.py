import heapq


def kth_largest_in_array(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError("k must be between 1 and the length of nums")

    heap = []
    for number in nums:
        heapq.heappush(heap, number)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest_in_array(nums, k))
