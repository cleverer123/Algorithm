# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def dfs(root, tail):            
            if not root :
                return None
            if not (root.left or root.right):
                # tail = root
                return root          
            
            left = root.left 
            right = root.right
            left_tail = None
            right_tail = None

            if left:
                left_tail = dfs(left, None)              
                root.left = None
                root.right = left
                tail = left_tail
                    
            if right:
                right_tail = dfs(right, None)
                if left_tail:
                    left_tail.right = right
                tail = right_tail
                
            return tail

        dfs(root, None)       
        
class Solution(object):
    def flatten(self, root):
        while root:
            if not root.left:
                root = root.right
            else:
                prev = root.left
                while prev.right:
                    prev = prev.right
                
                prev.right = root.right
                root.right = root.left
                root.left = None
            
                root = root.right



def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if  __name__ == '__main__':
    node_list = [TreeNode(i) for i in range(6)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]

    printTree(node_list[0], 0)

    Solution().flatten(node_list[0])

    printTree(node_list[0], 0)


        