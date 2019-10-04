class Solution:
    # 递归解法 Time: O(2^n) Space: O(n)
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
    
    # 动态规划 Time： O(n) Space: O(n)
    def Fibonacci2(self, n):
        if n < 2:
            return n
        dp = [0]*(n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    # 动态规划修改版 Time： O(n) Space: O(3)
    def Fibonacci2(self, n):
        if n < 2:
            return n
        a = 0
        b = 1
        c = 0
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c
    
    # 通项公式
    import math
    def Fibonacci(self, n):
        # write code here
        sqrtFive = math.sqrt(5)
        return sqrtFive / 5 * (math.pow(((1 + sqrtFive) / 2), n) - math.pow(((1 - sqrtFive) / 2), n))


# [牛客网在线编程专题《剑指offer-面试题9》斐波那契数列](https://blog.csdn.net/program_developer/article/details/83505258)

