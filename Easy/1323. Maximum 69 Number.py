# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))      

# Runtime: 56 ms, faster than 17.35% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 13.8 MB, less than 60.06% of Python3 online submissions for Maximum 69 Number.
