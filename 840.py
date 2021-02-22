class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        h = len(grid)
        w = len(grid)
        
        if(h < 3 or w < 3):
            return 0
        
        def find(x, y) :
            if(x < 2 or y < 2):
                return 0
            else :
                sm = 0
                for i in range(3):
                    sm = sm + grid[x][y - i]
                print(sm, "sm")
                if(check(x,y) and hor(x,y, sm) and ver(x, y, sm) and dia(x,y,sm)):
                    return 1
                return 0
                
                
        def check(x,y):
            ls = []
            for i in range(3):
                for j in range(3):
                    c = grid[x-i][y - j]
                    if c < 1 or c > 9 or c in ls:
                        return False
                    ls.append(c)
            return True
            
        
        
        def hor(x, y, sm):
            for i in range(3):
                t = 0
                for j in range(3):
                    t = t + grid[x - i][y-j]
                if(sm != t) :
                    return False
            print(sm, True, "hor")
            return True
        
        def ver(x, y, sm):
            for i in range(3):
                t = 0
                for j in range(3):
                    print(t, "loop")
                    t = t + grid[x - j][y - i]
                if(sm != t) :
                    print(t, "t", i)
                    return False
            print(sm, True, "True")
            
            return True
        
        
        def dia(x,y,sm):
            t = grid[x][y] + grid[x-1][y-1] + grid[x-2][y-2]
            u = grid[x - 2][y] + grid[x-1][y-1] + grid[x][y-2]
            if (t==sm and sm == u):
                return True
            return False
        
        c = 0
        # find(3,2)
        for i in range(2, h):
            for j in range(2, w):
                c = c + find(i, j)
                
                
        return c