# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if p is None:
            return q
        if q is None:
            return p
        if p == root or q == root:
            return root
        
        def dfs(node, search, path, finish):
            if finish :
                return
            if node == search:
                finish = 1
                res.append( path )
                return 
            if node.left:
                dfs(node.left, search, path + [node.left], finish)
            if node.right:
                dfs(node.right, search, path + [node.right], finish)

        res = []
        dfs(root, p, [root], 0)
        dfs(root, q, [root], 0)
        
        path_len = len(res[0]) if len(res[0]) < len(res[1]) else len(res[1])

        result = None
        for i in range(path_len):
            if res[0][i] == res[1][i]:
                result = res[0][i]
       
        return result

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root:
            if root == p or root == q:
                return root

            else:
                left = root.left and self.lowestCommonAncestor(root.left, p, q)

                right = root.right and self.lowestCommonAncestor(root.right, p, q)

                if left and right:
                    return root
                return left or right
        
        return None

if  __name__ == '__main__':
    node_list = [TreeNode(i) for i in range(4)]
    for i, node in enumerate(node_list):
        if 2*i + 1 < len(node_list):
            node.left = node_list[2*i+1]
        if 2*i + 2 < len(node_list):
            node.right = node_list[2*i+2]

    # printTree(node_list[0], 0)
    print(Solution().lowestCommonAncestor(node_list[0], node_list[1], node_list[3]))
