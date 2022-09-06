# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(0,n):
            nums.append(start+2*i)
        ans = 0
        for i in nums:
            ans=ans ^ i
        return ans

# Runtime: 24 ms, faster than 98.89% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.8 MB, less than 69.36% of Python3 online submissions for XOR Operation in an Array.
    
