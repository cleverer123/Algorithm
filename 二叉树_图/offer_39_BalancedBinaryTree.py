class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here

        def dfs(root):
            if not root:
                return True, 0
            w_l, h_l = dfs(root.left)
            w_r, h_r = dfs(root.right)

            if not w_l or not w_r or abs(h_l - h_r) > 1:
                return False, 0

            return True, max(h_l, h_r) + 1

        res, _ = dfs(pRoot)  

        return res

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    
 
    A1.left=A2
    # A1.right=A3
    A2.left=A3
    A3.left=A4
    A4.left=A5
 
    solution=Solution()
    ans=solution.IsBalanced_Solution(A1)
    print('ans=',ans)
        