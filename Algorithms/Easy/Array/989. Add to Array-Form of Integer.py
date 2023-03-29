# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = int("".join([str(elem) for elem in num]))+k
        return list(map(int, str(n)))
