# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowel=["A","E","I","O","U","a","e","i","o","u"]
        D=[]
        
        for i in s:
            if i in Vowel:
                D.append(i)         
        
        if len(D) <= 1:
            return s

        C=len(D)-1
        L=[0]*len(s)
        for i in range(len(s)):
            if s[i] in Vowel:
                L[i]=D[C]
                C-=1 
            else:
                L[i]=s[i]
        return "".join(L)
 
""" Runtime 63ms Beats 31.17% of users with Python3 
Memory 17.82MB Beats 63.45% of users with Python3 """
