class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m,n)
        
        tracker = [[-1 for i in range (n)] for j in range(m)]
        tracker[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if(obstacleGrid[i][j] == 1) :
                    tracker[i][j] = -2
        
        if(tracker[m - 1][n - 1] == -2):
            return 0
        
        def rec(x,y) :
            if(tracker[x][y] == -2) :
                return 0
            if(tracker[x][y] != -1) :
                return tracker[x][y]
            else :
                a = 0
                b = 0
                if(x > 0) :
                    a = rec(x - 1, y)
                if(y > 0) :
                    b = rec(x, y - 1)
                
                tracker[x][y] = a + b
                return a + b
        
        rec(m - 1, n - 1)
        print(tracker)
        return tracker[m - 1][n - 1]
            
            
        
        
        
        