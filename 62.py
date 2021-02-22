class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tracker = [[-1 for i in range(n)] for j in range(m)]
        
        tracker[0][0] = 1
        
        def rec(x, y):
            if(tracker[x][y] != -1) :
                return tracker[x][y]
            else :
                a = 0
                b = 0
                if(x > 0) :
                    a = rec(x-1, y)
                if(y > 0) :
                    b = rec(x, y - 1)
                tracker[x][y] = a + b
                return a + b
        
        rec(m-1, n - 1)
        return tracker[m-1][n-1]
        
        