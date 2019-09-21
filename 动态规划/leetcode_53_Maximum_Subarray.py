class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        res = dp[0]

        for i in range(1, len(nums)):
            
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(dp[i], res)

        return res

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))