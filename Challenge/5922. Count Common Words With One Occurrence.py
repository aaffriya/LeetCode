# https://leetcode.com/contest/biweekly-contest-66/problems/count-common-words-with-one-occurrence/
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        c1, c2 = Counter(words1), Counter(words2)
        
        return sum([1 for x in c1.keys() if c1[x] == c2[x] == 1])
