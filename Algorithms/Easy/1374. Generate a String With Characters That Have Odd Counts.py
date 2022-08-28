# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2!=0:
            return n*'a'
        else:
            return (n-1)*'a'+'b'

''' Runtime: 39 ms, faster than 61.01% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
Memory Usage: 13.9 MB, less than 11.54% of Python3 online submissions for Generate a String With Characters That Have Odd Counts. '''
