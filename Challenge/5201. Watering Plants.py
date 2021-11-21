# https://leetcode.com/contest/weekly-contest-268/problems/watering-plants/
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        step = 0
        
        temp = capacity
        
        for index, plant in enumerate(plants):
            if plant <= temp:
                step += 1
                temp -= plant
            else:
                step += index + index + 1
                temp = capacity - plant
                
        return step
                
