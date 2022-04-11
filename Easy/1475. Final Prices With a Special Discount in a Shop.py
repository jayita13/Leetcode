# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final = []
        
        for i in range(len(prices)):
            f = 0
            for j in range(i+1, len(prices)):
                if prices[j]<=prices[i]:
                    final.append(prices[i]-prices[j])
                    f+=1
                    break
            if f == 0:
                final.append(prices[i])
        return final

''' Runtime: 103 ms, faster than 12.77% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
Memory Usage: 14 MB, less than 70.35% of Python3 online submissions for Final Prices With a Special Discount in a Shop. '''
