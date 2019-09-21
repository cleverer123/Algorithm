# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node, path_val, stack):
            if not node:
                return
            
            if node.left == None and node.right == None and path_val + node.val == sum :
                res.append(stack + [node.val])
                return            
            
            dfs(node.left, path_val + node.val, stack + [node.val]) 
             
            dfs(node.right, path_val + node.val, stack + [node.val])                      
            
        dfs(root, 0, [])

        return res

def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if  __name__ == '__main__':
    node_list = [TreeNode(i) for i in range(12)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]

    # printTree(node_list[0], 0)
    print(Solution().pathSum(node_list[0], 11))


        