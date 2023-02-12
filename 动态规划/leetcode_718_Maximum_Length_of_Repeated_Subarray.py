class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = 0
        def getMaxLen(i, j):
            cnt = 0
            nonlocal res
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
                i += 1
                j += 1

        for j in range(len(nums2)):
            getMaxLen(0, j)
        for i in range(len(nums1)):
            getMaxLen(i, 0)
        return res

    def findLength2(self, nums1, nums2):
        dp = [0] * (len(nums2) + 1)
        res = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)-1, -1, -1):
                if nums2[j] == nums1[i]:
                    dp[j] = dp[j - 1] + 1
                    res = max(dp[j], res)
                else:
                    dp[j] = 0
            
        return res


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]
# nums1 = [1,2,3]
# nums2 = [0,0]
print(Solution().findLength2(nums1, nums2))   
