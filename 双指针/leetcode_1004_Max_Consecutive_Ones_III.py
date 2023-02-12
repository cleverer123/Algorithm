class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = [0] * 2
        left, right = 0, 0
        res = 0
        while right < len(nums):
            cnt[nums[right]] += 1
            if nums[right] == 0:
                while cnt[0] > k:                   
                    cnt[nums[left]] -= 1
                    left += 1

            if cnt[0] <= k:
                while  right + 1 < len(nums) and nums[right + 1] == 1:
                    right += 1
                    cnt[1] += 1
                res = max(right - left + 1, res)
            right += 1
        return res

    def longestOnes2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        for end, num in enumerate(nums):
            if num == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1    
                start += 1
        return end - start + 1

                
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2  
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3  
# nums = [1,1,1]
# k =0          
print(Solution().longestOnes2(nums, k))


