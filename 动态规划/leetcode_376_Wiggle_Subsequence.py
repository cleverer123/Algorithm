class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        up = [0] * len(nums)
        down = [0] * len(nums) 
        up[0] = 1
        down[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])

    def wiggleMaxLength2(self, nums):
        if len(nums) <= 2:
            return len(nums)
        up = 1
        down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        
        return max(up, down)

if __name__ == "__main__":
    nums = [1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums))