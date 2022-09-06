# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#         return n and not n & n-1

        if n < 1 :
            return False        

        while n % 2 == 0 :
            n /= 2        

        return n == 1

'''Runtime: 28 ms, faster than 97.91% of Python3 online submissions for Power of Two.
Memory Usage: 13.9 MB, less than 52.61% of Python3 online submissions for Power of Two.'''
