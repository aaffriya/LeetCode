# https://leetcode.com/problems/fibonacci-number/
# Day 1
class Solution:
    def fib(self, n: int) -> int:
        
        if n < 2: return n
        
        f = list((0, 1))
        for x in range(1, n):
            f.append(f[-1] + f[-2])
        else:
            return f[-1]
