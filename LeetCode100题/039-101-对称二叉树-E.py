class Solution:
    def isSymmetric(self, root ) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
       
    def isMirror(self, l, r):
        if not l and not r:
            return True
        elif not l and r or l and not r:
            return False
        return l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)