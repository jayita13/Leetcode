# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        while len(nums) > 0:
            mini = min(nums)
            maxi = max(nums)
            ans = (mini+maxi)/2
            avg.append(ans)
            nums.remove(mini)
            nums.remove(maxi)
        return min(avg)

""" Runtime
26
ms
Beats
99.97%

Memory
16.55
MB
Beats
43.74%
"""
