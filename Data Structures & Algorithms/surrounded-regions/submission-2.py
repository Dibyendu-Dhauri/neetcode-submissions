class Solution:
    def solve(self, board: List[List[str]]) -> None:
        list_unsurrounded = []
        def dfs(r,c):
            
            if 0 <= r < len(board) and 0<= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'T'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0,c)
            
            if board[len(board)-1][c] == 'O':
                dfs(len(board)-1,c)
        
        for r in range(1,len(board)-1):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][len(board[0])-1] == 'O':
                dfs(r,len(board[0])-1)
        
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        


        