# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prehead = ListNode(-1, head)

        slow, fast = prehead, head
        while fast:
            i = k
            while fast and i > 0:
                fast = fast.next
                i -= 1
            if i > 0: break
            prev = fast
            cur = slow.next            
            while cur != fast:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = slow.next
            slow.next = prev
            slow = tmp

        return prehead.next
            
                
                