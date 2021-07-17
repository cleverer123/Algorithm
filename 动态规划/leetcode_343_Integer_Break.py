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
        # if n == 1 or n == 2 :
        #     return 1
        # mem = [-1] * (n + 1)
        # mem[1] = 1

        # for i in range(2, n + 1):
        #     for j in range(1, i):
        #         mem[i] = max(mem[i], j * (i-j), j * mem[i-j]) 
        
        # return mem[n]

        if n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        
        return dp[-1]

    def integerBreak4(self, n):
        if n == 2: 
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return pow(3, n // 3)
        if n % 3 == 1:
            return 4 * pow(3, (n - 4)// 3)
        if n % 3 == 2:
            return 2* pow(3, n // 3)

# https://blog.csdn.net/program_developer/article/details/83897339
# https://blog.csdn.net/qq874455953/article/details/83686522
if __name__ == "__main__":
    print(Solution().integerBreak4(10))        
        

        
