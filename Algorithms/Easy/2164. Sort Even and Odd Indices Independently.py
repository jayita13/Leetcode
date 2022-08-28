# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        final = [None]*(len(even)+len(odd))
        eve = sorted(even)
        od = sorted(odd, reverse=True)
        final[::2] = eve
        final[1::2] = od
        
        return final

''' Success Details 
Runtime: 49 ms, faster than 98.77% of Python3 online submissions for Sort Even and Odd Indices Independently.
Memory Usage: 13.9 MB, less than 70.98% of Python3 online submissions for Sort Even and Odd Indices Independently. '''
