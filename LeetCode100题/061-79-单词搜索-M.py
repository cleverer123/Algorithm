from typing import Optional, List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def search(r, c, i):
            if not ( 0 <= r < m and 0 <= c < n ) or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            board[r][c] = ''
            res = search(r - 1, c, i + 1) or search(r + 1, c, i + 1) or search(r, c - 1, i + 1) or search(r, c + 1, i + 1)
            board[r][c] = word[i]
            return res

        for r in range(m):
            for c in range(n):
                if search(r, c, 0):
                     return True

        return False