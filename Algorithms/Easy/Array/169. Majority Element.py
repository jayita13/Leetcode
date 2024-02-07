# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

  """ Runtime 139ms Beats 53.79% of users with Python3
Memory 18.08 MB Beats 61.80% of users with Python3 """
