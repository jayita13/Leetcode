# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/submissions/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1)=="".join(word2)

# Runtime: 63 ms, faster than 13.97% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 13.9 MB, less than 81.20% of Python3 online submissions for Check If Two String Arrays are Equivalent.
