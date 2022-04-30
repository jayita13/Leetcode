# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = dict()
        for i in arr:
            res[i] = res.get(i,0) + 1
        c = 0
        ans = Counter(res.values())
        for i in ans.values():
            if i>1:
                return False
        return True

''' Runtime: 56 ms, faster than 35.35% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14.1 MB, less than 36.98% of Python3 online submissions for Unique Number of Occurrences. '''
