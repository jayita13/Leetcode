# https://leetcode.com/problems/create-target-array-in-the-given-order/

def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.insert(index[i], nums[i])
        return res

# Runtime: 36 ms, faster than 86.03% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 70.48% of Python3 online submissions for Create Target Array in the Given Order.
