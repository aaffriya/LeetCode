# https://leetcode.com/problems/rank-transform-of-an-array/submissions/
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        d = {k : i+1 for i, k in enumerate(sorted(set(arr)))}
        return [d[r] for r in arr]
