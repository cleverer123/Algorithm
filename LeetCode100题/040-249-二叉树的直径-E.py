class Solution:
    # 任意一条路径都可看作某节点，从左儿子向下的路径和右儿子向下的路径拼接得到
    def diameterOfBinaryTree(self, root ) -> int:
        self.ans = -1
        self.maxDepth(root)
        return self.ans - 1
        
    def maxDepth(self, node):
        if not node:
            return 0
        L = self.maxDepth(node.left)
        R = self.maxDepth(node.right)
        self.ans = max(L + R + 1, self.ans)
        return max(L, R) + 1
