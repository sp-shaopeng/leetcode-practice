class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        l = len(matrix)
        for i in range(l - 1) :
            for j in range(i, l - i - 1) :
                matrix[i][j], matrix[j][l - i - 1] = matrix[j][l - i - 1], matrix[i][j]
                matrix[i][j], matrix[l - 1 - i][l - 1 - j] = matrix[l - 1 - i][l - 1 - j], matrix[i][j]
                matrix[i][j], matrix[l - j - 1][i] = matrix[l - j - 1][i], matrix[i][j]
        
        
        
        