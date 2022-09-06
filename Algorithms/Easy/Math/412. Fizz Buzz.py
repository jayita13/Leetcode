# https://leetcode.com/problems/fizz-buzz/submissions/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans =[]
        for i in range(1,n+1):
            if i%5==0 and i%3==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

# Runtime: 69 ms, faster than 34.57% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15 MB, less than 88.38% of Python3 online submissions for Fizz Buzz.
