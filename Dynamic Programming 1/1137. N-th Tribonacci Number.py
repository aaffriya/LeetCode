# https://leetcode.com/problems/n-th-tribonacci-number/
# Day 1
class Solution:
    def tribonacci(self, n: int) -> int:
        
        first, second, third = 0, 1, 1
        
        for _ in range(n):
            first, second, third = second, third, first + second + third
            
        else:
            return first
