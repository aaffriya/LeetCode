# https://leetcode.com/problems/fibonacci-number/submissions/
class Solution:
    def fib(self, n: int) -> int:
        f = list((0, 1))
        for x in range(1, n):
            f.append(f[-1] + f[-2])
        else:
            return f[-1]
