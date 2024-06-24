# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_s = 0
        for i in range(len(s)-1):
            sum_s += abs(ord(s[i]) - ord(s[i+1]))  
        
        return sum_s

""" 
Runtime 32ms Beats 82.29%
Analyze Complexity Memory 16.40MB Beats 53.51%
"""
