class TreeNode(object):
    def __init__(self, x):
        self.val = x
        # res[0] 不抢当前节点能取到的最大值，res[1]抢劫当前节点能取到的最大值
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if not node:
                return [0, 0]
            left_res = dfs(node.left)
            right_res = dfs(node.right)
            res = [0, 0]
            res[0] = max(left_res) + max(right_res)
            res[1] = node.val + left_res[0] + right_res[0]
            return res

        return max(dfs(root))

def createTree(nodelist):
    if len(nodelist) == 0:
        return None
    root = TreeNode(nodelist[0])

    queue = [root]
    j = 1
    while j < len(nodelist):
        node = queue.pop(0)
        node.left = TreeNode(nodelist[j]) if nodelist[j] != None else None
        queue.append(node.left)
        j += 1
        node.right = TreeNode(nodelist[j]) if nodelist[j] != None else None
        j += 1
        queue.append(node.right)

    return root


# https://blog.csdn.net/program_developer/article/details/86102212

if __name__ == "__main__":
    # elements = [3,2,3,None,3,None,1]
    elements = [3, 4, 5, 1, 3, None, 1]
    root = createTree(elements)
    print(Solution().rob(root))