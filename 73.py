class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        r = []
        c = []
        
        h = len(matrix)
        w = len(matrix[0])
        
        for i in range(h):
            for j in range(w):
                if(matrix[i][j] == 0) :
                    if(i not in c) :
                        c.append(i)
                    if(j not in r) :
                        r.append(j)
        
        for m in c :
            for i in range(w):
                matrix[m][i] = 0
        
        for n in r:
            for i in range(h):
                matrix[i][n] = 0
        
        