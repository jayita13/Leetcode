# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        s = 0
        while left!=right:
            left >>= 1
            right >>= 1

            s += 1

        return left << s

""" Runtime
52
ms
Beats
59.50%
of users with Python3
Memory
16.56
MB
Beats
81.69%
of users with Python3 """      
