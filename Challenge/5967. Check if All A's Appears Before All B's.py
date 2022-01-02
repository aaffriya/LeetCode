# https://leetcode.com/contest/weekly-contest-274/problems/check-if-all-as-appears-before-all-bs/
class Solution:
    def checkString(self, s: str) -> bool:
        
        return s.find('ba') < 0
