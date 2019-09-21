# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        return new_head

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            head.next, new_head, head = new_head, head, head.next
        return new_head
