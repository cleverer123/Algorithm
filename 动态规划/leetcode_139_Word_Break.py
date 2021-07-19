# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * len(s)

        # for i in range(len(s)+1, 0, -1):
        #     for word in wordDict:
        #         if i > len(word) and word == s[i-len(word)-1:i-1]:
        #             dp[i] = dp[i-len(word)] and True


if __name__ == "__main__":
    s = '111'
    print(s + '1')
