class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        
        dp = [[-1 for i in range (w)] for j in range(h)]
        dp[0][0] = grid[0][0]
        def find(x,y) :
            if(dp[x][y] != -1) :
                return dp[x][y]
            
            a = float('inf')
            b = float('inf')
            
            if(x > 0) :
                a = find(x - 1, y)
            if(y > 0) :
                b = find(x, y - 1)
                
            dp[x][y] = grid[x][y] + min(a,b)
            
            return dp[x][y]
        
        find(h - 1, w - 1)
        return dp[h-1][w-1]