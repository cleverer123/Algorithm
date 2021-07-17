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


    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = sum(nums)
        if S % 2 != 0:
            return False
        # python S /=2 
        S //= 2 
        bag = [False] * (S + 1)
        
        for s in range(S + 1):
            bag[s] = (nums[0] == s)
        
        for i in range(1, len(nums)):
            for s in range(S, -1, -1):
                if s >= nums[i]:
                    bag[s] = bag[s] or bag[s - nums[i]]
                else:
                    continue
        return bag[-1]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 5]
    print(Solution().canPartition2(nums))
