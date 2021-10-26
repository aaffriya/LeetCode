# https://leetcode.com/problems/climbing-stairs/
# Day 2
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=3: return n
        
        l = [2,3]
            
        for i in range(3,n):
            l.append(l[-1] + l[-2])
        else:
            return l[-1]
