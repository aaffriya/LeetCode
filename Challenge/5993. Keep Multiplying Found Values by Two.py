# https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        c = collections.Counter(nums)
        
        while True:
            if c.get(original, False):
                original *= 2
            else:
                return original
