import math
class Solution(object):
    # 动态规划  失败  超时
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        k = 1
        
        for x in range(1, n+1):
            k = int(math.sqrt(x))
            if k**2 == x:
                dp[x] = 1
            else:
                tmp = []
                for j in range(1, x):
                    tmp.append(dp[j] + dp[x-j])
                # for j in range(2, x//2 + 1):
                #     tmp_max = min(tmp_max, dp[j] + dp[x-j])
                dp[x] = min(tmp)
        return dp[-1]

    # def numSquares(self, n: int) -> int:
    #     dp = [0] * (n + 1)
    #     k = 1
    #     x = 1
    #     while x <= n :
    #         if (k+1)**2 ==x:
    #             k += 1
    #             continue
    #         if k**2 == x:
    #             dp[x] = 1
    #         else:
    #             tmp_max = dp[k**2] + dp[x-k**2]
    #             for j in range(1, k):
    #                 tmp_max = min(tmp_max, dp[j**2] + dp[x-j**2])
    #             dp[x] = tmp_max
    #         x +=1
    #     return dp[-1]

# Lagrange 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
    def numSquares(self, n):
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        if int(math.sqrt(n)) ** 2 == n: return 1
        i = 1
        while i*i <= n:
            j = math.sqrt(n - i*i)
            if int(j) == j: return 2
            i += 1
        return 3
# https://blog.csdn.net/huhehaotechangsha/article/details/86597713

if __name__ == "__main__":
    # for i in range(1, 13):
    print(Solution().numSquares(13))        