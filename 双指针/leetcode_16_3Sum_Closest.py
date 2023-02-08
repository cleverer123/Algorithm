import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        min = sys.maxsize
        res = 0
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum - target) < min:
                    min = abs(sum - target)
                    res = sum
               
                if sum < target:
                    l += 1
                else:
                    r -= 1
        
        return res

arr = [-1,2,1,-4]
print(Solution().threeSumClosest(arr, 1))