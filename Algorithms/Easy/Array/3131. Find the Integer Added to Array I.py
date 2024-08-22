# https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)
        # return nums2[0] - nums1[0]
        return min(nums2) - min(nums1)

""" Runtime 48ms Beats 72.86%
Memory 16.45 MB Beats 80.53% """
