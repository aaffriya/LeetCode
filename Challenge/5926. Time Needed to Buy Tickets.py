# https://leetcode.com/contest/weekly-contest-267/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        res = i = 0
        
        while tickets[k]:
            try:
                j = tickets[i]
                if j:
                    tickets[i] = j - 1
                    i += 1
                    res += 1
                else:
                    i += 1
            except:
                i = 0
        return res
