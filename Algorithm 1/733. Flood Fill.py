# https://leetcode.com/problems/flood-fill/
# Day 7
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        
        total_r = len(image)
        
        total_c = len(image[0])
        
        def dfs(sr, sc):
            if total_r > sr >= 0 and total_c > sc >= 0 and oldColor == image[sr][sc] and newColor != image[sr][sc]:
                image[sr][sc] = newColor
                
                #print(image)
                
                dfs(sr+1, sc)
                dfs(sr,sc+1)
                dfs(sr-1,sc)
                dfs(sr,sc-1)
                
                
        dfs(sr, sc)
        
        return image
