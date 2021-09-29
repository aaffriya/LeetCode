# https://leetcode.com/problems/largest-perimeter-triangle/
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        while not len(nums) < 3:
            nums.sort(reverse=True)
            if nums[0] < sum(nums[1:3]):return sum(nums[0:3])
            else:del nums[0]
        else: return 0
