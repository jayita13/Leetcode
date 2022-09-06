# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

class Solution:
    def digitCount(self, num: str) -> bool:
        c = True
        for i in range(len(num)):
            if not num.count(str(i)) == int(num[i]):
                c = False
                break
        return c
    
''' Success Details 
Runtime: 45 ms, faster than 75.00% of Python3 online submissions for Check if Number Has Equal Digit Count and Digit Value.
Memory Usage: 13.9 MB, less than 75.00% of Python3 online submissions for Check if Number Has Equal Digit Count and Digit Value. '''
