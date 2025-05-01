# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 双指针
    def getIntersectionNode(self, headA, headB):
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A 

class Solution:
    # 哈希表
    def getIntersectionNode(self, headA, headB):
        A = headA
        hashtable = set()
        while A:
            hashtable.add(A)
            A = A.next

        B = headB
        while B:
            if B in hashtable:
                return B
            B = B.next
        return None
    