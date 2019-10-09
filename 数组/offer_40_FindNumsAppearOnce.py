class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = 0
        for e in array:
            ans ^= e
        
        FirstIdxIs1 = self.FindFirstIdxIs1(ans)

        num1, num2 = 0, 0
        for e in array:
            if self.IdxBitIs1(e, FirstIdxIs1):
                num1 ^= e
            else:
                num2 ^= e
        return num1, num2

    def FindFirstIdxIs1(self, num):
        idx = 0
        while num & 1 == 0 and idx <= 32:
            idx += 1
            num = num >> 1
        return idx
    
    def IdxBitIs1(self, num, idx):
        num = num >> idx
        return num & 1

if __name__ == "__main__":
    nums = [2,4,3,6,3,2,5,5]
    print(Solution().FindNumsAppearOnce(nums))

    