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
        if not root:
            return 'N'
        queue = [root]
        res = []
        while len(queue) > 0 :
            front = queue.pop(0)
            if not front:
                res.append('N')
                continue
            else:
                res.append(str(front.val))
            queue.append(front.left)
            queue.append(front.right)                

        return '#'.join(res)            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split('#')
        if res[0] == 'N':
            return None

        root = TreeNode(int(res.pop(0)))

        queue = [root]
        while len(res) > 0:
            node = queue.pop(0)
            if node:
                if res[0]=='N':
                    queue.append(None)
                else: 
                    node.left = TreeNode(int(res[0]))
                    queue.append(node.left)
                res.pop(0)

                if res[0] == 'N':
                    queue.append(None)
                else:
                    node.right = TreeNode(int(res[0]))    
                    queue.append(node.right)           
                res.pop(0)
            else:
                res.pop(0)
                res.pop(0) 

        return root


        # root = TreeNode(int(res[0]))
        # i = 0
        # queue = [[root, 0]]
        # while len(queue) > 0:
        #     front = queue.pop(0)
        #     node = front[0]
        #     depth = front[1]
        #     if res[2*depth] != 'N':
        #         node.left = TreeNode(int(res[2*depth]))
        #         queue.append([node.left, depth + 1])
        #     if res[2*depth+1] != 'N':
        #         node.right = TreeNode(int(res[2*depth+1]))
        #         queue.append([node.right, depth + 1])


class Solution:
    def BT_insert(self, root, insert_node):
        queue = [root]
        while len(queue) > 0 :
            node = queue.pop(0)
            if insert_node.val > node.val:
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = insert_node
                    break
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = insert_node 
                    break
            elif insert_node.val <= node.val:
                # 输入序列是有序时则，不会出现这种情况
                break



         

    def layer_dfs(self, node, layer):
        if not node:
            return
        
        for i in range(layer):
            print('....', end='')
        print(node.val)
        self.layer_dfs(node.left, layer+1)
        self.layer_dfs(node.right, layer+1)

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

if __name__ == '__main__':
    nodes = [TreeNode(2*i) for i in range(3)]
    root = TreeNode(0)
    sol = Solution()
    for node in nodes:
        sol.BT_insert(root, node)
    # sol.layer_dfs(root, 0)
    sol.layer_bfs(root)
    
# Your Codec object will be instantiated and called as such:
    codec = Codec()
    print(codec.serialize(root))
    sol.layer_bfs(codec.deserialize(codec.serialize(root)))