class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here

        if not pNode:
            return None
        if pNode.right :
            right = pNode.right
            while right.left:
                right = right.left
            return right
        else:
            cur  = pNode
            par = pNode.next
            #  当前结点无右子树，则需要找到一个它的父结点（包括自己）为左子树结点的父结点
            while par and par.right == cur:
                cur = par
                par = cur.next
            return par

if __name__=='__main__':
    A1 = TreeLinkNode(1)
    A2 = TreeLinkNode(2)
    A3 = TreeLinkNode(3)
    A4 = TreeLinkNode(4)
    A5 = TreeLinkNode(5)
    A6 = TreeLinkNode(6)
    A7 = TreeLinkNode(7)
    
 
    A1.left = A2
    A1.right = A3
    
    A2.left = A4
    A2.right = A5
    A2.next = A1

    A3.left = A6
    A3.right = A7
    A3.next = A1

    A4.next = A2
    A5.next = A2 

    A6.next = A3
    A7.next = A3
 
    solution=Solution()    
    # print(solution.GetNext(A2).val)          
    # print(solution.GetNext(A3).val) 
    print(solution.GetNext(A4).val) 
    # print(solution.GetNext(A5).val) 
    # print(solution.GetNext(A6).val) 
    # print(solution.GetNext(A7).val)          



