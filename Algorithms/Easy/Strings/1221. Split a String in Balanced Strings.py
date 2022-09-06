# https://leetcode.com/problems/split-a-string-in-balanced-strings/

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

# Runtime: 43 ms, faster than 54.82% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 13.9 MB, less than 64.64% of Python3 online submissions for Split a String in Balanced Strings.

