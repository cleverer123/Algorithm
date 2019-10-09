class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return 0
        
        dp = [0] * len(array)
        dp[0] = array[0]
        res = dp[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1] + array[i], array[i])
            res = max(res, dp[i])
        return res
