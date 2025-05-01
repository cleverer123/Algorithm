class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [0] * n
        res = []
        def backtracking(depth, path):
            if depth == n:
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i] = 1
                    backtracking(depth + 1, path + [nums[i]])
                    used[i] = 0

        backtracking(0, [])
        return res
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtracking(depth):
            if depth == n - 1:
                res.append(list(nums))
            for i in range(depth, n):
                nums[i], nums[depth] = nums[depth], nums[i]
                backtracking(depth + 1)
                nums[i], nums[depth] = nums[depth], nums[i]
        backtracking(0)
        return res

