class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return [] 
        queue_odd = [pRoot]
        queue_even = []
        flag = 1
        res = []
        odd = []
        even = []
        while len(queue_odd) > 0 or len(queue_even) > 0:
            if flag % 2 == 1:
                while len(queue_odd) > 0:
                    node = queue_odd.pop() 
                    odd.append(node.val)
                    if node.left:
                        queue_even.append(node.left)
                    if node.right:
                        queue_even.append(node.right)
                res.append(odd)
                odd = []
                flag += 1
            else:
                while len(queue_even) > 0:
                    node = queue_even.pop()
                    even.append(node.val)
                    if node.right:
                        queue_odd.append(node.right)
                    if node.left:
                        queue_odd.append(node.left)
                res.append(even)
                even = []
                flag += 1
            
        return res

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)
    
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7
    # A5.left = A7
 
    solution=Solution()    
    print(solution.Print(A1))    
