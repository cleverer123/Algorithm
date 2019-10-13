class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        def dfs(node, num, path):
            if not node:
                return 
            if not node.left and not node.right and num == node.val:
                res.append( path + [node.val])
                return
            dfs(node.left, num - node.val, path + [node.val])
            dfs(node.right, num - node.val, path + [node.val])
        dfs(root, expectNumber, [])

        return res

def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
 
    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    A4.left=A6
    
    printTree(A1, 0)

    solution=Solution()
    ans=solution.FindPath(A1,8)
    print('ans=',ans)   

