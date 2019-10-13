class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        left_tree = pRootOfTree.left

        #找到左子树的最右节点
        if left_tree:
            while left_tree.right:
                left_tree = left_tree.right
            pRootOfTree.left = left_tree
            left_tree.right = pRootOfTree

        self.Convert(pRootOfTree.right)
        right_tree = pRootOfTree.right

        # 找到右子树的最左节点
        if right_tree:
            while right_tree.left:
                right_tree = right_tree.left
            pRootOfTree.right = right_tree
            right_tree.left = pRootOfTree

        # 返回最左端链表头
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        
        return pRootOfTree
