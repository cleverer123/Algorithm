class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def BST_insert(self, node, insert_node):
      
        if insert_node.val < node.val :
            if node.left:
                self.BST_insert(node.left, insert_node)
            else:
                node.left = insert_node
        else:
            if node.right:
                self.BST_insert(node.right, insert_node)
            else:
                node.right = insert_node
        
    
    def BSF_search(self, node, target):
        if target == node.val:
            return True
        elif target < node.val:
            if node.left:
                return self.BSF_search(node.left, target)
            else:
                return False

        else:
            if node.right:
                return self.BSF_search(node.right, target)
            else:
                return False


def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if __name__ == '__main__':
    nodes = [TreeNode(2*i) for i in range(7)]
    root = TreeNode(5)
    sol = Solution()
    sol.BST_insert(root, TreeNode(1))
    for node in nodes:
        sol.BST_insert(root, node)
    printTree(root, 0)
    for i in range(10):
        print(i, sol.BSF_search(root, i))