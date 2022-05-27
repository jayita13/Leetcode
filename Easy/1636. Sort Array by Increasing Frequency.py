# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x: (nums.count(x), -x))

''' Runtime: 62 ms, faster than 64.13% of Python3 online submissions for Sort Array by Increasing Frequency.
Memory Usage: 13.9 MB, less than 66.69% of Python3 online submissions for Sort Array by Increasing Frequency. '''
