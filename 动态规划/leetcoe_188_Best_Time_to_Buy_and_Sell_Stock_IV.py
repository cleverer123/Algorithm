class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) <= 1:
            return 0
        
        if k >= len(prices) / 2:
            return self.greedy(prices)
        
        buy, sell = [-prices[0]] * k, [0] * (k+1)
        
        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                buy[j-1] = max(buy[j-1], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j-1] + prices[i])
        
        return max(sell)
    
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

if __name__ == "__main__":
    k = 2
    prices = [2,4,1]
    print(Solution().maxProfit(k, prices))