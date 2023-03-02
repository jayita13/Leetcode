# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            for j in str(i):
                l.append(int(j))
        return l
        
""" Runtime 72 ms Beats 85.70%
Memory 14.5 MB Beats 67.1% """        
