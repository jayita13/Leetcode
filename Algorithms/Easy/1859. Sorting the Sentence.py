# https://leetcode.com/problems/sorting-the-sentence/

def sortSentence(self, s: str) -> str:
        
        words = s.split()
        res = [None] * len(words)
        
        for i in words:
            res[int(i[-1])-1] = i[:-1]
             
        return ' '.join(res)

# Runtime: 32 ms, faster than 84.95% of Python3 online submissions for Sorting the Sentence.
# Memory Usage: 13.8 MB, less than 67.00% of Python3 online submissions for Sorting the Sentence.
