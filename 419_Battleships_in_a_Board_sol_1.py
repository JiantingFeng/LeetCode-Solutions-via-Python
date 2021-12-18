class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        cnt = 0
        def search(i, j) -> None:
            board[i][j] = '.'
            while i+1 < m and board[i+1][j] == 'X':
                search(i+1, j)
            while j+1 < n and board[i][j+1] == 'X':
                search(i, j+1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    search(i, j)
                    cnt += 1
        return cnt

