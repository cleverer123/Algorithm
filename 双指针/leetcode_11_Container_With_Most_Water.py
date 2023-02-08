class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            h_l, h_r = height[l], height[r]
            area = min(h_l, h_r) * (r - l) 
            if area > max:
                max = area
            if h_l <= h_r:
                while l < r and  height[l + 1] <= min(h_l, h_r):
                        l += 1
                l += 1
                continue          
            if h_l > h_r:
                while l < r and height[r - 1] <= min(h_l, h_r):
                        r -= 1
                r -= 1
                continue
            
        return max

height = [1,8,6,2,5,4,8,3,7]      
print(Solution().maxArea(height)) 

            
