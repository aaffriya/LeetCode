# https://leetcode.com/contest/weekly-contest-274/problems/number-of-laser-beams-in-a-bank/
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        res = count = 0
        
        for row in bank:
            temp = row.count('1')
            if temp != 0:
                print(count, temp)
                res += count * temp
                count = temp
            else:
                continue
                
        return res
        
