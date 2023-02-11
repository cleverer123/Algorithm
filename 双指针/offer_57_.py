class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        left = 1
        right = 1
        sum = 0
        res = []
        while left <= target / 2:
            if sum < target:
                sum += right
                right += 1
            else:
                if sum == target:
                    res.append([i for i in range(left, right)])
                sum -= left
                left += 1
            
        return res


print(Solution().findContinuousSequence(7))            
