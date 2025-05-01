class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            max_sum = max(max(l + r, l, r) + root.val, root.val)
            if max_sum > self.ans:
                self.ans = max_sum           
            return max(max(l, r) + root.val, root.val)
        helper(root)
        return self.ans
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def helper(root):
            if not root:
                return 0
            l = max(helper(root.left), 0)
            r = max(helper(root.right), 0)
            max_sum = l + r + root.val
            if max_sum > self.ans:
                self.ans = max_sum           
            return max(l, r) + root.val 
        helper(root)
        return self.ans