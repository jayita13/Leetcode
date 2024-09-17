# https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = []
        for i in nums:
            diff.append(abs(i))

        val = min(diff)
        return val if val in nums else -val

"""
Runtime 125ms Beats 31.57%
Memory 16.77MB Beats 61.25%
"""
