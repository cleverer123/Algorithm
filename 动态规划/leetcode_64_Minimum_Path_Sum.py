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

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))            