class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    # 递归，但递归过程中传递的参数是数组，会开辟新的空间
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if not inorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        root_idx = inorder.index(val)
        root.left = self.buildTree(preorder[1: 1 + root_idx], inorder[0: root_idx])
        root.right = self.buildTree(preorder[1 + root_idx: len(preorder)], inorder[root_idx + 1: len(inorder)])
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def mybuild(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            val = preorder[pre_left]
            root = TreeNode(val)

            root_idx = index[val]

            root.left = mybuild(pre_left + 1, pre_left + root_idx - in_left, in_left, root_idx - 1)
            root.right = mybuild(pre_left + root_idx - in_left + 1, pre_right, root_idx + 1, in_right)
            return root
        index = {element: i for i, element in enumerate(inorder)}
        return mybuild(0, len(preorder) - 1, 0, len(preorder) - 1)