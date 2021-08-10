class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # At most 2 days, just disconnect any two adjacent cell
        
        h = len(grid)
        w = len(grid[0])
        
        dp = [[0 for i in range(w)] for j in range(h)]
        
        def resetDp() :
            
            for i in range(h) :
                for j in range(w) :
                    dp[i][j] = 0
            

        def dfs(x, y) :
            if(x >= 0 and y >= 0 and x < h and y < w) :
                if(grid[x][y] == 1 and dp[x][y] == 0) :
                    dp[x][y] = 1
                    dfs(x - 1, y)
                    dfs(x + 1, y)
                    dfs(x, y - 1)
                    dfs(x, y + 1)
                    
        
        c = 0
        for i in range(h) :
            for j in range(w) :

                if(dp[i][j] == 0 and grid[i][j] == 1) :
                    dfs(i,j)
                    c += 1
                
                if(c > 1) :
                    return 0

        for i in range(h) :
            for j in range(w) :
                if(grid[i][j] == 1) :
                    grid[i][j] = 0
                    d = 0
                    resetDp()
                    # print("re", dp)
                    for m in range(h) :
                        for n in range(w) :
                            if(dp[m][n] == 0 and grid[m][n] == 1) :
                                dfs(m,n)
                                d += 1
                    if(d > 1 or d == 0) :
                        return 1
                    
                    grid[i][j] = 1
                    
        return 2
        
        
        