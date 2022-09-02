# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
        
# Runtime: 69 ms, faster than 45.10% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 88.63% of Python3 online submissions for Isomorphic Strings.       
