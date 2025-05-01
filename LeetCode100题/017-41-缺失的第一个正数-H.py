class Solution:
    def firstMissingPositive(self, nums) -> int:
        ans = 1
        tmp = nums[0]
        
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1        
            
        return len(nums) + 1