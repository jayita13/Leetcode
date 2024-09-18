# https://leetcode.com/problems/largest-number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_str = [str(num) for num in nums]
        new_str.sort(key=lambda a: a * 10, reverse=True)
        if new_str[0] == '0':
            return "0"
        return "".join(new_str)

""" Runtime 37 ms Beats  79.17% 
Memory 16.58 MB Beats 32.99% """
