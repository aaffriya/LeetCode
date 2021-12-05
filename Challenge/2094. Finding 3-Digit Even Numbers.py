# https://leetcode.com/contest/weekly-contest-270/problems/finding-3-digit-even-numbers/
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        return sorted(set((first * 100 ) + (second * 10) + (third)  for first, second, third in itertools.permutations(digits, 3) if first and not third & 1))
