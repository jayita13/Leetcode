# https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [ k for k, v in Counter(nums).items() if v > len(nums) // 3 ]

  """ Runtime
105
ms
Beats
45.84%
of users with Python3
Memory
17.90
MB
Beats
77.98%
of users with Python3 """
