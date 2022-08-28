# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        else:
            if num%10 == 0:
                return False
            return True

'''Runtime: 49 ms, faster than 33.14% of Python3 online submissions for A Number After a Double Reversal.
Memory Usage: 13.8 MB, less than 56.37% of Python3 online submissions for A Number After a Double Reversal.'''
