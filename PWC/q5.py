# # LC - 350
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersection(nums1, nums2):
    count = {}

    for i in range(len(nums1)):
        if nums1[i] in count:
            count[nums1[i]]+=1
        else:
            count[nums1[i]] = 1
    res = []

    for j in range(len(nums2)):
        if nums2[j] in count and count[nums2[j]]>0:
            res.append(nums2[j])
            count[nums2[j]]-=1
    return res

nums1 = [1, 1, 1, 2, 2]
nums2 = [1, 1, 1, 1, 2, 2, 2, 3]
print(intersection(nums1,nums2))