class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(grid1)
        n = len(grid1[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        
        def find(x,y) :
            if(x >= 0 and x < m and y >= 0 and y < n and grid2[x][y] == 1 and visited[x][y] == 0) :
                visited[x][y] = 1
                if(grid2[x][y] == grid1[x][y]) :
                    t = find(x-1, y)
                    l = find(x, y-1)
                    r = find(x, y+1)
                    d = find(x+1, y)
                    return t and l and r and d
                else :
                    find(x-1, y)
                    find(x, y-1)
                    find(x, y+1)
                    find(x+1, y)
                    return False
            return True
        

        for i in range(m) :
            for j in range(n) :
                if(grid2[i][j] and visited[i][j] == 0 and find(i,j)) :
                    count += 1
        
        return count
        
        
