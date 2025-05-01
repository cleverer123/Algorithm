# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 哈希表
    def hasCycle(self, head ) -> bool:
        hashtable = set()
        cur = head
        while cur:
            if cur in hashtable:
                return True
            hashtable.add(cur)
            cur = cur.next
        return False

    # 快慢指针 慢走一、快走二，环内必相遇
    def hasCycle(self, head ) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True