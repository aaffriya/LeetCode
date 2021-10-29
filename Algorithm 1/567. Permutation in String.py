# https://leetcode.com/problems/permutation-in-string/
# Day 5
# Not a Fast Solution but, it's working.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i, j = 0, len(s1)
        
        
        s1 = collections.Counter(s1)
        
        while j <= len(s2):
            
            temp = collections.Counter(s2[i:j])
            
            #print(temp, s1)
            
            if s1 == temp:
                return True
            
            else:
                i += 1
                j += 1
                
        else:
            return False
