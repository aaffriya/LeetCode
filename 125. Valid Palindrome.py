#https://leetcode.com/problems/valid-palindrome/submissions/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p = ""
        
        for i in s.lower():
            if i.isalnum():
                p += i
        else:
            return p == p[::-1]
