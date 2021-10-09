# https://leetcode.com/problems/check-if-it-is-a-straight-line/submissions/
class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        for i in range(len(c)-2):
            if (c[i+2][1]-c[i][1])*(c[i+1][0]-c[i][0])!=(c[i+1][1]-c[i][1])*(c[i+2][0]-c[i][0]):
                return False
        else:
            return True
