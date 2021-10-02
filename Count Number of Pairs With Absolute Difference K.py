# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        for i in nums:
            for j in nums:
                if i-j==k:
                    result+=1
        return result
        
