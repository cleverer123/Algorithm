class Solution:
    # 思路[双指针]：左右板其中一个向内移动一格，底-1，若移动长板，min(h(i), h(j))变小或者不变，面积必然减小，
    # 那么只需移动短板，min(h(i), h(j))可能变大，可使面积可能增大。
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            new_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, new_area)
        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
