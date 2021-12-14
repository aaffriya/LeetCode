# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(int(math.pow(abs(i), 2)))
        else:
            res.sort()
            return res
