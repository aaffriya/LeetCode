# https://leetcode.com/problems/find-the-duplicate-number/submissions/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for i in c:
            r = c.get(i)
            if r>1: return i
