# Making A large island

#You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

#Return the size of the largest island in grid after applying this operation.

#An island is a 4-directionally connected group of 1s.

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        visited = [[0 for i in range(w)] for j in range(h)]
        colorCount = {}
        
        def group(x,y, color) :
            if(x >= 0 and x < h and y >= 0 and y < w and visited[x][y] == 0) :
                visited[x][y] = 1
                if (grid[x][y]) :
                    grid[x][y] = color
                    colorCount[color] = colorCount.get(color, 0) + 1
                    group(x-1,y,color)
                    group(x+1,y,color)
                    group(x,y-1,color)
                    group(x,y+1,color)
        
        def getSurroundingCount(x,y) :
            existing = []
            c = 0
            if(x > 0 and grid[x - 1][y] not in existing) :
                existing.append(grid[x-1][y])
                c += colorCount.get(grid[x - 1][y], 0)
            
            if(x < h - 1 and grid[x + 1][y] not in existing) :
                existing.append(grid[x+1][y])
                c += colorCount.get(grid[x + 1][y], 0)
            
            if(y > 0 and grid[x][y - 1] not in existing) :
                existing.append(grid[x][y - 1])
                c += colorCount.get(grid[x][y - 1], 0)           
            
            if(y < w - 1 and grid[x][y + 1] not in existing) :
                existing.append(grid[x][y+1])
                c += colorCount.get(grid[x][y + 1], 0)        
            
            return c
                
                
                
        color = 100
        for i in range(h) :
            for j in range(w) :
                if(visited[i][j] == 0 and grid[i][j] == 1) :
                    group(i,j,color)
                    color += 1
        

        m = 0
        for i in range(h) :
            for j in range(w) :
                if(grid[i][j] == 0) :
                    m = max(m, 1 + getSurroundingCount(i,j))
        # print(grid)
        if(m == 0) :
            return h * w
        else: return m
        
        
        