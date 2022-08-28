# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            z = nums2.index(nums1[i])
            if z==len(nums2)-1 or nums2[z]>max(nums2[z+1:]):
                ans.append(-1)
            else:
                for i in nums2[z+1:]:
                    if i>nums2[z]:
                        ans.append(i)
                        break
                
        return ans
