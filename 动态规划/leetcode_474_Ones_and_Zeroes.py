class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            c0, c1 = s.count('0'), s.count('1')
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i - c0][j - c1] + 1, dp[i][j])
        
        return dp[-1][-1]
    
if __name__ == "__main__":
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m , n)) 
