# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def BST(node):
            if node:
                res.append(str(node.val))
                # res.append('#')
                BST(node.left)
                BST(node.right)
                        
        BST(root)
        return '#'.join(res) 
                     

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split('#')
        # res.pop()
        if len(res) == 0:
            return None
        root = TreeNode(int(res.pop(0)))

        vals = map(int, res)

        def bst_insert(node, insert_node):
            if insert_node.val < node.val:
                if node.left:
                    bst_insert(node.left, insert_node)
                else:
                    node.left = insert_node
            else:
                if node.right:
                    bst_insert(node.right, insert_node)
                else:
                    node.right = insert_node
      
        for val in vals:
            bst_insert(root, TreeNode(val))

        return root


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
# Your Codec object will be instantiated and called as such:

if __name__ == '__main__':
    nodes = [TreeNode(2*i) for i in range(7)]
    root = TreeNode(5)
    sol = Solution()
    sol.BST_insert(root, TreeNode(1))
    for node in nodes:
        sol.BST_insert(root, node)
    printTree(root, 0)
    codec = Codec()
    print(codec.serialize(root))
    printTree(codec.deserialize(codec.serialize(root)), 0)