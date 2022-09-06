# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original*=2
            
        return original
        
'''Runtime: 89 ms, faster than 48.78% of Python3 online submissions for Keep Multiplying Found Values by Two.
Memory Usage: 14.1 MB, less than 20.19% of Python3 online submissions for Keep Multiplying Found Values by Two.'''
