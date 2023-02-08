class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        right, left = 1, 0
        newB, newE = len(nums), 0 
        while right < len(nums):
            if nums[left] <= nums[right]:
                left += 1
                right += 1
            else:
                tmpL = left
                while tmpL >= 0:
                    if nums[tmpL] > nums[right]: tmpL -= 1
                    else: break
                tmpR = right
                while tmpR < len(nums): 
                    if nums[tmpR] < nums[left]: tmpR += 1
                    else: break
                newB, newE = min(newB, tmpL), max(newE, tmpR)
                right += 1
                left += 1

        return 0 if newE == 0 else newE - newB - 1

    def findUnsortedSubarray2(self, nums):
        find_first_index = -1
        find_last_index = -1
        first_index = -1
        last_index = -1

        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                find_first_index = i
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                find_last_index = i
                break

        if find_first_index == -1 or find_last_index == -1:
            return 0
        
        min_value = min(nums[find_first_index:find_last_index+1])
        max_value = max(nums[find_first_index:find_last_index+1])

        for i in range(len(nums)):
            if  nums[i] > min_value:
                first_index = i
                break
        for i in range(len(nums)-1,-1,-1):
            if   nums[i] < max_value:
                last_index = i
                break
       
        return (last_index - first_index +1)


    def findUnsortedSubarray3(self, nums):
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        strt = len(nums) - 1
        prev = nums[strt]
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                strt = i
            else:
                prev = nums[i]
        if end != 0:
            return end - strt + 1
        else: 
            return 0


# arr = [1,2,3,5,6,4,4,4,7]
# arr = [2,8,10,9,6,4,2,15]
arr = [1,3,2,2,2]
print(Solution().findUnsortedSubarray3(arr))