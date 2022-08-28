# https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for i in range(1, 101):
            if (i in nums1 and i in nums2) or (i in nums1 and i in nums3) or (i in nums2 and i in nums3):
                ans.append(i)
       
        return ans

''' Runtime: 114 ms, faster than 35.89% of Python3 online submissions for Two Out of Three.
Memory Usage: 13.9 MB, less than 84.67% of Python3 online submissions for Two Out of Three. '''
