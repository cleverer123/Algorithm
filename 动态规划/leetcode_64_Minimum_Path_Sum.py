import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        grid = np.array(grid)
        dp = np.zeros_like(grid)

        dp[0, :] = np.cumsum(grid[0, :]) 

        dp[:, 0] = np.cumsum(grid[:, 0])

        for i in range(1, grid.shape[0]):
            for j in range(1, grid.shape[1]):
                dp[i, j] = min(dp[i-1, j], dp[i, j-1]) + grid[i,j]
        
        return dp[-1, -1]

class Solution1(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m) ] 
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]            
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
                
        return dp[-1][-1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution1().minPathSum(grid))            