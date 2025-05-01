class Solution:
    # 按行解，会超时
    def trap1(self, height) -> int:
        area = 0
        for h in range(1, max(height) + 1):
            isStart = False
            tmp = 0
            for i in range(len(height)):
                if isStart and height[i] < h:
                    tmp += 1
                if height[i] >= h:
                    area += tmp
                    tmp = 0
                    isStart = True
        return area
    
    # 按列求，对某一列来说，需关注该列左边最高的墙和右边最高的墙，
    # 能装多少水则看左边最高列和右边最高列中较矮的一个
    # O(n^2) 超时
    def trap2(self, height):
        area = 0
        for i in range(1, len(height) - 1):

            left_max = 0
            for left in range(0, i):
                left_max = max(left_max, height[left])
            right_max = 0
            for right in range(i + 1, len(height)):
                right_max = max(right_max, height[right])
            
            if height[i] < min(left_max, right_max):
                area += min(left_max, right_max) - height[i]
        return area
    
    # 动态规划，将目标列左边最高的列和右边最高的列记录在数组
    # 时间复杂度O(n),空间复杂度O(n)
    def trap3(self, height):
        area = 0
        left_max = [0] * len(height)
        left_max[0] = height[0]
        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        for j in range(len(height) - 2, 0, -1):
            right_max[j] = max(right_max[j + 1], height[j])
        
        for i in range(1, len(height) - 1):
            if height[i] < min(left_max[i], right_max[i]):
                area += min(left_max[i], right_max[i]) - height[i]
        return area

    # 双指针优化, 
    # 时间复杂度O(n)，空间复杂度O(1)
    def trap4(self, height):
        area = 0
        left_max = height[0]
        right_max = height[-1]
        left, right = 1, len(height) - 2
        while left <= right:
            left_max = max(left_max, height[left - 1])
            right_max = max(right_max, height[right+1])
            if left_max < right_max:
                if left_max > height[left]:
                    area += left_max - height[left]
                left += 1
            else:
                if right_max > height[right]:
                    area += right_max - height[right]
                right -= 1
        return area
    
    # 栈，类比括号匹配
    # 遍历墙高，若当前墙高小于栈顶墙高，说明此处有积水，将墙的下标入栈，
    # 若当前墙高大于栈顶墙高，说明坑已形成，可以计算积水了，计算完，入栈，作为新的积水的墙。
    def trap(self, height):
        area = 0
        stack = []
        for i in range(0, len(height)):
            while stack and height[stack[-1]] < height[i]:
                h = height[stack.pop(-1)]
                if not stack:
                    break
                distance = i - stack[-1] - 1 
                area += (min(height[stack[-1]], height[i]) - h) * distance
            stack.append(i)
        return area

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height= [4,2,0,3,2,5]

print(Solution().trap(height))

                

