# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        i = 0
        while i < len(arr)-1:
            y = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = y
            i += 2
        return arr

""" Runtime 58ms Beats 30.92% of users with Python3 
Memory 16.58 MB Beats 93.76% of users with Python3 """
