# https://leetcode.com/problems/truncate-sentence/

def truncateSentence(self, s: str, k: int) -> str:
        s1 = s.split()
        s2 = []
        for i in range(len(s1)):
            if i == k:
                break
            else:
                s2.append(s1[i])
        return " ".join(s2)

# Runtime: 24 ms, faster than 98.61% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 14 MB, less than 10.49% of Python3 online submissions for Truncate Sentence.
