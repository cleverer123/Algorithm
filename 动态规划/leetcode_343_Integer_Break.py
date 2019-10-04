class Solution(object):
    # 递归
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2 :
            return 1
        maxProduct = 1
        for i in range(1, n):

            maxProduct = max(maxProduct, i * (n-i), i * self.integerBreak(n-i) )

        return maxProduct

    # 记忆化搜索
    def integerBreak2(self, n):
        if n == 1 or n == 2 :
            return 1
        mem = [-1] * (n + 1)
        mem[1] = 1
        mem[2] = 1
        maxProduct = 1
        for i in range(3, n):
            maxProduct = max(maxProduct, i * (n - i), i * self.integerBreak2(n-i))
        mem[n] = maxProduct
        return maxProduct

    # 动态规划
    def integerBreak3(self, n):
        if n == 1 or n == 2 :
            return 1
        mem = [-1] * (n + 1)
        mem[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                mem[i] = max(mem[i], j * (i-j), j * mem[i-j]) 
        
        return mem[n]

# https://blog.csdn.net/program_developer/article/details/83897339
if __name__ == "__main__":
    print(Solution().integerBreak3(10))        
        

        
