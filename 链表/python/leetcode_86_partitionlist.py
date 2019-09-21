# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = less_ptr = ListNode(0)
        more_head = more_ptr = ListNode(0)

        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = head
            else:
                more_ptr.next = head
                more_ptr = head

            head = head.next

        less_ptr.next = more_head.next
        more_ptr.next = None
        return less_head.next


            
