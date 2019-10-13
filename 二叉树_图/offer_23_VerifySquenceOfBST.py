class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True

        root = sequence[-1]
        i = 0
        while sequence[i] < root :
            i += 1
        for i in range(i, len(sequence) - 1):
            if sequence[i] < root:
                return False
        
        left, right = True, True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return  left and right
