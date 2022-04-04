# https://leetcode.com/problems/sum-of-unique-elements/

def sumOfUnique(self, nums: List[int]) -> int:
        counts = dict()        
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        # create copy to avoid Runtime error of dictionary changed size during iteration
        for i,j in counts.copy().items():       
            if j > 1:
                del counts[i]
        return sum(counts.keys())

''' Runtime: 52 ms, faster than 43.31% of Python3 online submissions for Sum of Unique Elements.
Memory Usage: 13.9 MB, less than 59.23% of Python3 online submissions for Sum of Unique Elements. '''
