from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = [] # origin rotten list

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        ans = 0
        while queue and fresh:
            ans += 1
            tmp_q = queue
            queue = []
            for i, j in tmp_q:
                for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
            
        return -1 if fresh else ans