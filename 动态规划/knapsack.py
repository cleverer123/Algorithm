class Solution():
    def knapsack(self, w, v, C):

        assert len(w) == len(v)

        dp = [[0]*(C+1) for _ in range(len(w))]

        for c in range(C+1):
            dp[0][c] = v[0] if c > w[0] else 0

        for i in range(1, len(v)):
            for j in range(C+1):
                dp[i][j] = dp[i-1][j]
                if j >= w[i]:
                    dp[i][j] = max(dp[i][j], v[i] + dp[i-1][j-w[i]])

        return dp[-1][-1]

    # 空间复杂度优化 O(C)
    def knapsack2(self, w, v, C):

        assert len(w) == len(v)

        dp = [0]*(C+1) 

        for c in range(C+1):
            dp[c] = v[0] if c > w[0] else 0

        for i in range(1, len(v)):
            for j in range(C, -1, -1):
                if j >= w[i]:
                    dp[j] = max(dp[j], v[i] + dp[j-w[i]])
                else:
                    continue

        return dp[-1]
# https://blog.csdn.net/program_developer/article/details/86292698
if __name__ == "__main__":
    w = [1, 2, 3]
    v = [6, 10, 12]
    C = 5
    print(Solution().knapsack2(w, v, C))

        

