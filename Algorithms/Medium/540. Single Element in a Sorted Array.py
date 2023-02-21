# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # return list(Counter(nums).most_common(len(nums)))[-1][0]

        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        for num, val in dic.items():
            if val==1:
                return num
                
# Runtime 197 ms Beats 21.95%
# Memory 26.3 MB Beats 6.16%                
