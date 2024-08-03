# https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sig = 0 
        db = 0
        bob = sum(nums) 
        for i in nums:
            if i < 10:
                sig += i
            elif i >= 10:
                db += i

        if sig > bob - sig or db > bob - db:
            return True
        else:
            return False

""" Runtime 62 ms Beats 20.15%      
Memory 16.40 MB Beats 95.14% """
