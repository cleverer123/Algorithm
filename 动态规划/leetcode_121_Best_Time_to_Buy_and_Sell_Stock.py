class Solution(object):
    # 动态规划1 维护到当前日期的最小值，当日股价减去最小值，即为截止至当日可获得的最大收益。
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        m = prices[0]
        tmp = 0
        for i in range(1, len(prices)):
            if prices[i] < m:
                m = prices[i]
            
            tmp = max(tmp, prices[i] - m)

        return tmp 
    
    # 动态规划2 维护 在当天卖出的最佳交易 和 到目前为止最好的交易
    def maxProfit(self, prices):
        local = 0
        glob = 0
        for i in range(len(prices) - 1):
            local = max(local+prices[i+1]-prices[i],0)
            glob = max(local, glob)
    
        return glob

# https://blog.csdn.net/program_developer/article/details/83245488