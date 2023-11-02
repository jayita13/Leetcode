# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s1,s2 = 0,0
        for i in range(1,n+1):
            if i%m != 0:
                s1 += i
            else:
                s2 += i
        return s1 - s2

""" Runtime
Details
41ms
Beats 67.19%of users with Python3
Memory
Details
16.27MB
Beats 40.73%of users with Python3 """
