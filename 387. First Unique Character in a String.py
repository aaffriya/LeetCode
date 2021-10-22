#https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        c = collections.Counter(s)
        
        for k , v in c.items():
            if v == 1:
                return s.index(k)
        else:
            return -1
