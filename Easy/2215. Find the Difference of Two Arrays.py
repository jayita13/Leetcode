# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums3 = [[],[]]
        for i in set(nums1):
            if i not in nums2:
                nums3[0].append(i)
        for i in set(nums2):
            if i not in nums1:
                nums3[1].append(i)
        return nums3

''' Runtime: 644 ms, faster than 22.76% of Python3 online submissions for Find the Difference of Two Arrays.
Memory Usage: 14.4 MB, less than 59.95% of Python3 online submissions for Find the Difference of Two Arrays. '''
