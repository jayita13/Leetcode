# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))

""" 96 ms 16.5 MB """
