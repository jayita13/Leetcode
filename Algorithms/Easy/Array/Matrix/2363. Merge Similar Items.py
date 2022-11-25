# https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = Counter(dict(items1))
        cnt += Counter(dict(items2))
        return sorted(cnt.items())
        
""" Success Details  
Runtime: 136 ms, faster than 92.77% of Python3 online submissions for Merge Similar Items.
Memory Usage: 14.8 MB, less than 11.36% of Python3 online submissions for Merge Similar Items. """        
