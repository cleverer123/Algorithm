# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        new_head = ptr = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        # if l1:
        #     ptr.next = l1
        # if l2:
        #     ptr.next = l2    
        ptr.next = l1 or l2
        return new_head.next


