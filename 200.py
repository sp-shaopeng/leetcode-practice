class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        count = 0
        def find(x,y):
            if(x < 0 or y < 0 or x >= h or y >= w ) :
                return 
            if(grid[x][y] == '1') :
                grid[x][y] = -1
                find(x+1, y)
                find(x, y + 1)
                find(x - 1, y)
                find(x, y - 1)
         
        for i in range(h) :
            for j in range(w) :
                    if(grid[i][j] == '1') :
                        find(i,j)
                        count += 1
        
        return count
            