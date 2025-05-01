class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res =[]
        while stack:
            size = len(stack)
            layer = []
            for _ in range(size):
                node = stack.pop(0)
                layer.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            res.append(layer)
        return res