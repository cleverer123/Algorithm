class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        begin = 0
        end = len(nums) - 1
        while index == -1:
            mid = (begin + end)//2
            if target == nums[mid]:
                index = mid
            elif target < nums[mid]:
                if mid == 0 or target > nums[mid-1]:
                    index = mid  
                end = mid - 1 
            else:
                if mid == (len(nums) - 1) or target < nums[mid+1]:
                    index = mid + 1
                begin = mid + 1 
        
        return index

if __name__ == "__main__":
    example = [1, 3, 5, 6, 7, 9, 11, 17, 43, 67, 432]

    # print(bs(example, 0, len(example)-1,  17))   
    print(Solution().searchInsert(example,  10))   

