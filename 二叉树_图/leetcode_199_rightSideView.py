# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [[root, 0]]
        view = []
        while len(queue) > 0:
            node_pair = queue.pop(0)
            node = node_pair[0]
            depth = node_pair[1]
            
            if len(view) < depth + 1:
                view.append(node.val)
            else:
                view[depth] = node.val

            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        
        return view

def printTree(node, layer):
    if not node:
        return
    
    for i in range(layer):
        print('....', end='')
    print(node.val)
    printTree(node.left, layer+1)
    printTree(node.right, layer+1)

if  __name__ == '__main__':
    node_list = [TreeNode(i) for i in range(8)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]
    printTree(node_list[0], 0)

    view = Solution().rightSideView(node_list[0])
    print(view)