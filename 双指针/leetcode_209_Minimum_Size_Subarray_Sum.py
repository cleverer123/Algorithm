import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target - sum(nums) > 0:
            return 0

        start = 0
        res = len(nums)
        delta = target
        for end in range(len(nums)):
            delta -= nums[end]

            while delta <= 0:
                res = min(end - start + 1, res)
                delta += nums[start]
                start += 1
        
        return res

# arr = [2,3,1,2,4,3,4,]
# target = 7
arr = [1,1,1]
target = 4
print(Solution().minSubArrayLen(target, arr))