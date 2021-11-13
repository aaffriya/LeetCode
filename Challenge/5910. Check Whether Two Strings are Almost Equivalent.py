# https://leetcode.com/contest/biweekly-contest-65/problems/check-whether-two-strings-are-almost-equivalent/
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        c1 = collections.Counter(word1)
        
        c2 = collections.Counter(word2)
        
        for key, value in c1.items():
            j = c2[key]
            if (value - j) > 3:
                return False
        else:
            for key, value in c2.items():
                j = c1[key]
                if (value - j) > 3:
                    return False
            else:
                return True
