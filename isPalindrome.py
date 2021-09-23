#https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if x == abs(x):
            if x == int(y[::-1]):
                return True
            else:
                return False
        else:
            return False
