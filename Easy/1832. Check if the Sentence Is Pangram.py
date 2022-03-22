# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def checkIfPangram(self, s: str) -> bool:
        # return len(set(sentence)) == 26
        seen = {}
        for i in set(s):
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        return sum(seen.values())==26

# Runtime: 28 ms, faster than 95.69% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 13.9 MB, less than 64.29% of Python3 online submissions for Check if the Sentence Is Pangram.
