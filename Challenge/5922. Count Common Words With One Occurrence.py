# https://leetcode.com/contest/biweekly-contest-66/problems/count-common-words-with-one-occurrence/
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        c1 = Counter(words1)
        
        c2 = Counter(words2)
        
        res, s = 0, set()
        
        for key, feq in c1.items():
            if feq == 1:
                s.add(key)
                res += 1
        for key, feq in c2.items():
            if feq == 1:
                s.add(key)
                res += 1
                
        return res - len(s)
