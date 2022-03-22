#https://leetcode.com/problems/create-target-array-in-the-given-order/


def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.insert(index[i], nums[i])
        return res
