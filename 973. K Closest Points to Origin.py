# https://leetcode.com/problems/k-closest-points-to-origin/submissions/
class Solution:
    def kClosest(self, p: List[List[int]], k: int) -> List[List[int]]:
        
        def magic(e):
            x, y = e[0], e[1]
            return x ** 2 + y ** 2
        
        p.sort(key = magic)
        
        return p[:k]
