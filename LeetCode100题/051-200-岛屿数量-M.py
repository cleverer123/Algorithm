from typing import Optional, List

# 网格问题，深度优先搜索通用模板：
# def inArea(r, c):
#     if r < 0 or r >= len(grid[0]) or c < 0 or c >= len(grid[grid]) :
#         return False
#     else:
#         return True

# grid = None
# def dfs(r, c):
#     if not inArea(r, c):
#         return
    
#     if grid[r][c] != 1:
#         return
    
#     grid[r][c] = 2 # 标记为遍历到的格子，避免重复

#     dfs(r - 1, c)
#     dfs(r, c - 1)
#     dfs(r + 1, c)
#     dfs(r, c + 1)



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return
            grid[r][c] = 2
            dfs(grid, r - 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r + 1, c)
            dfs(grid, r, c + 1)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(grid, r, c)
                    ans += 1
        return ans
    
grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
print(Solution().numIslands(grid))