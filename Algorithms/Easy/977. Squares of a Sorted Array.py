# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in nums:
        #     ans.append(i**2)
        # return sorted(ans)
        
        return sorted([i**2 for i in nums])
