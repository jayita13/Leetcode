# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            res = set()
            for j in range(i, len(nums)):
                res.add(nums[j])
                ans += pow(len(res), 2)
        return ans

""" Runtime 68ms Beats 80.43%
Memory 16.62 MB Beats 23.60% """
