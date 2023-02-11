class Solution(object):
    # 滑动窗口解法
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        res = 0
        right = 0
        while right < len(nums):
            if nums[right] % 2 != 0:
                k -= 1
            right +=1

            if k == 0:
                
                tmp_r = right
                left_even_cnt, right_even_cnt = 0, 0
                

                while right < len(nums) and nums[right] % 2 == 0:
                    right += 1
                right_even_cnt = right - tmp_r

                while nums[left] % 2 == 0:
                    left_even_cnt += 1
                    left += 1
                
                res += (left_even_cnt + 1) * (right_even_cnt + 1)
                
                left += 1
                k += 1
 
        return res

    # 前缀和解法
    def numberOfSubarrays2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

nums = [2,2,2,1,2,2,1,2,2,2,1,2]
# nums = [2,1,2,1,2]
k = 2
print(Solution().numberOfSubarrays(nums, k))