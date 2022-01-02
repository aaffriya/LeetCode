# https://leetcode.com/contest/weekly-contest-274/problems/destroying-asteroids/
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids.sort()
        
        for x in asteroids:
            if mass < x: return False
            else: mass += x
                
        return True
