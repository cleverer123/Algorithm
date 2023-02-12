class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = [1] * len(nums)
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dist[i] = dist[i-1] + 1
            if dist[i] > res:
                res = dist[i]
        return res
