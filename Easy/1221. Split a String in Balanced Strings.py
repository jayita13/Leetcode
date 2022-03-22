#https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balancedStringSplit(self, s: str) -> int:
        res = []
        sums=0
        p=0
        for i in s:
            if i == 'R':
                sums+= 1
            if i == 'L':
                sums-= 1
            if sums == 0:
                p+= 1
        return p
