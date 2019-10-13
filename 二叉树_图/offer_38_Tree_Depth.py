class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0    
        h_l = self.TreeDepth(pRoot.left)
        h_r = self.TreeDepth(pRoot.right)
        return max(h_l, h_r) + 1

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)
    
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    # A3.left = A4
    A3.right = A6
    A5.left = A7
 
    solution=Solution()    
    print(solution.TreeDepth(A1))    
