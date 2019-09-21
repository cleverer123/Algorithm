# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        
        mid = len(lists) // 2
        sub1_lists = lists[:mid]
        sub2_lists = lists[mid:]
        
        l1 = self.mergeKLists(sub1_lists)
        l2 = self.mergeKLists(sub2_lists)

        return self.mergeTwoLists(l1, l2)
        
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
        ptr.next = l1 or l2
        return new_head.next    