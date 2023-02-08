class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums
        l =  len(nums)
        p = 0
        while  p < l - 1:
            if nums[p+1] == nums[p]:
                nums.pop(p+1)
                l -= 1
            else:
                p += 1

        return l, nums

if __name__=="__main__":
    arr = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(arr))