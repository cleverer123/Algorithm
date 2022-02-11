# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def bst(root, k):
            if root : 
                bst(root.left, k)
                if len(res) >= k:
                    return 
                res.append(root.val)
                bst(root.right, k)            
        bst(root, k)
        return res[-1]

if __name__ == '__main__':
    r1 = root = TreeNode(5)
    r2 = root.left = TreeNode(3)
    r3 = root.right = TreeNode(6)
    r4 = r2.left = TreeNode(2)
    r5 = r2.right = TreeNode(4)
    r6 = r4.left = TreeNode(1)
    print(Solution().kthSmallest(root,3))

