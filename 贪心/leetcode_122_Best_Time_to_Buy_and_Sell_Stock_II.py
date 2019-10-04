class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0 

        m = prices[0]
        res = 0
        for i in range(1, len(prices)):
            # if prices[i] >= prices[i-1] :
            #     continue
            if prices[i] < prices[i-1]:
                res += prices[i-1] - m
                m = prices[i]

        return res

    def maxProfit2(self, prices):
        if len(prices) == 0:
            return 0 

        res = 0

        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                res += prices[i] - prices[i-1]
            
        return res

if __name__ == "__main__":
    p = [7,1,5,3,6,4]
    print(Solution().maxProfit2(p))