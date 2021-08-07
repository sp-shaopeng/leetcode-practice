class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])
        
        dp = [[[1, False] for i in range(w)] for j in range(h)]
        for i in range(h) :
            if(board[i][0] == 'O') :
                dp[i][0] = [0, False]          
            if(board[i][w - 1] == 'O') :
                dp[i][w - 1] = [0, False]
                
        for i in range(w) :
            if(board[0][i] == 'O') :
                dp[0][i] = [0, False]              
            if(board[h - 1][i] == 'O') :
                dp[h - 1][i] = [0, False]   
        
        def dfs(x, y) :
            if(x < 0 or y < 0 or x >= h or y >= w) :
                return
                
            if(dp[x][y][1] == False and board[x][y] == 'O') :
                dp[x][y] = [0, True]   
                dfs(x - 1, y)
                dfs(x + 1, y )
                dfs(x, y - 1)
                dfs(x, y + 1)
            
            
        if(h >1 and w > 1) :
            for i in range(1, h - 1) :
                for j in range(1, w - 1) :
                    if(dp[i][j] == -1) :
                        find(i, j)
        for i in range(h) :
            if(dp[i][0][0] == 0) :
                dfs(i, 0)
            if(dp[i][w - 1][0] == 0) :
                dfs(i, w - 1)
        for i in range(w) :
            if(dp[0][i][0] == 0) :
                dfs(0, i)
            if(dp[h - 1][i][0] == 0) :
                dfs(h - 1, i)

        for i in range(h) :
            for j in range(w) :
                if(dp[i][j][0] == 1) :
                    board[i][j] = 'X'
