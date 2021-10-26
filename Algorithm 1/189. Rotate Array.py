# https://leetcode.com/problems/rotate-array/
# Day 2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k:
            if len(nums) < k:
                k = k % len(nums)
                
            if len(nums) != 1:
                nums[0:0] = nums[-k:]
                nums[-k:] = []
