# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.inOrder(root)
        
    def inOrder(self, root):
        if not root:
            return True
        if not self.inOrder(root.left):
            return False
        if self.prev and root.val <= self.prev.val:
            return False
        self.prev = root
        return self.inOrder(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().isValidBST(root))        


