# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs(self, root):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            
            print(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
          
    def layer_bfs(self, root):
        queue = [[root, 0]]
        while len(queue) > 0:
            front = queue.pop(0)
            node = front[0]
            depth = front[1]

            for i in range(depth):
                print('----', end='')         
            print(node.val)            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    def dfs(self, root):
        if not root:
            return
        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def layer_dfs(self, node, layer):
        if not node:
            return
        
        for i in range(layer):
            print('....', end='')
        print(node.val)
        self.layer_dfs(node.left, layer+1)
        self.layer_dfs(node.right, layer+1)


if  __name__ == '__main__':
    node_list = [TreeNode(i) for i in range(6)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]
    # Solution().bfs(node_list[0])          
    # Solution().dfs(node_list[0])  
    Solution().layer_bfs(node_list[0])          
    Solution().layer_dfs(node_list[0], 0)          

