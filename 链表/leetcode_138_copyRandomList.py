# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        ptr = head
        node_map = {}
        
        while ptr:
            node_map[ptr] = Node(ptr.val, None, None)          
            ptr = ptr.next
        
        ptr = head

        while ptr: 
            if ptr.next:
                node_map[ptr].next = node_map[ptr.next]
            else:
                node_map[ptr].next = None

            if ptr.random:
                node_map[ptr].random = node_map[ptr.random]
            else:
                node_map[ptr].random = None
            
            ptr = ptr.next
        
        return node_map[head]
            