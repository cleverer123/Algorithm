class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root) 

    def helper(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        if lower >= node.val or node.val >= upper:
            return False
        
        return True and self.helper(node.left, lower, node.val) and self.helper(node.right, node.val, upper)
    
    # 中序遍历：递归
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        predecessor = root
        def helper(root):
            if not root:
                return True
            if not helper(root.left):
                return False
            if predecessor and predecessor.val >= root.val:
                return False
            predecessor = root
            return helper(root.right)
    # 中序遍历：迭代
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        predece = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val >= predece:
                return False
            predece = root.val
            
            root = root.right

        return True