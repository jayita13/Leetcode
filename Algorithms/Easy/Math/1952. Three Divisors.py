# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        s = 0
        for i in range(1,n+1):
            if n % i == 0:
                s+=1
        return True if s == 3 else False

""" Success Details 
Runtime: 80 ms, faster than 31.36% of Python3 online submissions for Three Divisors.
Memory Usage: 13.9 MB, less than 58.04% of Python3 online submissions for Three Divisors. """
