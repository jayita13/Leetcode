# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = str(n)
        p = 1
        s = 0
        for i in res:
            p = p * int(i)
            s = s + int(i)
        
        return p-s

# Runtime: 39 ms, faster than 63.50% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.9 MB, less than 15.70% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
