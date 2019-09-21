class Solution1(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1 and triangle[0] == []:
            return 0
        dps = []
        dps.append(triangle[-1])
        for i in range(1, len(triangle)):
            line = triangle[len(triangle) - 1 -i]
            dps.append([0 for _ in range(len(line))])
            for j in range(len(line)):
                dps[i][j] = min(dps[i-1][j], dps[i-1][j+1]) + line[j]

        return dps[len(triangle)-1][0]

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        dp = [0] * (len(triangle) + 1)

        for line in triangle[::-1]:
            for i in range(len(line)):
                dp[i] = line[i] + min(dp[i], dp[i+1])
       
        return dp[0]       

if __name__ == "__main__":
    t = [[2],[3,4],[6,5,7],[4,1,8,3]] 
    # t = []     
    print(Solution().minimumTotal(t)) 
            
