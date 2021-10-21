# https://leetcode.com/problems/check-if-n-and-its-double-exist/submissions/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] == False:
                try:
                    if arr[i+1] == False:
                        return True
                except:
                    pass
            if arr[i] + arr[i] in arr and arr[i] != False: 
                return True
        else:
            return False
