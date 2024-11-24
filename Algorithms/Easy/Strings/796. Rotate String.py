# https://leetcode.com/problems/rotate-string/description

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        # for i in range(len(s)):
        #     s = s[1:] + s[0]
        #     if s == goal:
        #         return True
        # return False 

        ds = s+s
        return ds.find(goal) != -1
