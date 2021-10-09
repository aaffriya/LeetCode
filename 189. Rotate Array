# https://leetcode.com/problems/rotate-array/submissions/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l<k:
            k = k%l
        temp1 = nums[:-k]
        temp2 = nums[-k:]
        for d in range(l):
            del nums[-1]
        else:
            nums.extend(temp2)
            nums.extend(temp1)
        
