# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        n = list(bin(num))
        nums = n[2:]
        nn = []
        for i in nums:
            if i == '0':
                nn.append('1')
            else:
                nn.append('0')
        return int("".join(nn),2)
        
""" Success Details 
Runtime: 41 ms, faster than 60.71% of Python3 online submissions for Number Complement.
Memory Usage: 14 MB, less than 9.10% of Python3 online submissions for Number Complement. """        
