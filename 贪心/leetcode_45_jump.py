class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0             

        current_max_index = nums[0]
        pre_max_index = nums[0]
        jump_min = 1

        for i in range(len(nums)):
            if i > current_max_index:
                jump_min += 1
                current_max_index = pre_max_index

            if nums[i] + i > pre_max_index :
                pre_max_index = nums[i] + i
        return jump_min
            
            