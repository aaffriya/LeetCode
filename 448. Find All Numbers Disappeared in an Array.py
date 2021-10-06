# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l, s, output = len(nums)+1, set(nums), []
        for i in range(1,l):
            if i not in s:
                output.append(i)
        else:
            return output
