# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        N = n*(n+1)//2
        k = isqrt(N)
        return k if N==k*k else -1
        
""" Runtime 32 ms Beats 91.72%
Memory 13.8 MB Beats 51.40%  """     
