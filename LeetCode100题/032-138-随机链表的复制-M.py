class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head ) :
        if not head:
            return None
        hashtable = {}
        cur = head
        while cur:
            new_node = Node(cur.val)
            hashtable[cur] = new_node
            cur = cur.next
        cur = head
        while cur:
            hashtable[cur].next = hashtable.get(cur.next)
            hashtable[cur].random = hashtable.get(cur.random)
            cur = cur.next
        return hashtable[head]

    # 方法二：先拼接后拆分