# https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set_nums, output = set(nums), []
        for i in nums:
            if i in set_nums:
                set_nums.remove(i)
            else:
                output.append(i)
        else:
            return output
