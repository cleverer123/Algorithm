from collections import defaultdict
class Solution(object):
    # 递归尝试，不对，因为存在不连续子串。
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 :
            return 0
        if len(nums)==0 and k > 0:
            return 0
        if len(nums) >=0 and k == 0:
            return 1
        res = 0
        res += self.subarraySum(nums[1:], k)
        res += self.subarraySum(nums[1:],  k-nums[0])
        return res

    # Hash表，统计sum-k出现的次数，复杂度Time: O(n) Space: O(n)
    def subarraySum2(self, nums, k):
        sum_map = defaultdict(lambda: 0)
        sum_map[0] = 1
        pre_sum = 0
        count = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            count += sum_map[pre_sum - k]
            sum_map[pre_sum] += 1
            
        return count
            



if __name__ == "__main__":
    nums = [1,1,-1,1]
    print(Solution().subarraySum2(nums, 1))