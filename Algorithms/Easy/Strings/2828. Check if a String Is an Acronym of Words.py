# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l = []
        for i in words:
            l.append(i[0])

        if "".join(l) == s:
            return True

""" Runtime
65 ms
Beats
22.21%
Memory
16.2 MB
Beats
76.34% """
