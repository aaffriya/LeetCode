# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        for i in range(math.ceil(math.sqrt(c))):
            j = math.sqrt(c-(i*i))
            if j-int(j) == 0:
                return True
        else:
            return False
