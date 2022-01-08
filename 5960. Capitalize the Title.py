# https://leetcode.com/contest/biweekly-contest-69/problems/capitalize-the-title/
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        res = []
        
        for i in title.split(" "):
            res.append(i.lower()) if len(i) < 3 else res.append(i.capitalize())
            
        return " ".join(res)
        
