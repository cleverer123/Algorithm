class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 1 :
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        idx = tin.index(pre[0])
        left = None
        right = None 
        if idx > 0:
            left = self.reConstructBinaryTree(pre[1:idx+1], tin[:idx])
        
        if idx < len(tin) - 1:
            right = self.reConstructBinaryTree(pre[idx+1:], tin[idx+1:])

        root.left = left
        root.right = right

        return root

def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]

    root = Solution().reConstructBinaryTree(pre, tin)
    printTree(root, 0)


        
        
