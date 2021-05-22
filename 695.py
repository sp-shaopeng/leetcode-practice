class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ans = 0

        Q = []
        
        h = len(grid)
        w = len(grid[0])
        tracker = [ [0 for i in range(w)] for j in range(h)]
        
        for i in range(h) :
            for j in range(w) :
                count = 0
                
                if(grid[i][j] == 1 and tracker[i][j] == 0) :
                    Q = [[i,j]]
                    tracker[i][j] = 1
                    newQ = []
                    
                    while(Q) :
                        while(Q) :
                            x, y = Q.pop()
                            count += 1
                            if(x < h - 1 and grid[x + 1][y] == 1 and tracker[x+1][y] == 0) :
                                newQ.append([x + 1, y])
                                tracker[x+1][y] = 1
                
                            if(y < w - 1 and grid[x][y + 1] == 1 and tracker[x][y + 1] == 0) :
                                newQ.append([x, y + 1])
                                tracker[x][y+1] = 1
                            
                            if(x > 0  and grid[x - 1][y] == 1 and tracker[x-1][y] == 0) :
                                newQ.append([x - 1, y ])
                                tracker[x-1] [y] = 1
                        
                            if(y > 0  and grid[x][y - 1] == 1 and tracker[x][y - 1] == 0) :
                                newQ.append([x, y - 1 ])
                                tracker[x][y - 1] = 1
                        
                        Q = newQ
                        
                tracker[i][j] = 1
                ans = max(ans, count)
                
        return ans
    