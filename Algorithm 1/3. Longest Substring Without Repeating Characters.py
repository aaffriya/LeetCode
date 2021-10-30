# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Day 6
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', ' ','0','1','2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        
        value = True
        
        counter = dict.fromkeys(key, value)
        
        i = j = r = 0
        
        while True:
            try:
                if counter.get(s[j]):
                    counter[s[j]] = False
                    j += 1
                
                else:
                    counter[s[i]] = True
                    l = j - i
                    i += 1
                    if l > r:
                        r = l
            except:
                l = j - i
                return l if l > r else r
