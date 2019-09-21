# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time O(nlogn) Space O(n)
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_set = set()

        while headA:
            node_set.add(headA)
            headA = headA.next

        
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next
        
        return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):    
        len_A = 0
        len_B = 0
        
        tmp_A = headA
        tmp_B = headB

        while headA:
            len_A += 1
            headA = headA.next
        
        while headB:
            len_B += 1
            headB = headB.next
        
        if len_A > len_B:
            for _ in range(len_A - len_B):
                tmp_A = tmp_A.next
        else:
            for _ in range(len_B - len_A):
                tmp_B = tmp_B.next
        
        while tmp_A and tmp_B:
            if tmp_A == tmp_B:
                return tmp_A
            else:
                tmp_A = tmp_A.next
                tmp_B = tmp_B.next
         
        return None

        
        







        

        


        