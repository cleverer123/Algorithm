# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node_set = set()

        while head:
            if not head in node_set:
                node_set.add(head)
                head = head.next
            else:
                return head
        
        return None
    
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        meet = None
        while fast:
            slow = slow.next
            fast = fast.next

            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                meet = fast
                break
        
        if not meet:
            return None
        
        while head and meet:
            if head == meet:
                return head
            else:
                head = head.next
                meet = meet.next
        
        return None

class Solution22(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                has_cycle = True                
                break        
        
        if not has_cycle:
            return None

        fast = head

        while fast and slow:
            if fast == slow:
                return slow
            else:
                fast = fast.next
                slow = slow.next
        
