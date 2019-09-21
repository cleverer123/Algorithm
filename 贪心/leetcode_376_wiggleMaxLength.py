class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        BEGIN = 0
        UP = 1
        DOWN = 2
        state = BEGIN

        

        if len(nums) < 2:
            return len(nums)

        wiggle = 1
        i = 1
         
        while i < len(nums):

            if state == BEGIN:
                if nums[i-1] == nums[i]:
                    i += 1
                    continue       
                elif nums[i-1] < nums[i]:
                    state = UP
                else:
                    state = DOWN
                wiggle += 1 
                i -= 1
            elif state == UP:
                if nums[i - 1] > nums[i]:
                    state = DOWN
                    wiggle += 1
                    i -= 1
            else:
                if nums[i - 1] < nums[i]:
                    state = UP
                    wiggle += 1
                    i -= 1

            i += 1    
        return wiggle 

if __name__ == '__main__':
    S = Solution()
    nums =[84]
    # nums = [0, 0]
    # nums = [1,17,5,10,13,15,10,5,16,8]
    print(S.wiggleMaxLength(nums))