# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

import re
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = 0
        new_sent = sentence.split(' ')
        for sent in new_sent:
            if re.match(f'^{searchWord}',sent):
                s = new_sent.index(sent) + 1
                break
            else:
                s = -1
#             if sent.startswith(searchWord):
#                 s = new_sent.index(sent) + 1
#                 break
#             else:
#                 s = -1
        return s
        

''' Runtime: 31 ms
Memory Usage: 13.9 MB '''
