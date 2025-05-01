class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    # Morris遍历：如果当前节点的左节点为空，无需展开；
    # 如果当前节点左节点不为空，需要展开。寻找左子树的最右节点，当前节点的右子树链接到左子树最右节点的右子节点，
    # 当前节点左子节点置空，当前节点右子节点链接到当前节点原左子节点。
    # 当前节点前进一步，即当前节点置为其右子节点。
    # 4ms
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        predecessor = None
        while root:
            if root.left:
                predecessor = nxt = root.left
                
                while predecessor.right:
                    predecessor = predecessor.right
                
                predecessor.right = root.right
                root.left = None
                root.right = nxt
            root = root.right

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preOrderList = []
        self.preOrder(root)

        for i in range(1, len(self.preOrderList)):
            pre, cur = self.preOrderList[i - 1], self.preOrderList[i]
            pre.left = None
            pre.right = cur
        
    def preOrder(self, node):
        if node:
            self.preOrderList.append(node)
            self.preOrder(node.left)
            self.preOrder(node.right)