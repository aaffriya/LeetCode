# https://leetcode.com/problems/merge-strings-alternately/submissions/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        l1, l2 = len(word1), len(word2)
        
        for i in range(min(l1, l2)):
            res += f"{word1[i]}{word2[i]}"
        else:
            if l1 > l2:
                res += word1[i+1:]
            else:
                res += word2[i+1:]
                
        return res
