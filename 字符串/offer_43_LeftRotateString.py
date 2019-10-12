class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n<=0 or s =='':
            return s
        
        n = n % len(s)

        return s[n:]+s[:n]
        
        
