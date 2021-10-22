# https://leetcode.com/problems/sort-characters-by-frequency/submissions/
class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = collections.Counter(s)
        
        res = []
        
        for string, times in c.items():
            res.append(string * times)
        
        def magic(i):
            return len(i)
        
        res.sort(reverse = True, key = magic)
        
        return "".join(res)
