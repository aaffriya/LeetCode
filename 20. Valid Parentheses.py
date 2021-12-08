# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        
        dct = {
          '(' : ')',
          '[' : ']',
          '{' : '}'
        }
        
        stack = []
        
        for i in s:
            if i in dct:
                stack.append(i)
            else:
                if stack and i == dct.get(stack[-1]): stack.pop()
                else: return False
                
        return  not stack
    
