class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        h = len(grid)
        w = len(grid[0])
        
        s = 0
        for r in grid :
            s += sum(r)
        
        for i in range(h) :
            if(sum(grid[i]) == 1) :
                for j in range(w) :
                    if(grid[i][j] == 1) :
                        cs = 0
                        for k in range(h) :
                            cs += grid[k][j]
                        if(cs == 1) :
                            s -= 1
                        break
        
        return s