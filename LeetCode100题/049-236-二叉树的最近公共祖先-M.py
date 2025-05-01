class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_anceslist = []
        self.ans = None
        def helper_p(root, anceslist):
            if root:
                if root == p:
                    self.p_anceslist = anceslist + [root]
                    return
                helper_p(root.left, anceslist + [root])
                helper_p(root.right, anceslist + [root])
        
        def helper_q(root, anceslist):
            if root:
                if root == q:
                    anceslist += [root]
                    for ances in reversed(anceslist):
                        if ances in self.p_anceslist:
                            self.ans = ances
                            return                   
                helper_q(root.left, anceslist + [root])
                helper_q(root.right, anceslist + [root])

        helper_p(root, [])
        helper_q(root, [])
        return self.ans

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def helper(root):
            if not root:
                return False
            lson = helper(root.left)
            rson = helper(root.right)
            if ( lson and rson ) or ( (root == p or root == q) and (lson or rson)) :
                self.ans = root
            return lson or rson or (root == p or root == q)
        helper(root)
        return self.ans

p = TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, right=TreeNode(1)))
q = TreeNode(-3, right=TreeNode(11))
root = TreeNode(10, p, q )
print(Solution().lowestCommonAncestor(root, p, q))
