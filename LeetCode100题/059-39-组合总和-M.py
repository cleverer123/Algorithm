from typing import Optional, List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(begin, path, target):
            if target <= 0:
                if target == 0:
                    res.append(path)
                return 
            for i in range(begin, len(candidates)):
                backtracking(i, path + [candidates[i]], target - candidates[i])

        backtracking(0, [], target)
        return res