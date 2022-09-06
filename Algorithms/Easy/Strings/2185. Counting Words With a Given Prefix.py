# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for word in words:
            if word.startswith(pref):
                c+=1
        return c

''' Runtime: 36 ms, faster than 97.40% of Python3 online submissions for Counting Words With a Given Prefix.
Memory Usage: 14 MB, less than 32.44% of Python3 online submissions for Counting Words With a Given Prefix. '''
