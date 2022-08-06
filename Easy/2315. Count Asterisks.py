# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split("|")
        c = 0
        for i in range(0, len(l), 2):
            c+= l[i].count("*")
        return c
                
""" Runtime: 58 ms, faster than 33.29% of Python3 online submissions for Count Asterisks.
Memory Usage: 13.9 MB, less than 13.66% of Python3 online submissions for Count Asterisks. """                
