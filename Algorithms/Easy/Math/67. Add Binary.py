# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(add(int(a,2),int(b,2)))[2:]

""" Runtime 35 ms Beats 62.46%
Memory 13.8 MB Beats 96.6% """
