# https://leetcode.com/problems/sum-of-digits-in-base-k/

def sumBase(self, n: int, k: int) -> int:
        s = 0
        while n > 0:
            s+=n%k
            n//=k
        return s

''' Runtime: 35 ms, faster than 72.32% of Python3 online submissions for Sum of Digits in Base K.
Memory Usage: 13.9 MB, less than 13.09% of Python3 online submissions for Sum of Digits in Base K. '''
