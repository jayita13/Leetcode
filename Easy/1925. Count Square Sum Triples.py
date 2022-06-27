# https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if sqrt(i**2 + j**2)==int(sqrt(i**2 + j**2)) and sqrt(i**2 + j**2) <= n:
                    ans += 1
        return ans
