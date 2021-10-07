# https://leetcode.com/problems/set-mismatch/submissions/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        for i in range(1, len(nums)+1):
            j = c.get(i)
            if j==2:
                mul = i 
            if i not in c:
                mis = i
        else:
            return [mul, mis]
                
