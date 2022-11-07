# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))    
   
#         Brute-Force solution     
#         arr = []
#         for i in range(len(str(num))):
#             arr.append(num%10)
#             num//=10
#         arr = arr[::-1]
#         for i in range(len(arr)):
#             if arr[i] == 6:
#                 arr[i] = 9
#                 break
                
#         return int("".join(map(str, arr)))

# Runtime: 56 ms, faster than 17.35% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 13.8 MB, less than 60.06% of Python3 online submissions for Maximum 69 Number.
