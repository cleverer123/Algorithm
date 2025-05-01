class Solution:
    def detectCycle(self, head )  :
        hashtable = set()
        cur = head
        while cur:
            if cur in hashtable:
                return cur
            hashtable.add(cur) 
            cur = cur.next
        return None