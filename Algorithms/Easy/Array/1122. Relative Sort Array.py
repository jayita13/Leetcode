# https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        return sorted(A, key=(B + sorted(A)).index)
        
""" Runtime 53 ms
Beats 77.82%
Memory 14 MB """
