# https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        for i in range(len(s)-2):
            if s[i] == s[i+1] and s[i] == s[i+2]:
                continue
            else:
                ans = ans + s[i]

        return ans + s[-2:]
