# https://leetcode.com/contest/weekly-contest-268/problems/two-furthest-houses-with-different-colors/
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        res = 0
        
        for i, j in enumerate(colors):
            for k, l in enumerate(colors):
                if j != l:
                    if abs(i-k) > res:
                        res = abs(i-k)
        return res
                
        
