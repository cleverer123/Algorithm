from collections import deque
class Solution:
    # 单调队列
    def maxSlidingWindow(self, nums, k: int):
        ans = []
        queue = deque()
        for i, num in enumerate(nums):
            # 入队
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(num)

            # 出队，队首已经离开左边界
            if queue[0] < i - k:
                queue.popleft()
            
            # 窗口长度达成，开始输出结果
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans


        
