class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val :
                nums[slow] = nums[fast]             
                slow += 1
            fast += 1

        return slow, nums

if __name__=="__main__":
    arr = [0,1,2,2,3,0,4,2]
    print(Solution().removeElement(arr, 2))