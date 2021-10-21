# https://leetcode.com/problems/move-zeroes/submissions/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = []
        for i, j in enumerate(nums):
            if j == False:
                count.append(i)
                
        l = len(count)
        while count:
            nums.pop(count[-1])
            count.pop()
            
        for append in range(l):
            nums.append(0)
