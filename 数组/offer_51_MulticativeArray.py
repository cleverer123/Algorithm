class Solution:
    def multiply(self, A):
        # write code here
        if len(A) == 0:
            return []
        B1 = [1] * len(A)

        for i in range(1, len(A)):
            B1[i] = B1[i-1] * A[i-1]

        B2 = [1] * len(A)
        for i in range(len(A)-2, -1, -1):
            B2[i] = B2[i+1] * A[i+1]

        for i in range(len(A)):
            B1[i] *= B2[i]
        
        return B1