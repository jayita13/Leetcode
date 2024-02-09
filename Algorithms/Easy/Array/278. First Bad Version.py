# https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right)//2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

""" Runtime
39
ms
Beats
33.95%
of users with Python3
Memory
16.50
MB
Beats
75.61%
of users with Python3 """  
