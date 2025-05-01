class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        # print(nums)

        
    def reverse(self, nums, start, end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))