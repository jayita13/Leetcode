# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image2 = []
        
        for i in range(len(image)):
            image2.append(image[i][::-1])
            
        for i in range(len(image2)):
            for j in range(len(image2)):
                if image2[i][j] == 0:
                    image2[i][j] = 1
                else:
                    image2[i][j] = 0
                    
        return image2

# Runtime: 67 ms, faster than 59.82% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.9 MB, less than 31.61% of Python3 online submissions for Flipping an Image.
