class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: len(nums)])
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)


nums = [-10,-3,0,5,9]
def printTree(root):
    if not root:
        print('None')
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
printTree(Solution().sortedArrayToBST(nums))