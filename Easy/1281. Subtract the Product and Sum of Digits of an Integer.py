#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = str(n)
        p = 1
        s = 0
        for i in res:
            p = p * int(i)
            s = s + int(i)
        
        return p-s