# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        res = []
        for i,j in zip(pos, neg):
            res.append(i)
            res.append(j)
        return res

        # n = len(nums)

        # # Initializing an answer array of size n
        # ans = [0] * n

        # # Initializing two pointers to track even and
        # # odd indices for positive and negative integers respectively
        # pos_index, neg_index = 0, 1

        # for i in range(n):
        #     if nums[i] > 0:
        #         # Placing the positive integer at the
        #         # desired index in ans and incrementing pos_index by 2
        #         ans[pos_index] = nums[i]
        #         pos_index += 2
        #     else:
        #         # Placing the negative integer at the
        #         # desired index in ans and incrementing neg_index by 2
        #         ans[neg_index] = nums[i]
        #         neg_index += 2

        # return ans
