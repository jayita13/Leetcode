# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(s)) == len(set(pattern)) == len(set(zip_longest(s,pattern)))

""" Runtime 32 ms 
Memory 13.8 MB """
