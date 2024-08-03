# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    s += 1
        return s

""" Runtime 43ms Beats 95.62% 
Memory 16.38MB Beats 99.23% """
