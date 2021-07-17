class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        newHead = None        
        while pHead:
            next = pHead.next
            pHead.next = newHead
            newHead = pHead
            pHead = next
        return newHead
            
