from collections import defaultdict
class Solution:
    # 前缀和，  
    def subarraySum(self, nums, k: int) -> int:
        s = [0] * len(nums)
        for i in range(1, len(nums)):
            s[i] = s[i - 1] + nums[i - 1]
        cnt = defaultdict(int)
        res = 0
        for sj in s:
            res += cnt[sj - k]
            cnt[s] += 1       
        return res

    # 一次遍历
    def subarraySum(self, nums, k: int) -> int:
        s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            res += cnt[s - k]
            cnt[s] += 1
           
        return res

nums = [1,1,1]
k = 2
# nums = [-1,-1,1]
# k = 0
print(Solution().subarraySum(nums, k))
