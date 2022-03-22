# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(self, num: int) -> int:
        c = 0
        while num>0:
            if num % 2 == 0:
                num = num // 2                
            else:
                num = num - 1
            c = c + 1
        return c

# Runtime: 37 ms, faster than 68.11% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
