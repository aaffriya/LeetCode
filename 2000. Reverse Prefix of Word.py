# https://leetcode.com/problems/reverse-prefix-of-word/submissions/
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        try:
            index = word.index(ch)
        except:
            return word
        
        word = list(word)
        part = word[:index+1]
        word[:index+1] = part[::-1]
        return "".join(word)
