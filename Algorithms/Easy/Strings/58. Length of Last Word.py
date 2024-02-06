# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        st = list(s.split(" "))
        return len(st[-1])

  """ Runtime
38
ms
Beats
46.12%
of users with Python3
Memory
16.62
MB
Beats
59.37%
of users with Python3 """
