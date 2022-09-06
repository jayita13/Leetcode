# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        num = str(num)
        for n in num:
            if int(n)%2 == 0:
                even.append(n)
            else:
                odd.append(n)
        even.sort()
        odd.sort()
        num = list(num)
        for i in range(len(num)):
            if int(num[i])%2 == 0:
                num[i] = even.pop()
            else:
                num[i] = odd.pop()
        return int("".join(num))

""" Success Details 
Runtime: 53 ms, faster than 31.51% of Python3 online submissions for Largest Number After Digit Swaps by Parity.
Memory Usage: 14 MB, less than 21.14% of Python3 online submissions for Largest Number After Digit Swaps by Parity. """
