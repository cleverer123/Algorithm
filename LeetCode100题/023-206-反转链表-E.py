# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # None 1 -> 2
    # prev head head.next
    # tmp = head.next
    # head.next = prev
    # prev = head
    # head = tmp
    def reverseList(self, head):
        prev = None
        while head:
            # head.next, prev, head = prev, head, head.next
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp 

        # 1 -> 2 -> 3  null
        # h   tmp       p

        # --------------
        # |             |
        # 1    2 -> 3  null
        # h   tmp       p       

        # --------------
        # |             |
        # 1    2 -> 3  null
        # p   h/tmp

        # --------------
        # |             |
        # 1    2 -> 3  null
        # p    h       tmp   

        # --------------
        # |             |
        # 1 <- 2    3  null
        # p    h   tmp  

        # --------------
        # |             |
        # 1 <- 2    3  null
        #     p/h   tmp 

        # --------------
        # |             |
        # 1 <- 2    3  null
        #      p   h/tmp

        # --------------------
        # |                   |
        # 1 <- 2    3->null  null
        #      p    h   tmp

        # --------------------
        # |                   |
        # 1 <- 2 <- 3 null  null
        #      p    h  tmp

        # --------------------
        # |                   |
        # 1 <- 2 <- 3 null  null
        #          p/h  tmp

        # --------------------
        # |                   |
        # 1 <- 2 <- 3 null  null
        #           p  h/tmp

        return prev