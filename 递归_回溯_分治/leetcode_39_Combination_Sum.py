class Solution0(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        res_path = []
        self._combinationSum(candidates, 0, target, [], res_path)
        return res_path

    def _combinationSum(self, candidates, index, target, path, res_path):
        
        if target == 0: 
            res_path.append(path) 
            return 
        if path and target < path[-1]:
            return
        
        for i in range(index, len(candidates)):
            self._combinationSum(candidates, i, target - candidates[i], path + [candidates[i]],res_path)


class Solution1(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(index, path, target):
            if target == 0:
                res.append(path)
                return
            if path and target < path[-1]:
                return
            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]], target - candidates[i])

        dfs(0, [], target)

        return res



if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution1().combinationSum(candidates, target))
        



