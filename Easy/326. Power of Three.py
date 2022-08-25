# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 :
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1
        
""" Runtime: 128 ms, faster than 56.55% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 57.97% of Python3 online submissions for Power of Three. """        
