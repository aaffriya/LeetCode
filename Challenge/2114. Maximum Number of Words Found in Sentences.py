# https://leetcode.com/contest/biweekly-contest-68/problems/maximum-number-of-words-found-in-sentences/
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        
        res = 0
        
        for i in sentences:
            l = i.split(" ")
            res = max(res, len(l))
            
        return res
