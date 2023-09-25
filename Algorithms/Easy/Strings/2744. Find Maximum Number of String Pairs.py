# https://leetcode.com/problems/find-maximum-number-of-string-pairs

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = 0
        for i in words:
            j = i[::-1]
            if j in words[:words.index(i)] or j in words[words.index(i)+1:]:
                s += 1
                words.remove(j)
        return s

""" Runtime Details
60ms Beats 33.37%of users with Python3
Memory Details
16.24MB Beats 64.60%of users with Python3 """
