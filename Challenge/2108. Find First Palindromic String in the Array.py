# https://leetcode.com/contest/weekly-contest-272/problems/find-first-palindromic-string-in-the-array/
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if word == word[::-1]:
                return word
        else:
            return ""
