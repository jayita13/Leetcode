# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1 :
            return False

        while n % 4 == 0:
            n /= 4

        return n == 1

""" Runtime: 75 ms, faster than 6.98% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four. """
