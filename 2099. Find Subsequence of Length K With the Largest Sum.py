# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        sortEd = sorted(enumerate(nums), key = lambda x : x[1])[-k:]
        
        return [i[1] for i in sorted(sortEd, key = lambda x : x[0])]
