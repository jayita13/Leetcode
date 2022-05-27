# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        
        for i in range(n):
            a,b = b,a+b
        return a
        
''' Runtime: 47 ms, faster than 50.85% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 55.02% of Python3 online submissions for Fibonacci Number. '''  
