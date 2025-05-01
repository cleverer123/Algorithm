class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    # 广度优先搜索
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        h = 0
        if not root:
            return h
        stack = [root]
        while stack:
            size = len(stack)
            for _ in range(size):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            h += 1
        return h

    # 深度优先
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1