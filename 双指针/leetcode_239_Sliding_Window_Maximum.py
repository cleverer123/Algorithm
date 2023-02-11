class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 遍历给定数组中的元素，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。直到，队列为空或当前考察元素小于新的队尾元素；
        # 当队首元素的下标小于滑动窗口左侧边界left时，表示队首元素已经不再滑动窗口内，因此将其从队首移除。
        # 由于数组下标从0开始，因此当窗口右边界right+1大于等于窗口大小k时，意味着窗口形成。此时，队首元素就是该窗口内的最大值。

        # 作者：hardcore-aryabhata
        # 链接：https://leetcode.cn/problems/sliding-window-maximum/solution/dong-hua-yan-shi-dan-diao-dui-lie-239hua-hc5u/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        que = []
        res = []
        for right in range(len(nums)):

            while que and nums[right] > nums[que[-1]]:
                que.pop(-1)

            que.append(right)    
            
            if right + 1 >= k:
                if que[0] < right + 1 - k:
                    que.pop(0)
                res.append(nums[que[0]])
        
        return res
                

nums = [1,3,-1,-3,5,3,6,7]
k = 3               
print(Solution().maxSlidingWindow(nums, k))


            