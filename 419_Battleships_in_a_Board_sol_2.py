class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        # method 2, enumerate the begin (with '.' on left and up)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i-1 >= 0 and board[i-1][j] == 'X':
                        continue
                    elif j-1 >= 0 and board[i][j-1] == 'X':
                        continue
                    else:
                        cnt += 1
        return cnt
