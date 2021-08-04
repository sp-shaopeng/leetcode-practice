class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        h = len(mat)
        w = len(mat[0])
        
        for i in range(h):
            for j in range(w):
                v = mat[i][j]
                a = v - 1
                b = a
                c = a
                d = a
                if(i > 0) :
                    a = mat[i - 1][j]
                if(i < h - 1) :
                    b = mat[i + 1][j]
                if(j > 0) :
                    c = mat[i][j - 1]
                if(j < w - 1) :
                    d = mat[i][j + 1]
                if(v > a and v > b and v > c and v > d) :
                    return [i,j]