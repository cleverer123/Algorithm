class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        C = sum(nums)

        if C % 2 != 0:
            return False
        C = C // 2

        dp = [False] * (C+1) 

        for c in range(C+1):
            dp[c] = (nums[0] == c)

        for i in range(1, len(nums)):
            for j in range(C, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    continue

        return dp[-1]

if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    print(Solution().canPartition(nums))
