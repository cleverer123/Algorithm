class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here

        if not root:
            return None 
        
        left = self.Mirror(root.left)
        right = self.Mirror(root.right)
        root.left = right
        root.right = left
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
    node_list = [TreeNode(i) for i in range(8)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]
    
    printTree(node_list[0], 0)

    printTree(Solution().Mirror(node_list[0]), 0)