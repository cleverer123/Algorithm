class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0:
            return False

        i = 0
        j = len(array[0]) - 1 
        
        while i < len(array) and j >=  0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1 
        return False

