# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Day 4
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")
        
        S = []
        
        for i in s:
            S.append(i[::-1])
            
        return " ".join(S)
