# https://leetcode.com/problems/max-area-of-island/
# Day 7
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        total_r = len(grid)
        
        total_c = len(grid[0])
        
        res = 0
        
        def dfs(r, c):
            if total_r > r >=0 and total_c > c >= 0 and grid[r][c] == 1:
                #print(res)
                grid[r][c] = 0
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            else:
                return 0
        
        for r in range(total_r):
            for c in range(total_c):
                res = max(res,dfs(r,c))
        
        return res
                    
        
