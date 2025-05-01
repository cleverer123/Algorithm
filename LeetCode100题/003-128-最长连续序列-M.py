from typing import List
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        hashtable = {}
        nums_set = set(nums)
        for num in nums_set:
            hashtable[num] = 1
        max_len = 0
        for num in nums_set:
            if num - 1 in hashtable:
                continue
            else:
                while num + 1 in hashtable:
                    hashtable[num + 1] = hashtable[num] + 1 
                    num = num + 1
                max_len = max(max_len, hashtable[num])
        return max_len
    
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            cur_num = num
            while cur_num in nums_set:
                cur_num += 1 
            max_len = max(max_len, cur_num - num)
        return max_len
    

        
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))