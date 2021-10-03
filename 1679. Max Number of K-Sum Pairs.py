# https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        rev = nums[::-1]
        operations, i, j, n = 0, 0, 0, len(nums)-2
        while not n<(i+j):
            sum = nums[i] + rev[j]
            if sum == k:
                operations+=1
                i+=1
                j+=1
            elif sum > k: j+=1
            else: i+=1
        return operations
