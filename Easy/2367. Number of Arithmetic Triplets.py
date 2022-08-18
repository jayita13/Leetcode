# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = 0
        for i in range(len(nums)-2):
            if nums[i] + diff in nums and nums[i] + 2*diff in nums:
                c+=1
        return c

""" Runtime: 73 ms, faster than 53.24% of Python3 online submissions for Number of Arithmetic Triplets.
Memory Usage: 13.8 MB, less than 97.79% of Python3 online submissions for Number of Arithmetic Triplets. """
