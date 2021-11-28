# https://leetcode.com/contest/weekly-contest-269/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        return [index for index, element  in enumerate(sorted(nums)) if element == target]
