# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i > 0:
                s.add(i)
        return len(s)
            
""" Runtime: 68 ms, faster than 35.00% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
Memory Usage: 13.9 MB, less than 15.05% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts. """            
