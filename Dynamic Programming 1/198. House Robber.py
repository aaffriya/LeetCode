# https://leetcode.com/problems/house-robber/
# Day 3
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0] + nums
        
        for i in range(3, len(nums)):
            a, b = nums[i] + nums[i-3], nums[i] + nums[i-2]
            nums[i] = max(a,b)
        else:
            return max(nums[-1], nums[-2])
