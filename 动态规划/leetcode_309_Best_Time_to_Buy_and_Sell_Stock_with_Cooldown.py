class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        rest = [0] * len(prices)
        hold = [0] * len(prices)
        sold = [0] * len(prices)

        hold[0] = - prices[0]
        sold[0] = - float("inf")
        for i in range(1, len(prices)):
            rest[i] = max(rest[i-1], sold[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]

        return max(sold[-1], rest[-1])

if __name__ == "__main__":
    # p = [1,2,3,0,2]
    p = [1,2]
    print(Solution().maxProfit(p))
