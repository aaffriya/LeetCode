# https://leetcode.com/problems/single-number/submissions/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for i in c:
            r = c.get(i)
            if r==1: return i
