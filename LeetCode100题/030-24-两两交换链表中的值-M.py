# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1, head)
        if not head :
            return head
        slow, fast = prehead, head.next
        while fast:
            tmp = fast.next
            fast.next = slow.next
            slow.next = fast
            fast.next.next = tmp

            slow = fast.next
            fast = tmp.next if tmp else None
        return prehead.next