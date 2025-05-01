from typing import Optional, List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        path = [''] * m
        res = []

        def backtracking(i, left):
            if i == m:
                res.append(''.join(path))
                return
            if left < n:
                path[i] = '('
                backtracking(i + 1, left + 1)
            if i - left < left:
                path[i] = ')'
                backtracking(i + 1, left)
            
        

        backtracking(0, 0)
        return res