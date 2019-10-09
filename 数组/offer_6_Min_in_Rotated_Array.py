class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        res = rotateArray[0]
        for i in range(1, len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                res = min(res, rotateArray[i])
            
        return res

if __name__ == "__main__":
    arr = [3,4,5,1,2]
    print(Solution().minNumberInRotateArray(arr))