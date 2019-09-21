import numpy as np
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dungeon = np.array(dungeon)
        if dungeon.size == 0:
            return 0
        row, column =dungeon.shape
        
        dp = np.zeros_like(dungeon)

        dp[-1,-1] = max(1, 1 - dungeon[-1, -1] )

        for i in range(row-2, -1, -1):
            dp[i, column-1] = max(1, dp[i+1, column-1] - dungeon[i, column-1])

        for j in range(column-2, -1, -1):
            dp[row-1, j] = max(1, dp[row-1, j+1] - dungeon[row-1, j])

        for i in range(row-2, -1, -1):
            for j in range(column-2, -1, -1):
                dp_min = min(dp[i+1,j], dp[i,j+1])
                dp[i,j] = max(1, dp_min - dungeon[i,j])

        return dp[0, 0]

if __name__ == "__main__":
    grid = [[-2,3,3],[-5,-10,1],[10,30,-5]]
    print(Solution().calculateMinimumHP(grid))