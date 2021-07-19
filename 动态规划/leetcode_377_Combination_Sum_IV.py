class Solution(object):
    def combination_sum(self, nums, target):

        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]


if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print(Solution().combination_sum(nums, target))