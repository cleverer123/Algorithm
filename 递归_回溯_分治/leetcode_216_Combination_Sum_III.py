class Solution(object):
    def combinationSum3(self, k, n):
        if k > n:
            return []
        res = []
        candidates = range(1, 10)
        self.k = k

        def dfs(index, path, n):
            if len(path) > self.k:
                return 
            if n == 0:
                if len(path) != self.k: 
                    return 
                res.append(path)
                return 
            if path and path[-1] > n:
                return 
            for i in range(index, len(candidates)):
                dfs(i+1, path + [candidates[i]], n - candidates[i])
            
        dfs(0, [], n)
        return res

if __name__ == "__main__":
    k, n = 3, 7
    print(Solution().combinationSum3(k, n))