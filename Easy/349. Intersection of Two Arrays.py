# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for i in set(nums1):
        #     if i in set(nums2):
        #         ans.append(i)
        # return ans
        return list((set(nums1).intersection(set(nums2))))

''' Success Details 
Runtime: 117 ms, faster than 6.80% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.3 MB, less than 25.27% of Python3 online submissions for Intersection of Two Arrays. '''
