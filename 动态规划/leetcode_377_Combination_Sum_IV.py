class Solution(object):
    def combination_sum(self, nums, target):

        dp = [0] * (target + 1)

        res = 0
        
        # for num in nums:
            dp[num] = 1
            for num in nums:
                for j in range(target, -1, -1):
                    if j >= num:
                        dp[j] = dp[j] or dp[j-num]
                