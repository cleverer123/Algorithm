class Solution:
    def productExceptSelf(self, nums):
        L, R = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]
            R[len(nums) - i - 1] = R[len(nums) - i] * nums[len(nums) - i]
        res = [1] * len(nums)
        res[0], res[-1] = R[0], L[-1]
        for i in range(1, len(nums) - 1):
            res[i] = L[i] * R[i]
        return res