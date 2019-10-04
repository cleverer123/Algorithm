import numpy as np
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m = len(text1)
        n = len(text2)

        dp = np.zeros((m + 1, n + 1))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i, j] = dp[i-1, j-1] + 1
                else:
                    dp[i, j] = max(dp[i-1, j], dp[i, j-1])
        # res = 0
        # while m > 0 and n>0:
        #     if text1[m-1] == text2[n-1]:
        #         res += 1
        #         m -= 1
        #         n -= 1
        #     else:
        #         if dp[m-1, n] > dp[m, n-1] :
        #             m -= 1
        #         else: 
        #             n -= 1
        
        return int(dp[-1,-1])
    
if __name__ == "__main__":
    text1 = "abc"

    text2 = "def"
    print(Solution().longestCommonSubsequence(text1, text2))






        