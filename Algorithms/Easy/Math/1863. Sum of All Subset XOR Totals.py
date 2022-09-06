# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
 
        for i in nums:
            bits |= i

        return bits * pow(2, len(nums)-1)
        
""" Runtime: 45 ms, faster than 92.64% of Python3 online submissions for Sum of All Subset XOR Totals.
Memory Usage: 13.9 MB, less than 71.29% of Python3 online submissions for Sum of All Subset XOR Totals. """       
