class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.targetSum = targetSum
        def helper(root, pathsum):
            if root:
                cursum = pathsum[-1] + root.val
                for s in pathsum:
                    if cursum - s == self.targetSum:
                        self.ans += 1
                
                helper(root.left, pathsum + [cursum])
                helper(root.right, pathsum + [cursum])

        helper(root, [0])
        return self.ans
    
# root = [10,5,-3,3,2,null,11,3,-2,null,1]
root = TreeNode(10,TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, right=TreeNode(1))), TreeNode(-3, right=TreeNode(11)))
targetSum = 8
print(Solution().pathSum(root, targetSum))