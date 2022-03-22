# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        out = []
        for i in range(0,len(candies)):
            if(candies[i] + extraCandies >= maxi) :
                out.append(True)
            else:
                out.append(False)
        return out  

# Runtime: 62 ms, faster than 36.11% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.9 MB, less than 71.24% of Python3 online submissions for Kids With the Greatest Number of Candies.
