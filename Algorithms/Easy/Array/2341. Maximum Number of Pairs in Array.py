# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        single = set()

        for num in nums:
            if num in single:
                single.remove(num)
                pairs += 1
            else:
                single.add(num)
            
        return [pairs, len(single)]

""" Runtime 44ms Beats 33.76% of users with Python3
Memory 16.35MB Beats 88.03% of users with Python3 """
