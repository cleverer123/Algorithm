class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        # dp[0] = 1
        LIS = 1
        for i in range(1, len(nums)):
            # dp[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            if dp[i] > LIS:
                LIS = dp[i]
        
        return LIS
        # dp = [1] * len(nums)
        
        # for i in range(len(nums)):
            
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        # return dp[-1]

class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        stack = []
        stack.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                for j in range(len(stack)):
                    if stack[j] >= nums[i] :
                        stack[j] = nums[i]
                        break
        
        return len(stack)

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bs(nums, target):
            begin = 0
            end = len(nums) - 1           
            index = -1
            while index == -1:
                mid = (begin + end) // 2
                if nums[mid] == target:
                    index = mid
                elif nums[mid] > target:
                    if mid == 0 or target > nums[mid-1]:
                        index = mid
                    end = mid - 1
                else:
                    if mid == len(nums) - 1 or target < nums[mid+1]:
                        index = mid + 1
                    begin = mid + 1
            return index 


        if len(nums) == 0:
            return 0
        stack = []
        stack.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                pos = bs(stack, nums[i])
                stack[pos] = nums[i]
        
        return len(stack)


import bisect
class Solution3:
    def lengthOfLIS(self, nums):
        Dp = [0]*len(nums)
        size = 0
        
        for num in nums:
            i = bisect.bisect_left(Dp,num,0,size)
            Dp[i] = num
            if i==size:
                size += 1
        return size

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))
