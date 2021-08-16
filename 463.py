class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        h = len(grid)
        w = len(grid[0])
        
        p = 0
        
        for i in range(h) :
            for j in range(w) :
                if(grid[i][j] == 1) :
                    c = 4
                    if(i > 0 and grid[i - 1][j] == 1) :
                        c -= 1
                    if(j > 0 and grid[i][j - 1] == 1) :
                        c -= 1
                    if(i < h - 1 and grid[i + 1][j] == 1) :
                        c -= 1
                    if(j < w - 1 and grid[i][j + 1] == 1) :
                        c -= 1
                    p += c
        return p