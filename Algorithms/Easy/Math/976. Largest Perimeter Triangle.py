# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse = True)
        for a, b, c in zip(A, A[1:], A[2:]):
            if a < b + c:
                return  a+b+c
        return 0
        
""" Runtime: 207 ms, faster than 90.36% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 45.69% of Python3 online submissions for Largest Perimeter Triangle. """        
