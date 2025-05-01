class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        predecessor = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
    # 递归
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        
        def helper(node):
            if not node:
                return 
            self.helper(node.left)
            k -= 1
            if k == 0:
                ans = node.val
                return
            self.helper(node.right)
        helper(root)
        return ans
                