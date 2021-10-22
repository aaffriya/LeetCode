# https://leetcode.com/problems/robot-return-to-origin/submissions/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        X = Y = 0
        
        for s in moves:
            if s == "U":
                X += 1
            elif s == "D":
                X -= 1
            elif s == "R":
                Y += 1
            else:
                Y -= 1
                
        return X == False and Y == False
