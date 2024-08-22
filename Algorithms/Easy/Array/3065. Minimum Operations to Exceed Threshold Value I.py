# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        for i in nums:
            if i < k:
                c += 1
        return c

""" Runtime 57 ms Beats 7.22% 
Memory 16.50 MB Beats 71.65% """
