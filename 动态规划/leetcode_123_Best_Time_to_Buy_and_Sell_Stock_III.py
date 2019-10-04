class Solution(object):
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        dp1 = self.dp1(prices)
        dp2 = self.dp2(prices)

        res = 0
        for i in range(len(dp1)):
            res = max(res, dp1[i] + dp2[i])
        
        return res

    # dp1[i] 表示在i之前进行一次交易获得的最大值
    def dp1(self, prices):
        local = 0
        dp = [0] * len(prices)
        for i in range(1, len(prices) ):
            local = max(local + prices[i] - prices[i-1], 0)
            dp[i] = max(dp[i-1], local)
        return dp
    
    # dp2[i] 表示在i之后进行一次交易获得的最大值，其实是从后往前寻找降幅最大值。 
    def dp2(self, prices):
        local = 0
        dp = [0] * len(prices)
        for i in range(len(prices) - 1, 0, -1):
            local = max(local + prices[i] - prices[i-1], 0)
            dp[i-1] = max(local, dp[i])
    
        return dp

if __name__ == "__main__":
    # p = [3,3,5,0,0,3,1,4]
    p = []
    print(Solution().maxProfit(p))