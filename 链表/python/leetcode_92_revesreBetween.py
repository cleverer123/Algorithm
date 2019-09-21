
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        change_len = n - m + 1
        pre_head = None
        result = head
        for _ in range(m-1):
            pre_head = head
            head = head.next

        reversed_tail = head 
        new_head = None
        for _ in range(change_len):
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        
        reversed_tail.next = head

        if pre_head :
            pre_head.next = new_head
        else:
            result = new_head
        return result    



            
        
            

        



