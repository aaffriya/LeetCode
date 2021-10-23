# https://leetcode.com/problems/top-k-frequent-elements/submissions/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        sort = sorted(collections.Counter(nums).items(), key=lambda x:x[1])
        
        res = set()
        
        while k:
            res.add(sort[-1][0])
            sort.pop()
            k -= 1
            
        return res
