class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        m = len(str1)
        n = len(str2)

        if not m:
            return str2
        if not n:
            return str1

        dp = [[0]*(n+1) for _ in range(m+1) ]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        res = []    
        while m > 0 and n > 0:

            if dp[m][n] == dp[m-1][n]:
                res.insert(0, str1[m-1])
                m -= 1
                
            elif dp[m][n] == dp[m][n-1]:
                res.insert(0, str2[n-1])
                n -= 1
            else:
                res.insert(0, str1[m-1])
                m -= 1
                n -= 1
                
        if m > 0 :
            res.insert(0, str1[0: m])
        if n > 0:
            res.insert(0, str2[0: n])
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if str1[i-1] == str2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # lcs = dp[-1][-1]
        

        # p, q = m, n
        # bp, bq = -1, -1
        # common = []
        # not_common = []
        # for i in range(lcs, 0, -1):
        #     bp, bq = p, q

        #     while p-1 > 0 and dp[p-1][q] == i: p -= 1
        #     while q-1 > 0 and dp[p][q-1] == i: q -= 1
        #     common.append(str1[p])
        #     not_common.append([str1[p+1:bp], str2[q+1:bq]])
        #     p -= 1
        #     q -= 1
        # not_common.append([str1[0:p], str2[0:q]])

        # res = not_common[-1]

        # for nc, c in zip(not_common[:-1][::-1], common[::-1]):
        #     res.append(c)
        #     res += nc
                
        
        return ''.join(res)

    
if __name__ == "__main__":
    str1 = "ababaabbbb"
    str2 = "cbcbacaab"
    print(Solution().shortestCommonSupersequence(str1, str2))
