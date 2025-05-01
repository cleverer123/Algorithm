from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] != target:
                    continue
                else:
                    return [i, j]
                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [i, hashtable[target - nums[i]]]
            hashtable[nums[i]] = i
        return []