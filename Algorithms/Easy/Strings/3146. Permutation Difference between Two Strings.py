# https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in s: 
            ans += abs(s.index(i)- t.index(i))

        return ans

""" Runtime 42ms Beats 36.74% 
Memory 16.54MB Beats 22.77% """
