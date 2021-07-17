class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i-coin] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coin] +1:
                        dp[i] = dp[i - coin] + 1
                
        return dp[amount]

    def coinChange2(self, coins, amount):
        dp = [-1] * (amount + 1)

        for i in range(amount + 1):
            for coin in coins:
                if coin <= i and dp[i-coin] != -1:
                    if dp[i - coin] + 1 < dp[i] or dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
        return dp[-1]

if __name__ == "__main__":
    coins = [2]
    amount = 3   
    print(Solution().coinChange(coins,amount))   