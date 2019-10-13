class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.count = 0
        def KthNodeCore(pRoot, k):
            target = None
            if not pRoot:
                return None
            
            target = target or KthNodeCore(pRoot.left, k)
            self.count += 1
            if self.count == k:
                target =  pRoot
            target = target or KthNodeCore(pRoot.right, k)
            return target
        
        return KthNodeCore(pRoot, k)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
if __name__=='__main__':
    A1 = TreeNode(5)
    A2 = TreeNode(3)
    A3 = TreeNode(7)
    A4 = TreeNode(2)
    A5 = TreeNode(4)
    A6 = TreeNode(6)
    A7 = TreeNode(8)
    
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7
    # A5.left = A7
 
    solution=Solution()    
    print(solution.KthNode(A1, 3).val)    
