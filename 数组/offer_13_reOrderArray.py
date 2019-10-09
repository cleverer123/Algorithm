class Solution:
    def reOrderArray(self, array):
        # write code here
        boder = -1
        for i in range(len(array)):
            if array[i] % 2 != 0:
                boder += 1
                array.insert(boder, array.pop(i))
        return array