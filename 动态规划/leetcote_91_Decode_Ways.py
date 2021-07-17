class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 and s[0]=='0':
            return 0
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            p = int(s[i-1])
            xp = int(s[i-2]) * 10 + p

            if p == 0:
                if xp < 10 or xp > 26:
                    # wuxiao
                    dp[i] = 0
                else:
                    dp[i] = dp[i-2]
            else:
                if xp < 10 or xp > 26:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def numDecodings2(self, s):
        if len(s) == 1 and s[0] == '0':
            return 0  
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            u = int(s[i - 1])
            uu = int(s[i - 2]) * 10 + u

            if u == 0:
                if uu < 10 or uu > 26:
                    dp[i] = 0
                else:
                    dp[i] = dp[i-2]
            else:
                if uu < 10 or uu > 26:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


# https://blog.csdn.net/program_developer/article/details/84324701
if __name__ == "__main__":
    s = "276"
    print(Solution().numDecodings(s))

