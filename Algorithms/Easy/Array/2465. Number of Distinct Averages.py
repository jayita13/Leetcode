# https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = []
        while len(nums) > 0:
            mini = min(nums)
            maxi = max(nums)
            ans = (mini+maxi)/2
            avg.append(ans)
            nums.remove(mini)
            nums.remove(maxi)
        return len(set(avg))

""" Runtime
24
ms
Beats
98.58%

Memory
16.63
MB
Beats
15.01%
"""
