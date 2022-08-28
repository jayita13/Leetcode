# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0
        for i in range(0,len(operations)):
            if (operations[i].startswith("-") or operations[i].endswith("-")):
                s = s - 1            
            if (operations[i].startswith("+") or operations[i].endswith("+")):
                s = s + 1            
        return s

# Runtime: 75 ms, faster than 48.53% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 14 MB, less than 26.26% of Python3 online submissions for Final Value of Variable After Performing Operations.
