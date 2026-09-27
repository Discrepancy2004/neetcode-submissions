class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        if rows < 3 or cols < 3:
            return
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != 'O':
                return

            if board[r][c] == 'O':
                board[r][c] = 'T'

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(rows):
            for j in range(cols):
                if i == 0 :
                    dfs(0,j)
                if i == rows - 1:
                    dfs(rows -1,j)

        for i in range(rows):
            for j in range(cols):
                if j == 0 :
                    dfs(i,0)
                if j == cols - 1:
                    dfs(i,cols - 1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'



                
