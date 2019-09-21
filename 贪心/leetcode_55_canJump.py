class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = []

        for i in range(len(nums)):
            index.append(i + nums[i])

        jump = 0
        max_index = nums[0]                
        
        while jump < len(index) and jump < max_index :

            if  index[jump] > max_index:
                max_index = index[jump]
            jump += 1

        if jump == len(nums):
            return True
        return False

        
                
            
            
            



