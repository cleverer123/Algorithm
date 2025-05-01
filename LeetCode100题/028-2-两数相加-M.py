# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        p = 0
        while l1 or l2 :
            r = 0
            if l1:
                r += l1.val
            if l2:
                r += l2.val
            r += p
            p = r // 10
            cur.next = ListNode(r % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if p > 0:
            cur.next = ListNode(p)
        return head.next
