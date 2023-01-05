# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = collections.Counter(text)
        b = collections.Counter("balloon")
        return min([t[c]//b[c] for c in b])
 
""" Runtime 30 ms
Beats 95.30% """
