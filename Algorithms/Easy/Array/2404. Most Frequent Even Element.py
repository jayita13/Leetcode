# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = []
        
        for num in nums:            
            if num % 2 == 0:
                even.append(num)
        if len(even) == 0:
            return -1
        return Counter(sorted(even)).most_common(1)[0][0]

""" Runtime 225 ms Beats 66.94% of users with Python3 
Memory 17.02 MB  Beats 72.53% of users with Python3 """
