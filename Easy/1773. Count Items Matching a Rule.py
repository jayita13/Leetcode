# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0       
        for i in range(len(items)):
            if ruleKey == "type" and ruleValue == items[i][0]:
                c+=1
            elif ruleKey == "color" and ruleValue == items[i][1]:
                c+=1
            elif ruleKey == "name" and ruleValue == items[i][2]:
                c+=1
        return c

# Runtime: 396 ms
# Memory Usage: 20.3 MB
