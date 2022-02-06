#https://leetcode.com/contest/weekly-contest-279/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def smallestNumber(self, num: int) -> int:
        
        l = len(str(num))
        res = 0
        sign = False if num > 0 else True
        
        if not sign:
            num = list(str(num))
            num.sort()
            for x, y in enumerate(num):
                if y != '0':
                    num.insert(0, y)
                    num.pop(x+1)
                    break
        else:
            num = list(str(num))
            num.sort(reverse = True)
            num.pop()
            print(num)
        
        for x in num:
            res *= 10
            res += int(x)
        if sign:res *= -1
        
        return res
            
            
