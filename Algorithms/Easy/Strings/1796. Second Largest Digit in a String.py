# https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for i in s:
            if ord(i)>= 48 and ord(i)<= 57:
                nums.add(int(i))
        if len(list(nums))<=1:
            return -1
        else:
            return sorted(list(nums))[-2]

"""  Runtime
46 ms
Beats
18.13%
Memory
13.9 MB
Beats
8.1% """
