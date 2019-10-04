class Solution(object):
    # 递归
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1: 
            return 1
        if n == 1:
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    # 动态规划
    def uniquePaths2(self, m, n):

        if m == 0 or n == 0:
            return 0

        dp = [[1]*m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[-1][-1]

    # 动态规划2
    def uniquePaths2(self, m, n):
        dp = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]           
        return dp[-1]


if __name__ == "__main__":
    print(Solution().uniquePaths2(3, 2))
        

