#https://leetcode.com/contest/weekly-contest-276/problems/divide-a-string-into-groups-of-size-k/
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        
        for x in range(0, len(s), k):
            res.append(s[x:x+k])
            
        if len(res) * k > len(s) and len(res[-1]) != k:
            temp = res[-1]
            i = k - len(temp)
            while len(temp) != k:
                temp += fill
                res[-1] = temp
                
        return res
