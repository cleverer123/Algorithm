class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        res = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                cnt += 1
            if nums[end] == 0:
                res = max(res, cnt)
                cnt = 0
        res = max(res, cnt)
        return res
nums = [1]
print(Solution().findMaxConsecutiveOnes(nums))