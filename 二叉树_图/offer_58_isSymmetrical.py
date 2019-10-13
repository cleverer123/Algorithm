class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.symmetrical(pRoot, pRoot)
    
    def symmetrical(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.symmetrical(root1.left, root2.right) and self.symmetrical(root1.right, root2.left)  


            

if __name__=='__main__':
    A1 = TreeNode(8)
    A2 = TreeNode(6)
    A3 = TreeNode(6)
    A4 = TreeNode(5)
    A5 = TreeNode(7)
    A6 = TreeNode(7)
    A7 = TreeNode(5)
    
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7
    # A5.left = A7
 
    solution=Solution()    
    print(solution.isSymmetrical(A1))    