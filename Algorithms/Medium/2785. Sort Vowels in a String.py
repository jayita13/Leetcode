# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        Vowel=["A","E","I","O","U","a","e","i","o","u"]
        D=[]
        C=0
        for i in s:
            if i in Vowel:
                D.append(i)
        D.sort()
        L=[0]*len(s)
        for i in range(len(s)):
            if s[i] in Vowel:
                L[i]=D[C]
                C+=1 
            else:
                L[i]=s[i]
        return "".join(L)

