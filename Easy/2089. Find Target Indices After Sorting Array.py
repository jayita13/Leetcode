# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        x = []
        for i in range(len(new)):
            if new[i] == target:
                x.append(i)
        return x

# Runtime: 76 ms, faster than 37.25% of Python3 online submissions for Find Target Indices After Sorting Array.
# Memory Usage: 13.9 MB, less than 72.24% of Python3 online submissions for Find Target Indices After Sorting Array.
