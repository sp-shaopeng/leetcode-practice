class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h = len(matrix)
        w = len(matrix[0])
        print(h,w)
        tracker = [[-1 for i in range(w)] for j in range(h)]
        
        for i in range(h) :
            tracker[i][0] = int(matrix[i][0])
            
        for j in range(w) :
            tracker[0][j] = int(matrix[0][j])

        
        def find(x,y):
            print(x,y, "p")
            if(int(tracker[x][y]) != -1) :
                return int(tracker[x][y])
            
            if(int(matrix[x][y]) == 0) :
                tracker[x][y] = 0
                return 0
            else:
                if(x > 0 and y > 0):
                    a = find(x - 1, y)
                    b = find(x, y - 1)
                    c = find(x - 1, y - 1)
                    print(a,b,c)
                    tracker[x][y] = 1 + min(a,b,c)
                    return int(tracker[x][y])
                else:
                    return 0
            
        print(tracker)
        
        m = 0
        for i in range(h):
            for j in range(w):
                find(i, j)
                if(m < int(tracker[i][j])):
                    m = int(tracker[i][j])
        print(tracker)
        return m * m
        