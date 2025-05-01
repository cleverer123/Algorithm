class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root:
            return 
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    # 迭代
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(-1)
            res.append(root.val)
            root = root.right
        return res

    # Morris 中序遍历
    def inorderTraversalMorris(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        predecessor = None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if predecessor.right == None:
                    predecessor.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
print(Solution().inorderTraversalMorris(root))
