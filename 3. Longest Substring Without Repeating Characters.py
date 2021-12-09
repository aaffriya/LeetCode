class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dct = dict()
        
        i = j = r = 0
        
        while True:
            try:
                if dct.get(s[j], True):
                    dct[s[j]] = False
                    j += 1
                
                else:
                    dct[s[i]] = True
                    l = j - i
                    i += 1
                    if l > r:
                        r = l
            except:
                l = j - i
                return l if l > r else r
