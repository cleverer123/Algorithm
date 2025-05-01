class Node:
    def __init__(self):
        self.is_end = False
        self.next = [None] * 26

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            c_idx = ord(c) - ord('a')
            if not cur.next[c_idx]:
                cur.next[c_idx] = Node()
            cur = cur.next[c_idx]
        cur.is_end = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            c_idx = ord(c) - ord('a')
            if cur.next[c_idx]:
                cur = cur.next[c_idx]
            else:
                return False
        return cur.is_end           

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            c_idx = ord(c) - ord('a')
            if cur.next[c_idx]:
                cur = cur.next[c_idx]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)