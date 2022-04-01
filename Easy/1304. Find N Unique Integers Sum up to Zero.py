# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        tot = 0
        for i in range(1,n):
            res.append(i)
            tot-=i
        res.append(tot)
        return res

'''Runtime: 41 ms, faster than 70.46% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 14 MB, less than 20.07% of Python3 online submissions for Find N Unique Integers Sum up to Zero.'''
