import math
class Solution:
    def maxSubArray(self, nums ) -> int:
        ans = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum = max(nums[i], sum + nums[i])
            ans = max(sum, ans)
        return ans
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))