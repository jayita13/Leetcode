# https://leetcode.com/problems/sum-of-digits-of-string-after-convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1 = ""
        for i in s:
            s1+=str(ord(i) - 96)
        x = sum(list(map(int, s1)))
        if k == 1:
            return x
        else:
            m = x
            while m>9 and k!=1:
                s2 = sum(list(map(int, str(m))))
                m = s2
                k-=1
            return m

# Runtime 35 ms Beats 72.93%
# Memory 13.9 MB Beats 55.54%          
