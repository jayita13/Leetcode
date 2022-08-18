# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for i in words:
            if set(i).issubset(allowed):
                c+=1
        return c

""" Runtime: 308 ms, faster than 77.49% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 16 MB, less than 86.72% of Python3 online submissions for Count the Number of Consistent Strings. """
