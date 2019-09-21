class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        c = 0
        z = 0
        while c < len(g) and z < len(s):
            if g[c] <= s[z]:
                c += 1
            z += 1
        
        return c
             