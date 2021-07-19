# 动态规划
class Solution0(object):
    def wordBreak(self, s, wordDict):
        res = [[] for _ in range(len(s)) ] 
        for i in range(len(s)):
            for word in wordDict:
                if i + 1 >= len(word) and word == s[i + 1 - len(word):i + 1]:
                    if i < len(word):
                        res[i].append(word)
                    else:
                        for j in range(len(res[i - len(word)])):
                            res[i].append(res[i - len(word)][j] + ' ' + word)
                            
        return res[-1]

# DFS
class Solution1(object):
    def wordBreak(self, s, wordDict):
        
        res = []

        def dfs(index, path):
            if index == len(s):
                res.append(path)
            if index > len(s):
                return
            for word in wordDict:
                if word == s[index : index + len(word)]:
                    if path == '':
                        dfs(index + len(word), word)
                    else:
                        dfs(index + len(word), path + ' ' + word)
        
        dfs(0, '')

        return res
if __name__ == "__main__":
    # s = "catsanddog"
    # wordDict = ["cat","cats","and","sand","dog"]
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(Solution1().wordBreak(s, wordDict))
