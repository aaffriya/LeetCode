# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3990/
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x%2==0]
        odd = [x for x in nums if x%2!=0]
        output = []
        for x , y in zip(even,odd):
            output.append(x)
            output.append(y)
        else: return output