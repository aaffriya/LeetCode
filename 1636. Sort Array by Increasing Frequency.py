# https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        c = collections.Counter(nums).most_common(len(nums))
        
        res = []
        
        while c:
            l = c[-1][1]
            n = c[-1][0]
            for i in range(l):
                res.append(n)
            else:
                c.pop()
        else:
            return res
