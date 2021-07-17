class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k :
            return None
        p1 = head
        p2 = head
        while p1 and k > 0:
            p1 = p1.next
            k -= 1
        
        if k > 0:
            return None
        
        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2